"""Query embedding using the same model the ingestion pipeline embeds procedures with."""

from __future__ import annotations

import os
from functools import lru_cache

from sentence_transformers import SentenceTransformer

DEFAULT_MODEL = "BAAI/bge-m3"


@lru_cache(maxsize=1)
def get_embedding_model() -> SentenceTransformer:
    model_name = os.environ.get("EMBEDDING_MODEL", DEFAULT_MODEL)
    return SentenceTransformer(model_name)


def embed_query(text: str) -> list[float]:
    vector = get_embedding_model().encode(text, normalize_embeddings=True)
    return vector.tolist()
