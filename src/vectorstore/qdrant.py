"""Qdrant client construction shared by the ingestion script and the MCP server."""

from __future__ import annotations

import os
from functools import lru_cache

from qdrant_client import QdrantClient

DEFAULT_COLLECTION = "f16_procedures"


@lru_cache(maxsize=1)
def get_qdrant_client() -> QdrantClient:
    url = os.environ.get("QDRANT_URL")
    if not url:
        raise RuntimeError(
            "QDRANT_URL is not set. Point it at your Qdrant Cloud cluster "
            "(e.g. https://xxxx.aws.cloud.qdrant.io) or a local instance."
        )
    return QdrantClient(url=url, api_key=os.environ.get("QDRANT_API_KEY"))


def get_collection_name() -> str:
    return os.environ.get("QDRANT_COLLECTION", DEFAULT_COLLECTION)
