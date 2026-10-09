# DCS-KAI
## Project Structure

```text
DCS-KAI/
├── data/
│   ├── F-16_통합_단계별체크리스트_qdrant_preprocessed.json   # ver260917 '통합 체크리스트' 시트에서 생성 (376건)
│   ├── F-16_통합_단계별체크리스트_ver260917.xlsx            # 이전 버전
│   └── F-16_통합_단계별체크리스트_ver261009.xlsx            # 최신 버전 (행위 레이어-BVR · BVR 거리 기준표 추가)
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

**체크리스트 버전**
| 버전 | 시트 | 변경 내용 |
|---|---|---|
| ver260917 | 통합 체크리스트 / 단계별 집계 | 최초 등록. Qdrant 전처리 JSON의 원본 |
| ver261009 | + **행위 레이어-BVR** / **BVR 거리 기준표** | 절차 레이어(376건, 변경 없음) 위에 행위 레이어 추가 — KAFTTP 3-3.5 §4.2 FENCE·§4.8 요격/표적할당 + BVR Timeline 기반 BVR 교전 전 행위 22개를 거리 게이트(PR→TR→MSR→MTR/DOR→MAR→DR→FR→WVR) 순으로 정리, '관련 절차 ID'로 절차 레이어와 연결. 기준표 시트는 위협(AIM-120C-7/PL-12/AA-12)·고도별 TR/MSR/MTR/DOR/MAR/DR 계산 |

- 통합 체크리스트 376건은 두 버전이 동일하므로 기존 Qdrant 전처리 JSON은 그대로 유효함
- 행위 레이어는 열 구성이 다르므로(순서·ID B-01~22·거리 구간·트리거·판단 기준·실행·주 역할·코파일럿 역할 등) 별도 컬렉션/전처리 필요

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
