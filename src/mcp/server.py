"""MCP server that exposes F-16 checklist retrieval (Qdrant-backed RAG) as a Claude tool.

Prerequisites: the `f16_procedures` Qdrant collection must already be populated
(see scripts/ingest_f16_checklist.py) and QDRANT_URL / QDRANT_API_KEY must be set.

Run directly for a local smoke test:
    QDRANT_URL=... QDRANT_API_KEY=... python src/mcp/server.py

Then register it with Claude Code / Claude Desktop. See README.md for the exact config.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from mcp.server.fastmcp import FastMCP

from src.rag.search import search_checklist

mcp = FastMCP("dcs-f16-rag")


@mcp.tool()
def search_f16_checklist(
    query: str,
    top_k: int = 5,
    phase_code: str | None = None,
    dcs_applicability: str | None = None,
) -> list[dict]:
    """Semantically search the F-16 integrated checklist for procedures matching `query`.

    Args:
        query: Natural-language question or DCS situation, in Korean or English
            (e.g. "공중급유 접촉 실패 시 절차" or "engine start sequence").
        top_k: Number of matching procedures to return (default 5).
        phase_code: Optional exact mission-phase filter, e.g. "P9" (air refueling).
        dcs_applicability: Optional exact filter on DCS applicability.

    Returns:
        Matching procedures with phase, title, trigger condition, checklist steps,
        and a similarity score, ordered by relevance.
    """
    return search_checklist(
        query=query,
        top_k=top_k,
        phase_code=phase_code,
        dcs_applicability=dcs_applicability,
    )


if __name__ == "__main__":
    # Load the embedding model before entering the stdio loop. Otherwise the
    # first real search pays for the (multi-GB, first-run) model
    # download/load inline, which can exceed the calling client's per-tool-call
    # timeout.
    from src.embeddings.embedder import get_embedding_model

    get_embedding_model()
    mcp.run(transport="stdio")
