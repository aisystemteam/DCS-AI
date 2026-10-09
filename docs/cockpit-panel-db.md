# F-16C 조종석 패널 DB (Cockpit Panel Knowledge Graph)

> 파일: `data/cockpit_panels/F-16_Cockpit_Panels_Duality.xlsx` · 생성 스크립트: `scripts/panel_db/`
> 최종 갱신: 2026-10-09

## 목적

절차/행위 문서(`F-16_통합_단계별체크리스트`)가 조작 항목을 **식별자 하나**로 참조하고, 향후 DCS-BIOS 쓰기 명령(`dcsbios_id` / `dcsbios_value`)과 연결하기 위한 조종석 스위치 DB.
LLM(Co-Pilot)이 임무 중 전체 자료를 뒤지지 않고 `(Phase, 상태) → 조작 ID 목록`만 조회하도록 설계한다.

## 수록 현황

**47 패널 / 359 컨트롤 / 746 position**

| 구역(zone) | 접근 우선순위 | 패널 |
|---|---|---|
| HOTAS | 1 | SSC, THROTTLE |
| FRONT | 2 | LEYEBROW, RWRAZ, RWRPRIME, AOAIDX, ARNWS, REYEBROW, ICP, MFDL, MFDR, MISC, INSTR, FUELQTY |
| LAUX | 3 | LG, RWRAUX, ALTGEAR, CMDS, HMCS |
| LCONS | 4 | CANOPY, CFBTN, FLTCTL, TEST, IFF, TRIM, EXTLT, AVTR, ECM, AUD1, AUD2, ELEC, FUEL, EPU, ENGJET, UHFBU, MPO |
| RAUX | 5 | RAUXINST, CAUTION |
| RCONS | 6 | SNSRPWR, RCONSMISC, INTLT, AIRCOND, PLAINCIPHER, OXYGEN, ANTSEL(ANTI ICE 포함), KY58, AVPWR |

출처: DCS F-16C Early Access Guide EN — p.43-79 (Cockpit Overview), p.83-89 HOTAS, p.98-121 ICP, p.122-128 MFD, p.252-262 무선/UHF BACKUP, p.693-708 방어 계통. IFF/AUD1/AUD2/ANTSEL은 Falcon BMS TO 1F-16CM/AM-1 p.148-157로 최초 작성 후 DCS 대조·수정.

미수록: HUD 표시 필드 및 HUD 제어판(p.90-97), EHSI, 사출좌석(p.81-82), 좌측 콘솔 ANTI-G 패널.

## 워크북 구조

| 시트 | 역할 |
|---|---|
| `ZONES` | 조종석 구역 6개 + 인체공학 접근 우선순위 (HOTAS > FRONT > LAUX > LCONS > RAUX > RCONS). 모든 표가 이 순서로 정렬 |
| `PANELS` / `CONTROLS` / `POSITIONS` | LLM 조회용 정규화 테이블 3장 (병합 셀·빈 칸·메모 없음, 1행 = 1개체) |
| `HOTAS_FUNCTIONS` | HOTAS 스위치의 문맥별 기능 (control_id, position, press, context_type, context) → function. press = SHORT/LONG/HOLD/ANY, context_type = MASTER_MODE/SOI/CMDS_MODE/STATE/ANY |
| `DED_PAGES` / `DED_TRANSITIONS` / `DED_FIELDS` / `ICP_ACTIONS` | ICP/DED 상태기계 층 (페이지 43 · 전이 54 · 필드 82 · 조작 매크로 26) |
| `MFD_FORMATS` / `MFD_OSB_MAP` / `MFD_TRANSITIONS` / `MFD_ACTIONS` | MFD 상태기계 층 (ICP와 같은 틀) |
| `PANEL_ACTIONS` | ICP/MFD가 아닌 일반 패널·HOTAS 조작 매크로 (HOTAS 16, CMDS 3, RWR 4, ECM 4, UHFBU 3) |
| `GRID_<panel_id>` | 사람 검수용 물리 배치 격자 (스위치 셀 오른쪽에 position 행, 셀에 control_id 병기) |

절차 문서가 참조할 키:
- 단순 스위치 → `POSITIONS.position_id`
- 조작열(여러 입력의 매크로) → `*_ACTIONS.action_id`

## 3층 구조 (ICP/DED, MFD)

```
1층  물리 패널      ICP (KEY_0~9, 기능키), MFDL/MFDR (OSB_1~20)
2층  상태 그래프    DED_PAGES / DED_TRANSITIONS / DED_FIELDS,  MFD_FORMATS / MFD_OSB_MAP / MFD_TRANSITIONS
3층  조작 매크로    ICP_ACTIONS, MFD_ACTIONS   ← 절차 문서가 참조
```

- `DED_FIELDS.edit_method` = KEYPAD_ENTR | MSEL_TOGGLE | KEY_TOGGLE | INCDEC_CYCLE | INCDEC_SPECIAL | SEQ_TOGGLE | DISPLAY
- ICP_ACTIONS 입력 열 표기: `>` 구분, `x4` 반복, 괄호는 조건부. 검증은 DCS-BIOS DED 5행 텍스트
- DED_FIELDS 채운 페이지: CNI, UHF, VHF, ALOW, CRUS 4종, TIME, BNGO, MAN, MODE, LIST, MISC, CMDS 5종
- MFD OSB 맵 채운 포맷: MASTER_MENU, COMMON, DTE_P1/P2. 마스터모드별 Format Select 할당은 조종사/DTC마다 달라 비워 둠 (런타임에 OSB 라벨을 읽어 재할당)
- DCS 미구현 DED 페이지: IFF, INTG, CORR, OFP, INSM, GPS, DRNG

## 식별자 규칙 (고정)

| 항목 | 규칙 | 예 |
|---|---|---|
| `panel_id` | 짧은 영문 대문자 | `SSC`, `ICP`, `MFDL`, `CMDS`, `UHFBU` |
| `control_code` | TO/가이드 명칭 기반 대문자+밑줄. 볼륨 전용 `_VOL`, 전원 겸용 `_PWR` | `COMM1_MODE`, `COMM1_PWR` |
| `position_code` | 각인을 대문자+밑줄로 정규화, 숫자는 그대로 | `INC_ON`, `A_B`, `M3_MS`, `PUSH`, `NA` |
| `position_id` | `panel_id.control_code.position_code` | `AUD1.COMM1_MODE.GD`, `CMDS.MODE.SEMI`, `SSC.CMS.AFT`, `UHFBU.MODE.PRESET` |

표기 관례: 볼륨 노브 `NONE_OFF/INC_ON`, 전원 노브 `OFF/INC_ON`, 버튼 `PUSH`, 표시기 `NA`, 표시등 `OFF/ON`, 연속 노브 `ADJ`, 래칭 버튼 `IN/OUT`, 짧게/길게 `PRESS_SHORT/HOLD/RELEASE`, 4방향 햇 `FWD/AFT/LEFT/RIGHT`, 트리거 `DETENT_1/2`.

## 생성 스크립트 (`scripts/panel_db/`)

| 파일 | 내용 |
|---|---|
| `build_audio.py` | 실행 진입점. BMS 기반 5개 패널 정의 + 테이블/격자 생성 |
| `dcs_panels.py` | DCS EA Guide p.43-79 패널 31개 정의 |
| `icp.py` | ICP 패널 + DED_PAGES / DED_TRANSITIONS / DED_FIELDS / ICP_ACTIONS |
| `mfd.py` | MFDL/MFDR 패널 + MFD_FORMATS / MFD_OSB_MAP / MFD_TRANSITIONS / MFD_ACTIONS |
| `cmds.py` | CMDS 패널 + CMDS DED 5페이지 + CMDS 조작 매크로 |
| `defensive.py` | RWR 방위표시기/Prime/Aux, ECM, 좌측 벽 CHAFF/FLARE 버튼 + 방어계통 조작 매크로 |
| `hotas.py` | SSC/THROTTLE 패널 + HOTAS_FUNCTIONS(133건) + HOTAS 조작 매크로 |
| `uhfbu.py` | DCS UHF Backup 패널 + UHF/VHF DED 필드 + 무선 동조 매크로 |

```bash
pip install openpyxl
cd scripts/panel_db
python build_audio.py      # 현재 폴더에 F-16_Cockpit_Panels_Duality.xlsx 생성
```

패널을 추가할 때는 해당 모듈에 정의를 추가하고 재생성한다. 작업 단위는 패널 1~2개로 작게 유지.

## 비행 로그 연계 방침

- 실제 DCS 비행 중 Phase별 조작을 식별자(`position_id` / `action_id`)로 기록 → LLM이 `(Phase, 상태) → 조작 ID 목록`만 조회
- 식별자는 "무엇을", 조작 시점의 텔레메트리(`get_player_status` / DCS-BIOS 자동 캡처)가 "언제"를 제공
- 여러 소티를 모아 반복 조작(필수)과 상황 조작(조건부)을 구분
- `access_rank`는 Phase와 상관: RCONS는 주로 지상/시동 1회 세팅(Co-Pilot 위임 후보), HOTAS/FRONT는 비행 중 조종사 직접 조작

## 다음 단계

1. HUD 제어판 + HUD 표시 필드(읽기 표), EHSI, 사출좌석 → 패널 배치 완료
2. DED_FIELDS 미기입 페이지·MFD_OSB_MAP 미기입 포맷 보완 (T-ILS, STPT, INS / FCR, SMS, HSD 우선)
3. `POSITIONS`에 `dcsbios_id` / `dcsbios_value` 열 추가
4. `F-16_통합_단계별체크리스트.xlsx`의 조작 항목 376건 → `position_id` / `action_id` 매핑
5. 비행 로그 형식 확정 (Phase, 트리거 상태, ID, 시각, 결과), MFD_LAYOUT_PROFILES 추가
