# -*- coding: utf-8 -*-
# MFD 물리 패널 + MFD 포맷 그래프 — DCS F-16C Early Access Guide EN p.122-128 (MFD, DTE)
from dcs_panels import C, P, NI

# ───────────── 1층: 물리 패널 (좌/우 동일 배치, ID만 구분) ─────────────
def _mfd(code, side, zone_note):
    ctl = []
    # OSB 링 배치: 상단 1→5 (좌→우), 우측 6→10 (상→하), 하단 11→15 (우→좌), 좌측 16→20 (하→상)
    grid = {}
    for i in range(1, 6):   grid[i] = (1, i + 1)
    for i in range(6, 11):  grid[i] = (i - 4, 7)
    for i in range(11, 16): grid[i] = (7, 17 - i)
    for i in range(16, 21): grid[i] = (22 - i, 1)
    common = {11: "DCLT (공통)", 12: "Format Select 좌 (공통)", 13: "Format Select 중 (공통)", 14: "Format Select 우 (공통)", 15: "SWAP (공통)"}
    for i in range(1, 21):
        lab = common.get(i, "")
        ctl.append(C(f"OSB_{i}", grid[i], f"OSB {i}" + (f" — {lab}" if lab else ""), "Push button (momentary)",
                     [("PUSH", "인접 표시 텍스트의 기능 선택/토글 — 의미는 현재 포맷/페이지에 따름 (MFD_OSB_MAP 참조)" + (f". 모든 포맷 공통: {lab}" if lab else ""))],
                     1))
    for cid, g, name, desc in (("GAIN", (1,1), "GAIN Rocker", "센서 영상(레이더 맵/FLIR) 밝기 — 심볼·전체 밝기와 독립. FCR GM/SEA: 맵 밝기, GMT: MTI 게인, TGP MGC: 열영상 게인"),
                               ("SYM", (1,7), "SYM Rocker", "MFD 심볼 밝기 — 영상·전체 밝기와 독립"),
                               ("BRT", (7,1), "BRT Rocker", "MFD 전체 밝기"),
                               ("CON", (7,7), "CON Rocker", "MFD 전체 대비")):
        ctl.append(C(cid, g, name, "2-way momentary rocker (hold = continuous)",
                     [("UP", desc + " 증가"), ("DN", desc + " 감소")], {"GAIN": 2, "SYM": 3, "BRT": 4, "CON": 5}[cid]))
    return P(code, code, f"{side} MULTI-FUNCTION DISPLAY (MFD)", f"Instrument Panel ({zone_note})", "122-123", 7, 7, ctl,
             note="4×4인치 컬러 LCD. OSB 20개 + 로커 4개. 포맷/페이지별 OSB 의미는 MFD_FORMATS / MFD_OSB_MAP / MFD_TRANSITIONS 참조. HOTAS DMS 좌/우로 포맷 순환")

MFDL = _mfd("MFDL", "LEFT", "ICP 좌측")
MFDR = _mfd("MFDR", "RIGHT", "ICP 우측")

# ───────────── 2층: 포맷(노드) ─────────────
# format_id, format_name, master_menu_osb, implemented, osb_map_filled, source_page, description
MFD_FORMATS = [
 ["MASTER_MENU", "Format Selection Master Menu", "", "Y", "Y", "124-125", "포맷 선택 메뉴. 강조된 Format Select OSB(12/13/14)에 포맷 할당"],
 ["COMMON", "(모든 포맷 공통 하단 행)", "", "Y", "Y", "122,124", "OSB 11 DCLT · 12/13/14 Format Select · 15 SWAP — 포맷과 무관하게 항상 표시"],
 ["BLANK", "BLANK", "OSB_1", "Y", "Y", "124", "빈 포맷. 여러 Format Select OSB에 중복 할당 가능. DMS 좌/우 순환에서 제외"],
 ["HAD", "HARM Attack Display", "OSB_2", "Y", "N", "124", "HTS 포드 운용 — SEAD. ASQ-213 장 참조"],
 ["RCCE", "Reconnaissance", "OSB_4", "N", "N", "124", "비기능 (DCS F-16C 미모의)"],
 ["RESET_MENU", "Reset Menu", "OSB_5", "N", "N", "124", NI + " — 심볼/밝기/대비 기본값 리셋"],
 ["FCR", "Fire Control Radar", "OSB_20", "Y", "N", "124", "APG-68 — A-A 탐지/추적, A-G 지상맵/GMT/SEA. APG-68 장 참조"],
 ["TGP", "Targeting Pod", "OSB_19", "Y", "N", "125", "AAQ-33 전자광학 포드. AAQ-33 장 참조"],
 ["WPN", "Weapon", "OSB_18", "Y", "N", "125", "AGM-65 / AGM-88 센서 영상·표적 데이터. 해당 무장 장 참조"],
 ["TFR", "Terrain Following Radar", "OSB_17", "N", "N", "125", "비기능"],
 ["FLIR", "Forward Looking Infrared", "OSB_16", "N", "N", "125", "비기능"],
 ["SMS", "Stores Management System", "OSB_6", "Y", "N", "125", "무장 선택·투하 프로파일·신관·공격 파라미터. Tactical Employment 장 참조"],
 ["HSD", "Horizontal Situation Display", "OSB_7", "Y", "N", "125", "항법·공역·위협·데이터링크 탑다운 전술 화면. Tactical Employment 장 참조"],
 ["DTE_P1", "Data Transfer Equipment — Page 1", "OSB_8", "Y", "Y", "127-128", "DTC 파티션별/전체 업로드"],
 ["DTE_P2", "Data Transfer Equipment — Page 2", "", "Y", "Y", "128", "GPS / COLR 업로드. DTE_P1 OSB_10(PAGE)로 진입"],
 ["TEST", "Test (MFL/BIT)", "OSB_9", "N", "N", "125", NI],
 ["FLCS", "Flight Control System", "OSB_10", "N", "N", "125", NI],
]

# ───────────── 2층: OSB 맵 (포맷별 OSB 의미) ─────────────
# osb_map_id, format_id, osb_no, label, action_type, function, dcs_note
# action_type: ASSIGN_FORMAT | SELECT_FORMAT | ENTER_MENU | SWAP | PAGE | COMMAND | TOGGLE | DISPLAY | NONE
_O = []
def O(fmt, osb, label, atype, func, ni=""):
    _O.append([f"{fmt}.OSB_{osb}", fmt, osb, label, atype, func, ni])

# 공통
O("COMMON", 11, "DCLT", "TOGGLE", "OSB 인접 텍스트 심볼 제거(명령은 유지)", NI)
for n, pos in ((12, "좌"), (13, "중"), (14, "우")):
    O("COMMON", n, "(할당 포맷명)", "SELECT_FORMAT", f"Format Select {pos}: 비강조 시 → 할당된 포맷 표시. 이미 강조(현재 표시 중)된 OSB 재누름 → MASTER_MENU 진입. BLANK 할당 시 텍스트 없음(누르면 강조, 재누름 시 메뉴)")
O("COMMON", 15, "SWAP", "SWAP", "좌/우 MFD에 표시 중인 포맷 및 Format Select 할당 전체 교환")

# MASTER MENU
for osb, fmt in ((1, "BLANK"), (2, "HAD"), (4, "RCCE"), (5, "RESET MENU"), (6, "SMS"), (7, "HSD"), (8, "DTE"), (9, "TEST"), (10, "FLCS"), (16, "FLIR"), (17, "TFR"), (18, "WPN"), (19, "TGP"), (20, "FCR")):
    ni = {"RCCE": "비기능", "RESET MENU": NI, "TEST": NI, "FLCS": NI, "FLIR": "비기능", "TFR": "비기능"}.get(fmt, "")
    O("MASTER_MENU", osb, fmt, "ASSIGN_FORMAT", f"{fmt} 포맷을 현재 강조된 Format Select OSB에 할당하고 즉시 표시. 다른 Format Select에 이미 할당돼 있으면 그쪽은 BLANK로 바뀜(BLANK는 중복 허용)", ni)
O("MASTER_MENU", 3, "", "NONE", "미사용")
for n in (12, 13, 14):
    O("MASTER_MENU", n, "(현재 할당 포맷)", "SELECT_FORMAT", "현재 강조된 Format Select OSB 재누름 또는 다른 Format Select 선택 → 변경 없이 메뉴 종료, 해당 포맷 표시")
O("MASTER_MENU", 15, "SWAP", "SWAP", "공통")
O("MASTER_MENU", 11, "DCLT", "TOGGLE", "공통", NI)

# DTE page 1
O("DTE_P1", 1, "ON", "DISPLAY", "DTE 전원 상태 표시")
O("DTE_P1", 2, "CLSD", "COMMAND", "기밀 데이터 업로드", NI)
O("DTE_P1", 3, "LOAD", "COMMAND", "DTC 데이터 파일의 모든 파티션 순차 업로드")
O("DTE_P1", 4, "FCR", "COMMAND", "FCR 설정 업로드", NI)
O("DTE_P1", 5, "(DTC ID)", "DISPLAY", "DTU에 삽입된 DTC 파일명 표시 (화면 중앙)")
O("DTE_P1", 20, "MPD", "COMMAND", "Mission Planning Data — 스티어포인트·항로·VIP/VRP·ATDT ROE·CMDS 프로그램·TACAN/ILS/BINGO 등 업로드. 업로드 전 CMDS MODE 노브 STBY 필요")
O("DTE_P1", 19, "COMM", "COMMAND", "ARC-164 UHF / ARC-222 VHF 프리셋 주파수 업로드")
O("DTE_P1", 18, "INV", "COMMAND", "무장 인벤토리", NI)
O("DTE_P1", 17, "PROF", "COMMAND", "무장 프로파일", NI)
O("DTE_P1", 16, "MSMD", "COMMAND", "마스터모드 초기화", NI)
O("DTE_P1", 6, "ELINT", "COMMAND", "ALR-56 RWR 위협 테이블 업로드")
O("DTE_P1", 7, "SMDL", "COMMAND", "보안 모뎀 데이터링크", NI)
O("DTE_P1", 8, "TNDL", "COMMAND", "전술 네트워크 데이터링크", NI)
O("DTE_P1", 9, "NCTR", "COMMAND", "비협조 표적 식별", NI)
O("DTE_P1", 10, "PAGE 1", "PAGE", "DTE_P2로 전환")
for n in (11, 12, 13, 14, 15):
    O("DTE_P1", n, "(공통)", "SELECT_FORMAT" if n in (12, 13, 14) else ("SWAP" if n == 15 else "TOGGLE"), "COMMON 참조")
# DTE page 2
O("DTE_P2", 1, "ON", "DISPLAY", "DTE 전원 상태 표시")
O("DTE_P2", 20, "GPS", "COMMAND", "GPS 수신기 데이터 업로드")
O("DTE_P2", 19, "COLR", "COMMAND", "MFD 심볼·텍스트·OSB 라벨 색상 설정 업로드")
O("DTE_P2", 10, "PAGE 2", "PAGE", "DTE_P1로 전환")
for n in (11, 12, 13, 14, 15):
    O("DTE_P2", n, "(공통)", "SELECT_FORMAT" if n in (12, 13, 14) else ("SWAP" if n == 15 else "TOGGLE"), "COMMON 참조")
MFD_OSB_MAP = _O

# ───────────── 2층: 전이 ─────────────
# transition_id, from_format, input, to_format, note
_T = []
def T(f, i, t, n=""): _T.append([f, i, t, n])
T("ANY", "MFDx.OSB_12 / 13 / 14 (비강조)", "(해당 OSB에 할당된 포맷)", "Format Select — 현재 마스터모드의 할당 테이블 참조")
T("ANY", "MFDx.OSB_12 / 13 / 14 (강조=현재 표시 중)", "MASTER_MENU", "같은 OSB 재누름 → 포맷 선택 메뉴")
T("MASTER_MENU", "MFDx.OSB_n (포맷 항목)", "(선택 포맷)", "강조된 Format Select OSB에 할당 후 그 포맷 표시. 다른 Format Select의 같은 포맷은 BLANK로")
T("MASTER_MENU", "MFDx.OSB_12 / 13 / 14", "(현재 할당 포맷)", "변경 없이 메뉴 종료")
T("ANY", "MFDx.OSB_15 (SWAP)", "(반대쪽 MFD의 포맷)", "좌/우 MFD 포맷·할당 교환")
T("DTE_P1", "MFDx.OSB_10 (PAGE)", "DTE_P2"); T("DTE_P2", "MFDx.OSB_10 (PAGE)", "DTE_P1")
T("ANY", "HOTAS DMS LEFT / RIGHT", "(다음/이전 할당 포맷)", "SSC DMS 좌/우 — 해당 MFD의 Format Select 할당 순환 (BLANK 제외). HOTAS_FUNCTIONS 참조")
T("ANY", "마스터모드 변경 (ICP.AA/AG, DGFT/MSL OVRD)", "(모드별 초기 할당 포맷)", "7개 마스터모드(NAV/A-A/A-G/MSL OVRD/DGFT/S-J/E-J)별로 Format Select 할당이 독립 저장됨")
MFD_TRANSITIONS = [[f"MT{i+1:03d}"] + r for i, r in enumerate(_T)]

# ───────────── 3층: 조작 매크로 (샘플) ─────────────
# action_id, goal, precondition, input_sequence, verify, source_page, note
MFD_ACTIONS = [
 ["MFD.SHOW_ASSIGNED", "Format Select OSB에 할당된 포맷 표시 — 예: 좌 MFD OSB 13", "ANY", "MFDL.OSB_13", "좌 MFD 하단 OSB 13 라벨 강조, 해당 포맷 표시", "124", "이미 강조 상태면 MASTER_MENU로 들어가므로 먼저 강조 여부 확인(DCS-BIOS MFD 텍스트)"],
 ["MFD.OPEN_MASTER_MENU", "포맷 선택 메뉴 열기 — 예: 좌 MFD OSB 12 기준", "ANY", "MFDL.OSB_12 > (강조 상태였으면 생략) MFDL.OSB_12", "좌 MFD에 BLANK/HAD/…/FCR 메뉴 표시", "124,126", "비강조→1회 누르면 강조+포맷 표시, 2회째 메뉴"],
 ["MFD.ASSIGN_TGP_OSB12", "좌 MFD OSB 12에 TGP 포맷 할당", "ANY", "MFD.OPEN_MASTER_MENU(MFDL.OSB_12) > MFDL.OSB_19", "좌 MFD에 TGP 포맷 표시, OSB 12 라벨 'TGP' 강조", "126", "현재 마스터모드에서만 유효. 다른 Format Select에 TGP가 있었으면 그쪽은 BLANK"],
 ["MFD.ASSIGN_FORMAT", "일반형: <MFD>.<FS OSB>에 <포맷> 할당", "ANY", "MFD.OPEN_MASTER_MENU(<MFD>.<FS OSB>) > <MFD>.OSB_<MFD_FORMATS.master_menu_osb>", "<FS OSB> 라벨 = 포맷명 강조", "124-126", "MFD_FORMATS.master_menu_osb로 포맷→OSB 번호 조회"],
 ["MFD.SWAP", "좌/우 MFD 포맷 교환", "ANY", "MFDL.OSB_15", "좌/우 표시 포맷 및 하단 할당 라벨 교환", "125", "어느 쪽 MFD의 OSB 15든 동일"],
 ["MFD.DTE_LOAD_ALL", "DTC 전체 업로드", "DTE_P1 표시 (예: 우 MFD)", "MFDR.OSB_13(DTE 할당 가정) > MFDR.OSB_3", "DTE 화면 상태 메시지(17) 업로드 진행/완료, DTC ID 표시", "127", "DTC가 DTU에 삽입돼 있어야 함. 시동 절차 단계"],
 ["MFD.DTE_LOAD_MPD", "미션 계획 데이터만 업로드", "DTE_P1 표시 + CMDS MODE=STBY", "MFDR.OSB_20", "상태 메시지 완료, STPT/CNI 데이터 반영", "127", "CMDS 패널 추가 시 전제조건을 position_id로 연결"],
 ["MFD.DTE_LOAD_COMM", "UHF/VHF 프리셋 업로드", "DTE_P1 표시", "MFDR.OSB_19", "CNI/UHF DED 페이지 프리셋 주파수 갱신", "128", ""],
 ["MFD.DTE_PAGE2_GPS", "GPS 데이터 업로드", "DTE_P1 표시", "MFDR.OSB_10 > MFDR.OSB_20", "DTE Page 2 표시 후 상태 메시지", "128", ""],
 ["MFD.BRT_UP", "MFD 밝기 증가 (연속)", "ANY", "MFDL.BRT.UP (유지)", "화면 밝기 증가", "123", "SYM/GAIN/CON 동일 패턴"],
]
