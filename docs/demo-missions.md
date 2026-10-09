# Duality Co-Pilot 실증 미션

> 최종 갱신: 2026-10-09
> 목적: DCS F-16C 환경에서 Duality의 두 AI 역할 — **이스투아(Histoire, AWACS형 관제·보조)** 와 **미스테어(Mystere, 자율 윙맨)** — 을 실제 임무로 실증한다.
> 세 번째 미션은 추후 추가 예정.

## 임무 요약

| # | 미션 | 참여 AI | 실증 대상 |
|---|---|---|---|
| M1 | 공대공 전투 — 교전수칙 판단·BVR Shot Plan·윙맨 분리 교전 | 이스투아 + 미스테어 | 교전 전 절차 Remind, ROE 판단 보조, 기종별 Shot Plan, 윙맨 자율 요격 |
| M2 | 공대지 전투 — 저고도 침투 Pop-up Attack | 이스투아 단독 | 경로 이탈 시 폭격 제원(IP·VRP 등) 재산출 및 고지, ICP/DED 직접 입력 |

---

## M1. 공대공 전투

### 시나리오
1. 조종사(호야)와 미스테어가 편대로 이륙, CAP/요격 임무 진입
2. 적 편조가 남하 — **적 폭격기 + 호위 전투기** 구성
3. **교전 전**: 이스투아가 적기의 **Hostile Intent / Hostile Act** 등 교전수칙(ROE) 판단 요소를 조종사에게 보고하고, 교전 진입 전 각종 절차(Fence-In, 무장·센서 세팅, 편대 분리 등)를 **Remind** 하며 조종사를 보조
4. **교전 분리**
   - 미스테어 → 남하하는 **적 폭격기 격추** (자율 수행)
   - 조종사 + 이스투아 → **적 전투기 교전**. 이스투아는 각 적 전투기의 **기종에 맞춘 BVR Timeline 기반 Shot Plan**을 제공 — **TR (Transition Range) · DOR (Desired Out Range) · DR (Decision Range)**
5. 교전 종료 후 RTB 및 착륙

### 역할별 기능
| 역할 | 기능 | 사용 자산 |
|---|---|---|
| 이스투아 | 적기 탐지·BRAA 보고, Hostile Intent/Act 판단 근거 제시 | `get_threats`, `get_aircraft_list` |
| 이스투아 | 교전 전 절차 Remind (P10 Fence-In, P11 공대공 교전 절차) | `F-16_통합_단계별체크리스트` 절차 레이어 + **행위 레이어-BVR** (B-01~22, 거리 게이트) |
| 이스투아 | 기종별 Shot Plan (TR/DOR/DR) | **BVR 거리 기준표** (AIM-120C-7/PL-12/AA-12 + 고도 보정), `get_player_status` |
| 미스테어 | 적 폭격기 요격 (표적 규율: 폭격기만) | `wingman_command` — `attack`(scope/focus, then_action), `disengage`, `rejoin`, `rtb` |
| 공통 | RTB·착륙 (P14 Fence-Out, P15 접근·착륙) | `get_airbase_info`, 체크리스트 P14~P16 |

### 검증 항목 (안)
- ROE 판단 보고가 적기의 실제 행동(레이더 락, 사격 등)보다 선행했는지
- 교전 전 절차 Remind의 누락·오순서 건수
- Shot Plan(TR/DOR/DR)이 적기 기종·고도에 맞게 산출되었는지, 보고 소요 시간
- 미스테어의 폭격기 격추 여부와 표적 규율 준수(전투기 추격 금지)
- 교전 결과(격추/피격) 및 RTB·착륙 완료

### 전제·미결
- 적 폭격기·전투기 **미사일 무장 소환** (기종별 로드아웃) 필요 — 현재 백로그
- BVR 거리 수치는 BVR Timeline(BMS 기준) 근사값
- Hostile Intent / Hostile Act 판단 기준(ROE 규칙화)은 별도 정리 필요

---

## M2. 공대지 전투 — 저고도 침투 Pop-up Attack

### 시나리오
1. 미스테어 없이 **이스투아만** 참여
2. **BEM(KAFTTP) 기반** 저고도 침투 후 **Pop-up Attack** 수행
3. 계획된 Route대로 진입하되, **Route가 틀어질 경우** 이스투아가 **Pop-up Attack 제원을 재계산** — IP, VRP 등 공대지 폭격 제원을 다시 산출
4. 바뀐 제원을 조종사에게 **고지**하거나, 가능하다면 **조종사의 ICP/DED에 직접 입력**
5. 제원대로 Pop-up 폭격 성공 후 RTB 및 착륙

### 역할별 기능
| 역할 | 기능 | 사용 자산 |
|---|---|---|
| 이스투아 | 경로 이탈 감지 (현 위치·방위·고도 vs 계획 Route) | `get_player_status`, `get_player_info`, DTC Route |
| 이스투아 | Pop-up 제원 재계산 (IP, VRP, pull-up point, 투하 고도·각도 등) | KAFTTP 공대지(Ch.5) 행위 레이어 (확장 예정), 체크리스트 P12 공대지 공격 |
| 이스투아 | 바뀐 제원 고지 | 음성 교신 (BRAA/브레비티 표준) |
| 이스투아 | ICP/DED 직접 입력 (VIP/VRP 페이지, STPT 수정) | 패널 DB `ICP_ACTIONS` + `DED_PAGES`/`DED_FIELDS` (VIP/VRP·STPT 페이지는 미기입, 보완 필요), DCS-BIOS 쓰기 |
| 이스투아 | 위협 경고·RTB 유도 | `get_threats`, `get_airbase_info` |

### 검증 항목 (안)
- 경로 이탈 감지까지의 시간과 재계산된 제원의 정확도 (수동 계산 대비)
- 고지 방식 vs ICP/DED 직접 입력 방식의 조종사 작업 부하 차이
- Pop-up 폭격 명중 여부
- RTB·착륙 완료

### 전제·미결
- 행위 레이어 **공대지(KAFTTP Ch.5) 확장** 필요 — 현재 BVR까지만 정리됨
- 패널 DB **DED VIP/VRP·STPT 페이지 필드 보완** 필요 (ICP/DED 직접 입력의 전제)
- DCS-BIOS 쓰기(3단계) 구현 전까지는 "고지" 방식으로 실증

---

## 공통 산출물
- 교신 대본 (`logs/무전대본-*.txt`)
- 조작 로그 — Phase, 트리거 상태, `position_id`/`action_id`, 시각, 결과
- 임무 디브리핑 (대본 + 전과 분석)
