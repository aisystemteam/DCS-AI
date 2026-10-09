# -*- coding: utf-8 -*-
# ICP 물리 패널 + DED 페이지 그래프 — DCS F-16C Early Access Guide EN p.98-121 (Upfront Controls)
from dcs_panels import C, BTN, P, NI

def KEY(n, grid, label, sub):
    return C(f"KEY_{n}", grid, f"Keypad {n} / {label}", "Push button (momentary)",
             [("PUSH", f"숫자 {n} 입력 · CNI 페이지에서 {label} 페이지 진입 · LIST/MISC 페이지에서 해당 항목 선택{sub}")],
             5, push="PUSH")

ICP = P("ICP", "ICP", "INTEGRATED CONTROL PANEL (ICP)", "Instrument Panel (상단 중앙, HUD 하단)", "99-100", 5, 6, [
    BTN("COM1", (1,1), "COM 1 Override Button", "UHF DED 페이지 호출 (재누름 시 이전 페이지 복귀)", 1),
    BTN("COM2", (1,2), "COM 2 Override Button", "VHF DED 페이지 호출 (재누름 시 이전 페이지 복귀)", 1),
    BTN("IFF", (1,3), "IFF Override Button", "IFF DED 페이지 호출 (재누름 시 이전 페이지 복귀) — 페이지 자체는 " + NI, 1),
    BTN("LIST", (1,4), "LIST Override Button", "LIST DED 페이지 호출 (재누름 시 이전 페이지 복귀)", 1),
    BTN("AA", (1,5), "A-A Master Mode Button", "공대공 마스터모드 선택. 현재 모드에서 재누름 시 NAV 복귀", 2),
    BTN("AG", (1,6), "A-G Master Mode Button", "공대지 마스터모드 선택. 현재 모드에서 재누름 시 NAV 복귀", 2),

    C("SYM", (2,1), "SYM Knob", "Rotary knob (OFF→BRT)", [("OFF", "HUD 심볼 OFF"), ("INC_ON", "CW 회전 시 HUD 심볼 밝기 증가")], 3),
    KEY(1, (2,2), "T-ILS", ""), KEY(2, (2,3), "ALOW", ""), KEY(3, (2,4), "(없음)", " · CNI에서 3번은 페이지 없음"),
    BTN("RCL", (2,5), "RCL Button", "1회: 입력 중 마지막 숫자 삭제(백스페이스). 2회: 입력 전체 거부 및 원래 값 복원 · LIST/MISC 페이지에서 R 항목(INTG/HMCS) 선택", 6),
    C("RET_DEPR", (2,6), "RET DEPR Knob", "Rotary knob (continuous, 0~260 mrad)", [("ADJ", "MAN 폭격 시 HUD 가변 조준선 상하 이동")], 4),

    C("BRT", (3,1), "BRT Knob", "Rotary knob (continuous)", [("ADJ", "HUD 래스터 밝기 — Block 50 비기능")], 8, note="비기능"),
    KEY(4, (3,2), "STPT", ""), KEY(5, (3,3), "CRUS", " · CRUS는 마지막 활성 모드(TOS/RNG/HOME/EDR) 페이지로 진입"), KEY(6, (3,4), "TIME", ""),
    BTN("ENTR", (3,5), "ENTR Button", "강조된 데이터 필드에 입력값 확정 · LIST/MISC 페이지에서 E 항목(DLNK/HTS) 선택", 7),
    BTN("WX", (3,6), "WX Button (TFR)", "지형추적 레이더 WX — Block 50 비기능", 14, note="비기능"),

    KEY(7, (4,2), "MARK", ""), KEY(8, (4,3), "FIX", ""), KEY(9, (4,4), "A-CAL", ""),
    C("FLIR_INCDEC", (4,6), "FLIR Increment/Decrement Rocker", "2-way momentary rocker", [("INC", "비기능"), ("DEC", "비기능")], 14, note="Block 50 비기능"),

    C("INCDEC", (5,1), "DED Increment/Decrement Rocker", "2-way momentary rocker",
      [("INC", "DED 상하 화살표(↕)가 붙은 필드 값 증가 — 스티어포인트 다음, 무선 프리셋 다음, TIME 페이지 HACK 시작/정지"),
       ("DEC", "필드 값 감소 — 스티어포인트 이전, 무선 프리셋 이전, TIME 페이지 HACK 제로화")], 11),
    C("DCS", (5,2), "Data Control Switch (DCS, Dobber)", "4-way momentary switch (center return)",
      [("RTN", "DED를 CNI 페이지로 복귀 (미확정 입력 삭제)"),
       ("SEQ", "페이지별 — CRUS: TOS→RNG→HOME→EDR 순환, CNI: 바람 표시 토글, MODE: A-A/A-G 토글, 기타 대부분 기능 없음"),
       ("UP", "DED 별표(asterisk)를 이전 데이터 필드로 이동"),
       ("DN", "DED 별표를 다음 데이터 필드로 이동")], 12),
    C("DRIFT_CO", (5,3), "DRIFT C/O & WARN RESET Switch", "3-position toggle switch (WARN RESET→NORM spring-loaded)",
      [("DRIFT_CO", "FPM을 HUD 중앙, 자세 바를 보어사이트 십자에 수평 케이지 (측풍/INS ATT 모드 시)"),
       ("NORM", "FPM·자세 바가 실제 비행경로를 따라 좌우 이동"),
       ("WARN_RESET", "순간 위치 — HUD 경고 및 음성 메시지 리셋, HUD 최대 G 1.0으로 리셋")], 13),
    C("KEY_0", (5,4), "Keypad 0 / M-SEL", "Push button (momentary)",
      [("PUSH", "숫자 0 입력 · 음수 부호 입력 · 별표 위치 필드의 모드/설정 활성-비활성 토글(M-SEL) · LIST에서 MISC 페이지, MISC에서 HARM 페이지 진입")], 10,
      push="PUSH", note="페이지별 동작은 DED_FIELDS.edit_method 참조"),
    C("FLIR_GAIN", (5,5), "FLIR GAIN/LVL/AUTO Switch", "3-position toggle switch",
      [("GAIN", "비기능"), ("LVL", "비기능"), ("AUTO", "비기능")], 14, note="Block 50 비기능"),
    C("CONT", (5,6), "CONT Knob", "Rotary knob (continuous)", [("ADJ", "HUD 래스터 대비 — Block 50 비기능")], 9, note="비기능"),
], note="C&I 노브=UFC일 때 사용 가능. 키패드 버튼의 의미는 현재 DED 페이지에 따라 달라짐 → DED_PAGES / DED_TRANSITIONS / DED_FIELDS 참조")

# ───────────── DED_PAGES ─────────────
# page_id, page_name, group, access_from, access_input, implemented, fields_filled, source_page, note
DED_PAGES = [
 ["CNI", "CNI (Communications/Navigation/IFF)", "HOME", "ANY", "ICP.DCS.RTN", "Y", "Y", "103-104", "기본(홈) 페이지. 전원 인가 시 표시. Priority 키패드는 이 페이지에서만 동작"],
 ["UHF", "UHF Radio", "OVERRIDE", "ANY", "ICP.COM1", "Y", "PARTIAL", "104", "상세는 Radio Communications 장"],
 ["VHF", "VHF Radio", "OVERRIDE", "ANY", "ICP.COM2", "Y", "PARTIAL", "104", "상세는 Radio Communications 장"],
 ["IFF", "IFF", "OVERRIDE", "ANY", "ICP.IFF", "N", "N", "105", NI],
 ["LIST", "LIST (secondary menu)", "OVERRIDE", "ANY", "ICP.LIST", "Y", "Y", "105,117", "메뉴 페이지 — 키패드로 하위 페이지 선택"],
 ["T_ILS", "T-ILS (TACAN / ILS)", "PRIORITY", "CNI", "ICP.KEY_1", "Y", "N", "106", "TACAN·ILS 장 참조"],
 ["ALOW", "ALOW (Altitude Low)", "PRIORITY", "CNI", "ICP.KEY_2", "Y", "Y", "107", ""],
 ["STPT", "STPT (Steerpoint)", "PRIORITY", "CNI", "ICP.KEY_4", "Y", "N", "106", "Navigation 장 참조"],
 ["CRUS_TOS", "CRUS TOS (Time Over Steerpoint)", "PRIORITY", "CNI", "ICP.KEY_5", "Y", "Y", "108-109", "KEY_5는 마지막 활성 CRUS 모드 페이지로 진입(기본 TOS)"],
 ["CRUS_RNG", "CRUS RNG (Range)", "PRIORITY", "CRUS_TOS", "ICP.DCS.SEQ", "Y", "Y", "110-111", ""],
 ["CRUS_HOME", "CRUS HOME", "PRIORITY", "CRUS_RNG", "ICP.DCS.SEQ", "Y", "Y", "112-113", ""],
 ["CRUS_EDR", "CRUS EDR (Endurance)", "PRIORITY", "CRUS_HOME", "ICP.DCS.SEQ", "Y", "Y", "114-115", ""],
 ["TIME", "TIME", "PRIORITY", "CNI", "ICP.KEY_6", "Y", "Y", "116", ""],
 ["MARK", "MARK", "PRIORITY", "CNI", "ICP.KEY_7", "Y", "N", "106", "Navigation 장 참조"],
 ["FIX", "FIX", "PRIORITY", "CNI", "ICP.KEY_8", "Y", "N", "106", "Navigation Updates 장 참조"],
 ["A_CAL", "A-CAL (Altitude Calibration)", "PRIORITY", "CNI", "ICP.KEY_9", "Y", "N", "106", "Navigation Updates 장 참조"],
 ["DEST", "DEST (Destination)", "LIST", "LIST", "ICP.KEY_1", "Y", "N", "117", "Editing a Steerpoint 장 참조"],
 ["BNGO", "BNGO (Bingo)", "LIST", "LIST", "ICP.KEY_2", "Y", "Y", "118", ""],
 ["VIP", "VIP (Visual Initial Point)", "LIST", "LIST", "ICP.KEY_3", "Y", "N", "117", "VRP/VIP 장 참조"],
 ["INTG", "INTG (Interrogator)", "LIST", "LIST", "ICP.RCL", "N", "N", "117", NI],
 ["NAV", "NAV (Navigation Status)", "LIST", "LIST", "ICP.KEY_4", "Y", "N", "117", "Navigation Solutions 장 참조"],
 ["MAN", "MAN (Manual gun/ballistics)", "LIST", "LIST", "ICP.KEY_5", "Y", "Y", "119", ""],
 ["INS", "INS", "LIST", "LIST", "ICP.KEY_6", "Y", "N", "117", "INS Alignment 장 참조"],
 ["DLNK", "DLNK (Datalink)", "LIST", "LIST", "ICP.ENTR", "Y", "N", "117", "TNDL 장 참조"],
 ["CMDS", "CMDS", "LIST", "LIST", "ICP.KEY_7", "Y", "N", "117", "Defensive Systems 장 참조"],
 ["MODE", "MODE (Master mode backup)", "LIST", "LIST", "ICP.KEY_8", "Y", "Y", "120", ""],
 ["VRP", "VRP (Visual Reference Point)", "LIST", "LIST", "ICP.KEY_9", "Y", "N", "117", "VRP/VIP 장 참조"],
 ["MISC", "MISC (misc menu)", "LIST", "LIST", "ICP.KEY_0", "Y", "Y", "121", "메뉴 페이지"],
 ["CORR", "CORR", "MISC", "MISC", "ICP.KEY_1", "N", "N", "121", NI],
 ["MAGV", "MAGV (Magnetic Variation)", "MISC", "MISC", "ICP.KEY_2", "Y", "N", "121", "INS Alignment 장 참조"],
 ["OFP", "OFP", "MISC", "MISC", "ICP.KEY_3", "N", "N", "121", NI],
 ["HMCS", "HMCS Display", "MISC", "MISC", "ICP.RCL", "Y", "N", "121", "JHMCS 장 참조"],
 ["INSM", "INSM", "MISC", "MISC", "ICP.KEY_4", "N", "N", "121", NI],
 ["LASR", "LASR (Laser codes)", "MISC", "MISC", "ICP.KEY_5", "Y", "N", "121", "AAQ-33 장 참조"],
 ["GPS", "GPS", "MISC", "MISC", "ICP.KEY_6", "N", "N", "121", NI],
 ["HTS", "HTS (HARM Targeting System)", "MISC", "MISC", "ICP.ENTR", "Y", "N", "121", "ASQ-213 장 참조"],
 ["DRNG", "DRNG", "MISC", "MISC", "ICP.KEY_7", "N", "N", "121", NI],
 ["BULL", "BULL (Bullseye)", "MISC", "MISC", "ICP.KEY_8", "Y", "N", "121", "Bullseye 장 참조"],
 ["HARM", "HARM (HARM tables)", "MISC", "MISC", "ICP.KEY_0", "Y", "N", "121", "AGM-88 장 참조"],
]

# ───────────── DED_TRANSITIONS ─────────────
# from_page, input, to_page, note
_T = []
def T(f, i, t, n=""): _T.append([f, i, t, n])
for btn, pg in (("ICP.COM1", "UHF"), ("ICP.COM2", "VHF"), ("ICP.IFF", "IFF"), ("ICP.LIST", "LIST")):
    T("ANY", btn, pg, "오버라이드 — 현재 페이지와 무관하게 진입")
    T(pg, btn, "PREV", "같은 오버라이드 버튼 재누름 → 직전 페이지 복귀")
T("ANY", "ICP.DCS.RTN", "CNI", "미확정 입력 삭제. CNI로 복귀")
for k, pg in ((1, "T_ILS"), (2, "ALOW"), (4, "STPT"), (5, "CRUS_TOS"), (6, "TIME"), (7, "MARK"), (8, "FIX"), (9, "A_CAL")):
    T("CNI", f"ICP.KEY_{k}", pg, "Priority Function — CNI 페이지에서만" + (" (마지막 활성 CRUS 모드 페이지로)" if k == 5 else ""))
T("CNI", "ICP.KEY_3", "CNI", "기능 없음 (CNI에서 3번 페이지 없음)")
T("CNI", "ICP.DCS.SEQ", "CNI", "바람 방향/속도 표시 토글 (페이지 이동 없음)")
T("CRUS_TOS", "ICP.DCS.SEQ", "CRUS_RNG"); T("CRUS_RNG", "ICP.DCS.SEQ", "CRUS_HOME")
T("CRUS_HOME", "ICP.DCS.SEQ", "CRUS_EDR"); T("CRUS_EDR", "ICP.DCS.SEQ", "CRUS_TOS")
for k, pg in ((1, "DEST"), (2, "BNGO"), (3, "VIP"), (4, "NAV"), (5, "MAN"), (6, "INS"), (7, "CMDS"), (8, "MODE"), (9, "VRP"), (0, "MISC")):
    T("LIST", f"ICP.KEY_{k}", pg)
T("LIST", "ICP.RCL", "INTG", "R 항목 = RCL 버튼 — " + NI); T("LIST", "ICP.ENTR", "DLNK", "E 항목 = ENTR 버튼")
for k, pg in ((1, "CORR"), (2, "MAGV"), (3, "OFP"), (4, "INSM"), (5, "LASR"), (6, "GPS"), (7, "DRNG"), (8, "BULL"), (0, "HARM")):
    T("MISC", f"ICP.KEY_{k}", pg)
T("MISC", "ICP.RCL", "HMCS", "R 항목 = RCL 버튼"); T("MISC", "ICP.ENTR", "HTS", "E 항목 = ENTR 버튼")
T("MODE", "ICP.DCS.SEQ", "MODE", "A-A ↔ A-G 표시 토글 (키패드 아무 키도 동일)")
T("ANY", "ICP.AA", "(no change)", "DED 이동 없음 — 마스터모드만 변경")
T("ANY", "ICP.AG", "(no change)", "DED 이동 없음 — 마스터모드만 변경")
DED_TRANSITIONS = [[f"TR{i+1:03d}"] + r for i, r in enumerate(_T)]

# ───────────── DED_FIELDS ─────────────
# page_id, field_no, label, editable, edit_method, value_format, asterisk_default, description, dcs_ni
# edit_method: KEYPAD_ENTR | MSEL_TOGGLE | INCDEC_CYCLE | INCDEC_SPECIAL | SEQ_TOGGLE | DISPLAY
_F = []
def F(pg, no, label, editable, method, fmt, ast, desc, ni=""):
    _F.append([f"{pg}.{label}", pg, no, label, editable, method, fmt, ast, desc, ni])

F("CNI", 1, "UHF_FREQ", "Y", "INCDEC_CYCLE", "채널 번호 또는 MHz", "N", "ARC-164 UHF 현재 프리셋 채널/수동 주파수. 별표가 이 필드에 있고 프리셋 동조 시 INC/DEC로 채널 순환")
F("CNI", 2, "UHF_STATUS", "N", "DISPLAY", "(공백)/GRD/BUP/OFF", "N", "공백=UFC 제어 중, GRD=243.0 Guard, BUP=백업 패널 제어, OFF=전원 OFF")
F("CNI", 3, "VHF_FREQ", "Y", "INCDEC_CYCLE", "채널 번호 또는 MHz", "N", "ARC-222 VHF 현재 프리셋/수동 주파수. 프리셋 동조 시 INC/DEC 순환")
F("CNI", 4, "VHF_STATUS", "N", "DISPLAY", "(공백)/GRD/BUP/OFF", "N", "공백=UFC 제어 중, GRD=121.5 Guard, BUP=BACKUP 모드(제어 불가), OFF")
F("CNI", 5, "IFF_MODES", "N", "DISPLAY", "M 코드", "N", "활성 IFF/트랜스폰더 모드", NI)
F("CNI", 6, "M3_CODE", "N", "DISPLAY", "4자리", "N", "Mode 3 트랜스폰더 코드", NI)
F("CNI", 7, "IFF_STATUS", "N", "DISPLAY", "(공백)/BUP", "N", "공백=UFC(IFF DED 페이지) 제어, BUP=IFF 제어판 제어")
F("CNI", 8, "INCDEC_SYMBOL", "N", "DISPLAY", "↕", "N", "INC/DEC 로커가 적용될 필드 표시. DCS UP/DN으로 이동")
F("CNI", 9, "STPT", "Y", "INCDEC_CYCLE", "정수", "Y", "선택 스티어포인트. 별표 인접 시 INC/DEC로 다음/이전 스티어포인트")
F("CNI", 10, "WIND", "N", "SEQ_TOGGLE", "DDD° / KTS", "N", "CADC 산출 자북 풍향/풍속. DCS SEQ로 표시 토글. 산출 불가 시 DFLT 표시")
F("CNI", 11, "SYS_TIME", "N", "DISPLAY", "HH:MM:SS (Zulu)", "N", "GPS 기반 자동 입력 시스템 시각")
F("CNI", 12, "HACK_TIME", "N", "DISPLAY", "HH:MM:SS", "N", "TIME 페이지에서 설정한 HACK 시각. 제로화 시 CNI에서 사라짐")
F("CNI", 13, "TACAN", "N", "DISPLAY", "T chXY / 거리 NM / -----", "N", "T 21X=REC 또는 T/R 모드 채널·밴드, 숫자=A/A T/R 거리(0.1~99.9 NM), -----=A/A T/R 거리 없음")

F("UHF", 1, "MODE", "N", "DISPLAY", "BOTH/MAIN 등", "N", "UHF 운용 모드", "Radio 장 참조")
F("UHF", 2, "ACTIVE_FREQ", "N", "DISPLAY", "MHz", "N", "현재 동조 주파수")
F("UHF", 3, "SCRATCHPAD", "Y", "KEYPAD_ENTR", "MHz 또는 프리셋 번호", "Y", "키패드로 주파수/프리셋 입력 후 ENTR")
F("UHF", 4, "PRE", "Y", "INCDEC_CYCLE", "1~20", "N", "프리셋 채널 — INC/DEC로 순환")
F("UHF", 5, "TOD", "N", "DISPLAY", "", "N", "Time of Day 송신", "Radio 장 참조")
F("UHF", 6, "NB", "N", "DISPLAY", "NB/WB", "N", "대역폭", "Radio 장 참조")
for no, (lab, desc) in enumerate((("MODE", "VHF 운용 모드"), ("ACTIVE_FREQ", "현재 동조 주파수"), ("SCRATCHPAD", "키패드 입력 후 ENTR"), ("PRE", "프리셋 채널 INC/DEC 순환"), ("GUARD_FREQ", "121.5 표시 등")), start=1):
    F("VHF", no, lab, "Y" if lab in ("SCRATCHPAD", "PRE") else "N", "KEYPAD_ENTR" if lab == "SCRATCHPAD" else ("INCDEC_CYCLE" if lab == "PRE" else "DISPLAY"), "", "Y" if lab == "SCRATCHPAD" else "N", desc, "Radio 장 참조")

F("ALOW", 1, "CARA_ALOW", "Y", "KEYPAD_ENTR", "ft AGL (정수)", "Y", "레이더 고도계 기준 저고도 경고 고도. 이하 시 HUD ALOW 점멸 + 'Altitude…altitude' 음성. 레이더 고도계 송신 중이어야 함, 기어 다운 시 음성 억제")
F("ALOW", 2, "MSL_FLOOR", "Y", "KEYPAD_ENTR", "ft MSL (정수)", "N", "기압 고도계 기준 저고도 경고 고도. 이하 시 음성 경고")
F("ALOW", 3, "STPT", "Y", "INCDEC_CYCLE", "정수", "N", "선택 스티어포인트")

F("CRUS_TOS", 1, "MODE_SEL", "Y", "MSEL_TOGGLE", "TOS 강조/비강조", "Y", "0/M-SEL로 CRUS TOS 모드 활성/비활성. 활성 시 HUD 속도 캐럿 + ETA 표시. CRUS 모드는 하나만 활성")
F("CRUS_TOS", 2, "SYS_TIME", "N", "DISPLAY", "HH:MM:SS", "N", "시스템 시각")
F("CRUS_TOS", 3, "DES_TOS", "Y", "KEYPAD_ENTR", "HH:MM:SS", "N", "선택 스티어포인트의 목표 통과 시각. 무효(음수) 시 공백")
F("CRUS_TOS", 4, "ETA", "N", "DISPLAY", "#n HH:MM:SS", "N", "유효 TOS가 있는 다음 스티어포인트 번호와 현재 지상속도 기준 도착 예정 시각")
F("CRUS_TOS", 5, "REQ_GS", "N", "DISPLAY", "KTS", "N", "다음 유효 TOS 스티어포인트 정시 도착에 필요한 지상속도")
F("CRUS_TOS", 6, "STPT", "Y", "INCDEC_CYCLE", "정수", "N", "선택 스티어포인트")

F("CRUS_RNG", 1, "MODE_SEL", "Y", "MSEL_TOGGLE", "RNG 강조/비강조", "Y", "0/M-SEL로 CRUS RNG 모드 활성/비활성. 활성 시 HUD에 최대 항속거리 속도 캐럿")
F("CRUS_RNG", 2, "STPT", "Y", "INCDEC_CYCLE", "정수", "N", "선택 스티어포인트")
F("CRUS_RNG", 3, "FUEL", "N", "DISPLAY", "LBS", "N", "현재 속도·연료 소모·바람 기준 선택 스티어포인트 도착 시 잔여 연료 추정 (기어 다운 시 마지막 값 유지)")
F("CRUS_RNG", 4, "WIND", "N", "DISPLAY", "DDD° KTS", "N", "CADC 풍향/풍속")

F("CRUS_HOME", 1, "MODE_SEL", "Y", "MSEL_TOGGLE", "HOME 강조/비강조", "Y", "0/M-SEL로 CRUS HOME 모드 활성/비활성. 활성 시 HMPT가 선택 스티어포인트가 되고 HUD에 속도·고도 캐럿, HUD 좌하단에 Home 도착 연료(100 lb 단위)")
F("CRUS_HOME", 2, "HMPT", "Y", "KEYPAD_ENTR", "정수 (INC/DEC도 가능)", "N", "Home 포인트 스티어포인트 번호 — INC/DEC 순환 또는 별표 위치 후 키패드 입력+ENTR")
F("CRUS_HOME", 3, "FUEL", "N", "DISPLAY", "LBS", "N", "최적 속도·고도로 비행 시 Home 도착 잔여 연료 추정")
F("CRUS_HOME", 4, "OPT_ALT", "N", "DISPLAY", "FT", "N", "현재 총중량 기준 최적 순항 고도 (연료 소모에 따라 상승)")
F("CRUS_HOME", 5, "WIND", "N", "DISPLAY", "DDD° KTS", "N", "CADC 풍향/풍속")

F("CRUS_EDR", 1, "MODE_SEL", "Y", "MSEL_TOGGLE", "EDR 강조/비강조", "Y", "0/M-SEL로 CRUS EDR 모드 활성/비활성. 활성 시 HUD에 최대 체공 마하 속도 캐럿")
F("CRUS_EDR", 2, "STPT", "Y", "INCDEC_CYCLE", "정수", "N", "선택 스티어포인트")
F("CRUS_EDR", 3, "TO_BNGO", "N", "DISPLAY", "HH:MM:SS", "N", "현재 소모율 기준 BNGO 설정값 도달까지 남은 시간")
F("CRUS_EDR", 4, "OPT_MACH", "N", "DISPLAY", "Mach", "N", "현재 고도 기준 최대 체공 마하")
F("CRUS_EDR", 5, "WIND", "N", "DISPLAY", "DDD° KTS", "N", "CADC 풍향/풍속")

F("TIME", 1, "SYS_TIME", "Y", "KEYPAD_ENTR", "HHMMSS", "Y", "Zulu 시스템 시각. GPS 가용 시 자동('GPS SYSTEM' 표시), 수동 입력 시 'SYSTEM'")
F("TIME", 2, "HACK", "Y", "INCDEC_SPECIAL", "HHMMSS", "N", "독립 시각 참조/스톱워치. 키패드+ENTR로 설정, INC=시작/정지(freeze) 토글, DEC=제로화(CNI에서 제거)")
F("TIME", 3, "DELTA_TOS", "Y", "KEYPAD_ENTR", "±HHMMSS (-23:59:59~23:59:59)", "N", "모든 스티어포인트 TOS를 일괄 이동. 음수는 0/M-SEL로 '-' 입력 후 값. 누적 적용, 페이지 벗어나면 0으로 표시되나 적용은 유지")
F("TIME", 4, "DATE", "N", "DISPLAY", "MM/DD/YY", "N", "GPS 기반 자동 시스템 날짜")

F("BNGO", 1, "SET", "Y", "KEYPAD_ENTR", "LBS (정수)", "Y", "Bingo 연료. 총연료가 이하로 떨어지면 HUD 좌하단 Bingo 표시 + 'Bingo…bingo' 음성 + HUD 중앙 FUEL 점멸(WARN RESET으로 확인)")
F("BNGO", 2, "TOTAL", "N", "DISPLAY", "LBS", "N", "외부탱크 포함 총 탑재 연료")
F("BNGO", 3, "STPT", "Y", "INCDEC_CYCLE", "정수", "N", "선택 스티어포인트")

F("MAN", 1, "WSPAN", "Y", "KEYPAD_ENTR", "FT (정수)", "Y", "EEGS 퍼널 폭 기준 표적 날개폭 (Level 2 EEGS 시 중요)")
F("MAN", 2, "RNG", "N", "DISPLAY", "FT", "N", "자유낙하 무장 수평 비행거리", NI)
F("MAN", 3, "TOF", "N", "DISPLAY", "SEC", "N", "투하~탄착 시간", NI)
F("MAN", 4, "STPT", "Y", "INCDEC_CYCLE", "정수", "N", "선택 스티어포인트")

F("MODE", 1, "MODE_SEL", "Y", "MSEL_TOGGLE", "A-A / A-G", "Y", "표시된 모드로 0/M-SEL 누르면 해당 마스터모드 진입. SEQ 또는 키패드 아무 키로 A-A↔A-G 토글. 현재 모드와 같으면 강조 표시, 그 상태에서 M-SEL 시 NAV. 스로틀 Dogfight 스위치가 DGFT/MSL OVRD면 비기능")

F("LIST", 1, "MENU", "N", "DISPLAY", "1 DEST 2 BNGO 3 VIP R INTG / 4 NAV 5 MAN 6 INS E DLNK / 7 CMDS 8 MODE 9 VRP 0 MISC", "N", "키패드/RCL/ENTR로 하위 페이지 선택 (DED_TRANSITIONS 참조)")
F("MISC", 1, "MENU", "N", "DISPLAY", "1 CORR 2 MAGV 3 OFP R HMCS / 4 INSM 5 LASR 6 GPS E HTS / 7 DRNG 8 BULL 0 HARM", "N", "키패드/RCL/ENTR로 하위 페이지 선택")
DED_FIELDS = _F

# ───────────── ICP_ACTIONS (샘플) ─────────────
# action_id, goal, precondition_page, input_sequence, verify, source_page, note
ICP_ACTIONS = [
 ["ICP.RETURN_CNI", "DED를 CNI 홈 페이지로 복귀", "ANY", "ICP.DCS.RTN", "DED 1행에 'UHF', 3행에 'VHF', 5행 'M'/'T' 표시", "101,103", "모든 ICP 매크로의 시작·종료 상태"],
 ["ICP.SET_ALOW_CARA", "CARA ALOW(레이더 고도 저고도 경고) 설정 — 예: 1500 ft", "CNI", "ICP.DCS.RTN > ICP.KEY_2 > ICP.KEY_1 > ICP.KEY_5 > ICP.KEY_0 > ICP.KEY_0 > ICP.ENTR > ICP.DCS.RTN", "ALOW 페이지 2행 'CARA ALOW  1500FT' (강조 해제). HUD 하단 'AL 1500'", "107", "ALOW 진입 시 별표 기본 위치 = CARA ALOW. SNSRPWR.RDR_ALT.RDR_ALT 필요"],
 ["ICP.SET_ALOW_MSL", "MSL FLOOR 설정 — 예: 10000 ft", "CNI", "ICP.DCS.RTN > ICP.KEY_2 > ICP.DCS.DN > ICP.KEY_1 > ICP.KEY_0 x4 > ICP.ENTR > ICP.DCS.RTN", "ALOW 페이지 3행 'MSL FLOOR 10000FT'", "107", "별표를 MSL FLOOR로 DN 1회 이동"],
 ["ICP.SET_BINGO", "Bingo 연료 설정 — 예: 3500 lb", "CNI", "ICP.DCS.RTN > ICP.LIST > ICP.KEY_2 > ICP.KEY_3 > ICP.KEY_5 > ICP.KEY_0 > ICP.KEY_0 > ICP.ENTR > ICP.DCS.RTN", "BNGO 페이지 2행 'SET  3500LBS'", "118", "BNGO 진입 시 별표 기본 위치 = SET"],
 ["ICP.SELECT_STPT_NEXT", "다음 스티어포인트 선택", "CNI", "ICP.DCS.RTN > (별표가 STPT에 없으면 ICP.DCS.DN/UP) > ICP.INCDEC.INC", "CNI 1행 우측 'STPT ↕ n+1', HUD 스티어포인트 번호 증가", "103", "별표 위치는 DED 1행 'STPT' 옆 ↕ 확인"],
 ["ICP.SELECT_STPT_DIRECT", "특정 스티어포인트 직접 선택 — 예: 7번", "CNI", "ICP.DCS.RTN > ICP.KEY_4 > ICP.KEY_7 > ICP.ENTR > ICP.DCS.RTN", "CNI 'STPT 7'", "106", "STPT 페이지 필드 상세는 Navigation 장에서 보완"],
 ["ICP.ENABLE_CRUS_TOS", "CRUS TOS 모드 활성 (HUD 속도 캐럿)", "CNI", "ICP.DCS.RTN > ICP.KEY_5 > (TOS 페이지 아니면 ICP.DCS.SEQ 반복) > ICP.KEY_0 > ICP.DCS.RTN", "CRUS 페이지 1행 'TOS' 강조, HUD 속도 눈금에 캐럿·ETA 표시", "108-109", "KEY_5는 마지막 활성 CRUS 모드로 진입하므로 SEQ로 TOS까지 순환 필요"],
 ["ICP.ENABLE_CRUS_HOME", "CRUS HOME 모드 활성 + Home 포인트 지정 — 예: 11번", "CNI", "ICP.DCS.RTN > ICP.KEY_5 > ICP.DCS.SEQ x(HOME까지) > ICP.DCS.DN > ICP.KEY_1 > ICP.KEY_1 > ICP.ENTR > ICP.DCS.UP > ICP.KEY_0 > ICP.DCS.RTN", "CRUS 페이지 'HOME' 강조, 'HMPT 11', HUD 좌하단 Home 도착 연료", "112-113", ""],
 ["ICP.HACK_START", "HACK 타이머 시작/정지", "CNI", "ICP.DCS.RTN > ICP.KEY_6 > ICP.DCS.DN > ICP.INCDEC.INC > ICP.DCS.RTN", "TIME 페이지 HACK 진행, CNI 4행에 HACK 시각 표시", "116", "DEC = 제로화"],
 ["ICP.SET_DELTA_TOS", "전체 TOS 일괄 이동 — 예: -5분", "CNI", "ICP.DCS.RTN > ICP.KEY_6 > ICP.DCS.DN x2 > ICP.KEY_0 > ICP.KEY_0 > ICP.KEY_0 > ICP.KEY_5 > ICP.KEY_0 > ICP.KEY_0 > ICP.ENTR > ICP.DCS.RTN", "모든 STPT TOS 5분 앞당겨짐 (CRUS TOS 페이지 DES TOS로 확인)", "116", "첫 KEY_0 = 음수 부호 (별표가 DELTA TOS에 있을 때)"],
 ["ICP.MASTER_MODE_AA", "A-A 마스터모드", "ANY", "ICP.AA", "HUD 좌하단 마스터모드 표시 'AA' / MFD FCR A-A 모드", "99", "재누름 시 NAV"],
 ["ICP.MASTER_MODE_AG", "A-G 마스터모드", "ANY", "ICP.AG", "HUD 'AG'", "99", "재누름 시 NAV"],
 ["ICP.MASTER_MODE_NAV", "NAV 마스터모드 복귀", "ANY", "ICP.AA 또는 ICP.AG (현재 활성 모드 버튼 재누름)", "HUD 'NAV'", "99", "백업: LIST > KEY_8(MODE) > 현재 모드 강조 상태에서 KEY_0"],
 ["ICP.WARN_RESET", "HUD 경고/음성 리셋, 최대 G 리셋", "ANY", "ICP.DRIFT_CO.WARN_RESET", "HUD 중앙 점멸 경고 소거", "100", "스프링 복귀"],
 ["ICP.TUNE_UHF_MANUAL", "UHF 수동 주파수 입력 — 예: 305.00", "ANY", "ICP.COM1 > ICP.KEY_3 > ICP.KEY_0 > ICP.KEY_5 > ICP.ENTR > ICP.COM1", "CNI 1행 'UHF 305.00'", "104", "입력 규칙(소수점 생략 등)은 Radio Communications 장에서 보완"],
 ["ICP.TUNE_UHF_PRESET", "UHF 프리셋 채널 선택 — 예: 4", "ANY", "ICP.COM1 > ICP.DCS.DN (별표를 PRE로) > ICP.INCDEC.INC/DEC 또는 ICP.KEY_4 > ICP.ENTR > ICP.COM1", "UHF 페이지 'PRE 4', CNI 1행 채널 표시", "104", "Radio 장에서 보완"],
]
