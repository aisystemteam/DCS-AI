# -*- coding: utf-8 -*-
# UHF Backup Control Panel (DCS) + UHF/VHF DED 페이지 보완 — DCS F-16C EA Guide p.253-262
from dcs_panels import C, IND, BTN, P, NI

def _digits(desc):
    return [(str(d), f"{desc} = {d}") for d in range(10)]

UHFBU = P("UHFBU", "UHF BACKUP", "UHF BACKUP CONTROL PANEL (ARC-164)", "Left Console (ENG & JET START 후방)", "260-262", 5, 5, [
    C("CARD_DOOR", (1,1), "Preset Channel Card & Access Door", "Hinged door",
      [("CLOSED", "프리셋 주파수 카드 표시"), ("OPEN", "들어올리면 프리셋/Anti-jam 프로그래밍 — " + NI)], 1),
    IND("CHAN_DISP", (1,4), "CHAN Display", "MODE=PRESET 시 선택 프리셋 번호 표시, MNL 시 공백", 3),
    C("CHAN", (1,5), "CHAN Knob", "20-position rotary knob",
      [(str(i), f"프리셋 채널 {i} 선택 (MODE=PRESET 시 유효)") for i in range(1, 21)], 4),
    BTN("TEST_DISP", (2,1), "TEST DISPLAY Button", "Frequency Status/Display·CHAN 표시 전 세그먼트 점등 시험", 2),
    IND("FREQ_DISP", (2,2), "Frequency Status/Display", "수동 주파수 노브로 설정된 주파수 표시. STATUS 누르면 현재 동조 주파수 표시", 5),
    BTN("STATUS", (2,5), "STATUS Button", "누르는 동안 UHF가 실제 동조된 주파수를 Frequency Status/Display에 표시 (PRESET 시 프리셋 주파수 확인용)", 6),
    C("A32", (3,1), "A-3-2 Knob", "3-position rotary knob",
      [("A", "Anti-Jam 기능 — " + NI), ("3", "MNL 시 주파수 첫 자리 3 (3xx.xxx MHz)"), ("2", "MNL 시 주파수 첫 자리 2 (2xx.xxx MHz)")], 7),
    C("FREQ_10MHZ", (3,2), "Manual Frequency Knob — 10 MHz", "10-position rotary knob", _digits("10 MHz 자리"), 8),
    C("FREQ_1MHZ", (3,3), "Manual Frequency Knob — 1 MHz", "10-position rotary knob", _digits("1 MHz 자리"), 8),
    C("FREQ_100KHZ", (3,4), "Manual Frequency Knob — 100 kHz", "10-position rotary knob", _digits("100 kHz 자리"), 8),
    C("FREQ_25KHZ", (3,5), "Manual Frequency Knob — 25 kHz", "4-position rotary knob",
      [("000", "25 kHz 자리 = .000"), ("025", ".025"), ("050", ".050"), ("075", ".075")], 8,
      note="5개 노브로 225.000~399.975 MHz, 0.025 MHz 단위"),
    C("FUNCTION", (4,1), "Function Knob", "4-position rotary knob",
      [("OFF", "백업 패널 전원 OFF. 배터리 전원만이거나 C&I=BACKUP이면 UHF 무선기 자체 전원도 OFF"),
       ("MAIN", "AUD1.COMM1_PWR≠OFF 시 선택 프리셋/주파수로 운용, GUARD 보조 수신기 OFF"),
       ("BOTH", "선택 프리셋/주파수로 운용 + GUARD 보조 수신기로 243.0 감시"),
       ("ADF", "기능 없음")], 9),
    C("VOL", (4,3), "VOL Knob", "Rotary knob (continuous)", [("ADJ", "기능 없음 — 볼륨은 AUD1.COMM1_PWR")], 12, note="No function"),
    C("MODE", (4,5), "Mode Knob", "3-position rotary knob",
      [("MNL", "수동 주파수 노브로 설정된 주파수(Frequency Status/Display)로 동조"),
       ("PRESET", "CHAN 노브로 선택된 프리셋 주파수로 동조"),
       ("GRD", "243.0 MHz 동조, 전용 GUARD 수신기 OFF")], 10),
    BTN("TONE", (5,2), "TONE Button", "수신 중단 후 현재 주파수로 톤 송신 — " + NI, 11),
    C("SQUELCH", (5,4), "SQUELCH Switch", "2-position toggle switch", [("ON", "스켈치 활성"), ("OFF", "스켈치 비활성")], 13),
], note="UFC(ICP/DED) 고장 시 또는 C&I=BACKUP 시 UHF 제어. 배터리 전원만으로 쓸 수 있는 유일한 무선기(엔진 시동 전). 정상 운용 중엔 비상 대비로 프리셋/수동 주파수를 미리 세팅")

# ── DED UHF/VHF 페이지 필드 (p.253-256) — icp.py의 부분 기입을 교체
_F = []
def F(pg, no, label, editable, method, fmt, ast, desc, ni=""):
    _F.append([f"{pg}.{label}", pg, no, label, editable, method, fmt, ast, desc, ni])
for pg, radio, rng, pwr in (("UHF", "ARC-164 UHF", "225.000~399.975", "OFF/MAIN/BOTH"), ("VHF", "ARC-222 VHF", "30.00~87.975 FM / 108.000~151.975 AM", "OFF/ON")):
    F(pg, 1, "ACTIVE_FREQ", "N", "DISPLAY", "MHz 또는 채널", "N", f"{radio} 현재 동조 프리셋 채널/수동 주파수")
    F(pg, 2, "PRE", "Y", "INCDEC_CYCLE", "1~20 (키패드 입력+ENTR도 가능)", "N", "편집 대상 프리셋 채널 번호 — INC/DEC 순환 또는 별표 위치 후 키패드+ENTR. 동조는 바뀌지 않음")
    F(pg, 3, "PRE_FREQ", "Y", "KEYPAD_ENTR", "4~5자리 연속 입력 (선행 0·마지막 자리 생략)", "N", "PRE 채널에 할당된 주파수 편집. 동조는 바뀌지 않음")
    if pg == "UHF":
        F(pg, 4, "MODE_STATUS", "Y", "SEQ_TOGGLE", pwr, "N", "DCS SEQ로 MAIN↔BOTH 토글. OFF=AUD1.COMM1_PWR OFF. BOTH=GUARD 보조 수신기 243.0 감시. BACKUP 표시 시 ICP 무효(UHFBU 패널 제어)")
    else:
        F(pg, 4, "POWER_STATUS", "N", "DISPLAY", pwr, "N", "OFF=AUD1.COMM2_PWR OFF / ON. AUD1.COMM2_MODE=GD 시 'AM GUARD' 표시, ICP 무효")
    F(pg, 5, "SCRATCHPAD", "Y", "KEYPAD_ENTR", f"채널 1~20 또는 주파수 {rng} (4~5자리 연속, 마지막 자리 생략)", "Y", "동조 입력 — ENTR로 확정되면 DED는 오버라이드 전 페이지로 자동 복귀")
    F(pg, 6, "BAND", "Y", "KEY_TOGGLE", "NB/WB", "N", "수신 대역폭 — 별표 위치에서 키패드 1-9로 토글", NI)
UHFVHF_DED_FIELDS = _F

UHFBU_ACTIONS = [
 ["UHFBU.TUNE_PRESET", "백업 패널로 UHF 프리셋 동조 — 예: 채널 4", "배터리 전원 또는 IFF.CNI.BACKUP", "UHFBU.FUNCTION.MAIN|BOTH > UHFBU.MODE.PRESET > UHFBU.CHAN.4 > (UHFBU.STATUS.PUSH로 주파수 확인)", "CHAN 표시 '04', STATUS 누르면 주파수 표시. DED UHF 페이지 'BACKUP' + 채널/주파수", "262, 254", "엔진 시동 전 ATC 교신용"],
 ["UHFBU.TUNE_MANUAL", "백업 패널로 UHF 수동 주파수 동조 — 예: 360.400", "배터리 전원 또는 IFF.CNI.BACKUP", "UHFBU.FUNCTION.MAIN|BOTH > UHFBU.MODE.MNL > UHFBU.A32.3 > UHFBU.FREQ_10MHZ.6 > UHFBU.FREQ_1MHZ.0 > UHFBU.FREQ_100KHZ.4 > UHFBU.FREQ_25KHZ.000", "Frequency Status/Display '360.400'", "262", ""],
 ["UHFBU.PRESET_FOR_EMERGENCY", "비상 대비 백업 패널 사전 세팅 (전투구역 진입 전)", "정상 운용 중", "UHFBU.MODE.PRESET > UHFBU.CHAN.n(탱커/홈 기지) > UHFBU.FUNCTION.BOTH", "주전원 상실 시 UHF가 이 설정으로 복귀", "252", "UFC 정상 시 패널 설정은 동조에 영향 없음"],
]

ICP_RADIO_ACTIONS = [
 ["ICP.TUNE_UHF_PRESET", "UHF 프리셋 채널 동조 — 예: 5", "ANY (UFC 제어 중)", "ICP.COM1 > ICP.KEY_5 > ICP.ENTR", "CNI 1행 'UHF' 채널/주파수 갱신, DED 이전 페이지 자동 복귀", "257", "SCRATCHPAD가 기본 별표 위치. 2자리는 KEY 두 번"],
 ["ICP.TUNE_UHF_MANUAL", "UHF 수동 주파수 동조 — 예: 360.10", "ANY (UFC 제어 중)", "ICP.COM1 > ICP.KEY_3 > ICP.KEY_6 > ICP.KEY_0 > ICP.KEY_1 > ICP.ENTR", "CNI 1행 'UHF 360.10'", "259", "4~5자리 연속 입력, 선행 0·마지막 자리 생략 (360.100 → 3601)"],
 ["ICP.TUNE_VHF_PRESET", "VHF 프리셋 채널 동조 — 예: 7", "ANY", "ICP.COM2 > ICP.KEY_7 > ICP.ENTR", "CNI 3행 'VHF' 갱신", "257", ""],
 ["ICP.TUNE_VHF_MANUAL", "VHF 수동 주파수 동조 — 예: 122.10", "ANY", "ICP.COM2 > ICP.KEY_1 > ICP.KEY_2 > ICP.KEY_2 > ICP.KEY_1 > ICP.ENTR", "CNI 3행 'VHF 122.10'", "259", "FM 30.00~87.975 / AM 108.000~151.975"],
 ["ICP.EDIT_UHF_PRESET", "UHF 프리셋 채널 주파수 편집 — 예: 채널 6 = 360.40", "ANY", "ICP.COM1 > ICP.DCS.DN (별표 PRE로) > ICP.KEY_6 > ICP.ENTR > ICP.DCS.DN (PRE_FREQ로) > ICP.KEY_3 > ICP.KEY_6 > ICP.KEY_0 > ICP.KEY_4 > ICP.ENTR > ICP.COM1", "UHF 페이지 'PRE 6' 아래 주파수 '360.40'. 동조는 불변", "258", "PRE 선택은 INC/DEC로도 가능"],
 ["ICP.CYCLE_UHF_PRESET_CNI", "CNI 페이지에서 UHF 프리셋 순환 (이미 프리셋 동조 중)", "CNI + UHF 프리셋 동조", "ICP.DCS.UP/DN (↕를 UHF 필드로) > ICP.INCDEC.INC|DEC", "CNI 1행 채널 번호 증감", "257", "VHF도 동일"],
 ["ICP.UHF_MODE_TOGGLE", "UHF MAIN ↔ BOTH(GUARD 감시) 토글", "UHF 페이지", "ICP.COM1 > ICP.DCS.SEQ > ICP.COM1", "UHF 페이지 1행 'MAIN'/'BOTH'", "254", "즉시 243.0 동조는 AUD1.COMM1_MODE.GD"],
]
