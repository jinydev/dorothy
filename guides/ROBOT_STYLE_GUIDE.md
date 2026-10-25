# 🤖 로봇 틴맨(Tinny / OzBot) 캐릭터 스타일 가이드라인 (Robot Style Guide)

> **"양철의 몸속에 뛰는 따뜻한 인공지능의 심장 — 시행착오를 겪으며 스스로 두 발로 걷는 법을 배우는 강화학습 에이전트 로봇"**

본 가이드라인은 도로시(Dorothy) 세계관의 다섯 번째 주인공이자 인공지능·강화학습·로보틱스 실습의 핵심 마스코트인 **로봇 '틴맨(Tinny / OzBot)'**의 외형, 소재, 표정, 동작, 화풍의 일관성을 유지하기 위한 표준 규격서입니다.

---

## 1. 캐릭터 디자인 표준 규격 (Character Specification)

### 🤖 기본 프로필
* **이름:** 틴맨 (Tinny / OzBot)
* **모티브:** 오즈의 마법사 '양철 나무꾼 (Tin Woodman)' + 지브리 감성의 레트로 퓨처리즘 메이커 로봇
* **신체 규격:** 신장 약 65cm, 3~4등신 소형 휴머노이드 로봇 비율
* **제작자:** 도로시(Dorothy) & 이호진 교수님 (Prof. Hojin)

### 🎨 외형 및 소재 디테일
* **바디 프레임 (Body & Armor):**
  * 소재: 따뜻한 매트 실버(Matte Silver) 양철/알루미늄 바디 + 부드러운 황동(Brass/Bronze) 관절 및 볼트
  * 질감: 차가운 SF 메카닉이 아닌, 손으로 직접 깎고 3D 프린팅하여 조립한 따뜻한 핸드크래프트 아날로그 감성
  * 디테일: 어깨와 무릎의 둥근 황동 볼 관절, 몸통 측면의 아기자기한 볼트와 리벳 라인
* **심장 코어 (The Glowing Heart Core):**
  * 위치: 가슴 중앙의 투명 강화 아크릴 원형 윈도우
  * 형태: **따뜻하게 회전하는 황동 톱니바퀴와 붉은빛/황금빛으로 은은하게 맥동하는 LED 하트 코어 (Pulsing Heart Core)**
  * 의미: 단순한 기계가 아닌 '마음과 호기심을 가진 인공지능'을 상징
* **헤드 & 페이스 플레이트 (Head & Face):**
  * 형태: 둥근 모서리의 레트로 모니터/잠수헬멧 스타일 헤드
  * 안테나: 머리 정수리에 솟은 작은 황동 코일 스프링 안테나 (끝에 노란 꼬마전구 LED가 달려있어 아이디어가 떠오를 때 반짝 점등)
  * **표정 LED 눈 (Expressive LED Eyes):**
    * 디스플레이: 스카이블루/에메랄드 그린 빛의 디지털 도트 매트릭스 눈
    * 표정 변화:
      * 평상시/기쁨: 반달 모양 눈 `^^`
      * 호기심/질문: 한쪽 눈이 커지며 물음표 `?` 표시
      * 강화학습 실패/당황: 소용돌이 `@_@` 또는 물결 `~_~`
      * 충전/수면: 포근한 직선 슬립 모드 `-_ - zZ`
* **사지 & 구동계 (Limbs & Actuators):**
  * 팔과 손: 3개의 부드러운 고무 패드 손가락(3-finger gripper), 공구를 쥐거나 도로시와 하이파이브 가능
  * 다리와 발: 서보 모터(Servo Motor) 기반의 2족 보행 관절 + 안정적인 평평한 고무 패드 발바닥 (발바닥에 미니 바퀴 롤러 내장)

---

## 2. 공통 아트 스타일 & 비주얼 톤 (Art Style & Rules)

* **핵심 화풍:** 스튜디오 지브리(천공의 성 라퓨타의 거신병, 하울의 움직이는 성의 메커니즘 감성)풍의 2D 클린 라인아트 + 소프트 웜톤 셀 셰이딩
* **색상 팔레트:**
  * 주색상: 부드러운 웜 실버 그레이 (`#C5CBD3`)
  * 보조색상: 황동 브론즈 골드 (`#C89D56`), 앤틱 구리 (`#A76D43`)
  * 포인트 발광색: 가슴 심장 코어 (웜 앰버 골드 / 루비 레드), 눈 및 안테나 (에메랄드 시안 블루 / 선샤인 옐로우)
* **금지 요소 (Negative Rules):**
  * ❌ 과도하게 날카롭고 공격적인 건담/트랜스포머 스타일 메카닉
  * ❌ 차가운 크롬 반사 및 실사 CGI 3D 렌더링
  * ❌ 부자연스러운 신체 왜곡 또는 기괴한 전선 노출

---

## 3. 프롬프트 표준 템플릿 (Prompt Construction)

### ① 코어 긍정 프롬프트 (Core Positive Prompt)
```text
Tinny the AI maker robot, cute friendly small humanoid robot, warm matte silver tin body with brass joints and bolts, round retro monitor head with expressive glowing sky-blue LED dot matrix eyes, brass spring antenna with yellow bulb tip on head, glowing heart core with visible rotating brass cogwheel inside transparent chest window, 3-finger mechanical hands, cute robotic feet, studio ghibli anime style, 2D animation aesthetic, clean anime line art, soft warm cel shading
```

### ② 부정 프롬프트 (Negative Prompt)
```text
3d, photorealistic, realistic, cgi, complex gundam, aggressive mecha, sharp weapons, scary face, dark gritty noir, rusted scrap, broken parts, deformed, low quality, blurry
```

---

## 4. 데이터셋 구축 20종 기획 (`data/dataset/robot/`)

| 번호 | 파일명 | 콘셉트 및 상황 | 구도 및 배경 |
| :---: | :--- | :--- | :--- |
| **01** | `robot_01` | 틴맨 정면 전신 스탠딩 대표 프로필 (기본 차렷) | 전신 정면, 화이트 배경 |
| **02** | `robot_02` | 측면 턴어라운드 뷰 (관절과 배터리 팩 확인) | 전신 측면, 화이트 배경 |
| **03** | `robot_03` | 얼굴 클로즈업 포트레이트 (반짝이는 LED 눈) | 헤드샷 클로즈업, 화이트 배경 |
| **04** | `robot_04` | 가슴의 빛나는 톱니바퀴 하트 코어 클로즈업 | 상반신 가슴 줌인, 따뜻한 발광 |
| **05** | `robot_05` | 호기심에 고개를 갸우뚱(Head-tilt)하는 모습 | 상반신 3/4 뷰, 화이트 배경 |
| **06** | `robot_06` | 손을 번쩍 들어 인사하는 웰컴 포즈 | 전신, 한 손 흔들기, 화이트 배경 |
| **07** | `robot_07` | 첫 2족 보행 강화학습: 비틀거리며 한 발 내딛기 | 전신 액션, 균형 잡기, 연구실 바닥 |
| **08** | `robot_08` | 엉덩방아 찧고 넘어져 당황한 표정 (`@_@`) | 바닥에 앉아 머리 긁적이기 |
| **09** | `robot_09` | 스스로 양손 짚고 다시 씩씩하게 일어서기 | 재도전 포즈, 결연한 눈빛 |
| **10** | `robot_10` | 멋지게 두 발로 균형 잡고 한 발 들기 성공! | 1족 균형 잡기, 환호 포즈 |
| **11** | `robot_11` | 도로시와 활짝 웃으며 손바닥 하이파이브! | 도로시와 틴맨 페어 컷, 연구실 |
| **12** | `robot_12` | 토토와 함께 자율주행 모형차를 관찰하는 모습 | 틴맨과 토토 듀오, 바닥 앵글 |
| **13** | `robot_13` | 머리 위에 조교 지니가 올라타 식빵 굽는 씬 | 틴맨 위에 지니 탑승, 힐링 컷 |
| **14** | `robot_14` | 충전 도크에 앉아 충전 중인 수면 모드 (`zzZ`) | 벽면 도크, 케이블 연결, 밤 연구실 |
| **15** | `robot_15` | 머리 위 안테나 전구가 번쩍 켜지며 아이디어 번뜩! | 아이디어 💡 발광, 신나는 제스처 |
| **16** | `robot_16` | 작은 드라이버를 쥐고 스스로 팔 볼트를 조이는 메이커 씬 | 공구 사용, 자기 수리, 워크벤치 |
| **17** | `robot_17` | 이호진 교수님과 칠판 앞에서 강화학습 수식 응시 | 교수님과 틴맨 멘토링 씬 |
| **18** | `robot_18` | 미로 그리드월드(GridWorld) 블록 통과 훈련 | 미로 매트 위 자율 탐색 씬 |
| **19** | `robot_19` | 기쁨에 겨워 양팔을 벌리고 귀엽게 춤추는 씬 | 다이내믹 댄스 포즈, 화이트 배경 |
| **20** | `robot_20` | 도로시, 호진, 지니, 토토와 함께 완벽한 팀 단체 샷 | 5인 완전체 연구실 피날레 컷 |
