# -*- coding: utf-8 -*-
# CMDS (AN/ALE-47) 제어판 + CMDS DED 페이지 — DCS F-16C Early Access Guide EN p.697-702
from dcs_panels import C, IND, P, NI

CMDS = P("CMDS", "CMDS", "CMDS CONTROL PANEL (AN/ALE-47)", "Left Auxiliary Console (LG 패널 우하단)", "697-699", 4, 5, [
    C("STATUS", (1,2), "STATUS Display", "Indicator (3-state)",
      [("NO_GO", "CMDS 전원 ON이나 고장 — 투발 불가"),
       ("GO", "CMDS 전원 ON, 투발 준비 완료"),
       ("DISPENSE_RDY", "위협에 대응해 투발 준비 — MODE=SEMI 시 조종사 동의(CMS Aft) 필요. BINGO DED 페이지 REQCTR ON이면 'Counter' 음성 동반")], 1),
    IND("QTY", (1,4), "Quantity Display (O1 / O2 / CH / FL)", "탑재 대응책 종류별 잔량. 해당 스위치 ON 시만 표시. BINGO 수량 이하 시 'LO' 표시(+BINGO 음성 ON 시 'Low' 음성). 시스템 고장 메시지도 표시", 2),
    C("RWR", (2,1), "RWR Switch", "2-position toggle switch",
      [("ON", "MODE=SEMI/AUTO 시 ALR-56M RWR 위협 정보로 자동 프로그램 선택 허용"), ("OFF", "RWR 연동 차단")], 3),
    C("O1", (2,2), "O1 Switch", "2-position toggle switch", [("ON", "기능 없음"), ("OFF", "기능 없음")], 4, note="No function"),
    C("O2", (2,3), "O2 Switch", "2-position toggle switch", [("ON", "기능 없음"), ("OFF", "기능 없음")], 4, note="No function"),
    C("CH", (2,4), "CH Switch", "2-position toggle switch",
      [("ON", "채프 투발 활성, 잔량 표시"), ("OFF", "채프 투발 차단")], 4),
    C("FL", (2,5), "FL Switch", "2-position toggle switch",
      [("ON", "플레어 투발 활성, 잔량 표시"), ("OFF", "플레어 투발 차단")], 4),
    C("JMR", (3,1), "JMR Switch", "2-position toggle switch", [("ON", "기능 없음"), ("OFF", "기능 없음")], 5, note="No function"),
    C("JETT", (3,3), "JETT Switch", "2-position toggle switch",
      [("JETT", "전방 위치 — MODE 노브와 무관하게 탑재 대응책 전량 동시 투발"), ("OFF", "정상")], 7),
    C("PRGM", (3,4), "PRGM Knob", "5-position rotary knob",
      [("BIT", "CMDS BIT 시작 — " + NI), ("1", "Manual Program 1 선택"), ("2", "Manual Program 2 선택"),
       ("3", "Manual Program 3 선택"), ("4", "Manual Program 4 선택")], 8,
      note="MODE=MAN/SEMI/AUTO에서 CMS Forward로 선택 프로그램 투발. Program 5 = 좌측 벽 CHAFF/FLARE 버튼, Program 6 = CMS Left"),
    C("MODE", (3,5), "MODE Knob", "6-position rotary knob",
      [("OFF", "CMDS 전원 OFF — JETT 제외 투발 불가, ECM 포드 방사 불가"),
       ("STBY", "전원 ON, 투발 불가(JETT 제외). CMDS DED 페이지 설정 변경은 이 위치에서. ECM 방사 불가"),
       ("MAN", "수동 프로그램만 투발. CMS Aft=ECM 잡음 재밍 ON(XMIT=3 시), CMS Right=ECM OFF. PRGM 1-4 + 5/6"),
       ("SEMI", "위협 기반 자동 프로그램 선택, 투발은 조종사 동의(CMS Aft) 시 1회. DISPENSE RDY/'Counter' 프롬프트. ECM 기만 재밍은 lock 시 동의 후. 채프 LO 시 자동 프로그램 투발 안 함"),
       ("AUTO", "위협 기반 자동 프로그램을 동의 후 반복 투발(lock 지속 중). CMS Right=동의 철회·진행 중단, CMS Aft=동의. AUTO 진입 시 동의 기본 부여. ECM은 동의 없이 lock 시 방사(XMIT 1/2)"),
       ("BYP", "바이패스 — 다른 모드 고장 시. CMS Forward마다 채프 1 + 플레어 1 투발. 수동 프로그램·기타 CMS 기능 불가")], 9),
    C("MWS", (4,1), "MWS Switch", "2-position toggle switch", [("ON", "기능 없음"), ("OFF", "기능 없음")], 6, note="No function"),
], note="주 투발 조작은 HOTAS CMS(SSC): Fwd=선택 프로그램, Aft=동의/ECM, Left=Program 6, Right=철회/ECM OFF. HOTAS_FUNCTIONS 참조: SSC.CMS.*")

# ── DED: LIST > 7 CMDS → BINGO 페이지, DCS SEQ로 CHAFF → FLARE → OTHER1 → OTHER2 → BINGO 순환
CMDS_DED_PAGES = [
 ["CMDS_BINGO", "CMDS BINGO", "LIST", "LIST", "ICP.KEY_7", "Y", "Y", "700", "채프/플레어 Bingo 수량 및 음성 메시지 토글. 설정 변경 전 CMDS.MODE=STBY 필요"],
 ["CMDS_CHAFF", "CMDS CHAFF (program edit)", "LIST", "CMDS_BINGO", "ICP.DCS.SEQ", "Y", "Y", "701-702", "수동 프로그램 1-6 채프 투발 시퀀스. 변경 전 CMDS.MODE=STBY"],
 ["CMDS_FLARE", "CMDS FLARE (program edit)", "LIST", "CMDS_CHAFF", "ICP.DCS.SEQ", "Y", "Y", "701-702", "수동 프로그램 1-6 플레어 투발 시퀀스. 변경 전 CMDS.MODE=STBY"],
 ["CMDS_OTHER1", "CMDS OTHER1", "LIST", "CMDS_FLARE", "ICP.DCS.SEQ", "N", "Y", "702", "기능 없음 (채프/플레어만 모의)"],
 ["CMDS_OTHER2", "CMDS OTHER2", "LIST", "CMDS_OTHER1", "ICP.DCS.SEQ", "N", "Y", "702", "기능 없음"],
]
CMDS_DED_TRANSITIONS = [
 ["CMDS_BINGO", "ICP.DCS.SEQ", "CMDS_CHAFF", ""],
 ["CMDS_CHAFF", "ICP.DCS.SEQ", "CMDS_FLARE", ""],
 ["CMDS_FLARE", "ICP.DCS.SEQ", "CMDS_OTHER1", ""],
 ["CMDS_OTHER1", "ICP.DCS.SEQ", "CMDS_OTHER2", ""],
 ["CMDS_OTHER2", "ICP.DCS.SEQ", "CMDS_BINGO", "순환 복귀"],
]
_F = []
def F(pg, no, label, editable, method, fmt, ast, desc, ni=""):
    _F.append([f"{pg}.{label}", pg, no, label, editable, method, fmt, ast, desc, ni])
F("CMDS_BINGO", 1, "CH", "Y", "KEYPAD_ENTR", "0~99", "Y", "채프 Bingo('LO') 임계 수량")
F("CMDS_BINGO", 2, "FL", "Y", "KEYPAD_ENTR", "0~99", "N", "플레어 Bingo 임계 수량")
F("CMDS_BINGO", 3, "O1", "N", "DISPLAY", "0", "N", "Other 1 Bingo — 기능 없음", "No function")
F("CMDS_BINGO", 4, "O2", "N", "DISPLAY", "0", "N", "Other 2 Bingo — 기능 없음", "No function")
F("CMDS_BINGO", 5, "STPT", "Y", "INCDEC_CYCLE", "정수", "N", "선택 스티어포인트")
F("CMDS_BINGO", 6, "FDBK", "Y", "KEY_TOGGLE", "ON/OFF", "N", "Feedback 음성: 자동/수동 프로그램 투발 시작 시 'Chaff flare' 음성. 별표 위치에서 키패드 1-9 아무 키로 토글")
F("CMDS_BINGO", 7, "REQCTR", "Y", "KEY_TOGGLE", "ON/OFF", "N", "Request Counter 음성: MODE=SEMI에서 동의 요청 시 'Counter' 음성. 키패드 1-9로 토글")
F("CMDS_BINGO", 8, "BINGO", "Y", "KEY_TOGGLE", "ON/OFF", "N", "Bingo 음성: Bingo 도달 시 'Low', 소진 시 'Out'. 키패드 1-9로 토글")
for pg, cm in (("CMDS_CHAFF", "채프"), ("CMDS_FLARE", "플레어")):
    F(pg, 1, "BQ", "Y", "KEYPAD_ENTR", "0~99", "Y", f"Burst Quantity — 살보당 {cm} 카트리지 수. 0이면 이 프로그램에서 {cm} 미투발")
    F(pg, 2, "BI", "Y", "KEYPAD_ENTR", "0.020~10.000 s (0.001 단위)", "N", "Burst Interval — 살보 내 카트리지 간 간격")
    F(pg, 3, "SQ", "Y", "KEYPAD_ENTR", "0~99", "N", "Salvo Quantity — 프로그램 내 살보 수")
    F(pg, 4, "SI", "Y", "KEYPAD_ENTR", "0.50~150.00 s (0.01 단위)", "N", "Salvo Interval — 살보 간 간격")
    F(pg, 5, "PROG", "Y", "INCDEC_CYCLE", "1~6", "N", "편집 중인 수동 프로그램 번호. 1-4=PRGM 노브+CMS Fwd, 5=좌측 벽 CHAFF/FLARE 버튼, 6=CMS Left")
for pg in ("CMDS_OTHER1", "CMDS_OTHER2"):
    F(pg, 1, "PROG", "N", "DISPLAY", "1~6", "N", "기능 없음", "No function")
CMDS_DED_FIELDS = _F

CMDS_ACTIONS = [
 ["ICP.CMDS_SET_CHAFF_BINGO", "채프 Bingo 수량 설정 — 예: 20", "CNI + CMDS.MODE.STBY", "CMDS.MODE.STBY > ICP.DCS.RTN > ICP.LIST > ICP.KEY_7 > ICP.KEY_2 > ICP.KEY_0 > ICP.ENTR > ICP.DCS.RTN", "CMDS BINGO 페이지 2행 'CH 20'", "700", "BINGO 진입 시 별표 기본 = CH. 설정 후 MODE 원위치"],
 ["ICP.CMDS_SET_FLARE_BINGO", "플레어 Bingo 수량 설정 — 예: 10", "CNI + CMDS.MODE.STBY", "CMDS.MODE.STBY > ICP.DCS.RTN > ICP.LIST > ICP.KEY_7 > ICP.DCS.DN > ICP.KEY_1 > ICP.KEY_0 > ICP.ENTR > ICP.DCS.RTN", "CMDS BINGO 페이지 3행 'FL 10'", "700", ""],
 ["ICP.CMDS_TOGGLE_BINGO_VOICE", "Bingo 음성('Low'/'Out') ON/OFF 토글", "CNI", "ICP.DCS.RTN > ICP.LIST > ICP.KEY_7 > ICP.DCS.DN x(BINGO 필드까지) > ICP.KEY_1 > ICP.DCS.RTN", "BINGO 페이지 4행 'BINGO ON/OFF' 반전", "700", "별표 이동 횟수는 DED_FIELDS field_no 순서 기준(CH→FL→O1→O2→STPT→FDBK→REQCTR→BINGO 중 편집 가능 필드만)"],
 ["ICP.CMDS_SET_CHAFF_PROGRAM", "수동 프로그램 n 채프 시퀀스 설정 — 예: PROG 1, BQ 2 / BI 0.5 / SQ 2 / SI 2.0", "CNI + CMDS.MODE.STBY", "CMDS.MODE.STBY > ICP.DCS.RTN > ICP.LIST > ICP.KEY_7 > ICP.DCS.SEQ > (PROG≠1이면 ICP.INCDEC.INC/DEC) > ICP.KEY_2 > ICP.ENTR > ICP.DCS.DN > ICP.KEY_0 > ICP.KEY_5 > ICP.ENTR > ICP.DCS.DN > ICP.KEY_2 > ICP.ENTR > ICP.DCS.DN > ICP.KEY_2 > ICP.ENTR > ICP.DCS.RTN", "CMDS CHAFF 페이지 'PROG 1', BQ 2 / BI 0.500 / SQ 2 / SI 2.00", "701", "소수 입력 규칙(소수점 생략 여부)은 게임 내 확인 필요"],
 ["ICP.CMDS_SET_FLARE_PROGRAM", "수동 프로그램 n 플레어 시퀀스 설정", "CNI + CMDS.MODE.STBY", "위와 동일하되 ICP.DCS.SEQ x2로 CMDS_FLARE 진입", "CMDS FLARE 페이지 값 반영", "701-702", ""],
 ["CMDS.ARM_SEMI", "CMDS 반자동 운용 세팅 (이륙 전/FENCE IN)", "지상 또는 FENCE IN", "CMDS.RWR.ON > CMDS.CH.ON > CMDS.FL.ON > CMDS.PRGM.1 > CMDS.MODE.SEMI", "STATUS 'GO', QTY에 CH/FL 잔량 표시", "697-699", "AUTO 원하면 MODE.AUTO (진입 시 동의 자동 부여)"],
 ["CMDS.SAFE", "CMDS 안전화 (착륙 후/FENCE OUT)", "ANY", "CMDS.MODE.STBY 또는 CMDS.MODE.OFF", "STATUS 소등 또는 GO(STBY)", "698", ""],
 ["CMDS.JETTISON_ALL", "대응책 전량 비상 투발", "ANY", "CMDS.JETT.JETT", "QTY 0, 'Out' 음성(BINGO 음성 ON 시)", "698", "MODE 무관"],
]
