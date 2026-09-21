# DCS-KAI
## Project Structure

```text
DCS-KAI/
├── data/
│   ├── F-16_통합_단계별체크리스트_qdrant_preprocessed.json
│   └── F-16_통합_단계별체크리스트_ver260917.xlsx
│
├── scripts/
│   └── ingest_f16_checklist.py   # xlsx -> embeddings -> Qdrant upsert
│
└── src/
    ├── embeddings/
    │   └── embedder.py           # query embedding (BAAI/bge-m3)
    ├── vectorstore/
    │   └── qdrant.py             # Qdrant client
    ├── rag/
    │   └── search.py             # semantic search over f16_procedures
    └── mcp/
        └── server.py             # MCP server exposing search as a Claude tool
```

## RAG / MCP Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Create a Qdrant Cloud free-tier cluster (https://qdrant.tech/pricing/) and copy its URL + API key,
   or run Qdrant locally (`docker run -p 6333:6333 qdrant/qdrant`) for an internal-network setup.
3. Copy `.env.example` to `.env` (or export the vars directly) and fill in `QDRANT_URL` / `QDRANT_API_KEY`.
4. Ingest the checklist into Qdrant:
   ```bash
   export QDRANT_URL=... QDRANT_API_KEY=...
   python scripts/ingest_f16_checklist.py "data/F-16_통합_단계별체크리스트_ver260917.xlsx"
   ```
5. Smoke-test the MCP server locally (stdio transport, Ctrl+C to stop). The first run
   downloads the embedding model (a few GB) before the server signals ready, so let it
   finish here rather than hitting that cold start from inside a Claude tool call:
   ```bash
   python src/mcp/server.py
   ```
6. Register it with Claude Code:
   ```bash
   claude mcp add dcs-f16-rag \
     --env QDRANT_URL=... --env QDRANT_API_KEY=... \
     -- /absolute/path/to/venv/bin/python /absolute/path/to/DCS-KAI/src/mcp/server.py
   ```
   Or in Claude Desktop's `claude_desktop_config.json`:
   ```json
   {
     "mcpServers": {
       "dcs-f16-rag": {
         "command": "/absolute/path/to/venv/bin/python",
         "args": ["/absolute/path/to/DCS-KAI/src/mcp/server.py"],
         "env": { "QDRANT_URL": "...", "QDRANT_API_KEY": "..." }
       }
     }
   }
   ```
   Any other MCP-compatible client (e.g. ChatGPT desktop/connectors) can point at the same
   `src/mcp/server.py` stdio command.

   **Gotchas that actually bite in practice:**
   - Use the **full path to the Python interpreter inside your venv** (`.../venv/bin/python`),
     not bare `python`/`python3`. Claude Desktop/Code launches the server without your shell's
     PATH or activated venv, so a bare `python` often resolves to the wrong interpreter (or none)
     and the server fails silently on startup.
   - `env` in the config is required — the client does **not** inherit your shell's exported
     `QDRANT_URL`/`QDRANT_API_KEY`; set them there explicitly.
   - Python **3.10+** is required (the `mcp` package's typing requires it).
   - Do step 5 (manual run) at least once before registering — it forces the embedding model
     download/load to happen outside of Claude's tool-call timeout window.

**임무 단계 (코드)**
| 코드 | 단계명 | 절차 수 |
|---|---|---|
| P0 | 임무계획 / DTC 준비 | 4 |
| P1 | 조종석 진입 전 · 외부점검 | 14 |
| P2 | 전원 인가 · 시동 전 | 11 |
| P3 | 엔진 시동 · 항전 전원 | 4 |
| P4 | INS 정렬 · 항법 초기화 | 4 |
| P5 | 시동 후 점검 · 무장/센서 셋업 · BIT | 20 |
| P6 | 택시 · 이륙 전 점검 | 12 |
| P7 | 이륙 · 상승 | 6 |
| P8 | 순항 · 항법 · 연료관리 | 23 |
| P9 | 공중급유 | 57 |
| P10 | 전투진입 준비 (Fence-In) | 5 |
| P11 | 공대공 교전 | 6 |
| P12 | 공대지 공격 | 16 |
| P13 | 방어 · 회피 | 2 |
| P14 | 이탈 · 복귀 (Fence-Out / RTB) | 4 |
| P15 | 접근 · 착륙 | 11 |
| P16 | 착륙 후 · 엔진 정지 | 6 |
| PX | 비정상 · 비상 (발생 시) | 154 |
| PA | 상시 · 필요 시 | 17 |
| **합계** | | **376** |


## Some works to do
### Data Preprocessing
### Build a Vector DB (Qdrant)
- Qdrant Cloud (Free Tier) (외부망) (https://qdrant.tech/pricing/)
- Qdrant (내부망)
- [ ] Populate the `f16_procedures` collection by running `scripts/ingest_f16_checklist.py`
      against a real Qdrant Cloud free-tier cluster (needs a network-unrestricted
      environment; see "RAG / MCP Setup" above)
### RAG System
- [x] `src/rag/search.py`: semantic search over `f16_procedures`
### Build a mcp tool for both claude and chatgpt
- [x] `src/mcp/server.py`: stdio MCP server exposing `search_f16_checklist`
- [ ] Verify end-to-end against a populated collection, then register with Claude Code/Desktop


## Related papers and githubs
- FalconCopilot: https://aclanthology.org/2026.findings-acl.1500.pdf
- Chuck's guide: https://chucksguides.com/
- HAF-F16: https://info.publicintelligence.net/HAF-F16.pdf
- EASA Artificial Intelligence Concept Paper : https://www.easa.europa.eu/en/document-library/general-publications/easa-artificial-intelligence-concept-paper-proposed-issue-3
- dcs-lua-runner-mcp: https://github.com/sevenfifty777/dcs-lua-runner-mcp
- Real-time speech full duplex (FD) model : https://huggingface.co/nvidia/NVIDIA-NemotronLabs-VoiceChat-11B
    
## Goal
- 한국항공우주학회 추계학술대회 (26.11.12)
- https://aclrollingreview.org/dates 
