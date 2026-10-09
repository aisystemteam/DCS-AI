# -*- coding: utf-8 -*-
# HOTAS: Side Stick Controller + Throttle — DCS F-16C EA Guide p.83-89
from dcs_panels import C, BTN, P, NI

CTX = "문맥 의존 (마스터모드/SOI/CMDS 모드) — HOTAS_FUNCTIONS 참조"

SSC = P("SSC", "SSC", "SIDE STICK CONTROLLER (HOTAS)", "HOTAS (우측 사이드스틱)", "83-85, 88", 5, 2, [
    C("WPN_REL", (1,1), "Weapon Release Button", "Push button (hold)",
      [("HOLD", "누르고 유지: 공대공 미사일 발사 / 공대지 무장 투하")], 1),
    C("TRIM", (1,2), "Trim Switch (4-way)", "4-way momentary hat",
      [("FWD", "기수 하향 트림"), ("AFT", "기수 상향 트림"), ("LEFT", "좌익 하향 트림"), ("RIGHT", "우익 하향 트림")], 2,
      note="MANUAL TRIM 패널 TRIM/AP DISC=DISC 시 비활성"),
    C("TMS", (2,1), "Target Management Switch (4-way)", "4-way momentary hat (short <0.5 s / long >0.5 s, 일부 1 s)",
      [("FWD", "표적 지정/락 등 — " + CTX), ("AFT", "표적 거부/해제 등 — " + CTX),
       ("LEFT", "질문/모드 전환 등 — " + CTX), ("RIGHT", "표적 스텝/모드 토글 등 — " + CTX)], 5),
    C("DMS", (2,2), "Display Management Switch (4-way)", "4-way momentary hat (short/long)",
      [("FWD", "SOI → HUD"), ("AFT", "짧게: SOI → MFD / MFD 간 SOI 교환, 길게: HMD ON/OFF"),
       ("LEFT", "좌 MFD 다음 포맷"), ("RIGHT", "우 MFD 다음 포맷")], 6),
    C("TRIGGER", (3,1), "Trigger (2-detent)", "2-stage trigger",
      [("DETENT_1", "1단: 타게팅 포드 레이저 조사(포드 장착·전원 시)"),
       ("DETENT_2", "2단: 기총 발사(선택·ARM 시) 또는 CCIP 모드에서 레이저 30초 조사")], 3),
    C("MSL_STEP", (3,2), "Missile Step Button", "Push button (short/long)",
      [("SHORT", "공중: 미사일 스텝 / A-G: CCIP→DTOS→CCRP 순환. 지상: NWS ON/OFF. 급유 중: 붐 분리 — " + CTX),
       ("LONG", "A-A/MSL OVRD/DGFT: 미사일 종류 순환 — " + CTX)], 4),
    C("CMS", (4,1), "Countermeasures Management Switch (4-way)", "4-way momentary hat",
      [("FWD", "수동 프로그램 1-4 투발 (CMDS PRGM 노브 선택)"), ("LEFT", "수동 프로그램 6 투발"),
       ("RIGHT", "ECM 송신 중지 / AUTO 투발 중단 — CMDS 모드별"), ("AFT", "ECM 송신 개시 / 자동 프로그램 동의·투발 — CMDS 모드별")], 7),
    C("PADDLE", (5,1), "Paddle Switch", "Lever (hold)",
      [("HOLD", "유지하는 동안 오토파일럿 권한 차단(수동 조종). 놓으면 현재 피치/롤/고도를 새 기준값으로 오토파일럿 재결합")], 8),
    C("EXP_FOV", (5,2), "Expand/FOV Button", "Push button (short/long)",
      [("SHORT", "SOI 센서 시야/확대 순환 (FCR/HSD/HAD EXP, TGP FOV/XR, WPN 미사일 FOV/POS) — " + CTX),
       ("LONG", "유지 중 HSD ZOOM")], 9),
], note="기능 상세(마스터모드·SOI·CMDS 모드별)는 HOTAS_FUNCTIONS 표. 부록 D 그림 미수록")

THROTTLE = P("THROTTLE", "THROTTLE", "THROTTLE GRIP (HOTAS)", "HOTAS (좌측 콘솔 상부 스로틀)", "86-87, 89", 4, 2, [
    C("CUTOFF_RELEASE", (1,1), "Throttle Cutoff Release", "Lift latch",
      [("LIFT", "들어올려 스로틀을 IDLE ↔ OFF 디텐트 통과 허용")], None),
    C("UHF_VHF_XMIT", (1,2), "UHF VHF Transmit Switch (4-way)", "4-way momentary hat (short/long)",
      [("FWD", "ARC-222 VHF 송신(PTT)"), ("AFT", "ARC-164 UHF 송신(PTT)"),
       ("LEFT", "IFF OUT — 짧게: FCR 데이터링크 정보 표시 토글"), ("RIGHT", "IFF IN — 짧게: FCR 데이터링크 필터 순환, 길게: 선택 STPT/SPI/SEAD 표적 데이터링크 송신")], 1),
    C("LEVER", (2,1), "Throttle Lever", "Lever with detents (continuous)",
      [("OFF", "점화·연료 차단 (CUTOFF RELEASE 필요)"), ("IDLE", "최소 추력 — 지상/공중 시동"),
       ("MIL", "군용 최대 (AB 디텐트 직전) — IDLE~MIL 연속"), ("MAX_AB", "애프터버너 최대 — MIL~MAX 연속")], None),
    C("MAN_RNG", (2,2), "MAN RNG / UNCAGE Knob", "Rotary knob + push (short/long)",
      [("ROTATE", "TGP 수동 줌 레벨 증감"),
       ("DEPRESS_SHORT", "NAV(기어 다운): HUD ILS 편차 바·롤 지시 디클러터 / A-A·MSL·DGFT: AIM-9 시커 언케이지 / A-G: TGP 레이저 스폿 트랙 토글"),
       ("DEPRESS_LONG", "A-G: 기총 STRF 모드 토글 (>1 s)")], 2),
    C("RDR_CURSOR", (3,1), "RDR CURSOR / ENABLE Control", "Multi-directional + depress",
      [("SLEW", "HUD/HMCS: TD 박스·마크 큐 / FCR·HSD·HAD: MFD 커서 / TGP: 센서 / WPN: MAV 시커·HAS 커서 슬루"),
       ("DEPRESS", "A-A·MSL·DGFT: 누르는 동안 AIM-9 BORE/SLAVE 교환 / A-G AGM-65: PRE→VIS→BORE 순환 / AGM-88: HAS↔POS")], 5),
    C("DOGFIGHT", (3,2), "DOG FIGHT Switch", "3-position switch (center = previous mode)",
      [("DGFT", "바깥(UP): DOGFIGHT 마스터모드 — FCR ACM, 송신 명령 전까지 대기, 기총+AIM-9/120 조준선. HUD 'DGFT'"),
       ("CTR", "중앙: 진입 전 마스터모드/서브모드로 복귀"),
       ("MSL_OVRD", "안쪽(DOWN): MISSILE OVERRIDE — FCR CRM/RWS, A-A 미사일 심볼. HUD 'MRM'/'SRM'/'HOB' 또는 'MSL'")], 3,
      note="비상투하 제외 모든 모드 오버라이드. 이 위치에서는 DED MODE 페이지 무효"),
    C("SPD_BRK", (4,1), "SPD BRK Switch", "3-position switch (AFT momentary)",
      [("FWD", "스피드브레이크 수납"), ("CTR", "현재 위치 유지"), ("AFT", "유지하는 동안 전개 (스프링 복귀)")], 6,
      note="우 주기어 다운&잠김 시 43° 제한(지상 충돌 방지), AFT 유지 시 60°까지 임시 허용. 노즈기어 압축 후 제한 해제"),
    C("ANT_ELEV", (4,2), "ANT ELEV Knob", "Rotary knob (center detent)",
      [("ADJ", "FCR 안테나 앙각 수동 증감 (중앙 디텐트 = 0)")], 4),
], note="기능 상세는 HOTAS_FUNCTIONS 표")

# ───────────── HOTAS_FUNCTIONS: control + position + press × context → function ─────────────
# function_id, control_id, position, press, context_type, context, function, source_page
_H = []
def H(ctl, pos, press, ctype, ctx, func, pg):
    _H.append([f"{ctl}.{pos}.{press}.{ctx}".replace(" ", "_").replace("/", "-"), ctl, pos, press, ctype, ctx, func, pg])

# MSL STEP (p.84, 88)
for ctx, f in (("NAV", "(동작 없음)"), ("A-A", "미사일 스텝(같은 종류 다음 스테이션)"), ("MSL_OVRD", "미사일 스텝"), ("DGFT", "미사일 스텝"),
               ("A-G", "CCIP→DTOS→CCRP 순환"), ("A-G_AGM65", "미사일 스텝"), ("A-G_AGM88", "미사일 스텝")):
    H("SSC.MSL_STEP", "SHORT", "SHORT", "MASTER_MODE", ctx, f, "84")
for ctx, f in (("NAV", "(동작 없음)"), ("A-A", "미사일 종류 순환"), ("MSL_OVRD", "미사일 종류 순환"), ("DGFT", "미사일 종류 순환"), ("A-G", "(동작 없음)")):
    H("SSC.MSL_STEP", "LONG", "LONG", "MASTER_MODE", ctx, f, "84")
H("SSC.MSL_STEP", "SHORT", "SHORT", "STATE", "AIR_REFUEL", "급유 붐 수동 분리 (AIR REFUEL=OPEN, 공중)", "84")
H("SSC.MSL_STEP", "SHORT", "SHORT", "STATE", "GROUND", "노즈휠 조향(NWS) ON/OFF 토글", "83")

# TMS (p.84, 88) by SOI
TMS = {
 ("FWD","SHORT"): {"HUD":"DTOS/VIS 지정","HMCS":"지정","FCR":"지정 / ACM BORE","HSD":"지정 / 표시 링","HAD":"지정","TGP":"Point Track (놓을 때)","WPN":"Track / Force Correlate"},
 ("FWD","LONG"):  {"HUD":"SOI → HMCS","HMCS":"(동작 없음)","FCR":"Spotlight Scan (유지 중)","HSD":"(동작 없음)","HAD":"HARM POS 순환 (1 s)","TGP":"Area Track (유지 중)","WPN":"(동작 없음)"},
 ("LEFT","SHORT"):{"HUD":"(동작 없음)","HMCS":"(동작 없음)","FCR":"Scan 질문(Interrogate)","HSD":"(동작 없음)","HAD":"DED → SEAD 페이지","TGP":"TV/FLIR 및 FLIR 극성","WPN":"HARM 테이블 / MAV 극성"},
 ("LEFT","LONG"): {"HUD":"(동작 없음)","HMCS":"(동작 없음)","FCR":"NCTR/LOS 질문","HSD":"(동작 없음)","HAD":"TDOA 개시","TGP":"(동작 없음)","WPN":"(동작 없음)"},
 ("RIGHT","SHORT"):{"HUD":"조준점 순환(A-G 조준점 옵션 시)","HMCS":"(동작 없음)","FCR":"표적 스텝 / ACM 30×20 / 조준점 순환(A-G)","HSD":"(동작 없음)","HAD":"표적 스텝","TGP":"Area Track / IR Pointer(2회)","WPN":"HARM 표적 스텝"},
 ("RIGHT","LONG"):{"HUD":"(동작 없음)","HMCS":"(동작 없음)","FCR":"TWS 토글/교환 (1 s)","HSD":"(동작 없음)","HAD":"(동작 없음)","TGP":"Inertial Track","WPN":"(동작 없음)"},
 ("AFT","SHORT"): {"HUD":"표적 거부","HMCS":"표적 거부 / SOI → HUD","FCR":"표적 거부 / ACM 10×60","HSD":"PDLT 드롭 / 링 숨김","HAD":"표적 거부 / DED → CNI","TGP":"Slave 모드 / 커서 제로","WPN":"표적 거부 / MAV Slave"},
 ("AFT","LONG"):  {"HUD":"(동작 없음)","HMCS":"(동작 없음)","FCR":"(동작 없음)","HSD":"(동작 없음)","HAD":"TDOA 종료","TGP":"디클러터 (유지 중)","WPN":"(동작 없음)"},
}
for (pos, pr), d in TMS.items():
    for soi, f in d.items():
        H("SSC.TMS", pos, pr, "SOI", soi, f, "84")

# DMS (p.84, 88)
for soi in ("HUD","HMCS","FCR","HSD","HAD","TGP","WPN"):
    H("SSC.DMS", "FWD", "SHORT", "SOI", soi, "(동작 없음)" if soi == "HUD" else "SOI → HUD", "84")
    H("SSC.DMS", "AFT", "SHORT", "SOI", soi, "SOI → MFD" if soi in ("HUD","HMCS") else "좌/우 MFD 간 SOI 교환", "84")
H("SSC.DMS", "LEFT", "SHORT", "ANY", "ANY", "좌 MFD 다음 포맷 (Format Select 할당 순환, BLANK 제외)", "84")
H("SSC.DMS", "RIGHT", "SHORT", "ANY", "ANY", "우 MFD 다음 포맷", "84")
H("SSC.DMS", "AFT", "LONG", "ANY", "ANY", "헬멧 디스플레이(HMD) ON/OFF", "84")

# CMS (p.85, 88) by CMDS mode
H("SSC.CMS", "FWD", "ANY", "CMDS_MODE", "MAN/SEMI/AUTO", "수동 프로그램 1-4 × 1회 투발 (CMDS.PRGM 선택). 다른 프로그램 진행 중이면 무시", "85")
H("SSC.CMS", "LEFT", "ANY", "CMDS_MODE", "MAN/SEMI/AUTO", "수동 프로그램 6 × 1회 투발", "85")
H("SSC.CMS", "RIGHT", "ANY", "CMDS_MODE", "MAN", "ECM 송신 중지", "85")
H("SSC.CMS", "RIGHT", "ANY", "CMDS_MODE", "SEMI", "ECM 송신 중지", "85")
H("SSC.CMS", "RIGHT", "ANY", "CMDS_MODE", "AUTO", "자동 프로그램 투발 동의 철회 / 진행 중 프로그램 중단", "85")
H("SSC.CMS", "AFT", "ANY", "CMDS_MODE", "MAN", "ECM.XMIT=3이면 잡음 재밍 송신 개시", "85")
H("SSC.CMS", "AFT", "ANY", "CMDS_MODE", "SEMI", "자동 프로그램 1회 투발(동의) / ECM.XMIT=1·2이면 기만 재밍 허용", "85")
H("SSC.CMS", "AFT", "ANY", "CMDS_MODE", "AUTO", "자동 프로그램 연속 투발 동의", "85")
H("SSC.CMS", "FWD", "ANY", "CMDS_MODE", "BYP", "채프 1 + 플레어 1 투발", "699")

# EXP/FOV, PADDLE, TRIGGER, WPN_REL, TRIM
for soi, f in (("HUD","(동작 없음)"),("HMCS","(동작 없음)"),("FCR","FCR EXP 모드 순환"),("HSD","HSD EXP 모드 순환"),("HAD","HAD EXP 모드 순환"),("TGP","FOV / XR 줌 순환(2회)"),("WPN","미사일 FOV/POS 토글")):
    H("SSC.EXP_FOV", "SHORT", "SHORT", "SOI", soi, f, "85")
H("SSC.EXP_FOV", "LONG", "LONG", "ANY", "ANY", "유지 중 HSD ZOOM", "85")
H("SSC.PADDLE", "HOLD", "HOLD", "ANY", "ANY", "오토파일럿 권한 차단(수동 조종). 놓으면 새 기준값으로 재결합", "85")
H("SSC.TRIGGER", "DETENT_1", "HOLD", "ANY", "ANY", "TGP 레이저 조사", "83")
H("SSC.TRIGGER", "DETENT_2", "HOLD", "ANY", "ANY", "기총 발사 / CCIP 레이저 30초", "83")
H("SSC.WPN_REL", "HOLD", "HOLD", "ANY", "ANY", "A-A 미사일 발사 / A-G 무장 투하", "83")

# Throttle (p.86-87, 89)
H("THROTTLE.UHF_VHF_XMIT", "FWD", "ANY", "ANY", "ANY", "VHF(ARC-222) 송신", "86")
H("THROTTLE.UHF_VHF_XMIT", "AFT", "ANY", "ANY", "ANY", "UHF(ARC-164) 송신", "86")
H("THROTTLE.UHF_VHF_XMIT", "LEFT", "SHORT", "ANY", "ANY", "FCR 데이터링크 정보 표시 토글", "86")
H("THROTTLE.UHF_VHF_XMIT", "RIGHT", "SHORT", "ANY", "ANY", "FCR 데이터링크 필터 순환", "86")
H("THROTTLE.UHF_VHF_XMIT", "RIGHT", "LONG", "ANY", "ANY", "선택 STPT/SPI/SEAD 표적을 데이터링크로 송신", "86")
H("THROTTLE.MAN_RNG", "ROTATE", "ANY", "ANY", "ANY", "TGP 수동 줌 증감", "86")
H("THROTTLE.MAN_RNG", "DEPRESS_SHORT", "SHORT", "MASTER_MODE", "NAV_LG_DOWN", "HUD ILS 편차 바·롤 지시 디클러터, 방위 눈금 상단 이동", "86")
H("THROTTLE.MAN_RNG", "DEPRESS_SHORT", "SHORT", "MASTER_MODE", "A-A/MSL_OVRD/DGFT", "AIM-9 시커 언케이지", "86")
H("THROTTLE.MAN_RNG", "DEPRESS_SHORT", "SHORT", "MASTER_MODE", "A-G", "TGP 레이저 스폿 트랙(LST) 토글", "86")
H("THROTTLE.MAN_RNG", "DEPRESS_LONG", "LONG", "MASTER_MODE", "A-G", "기총 STRF 모드 토글 (>1 s)", "86")
H("THROTTLE.DOGFIGHT", "DGFT", "ANY", "ANY", "ANY", "DOGFIGHT 마스터모드 진입 — FCR ACM, 대기", "87")
H("THROTTLE.DOGFIGHT", "CTR", "ANY", "ANY", "ANY", "이전 마스터모드/서브모드 복귀", "87")
H("THROTTLE.DOGFIGHT", "MSL_OVRD", "ANY", "ANY", "ANY", "MISSILE OVERRIDE 진입 — FCR CRM/RWS", "87")
H("THROTTLE.ANT_ELEV", "ADJ", "ANY", "ANY", "ANY", "FCR 안테나 앙각 증감", "87")
for soi, f in (("HUD/HMCS","TD 박스 / 마크 큐 슬루"),("FCR/HSD/HAD","MFD 커서 / ACM 슬루"),("TGP","TGP 센서 슬루"),("WPN_AGM65","MAV 시커 슬루"),("WPN_AGM88","HAS 커서 슬루")):
    H("THROTTLE.RDR_CURSOR", "SLEW", "ANY", "SOI", soi, f, "87")
H("THROTTLE.RDR_CURSOR", "DEPRESS", "HOLD", "MASTER_MODE", "A-A/MSL_OVRD/DGFT", "누르는 동안 AIM-9 BORE/SLAVE 교환", "87")
H("THROTTLE.RDR_CURSOR", "DEPRESS", "SHORT", "MASTER_MODE", "A-G_AGM65", "PRE→VIS→BORE 순환", "87")
H("THROTTLE.RDR_CURSOR", "DEPRESS", "SHORT", "MASTER_MODE", "A-G_AGM88", "HAS↔POS", "87")
H("THROTTLE.SPD_BRK", "FWD", "ANY", "ANY", "ANY", "스피드브레이크 수납", "87")
H("THROTTLE.SPD_BRK", "CTR", "ANY", "ANY", "ANY", "현재 위치 유지", "87")
H("THROTTLE.SPD_BRK", "AFT", "HOLD", "ANY", "ANY", "유지 중 전개 (우 주기어 다운 시 43° 제한, 유지 시 60°)", "87")
HOTAS_FUNCTIONS = _H

HOTAS_ACTIONS = [
 ["HOTAS.NWS_TOGGLE", "지상에서 노즈휠 조향 ON/OFF", "지상(WOW)", "SSC.MSL_STEP.SHORT", "AR/NWS 표시기 'AR NWS' 점등/소등", "83", ""],
 ["HOTAS.AR_DISCONNECT", "공중급유 붐 수동 분리", "공중 + FUEL.AIR_REFUEL.OPEN", "SSC.MSL_STEP.SHORT", "AR/NWS 표시기 'DISC' 점등 → 3초 후 'RDY'", "84", ""],
 ["HOTAS.ENTER_DGFT", "DOGFIGHT 모드 진입", "ANY", "THROTTLE.DOGFIGHT.DGFT", "HUD 'DGFT', FCR ACM", "87", "복귀: THROTTLE.DOGFIGHT.CTR"],
 ["HOTAS.ENTER_MSL_OVRD", "MISSILE OVERRIDE 진입", "ANY", "THROTTLE.DOGFIGHT.MSL_OVRD", "HUD 'MRM'/'SRM'/'HOB'/'MSL', FCR RWS", "87", ""],
 ["HOTAS.SPD_BRK_OUT", "스피드브레이크 전개", "ANY", "THROTTLE.SPD_BRK.AFT (유지)", "LG 패널 SPEED BRAKE 표시기 OPEN 패턴", "87", "지상 43° 제한"],
 ["HOTAS.SPD_BRK_IN", "스피드브레이크 수납", "ANY", "THROTTLE.SPD_BRK.FWD", "표시기 CLOSED", "87", ""],
 ["HOTAS.CMDS_DISPENSE_MANUAL", "선택 수동 프로그램 1회 투발", "CMDS.MODE.MAN|SEMI|AUTO", "SSC.CMS.FWD", "CMDS QTY 감소, FDBK ON 시 'Chaff flare' 음성", "85", "프로그램 = CMDS.PRGM"],
 ["HOTAS.CMDS_CONSENT", "자동 프로그램 동의(SEMI 1회 / AUTO 연속)", "CMDS.MODE.SEMI|AUTO + DISPENSE_RDY", "SSC.CMS.AFT", "STATUS DISPENSE_RDY 해제, QTY 감소", "85", ""],
 ["HOTAS.CMDS_INTERRUPT", "자동 투발 중단/동의 철회", "CMDS.MODE.AUTO", "SSC.CMS.RIGHT", "투발 정지", "85", ""],
 ["HOTAS.ECM_NOISE_ON", "잡음 재밍 송신 개시", "ECM.PWR.OPR + ECM.XMIT.3 + CMDS.MODE.MAN", "SSC.CMS.AFT", "ECM 모듈 등 T", "85, 706", "중지: SSC.CMS.RIGHT"],
 ["HOTAS.SOI_TO_HUD", "SOI를 HUD로", "ANY", "SSC.DMS.FWD (short)", "HUD에 SOI 박스", "84", ""],
 ["HOTAS.SOI_SWAP_MFD", "좌/우 MFD 간 SOI 교환", "SOI가 MFD", "SSC.DMS.AFT (short)", "SOI 박스 반대 MFD로", "84", "SOI가 HUD/HMCS면 SOI → MFD"],
 ["HOTAS.NEXT_LEFT_FORMAT", "좌 MFD 다음 포맷", "ANY", "SSC.DMS.LEFT (short)", "좌 MFD 하단 강조 라벨 이동", "84", "MFD_TRANSITIONS MT008 연결"],
 ["HOTAS.NEXT_RIGHT_FORMAT", "우 MFD 다음 포맷", "ANY", "SSC.DMS.RIGHT (short)", "우 MFD 하단 강조 라벨 이동", "84", ""],
 ["HOTAS.UNCAGE_AIM9", "AIM-9 시커 언케이지", "A-A/MSL_OVRD/DGFT + AIM-9 선택", "THROTTLE.MAN_RNG.DEPRESS_SHORT", "HUD 시커 서클 자유 이동, 톤 변화", "86", ""],
 ["HOTAS.PTT_UHF", "UHF 송신", "ANY", "THROTTLE.UHF_VHF_XMIT.AFT (유지)", "", "86", "VHF = FWD"],
]
