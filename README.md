# DCS-KAI
## Project Structure

```text
DCS-KAI/
├── data/
│   ├── F-16_통합_단계별체크리스트_qdrant_preprocessed.json
│   ├── F-16_통합_단계별체크리스트_ver260917.xlsx
│   ├── csv2qdrant.py
│   └── cockpit_panels/
│       └── F-16_Cockpit_Panels_Duality.xlsx   # 조종석 패널 DB (47 패널 / 359 컨트롤 / 746 position)
│
├── docs/
│   └── cockpit-panel-db.md                    # 패널 DB 구조·식별자 규칙
│
├── scripts/
│   ├── ingest_f16_checklist.py
│   └── panel_db/                              # 패널 DB 엑셀 생성 스크립트 (python build_audio.py)
│
└── src/
    ├── embeddings/
    ├── vectorstore/
    │   └── qdrant.py
    └── rag/
```

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


## Cockpit Panel DB (조종석 패널 매핑)
- 절차 문서의 조작 항목을 식별자 하나(`panel_id.control_code.position_code`, 예: `CMDS.MODE.SEMI`)로 참조하기 위한 F-16C 조종석 스위치 DB
- 정규화 테이블(PANELS/CONTROLS/POSITIONS) + ICP/DED·MFD 상태기계 층 + 조작 매크로(ICP_ACTIONS/MFD_ACTIONS/PANEL_ACTIONS) + HOTAS 문맥별 기능표
- 상세: [docs/cockpit-panel-db.md](docs/cockpit-panel-db.md)

## Some works to do
### Data Preprocessing
### Build a Vector DB (Qdrant)
- Qdrant Cloud (Free Tier) (외부망) (https://qdrant.tech/pricing/)
- Qdrant (내부망)
### RAG System
### Build a mcp tool for both claude and chatgpt


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
