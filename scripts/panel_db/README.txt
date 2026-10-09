F-16_Cockpit_Panels_Duality.xlsx 생성 스크립트
- build_audio.py : BMS 5개 패널 정의 + 테이블/격자 생성 (실행 진입점)
- dcs_panels.py  : DCS EA Guide p.43-79 패널 31개 정의
- icp.py         : ICP 패널 + DED_PAGES / DED_TRANSITIONS / DED_FIELDS / ICP_ACTIONS
- mfd.py         : MFDL/MFDR 패널 + MFD_FORMATS / MFD_OSB_MAP / MFD_TRANSITIONS / MFD_ACTIONS
실행: python build_audio.py  (openpyxl 필요, 출력 경로는 build_audio.py 하단 out 변수)
- cmds.py        : CMDS 패널 + CMDS DED 5페이지(BINGO/CHAFF/FLARE/OTHER1/2) + CMDS 조작 매크로
- defensive.py   : RWR 방위표시기/Prime/Aux 패널, ECM 패널, 좌측 벽 CHAFF/FLARE 버튼 + 방어계통 조작 매크로(PANEL_ACTIONS)
- hotas.py       : SSC/THROTTLE 패널 + HOTAS_FUNCTIONS(문맥별 기능) + HOTAS 조작 매크로
- uhfbu.py       : DCS UHF Backup 패널(BMS 정의 대체) + UHF/VHF DED 필드 + 무선 동조 매크로
