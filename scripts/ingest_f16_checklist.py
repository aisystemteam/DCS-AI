#!/usr/bin/env python3
"""Ingest the F-16 integrated checklist workbook into Qdrant.

Each checklist row becomes one Qdrant point. Semantic fields are embedded together,
while phase/source/applicability fields remain structured payload metadata for filters.
"""

from __future__ import annotations

import argparse
import os
import sys
import uuid
from pathlib import Path
from typing import Any, Iterable

import pandas as pd
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.embeddings.embedder import DEFAULT_MODEL
from src.vectorstore.qdrant import DEFAULT_COLLECTION

DEFAULT_SHEET = "통합 체크리스트"
DATASET_NAME = "F-16 단계별체크리스트"
AIRCRAFT = "F-16"

COLUMN_MAP = {
    "임무단계": "phase_code",
    "단계명": "phase_name",
    "출처": "source",
    "ID": "procedure_id",
    "절차명(KO)": "title_ko",
    "절차명(EN)": "title_en",
    "트리거": "trigger",
    "한 줄 체크리스트 (DCS 조작)": "checklist",
    "DCS 적용성": "dcs_applicability",
    "BOLDFACE": "boldface",
    "원문 p.": "source_page",
}

REQUIRED_COLUMNS = set(COLUMN_MAP)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Embed F-16 checklist rows and upsert them into Qdrant."
    )
    parser.add_argument("xlsx", type=Path, help="Path to the checklist .xlsx file")
    parser.add_argument("--sheet", default=DEFAULT_SHEET)
    parser.add_argument("--collection", default=DEFAULT_COLLECTION)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--qdrant-url", default=os.getenv("QDRANT_URL", "http://localhost:6333"))
    parser.add_argument("--qdrant-api-key", default=os.getenv("QDRANT_API_KEY"))
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument(
        "--recreate",
        action="store_true",
        help="Delete and recreate the collection before ingesting.",
    )
    return parser.parse_args()


def clean_value(value: Any) -> Any:
    """Convert pandas/Excel null-ish and scalar values to JSON-safe Python values."""
    if value is None:
        return None
    try:
        if pd.isna(value):
            return None
    except (TypeError, ValueError):
        pass

    # Convert numpy scalar types returned by pandas.
    if hasattr(value, "item"):
        try:
            value = value.item()
        except (ValueError, AttributeError):
            pass

    if isinstance(value, str):
        value = value.strip()
        return value or None
    return value


def as_bool(value: Any) -> bool:
    value = clean_value(value)
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    return str(value).strip().lower() in {"1", "true", "yes", "y", "x", "o", "bold", "boldface"}


def load_checklist(path: Path, sheet: str) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Workbook not found: {path}")

    df = pd.read_excel(path, sheet_name=sheet, dtype=object)
    missing = REQUIRED_COLUMNS.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

    # Section header rows (e.g. '■ P0 ...') have no procedure ID.
    df = df[df["ID"].notna()].copy()
    df = df.rename(columns=COLUMN_MAP)

    for column in COLUMN_MAP.values():
        df[column] = df[column].map(clean_value)

    df["procedure_id"] = df["procedure_id"].map(lambda v: str(v) if v is not None else None)
    df["boldface"] = df["boldface"].map(as_bool)
    return df.reset_index(drop=True)


def build_embedding_text(row: pd.Series) -> str:
    fields = [
        ("임무 단계", row["phase_name"]),
        ("절차명", row["title_ko"]),
        ("영문 절차명", row["title_en"]),
        ("실행 조건", row["trigger"]),
        ("체크리스트", row["checklist"]),
    ]
    return "\n".join(f"{label}: {value}" for label, value in fields if value)


def build_payload(row: pd.Series, source_file: str, embedding_text: str) -> dict[str, Any]:
    return {
        "aircraft": AIRCRAFT,
        "dataset": DATASET_NAME,
        "source_file": source_file,
        "procedure_id": row["procedure_id"],
        "phase_code": row["phase_code"],
        "phase_name": row["phase_name"],
        "source": row["source"],
        "source_page": row["source_page"],
        "title_ko": row["title_ko"],
        "title_en": row["title_en"],
        "trigger": row["trigger"],
        "checklist": row["checklist"],
        "dcs_applicability": row["dcs_applicability"],
        "boldface": row["boldface"],
        "text": embedding_text,
    }


def point_id(row: pd.Series) -> str:
    # Stable IDs make reruns idempotent: the same procedure is updated, not duplicated.
    key = f"{AIRCRAFT}:{row['source']}:{row['procedure_id']}"
    return str(uuid.uuid5(uuid.NAMESPACE_URL, key))


def batches(items: list[models.PointStruct], size: int) -> Iterable[list[models.PointStruct]]:
    for start in range(0, len(items), size):
        yield items[start : start + size]


def ensure_collection(
    client: QdrantClient,
    collection: str,
    vector_size: int,
    recreate: bool,
) -> None:
    exists = client.collection_exists(collection)
    if exists and recreate:
        client.delete_collection(collection)
        exists = False

    if not exists:
        client.create_collection(
            collection_name=collection,
            vectors_config=models.VectorParams(
                size=vector_size,
                distance=models.Distance.COSINE,
            ),
        )

    # Frequently filtered fields get payload indexes. Ignore "already exists" errors.
    for field_name in ("aircraft", "procedure_id", "phase_code", "source", "dcs_applicability"):
        try:
            client.create_payload_index(
                collection_name=collection,
                field_name=field_name,
                field_schema=models.PayloadSchemaType.KEYWORD,
            )
        except Exception as exc:  # qdrant versions differ in the exact duplicate-index error type
            if "already" not in str(exc).lower():
                raise

    try:
        client.create_payload_index(
            collection_name=collection,
            field_name="boldface",
            field_schema=models.PayloadSchemaType.BOOL,
        )
    except Exception as exc:
        if "already" not in str(exc).lower():
            raise


def main() -> None:
    args = parse_args()
    if args.batch_size < 1:
        raise ValueError("--batch-size must be >= 1")

    df = load_checklist(args.xlsx, args.sheet)
    if df.empty:
        raise ValueError("No checklist rows found after removing section headers.")

    texts = [build_embedding_text(row) for _, row in df.iterrows()]
    model = SentenceTransformer(args.model)
    vectors = model.encode(
        texts,
        batch_size=args.batch_size,
        normalize_embeddings=True,
        show_progress_bar=True,
    )

    client = QdrantClient(url=args.qdrant_url, api_key=args.qdrant_api_key)
    ensure_collection(client, args.collection, len(vectors[0]), args.recreate)

    source_file = args.xlsx.name
    points: list[models.PointStruct] = []
    for (_, row), text, vector in zip(df.iterrows(), texts, vectors, strict=True):
        points.append(
            models.PointStruct(
                id=point_id(row),
                vector=vector.tolist(),
                payload=build_payload(row, source_file, text),
            )
        )

    for chunk in batches(points, args.batch_size):
        client.upsert(
            collection_name=args.collection,
            points=chunk,
            wait=True,
        )

    print(
        f"Upserted {len(points)} points into '{args.collection}' "
        f"at {args.qdrant_url} using '{args.model}'."
    )


if __name__ == "__main__":
    main()
