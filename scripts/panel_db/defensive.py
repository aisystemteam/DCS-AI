# -*- coding: utf-8 -*-
# RWR(ALR-56M) 표시기/제어판 + ECM 제어판 + 좌측 벽 CHAFF/FLARE 버튼 — DCS F-16C EA Guide p.693-696, 706-708
from dcs_panels import C, IND, LIGHT, BTN, P, NI

RWRAZ = P("RWRAZ", "RWR AZIMUTH", "THREAT WARNING AZIMUTH INDICATOR (ALR-56M)", "Instrument Panel (좌측 상단, HUD 좌측)", "694", 1, 2, [
    C("BRT", (1,1), "Brightness Knob", "Rotary knob (continuous)", [("ADJ", "CW 회전 시 방위 표시기 밝기 증가")], 1),
    IND("DISPLAY", (1,2), "Azimuth Display", "360° 탑다운 위협 표시(중심=자기). 외곽=탐색/획득, 흰 원 바깥 사각 강조=추적, 원 안 점멸 원=미사일 유도, 쉐브론=공중 레이더, 다이아몬드=최우선 위협(Handoff Floating 시). 최대 16개(OPEN)/5개(PRIORITY). 중앙 S=Search 모드, L=Low Alt 모드(교대 표시)", None,
        note="고도 커버리지 ±45° — 고피치/롤 기동 시 사각. 심볼 목록은 가이드 부록 B"),
], note="AUDIO 1 THREAT 노브로 경고음 볼륨 조절")

RWRPRIME = P("RWRPRIME", "RWR PRIME", "THREAT WARNING PRIME CONTROL PANEL", "Instrument Panel (방위 표시기 좌측)", "695-696", 4, 2, [
    C("HANDOFF", (1,2), "HANDOFF Button (H / diamond)", "Push button light (short/long press)",
      [("PRESS_SHORT", "<1초: Handoff 모드 Floating ↔ Off 토글. Off 시 버튼 상단 다이아몬드 소등, 표시기 다이아몬드 위협 제거"),
       ("HOLD", ">1초 유지: Transient 모드 — 다이아몬드가 우선순위 내림차순으로 위협을 순환"),
       ("RELEASE", "Transient에서 놓으면 Latched — 우선순위 무관하게 현재 선택 위협에 다이아몬드 고정")], 1),
    LIGHT("LAUNCH", (2,1), "MISSILE LAUNCH Light", "위협 레이더가 미사일 유도 모드 — 'MISSILE LAUNCH' 점멸", 3),
    C("MODE", (2,2), "MODE Button (PRIORITY / OPEN)", "Push button (toggle) + 2 lights",
      [("OPEN", "하단 'OPEN' 점등 — 상위 16개 위협 표시"),
       ("PRIORITY", "상단 'PRIORITY' 점등 — 상위 5개 위협 표시")], 2,
      note="우선순위: 치명도(유도>추적>탐색) → 위협 테이블 내 레이더 유형(HIGH/LOW ALT 테이블은 AUX ALTITUDE 버튼) → 신호 강도"),
    C("UNKNOWN", (3,1), "UNKNOWN Button (U)", "Push button (toggle) + light",
      [("ON", "상단 'U' 점등 — 미식별 레이더를 'U' 심볼로 표시"),
       ("OFF", "미식별 레이더 숨김, 존재 시 'U' 점멸")], 5, note="숨겨지는 레이더 종류는 위협 테이블(DTC) 업로드로 변경"),
    BTN("TGT_SEP", (3,2), "TGT SEP Button", "겹친 위협 심볼을 5초간 방사상으로 분리 표시 ('TGT SEP' 상단 점등)", 4),
    C("SYS_TEST", (4,2), "SYS TEST Button", "Push button (hold 1 s) + light",
      [("HOLD_1S", "1초 유지: 자체 시험 — 'ON' 점등, Prime/Aux 전 버튼 점등, 표시기 진단 메시지, 경고음 순차 재생. 완료 시 자동 복귀"),
       ("PRESS_AGAIN", "시험 중 재누름: 시험 중단")], 6),
])

RWRAUX = P("RWRAUX", "RWR AUX", "THREAT WARNING AUXILIARY CONTROL PANEL", "Left Auxiliary Console (CMDS 좌측)", "696", 3, 2, [
    C("SEARCH", (1,1), "SEARCH Button (S)", "Push button (toggle) + light",
      [("ON", "상단 'S' 점등 — 조기경보/감시/비치명 획득 레이더도 표시. 표시기 중앙 'S'"),
       ("OFF", "해당 레이더 숨김, 존재 시 'S' 점멸")], 1, note="숨겨지는 종류는 위협 테이블로 변경"),
    C("ACT_PWR", (1,2), "ACT/PWR Indicator (ACTIVITY / POWER)", "2 lights (indicator)",
      [("POWER", "하단 'POWER' 점등 — ALR-56M 전원 ON"),
       ("ACTIVITY", "상단 'ACTIVITY' 점등 — 추적 또는 미사일 유도 모드 레이더 감지")], 2),
    C("ALTITUDE", (2,1), "ALTITUDE Button (LOW / ALT)", "Push button (toggle) + 2 lights",
      [("HIGH", "'ALT'만 점등 — 고고도 위협 테이블: 장거리·고고도 방공·전투기 우선 (전투기 스윕/CAP/고고도 공습)"),
       ("LOW", "'LOW'+'ALT' 점등 — 저고도 위협 테이블: 단거리·저고도 방공·전투기 우선 (저고도 공습/차단/CAS). 표시기 중앙 'L'")], 3),
    C("POWER", (2,2), "POWER Button (SYSTEM POWER)", "Push button (toggle) + light",
      [("ON", "'SYSTEM POWER' 점등 — ALR-56M 전원 ON"), ("OFF", "RWR 전원 OFF")], 4),
    C("DIM", (3,2), "DIM Knob", "Rotary knob (continuous)", [("ADJ", "CW 회전 시 Aux·Prime 패널 표시등 밝기 증가")], 5),
])

ECM = P("ECM", "ECM", "ECM CONTROL PANEL (ALQ-131 / ALQ-184)", "Left Console (AVTR와 AUDIO 사이)", "706-707", 3, 7, [
    C("PWR", (1,1), "ECM Power Switch", "3-position toggle switch",
      [("OPR", "포드 작동 — 위협 신호 처리 및 패널/HOTAS 설정에 따라 송신 (STBY 예열 미완 시 완료까지 송신 없음)"),
       ("STBY", "전원 ON + 예열(약 3분), 위협 처리·송신 없음"),
       ("OFF", "포드 전원 OFF")], 1),
    C("XMIT", (2,2), "XMIT Switch", "3-position rotary switch",
      [("1", "기만 재밍 (Avionics Priority) — 추적/교전 시 반응 송신, FCR 계속 동작하나 탐지·락 거리 감소. CMDS MODE=SEMI/AUTO 필요"),
       ("2", "기만 재밍 (ECM Priority) — 반응 송신, FCR 대기(무장 프로파일 AIM-120이면 Avionics Priority). CMDS MODE=SEMI/AUTO 필요"),
       ("3", "잡음 재밍 (ECM Priority) — 선제 연속 송신, FCR 대기. 피탐 가능성 증가. CMDS MODE=MAN 필요")], 2,
      note="실제 송신 개시/중지는 HOTAS CMS Aft/Right"),
    C("DIM", (2,1), "DIM Knob", "Rotary knob (continuous)", [("ADJ", "모듈 버튼 표시등 밝기")], 3),
    BTN("RESET", (3,1), "RESET Button", "기능 없음", 4, note="No function"),
    BTN("BIT", (3,2), "BIT Button", "ECM 포드 자체 시험 — " + NI, 5, note=NI),
    C("MOD_1", (1,3), "Module 1 Button", "Latching push button + S/A/F/T lights", [("IN", "Band 1 모듈 송신 허용"), ("OUT", "Band 1 모듈 비활성")], 6),
    C("MOD_2", (1,4), "Module 2 Button", "Latching push button + S/A/F/T lights", [("IN", "Band 2 모듈 송신 허용"), ("OUT", "비활성")], 6),
    C("MOD_3", (1,5), "Module 3 Button", "Latching push button + S/A/F/T lights", [("IN", "Band 3 모듈 송신 허용"), ("OUT", "비활성")], 6),
    C("MOD_4", (1,6), "Module 4 Button", "Latching push button + S/A/F/T lights", [("IN", "Band 4 모듈 송신 허용"), ("OUT", "비활성")], 6),
    C("MOD_BLANK", (1,7), "Module (blank) Button", "Latching push button + S/A/F/T lights", [("IN", "예비(미표기) 모듈 활성"), ("OUT", "비활성")], 6),
    C("MOD_5", (2,3), "Module 5 Button", "Latching push button + S/A/F/T lights", [("IN", "Band 5 모듈 송신 허용"), ("OUT", "비활성")], 6),
    C("FRM", (2,4), "FRM Button", "Latching push button", [("IN", "기능 없음"), ("OUT", "기능 없음")], 6, note="No function"),
    C("SPL", (2,5), "SPL Button", "Latching push button", [("IN", "기능 없음"), ("OUT", "기능 없음")], 6, note="No function"),
], note="모듈 버튼 상태등: S=대기(전원 ON·송신 불가), A=활성(송신 허용), F=고장, T=송신 중. DCS에서는 모듈 선택이 위협별 효과 차이를 만들지 않음. ALQ-131/184 기능 동일")

CFBTN = P("CFBTN", "CHAFF-FLARE BTN", "CHAFF/FLARE DISPENSE BUTTON (좌측 벽)", "Left Console (좌측 벽, 스로틀 상부 외측, 캐노피 잠금 레버 후방)", "708", 1, 1, [
    BTN("DISPENSE", (1,1), "CHAFF/FLARE Dispense Button", "CMDS MODE=MAN/SEMI/AUTO 시 Manual Program 5 투발 (SSC CMS와 독립)", None),
])

DEF_ACTIONS = [
 ["RWR.POWER_ON", "RWR 전원 및 기본 세팅 (시동/FENCE IN)", "ANY", "RWRAUX.POWER.ON > RWRAUX.SEARCH.ON(선택) > RWRAUX.ALTITUDE.HIGH|LOW(임무 고도) > RWRPRIME.MODE.OPEN > RWRPRIME.HANDOFF.PRESS_SHORT(Floating 확인)", "RWRAUX 'SYSTEM POWER' 점등, 표시기 활성", "695-696", "SEARCH ON이면 조기경보 레이더까지 표시(잡음 증가). 저고도 임무면 LOW"],
 ["RWR.SYS_TEST", "RWR 자체 시험", "RWR 전원 ON", "RWRPRIME.SYS_TEST.HOLD_1S", "'ON' 점등 → 전 버튼 점등·진단 메시지·경고음 → 자동 복귀", "696", "중단: 재누름"],
 ["RWR.PRIORITY_MODE", "표시 위협 5개로 축소 (고밀도 환경)", "RWR 전원 ON", "RWRPRIME.MODE.PRIORITY", "'PRIORITY' 점등", "695", "복귀: MODE.OPEN"],
 ["RWR.HANDOFF_NEXT", "다이아몬드를 다음 위협으로 수동 이동 후 고정", "RWR 전원 ON", "RWRPRIME.HANDOFF.HOLD (순환) > RWRPRIME.HANDOFF.RELEASE", "선택 위협에 다이아몬드 고정 (Latched)", "695", "Floating 복귀: PRESS_SHORT 2회(Off→Floating)"],
 ["ECM.WARMUP", "ECM 포드 예열 (지상 또는 FENCE IN 전 3분)", "포드 장착", "ECM.PWR.STBY", "모듈 등 S", "706", "3분 후 OPR 가능"],
 ["ECM.SET_DECEPTION", "기만 재밍 반응 모드 세팅", "ECM.PWR.STBY 예열 완료 + CMDS.MODE.SEMI|AUTO", "ECM.PWR.OPR > ECM.XMIT.2 > ECM.MOD_1..5.IN", "모듈 등 A, lock 시 CMS Aft(SEMI) 또는 자동(AUTO)으로 T", "706, 699", "XMIT 1이면 FCR 유지(거리 감소), 2면 FCR 대기"],
 ["ECM.SET_NOISE", "잡음 재밍 선제 모드 세팅", "ECM.PWR.STBY 예열 완료 + CMDS.MODE.MAN", "ECM.PWR.OPR > ECM.XMIT.3 > (HOTAS CMS Aft로 송신 개시)", "모듈 등 T — 연속 송신", "706, 698", "피탐 증가 주의. 중지: CMS Right"],
 ["ECM.OFF", "ECM 포드 OFF (FENCE OUT/착륙 전)", "ANY", "ECM.PWR.OFF", "모듈 등 소등", "706", ""],
]
