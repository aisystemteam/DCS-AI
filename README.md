# DCS-KAI
## Project Structure

```text
DCS-KAI/
├── data/
│   ├── F-16_통합_단계별체크리스트_qdrant_preprocessed.json
│   └── F-16_통합_단계별체크리스트_ver260917.xlsx
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
## Data

### `F-16_통합_단계별체크리스트_ver260917.xlsx`
F-16 비행/항전 절차를 임무 단계별로 정리한 통합 체크리스트. Dash-1(비행 매뉴얼 T.O. GR1F-16CJ-1)과 Dash-34(항전·무장 매뉴얼 T.O. GR1F-16CJ-34-1-1)의 절차를 같은 임무단계 코드로 합쳐 정리했다.

**시트 구성**
- `통합 체크리스트` — 절차 376건 (컬럼: `☐`, 임무단계, 단계명, 출처, ID, 절차명(KO/EN), 트리거, 한 줄 체크리스트(DCS 조작), DCS 적용성, BOLDFACE, 원문 p.)
- `단계별 집계` — 임무단계별 절차 수, 출처별 절차 수, DCS 적용성(적용/부분적용/미구현) 집계

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

**DCS 적용성** (전체 376건 기준): 적용 85 / 부분적용 198 / 미구현 93
**출처별**: Dash-1 248건, Dash-34 128건
**BOLDFACE(●)**: 비상 시 암기가 필요한 절차 표시

### `F-16_통합_단계별체크리스트_qdrant_preprocessed.json`
위 xlsx의 `통합 체크리스트` 시트를 Qdrant 벡터 DB 적재용으로 전처리한 JSON (`csv2qdrant.py`로 생성). 절차 376건 각각을 `id`(UUID), 임베딩용 `text`(임무 단계/절차명/실행조건/체크리스트를 합친 문자열), `payload`(procedure_id, phase_code, phase_name, source, source_page, title_ko/en, trigger, checklist, dcs_applicability, boldface 등 원본 컬럼 매핑)로 구성. 임베딩 모델은 `BAAI/bge-m3`를 기준으로 준비됨(`embedding_model_hint`).

### `csv2qdrant.py`
xlsx 체크리스트를 위 JSON 포맷으로 변환하는 전처리 스크립트.

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
