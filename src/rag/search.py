"""Semantic search over the F-16 checklist collection stored in Qdrant."""

from __future__ import annotations

from typing import Any

from qdrant_client import models

from src.embeddings.embedder import embed_query
from src.vectorstore.qdrant import get_collection_name, get_qdrant_client

PAYLOAD_FIELDS = (
    "procedure_id",
    "phase_code",
    "phase_name",
    "source",
    "source_page",
    "title_ko",
    "title_en",
    "trigger",
    "checklist",
    "dcs_applicability",
    "boldface",
)


def search_checklist(
    query: str,
    top_k: int = 5,
    phase_code: str | None = None,
    dcs_applicability: str | None = None,
) -> list[dict[str, Any]]:
    """Embed `query` and return the top matching F-16 checklist procedures."""
    conditions = []
    if phase_code:
        conditions.append(
            models.FieldCondition(key="phase_code", match=models.MatchValue(value=phase_code))
        )
    if dcs_applicability:
        conditions.append(
            models.FieldCondition(
                key="dcs_applicability", match=models.MatchValue(value=dcs_applicability)
            )
        )
    query_filter = models.Filter(must=conditions) if conditions else None

    hits = get_qdrant_client().query_points(
        collection_name=get_collection_name(),
        query=embed_query(query),
        query_filter=query_filter,
        limit=top_k,
        with_payload=True,
    ).points

    return [
        {"score": hit.score, **{field: hit.payload.get(field) for field in PAYLOAD_FIELDS}}
        for hit in hits
    ]
