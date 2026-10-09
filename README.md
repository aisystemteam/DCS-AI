# DCS-KAI
## Project Structure

```text
DCS-KAI/
├── data/
│   ├── F-16_통합_단계별체크리스트_qdrant_preprocessed.json
│   └── F-16_통합_단계별체크리스트_ver260917.xlsx
│
├── docs/
│   └── demo-missions.md                       # 실증 미션 (M1 공대공 / M2 공대지 Pop-up)
│
├── scripts/
│   └── ingest_f16_checklist.py
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


## Demo Missions (실증 미션)
| # | 미션 | 참여 AI | 실증 대상 |
|---|---|---|---|
| M1 | 공대공 전투 | 이스투아 + 미스테어 | ROE(Hostile Intent/Act) 판단 보조, 교전 전 절차 Remind, 기종별 BVR Shot Plan(TR/DOR/DR), 미스테어의 적 폭격기 자율 격추 |
| M2 | 공대지 전투 — 저고도 침투 Pop-up Attack | 이스투아 | 경로 이탈 시 IP/VRP 등 폭격 제원 재산출·고지, ICP/DED 직접 입력 |

- 상세: [docs/demo-missions.md](docs/demo-missions.md) (세 번째 미션 추후 추가)

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
