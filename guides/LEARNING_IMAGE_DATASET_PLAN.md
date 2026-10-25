# 🎨 도로시 컴퓨팅 과학 신규 기술 학습 이미지 생성 계획 (Learning Image Dataset Plan)

본 문서는 **14대 컴퓨터 과학·인공지능·인프라 기술 스택**(인공지능, 딥러닝, 강화학습, 연합학습, 파이썬, 자바스크립트, 자바, PHP, 아두이노, 라즈베리파이, MySQL, PostgreSQL, 도커, 리눅스)을 학습하는 도로시와 동료들의 추가 학습용 이미지(LoRA 데이터셋 확장용)의 시나리오 및 프롬프트 명세입니다.

---

## 📌 1. 토토(Toto) 데이터셋 잔여 완료 작업 (4장 -> 20장 완성)

| 파일 번호 | 주요 씬 및 구도 | 프롬프트 키워드 요약 | LoRA 태그 캡션 요약 |
| :---: | :--- | :--- | :--- |
| **`toto_17`** | **뒷다리로 일어서서 두 앞발 모은 포즈 (미어캣/간식 조르기)** | `standing on hind legs, begging pose, folded front paws, tail wagging, cream white puppy, sky blue bandana` | `1dog, toto, puppy, standing on hind legs, begging, fluffy dog, blue bandana, anime style, ghibli aesthetic` |
| **`toto_18`** | **연구실 작업대 위 아크릴 기어와 톱니바퀴 냄새 맡기** | `sniffing colorful acrylic gear on workbench, curious puppy face, electronics lab background` | `1dog, toto, puppy, sniffing gear, cogwheel, maker workshop, breadboard background, blue bandana` |
| **`toto_19`** | **초록 잔디밭과 야생화 사이에서 바람을 맞으며 쉬는 힐링 컷** | `sitting in sunny green lawn meadow, soft breeze blowing fur, wildflowers, warm sunshine` | `1dog, toto, puppy, outdoors, green grass, meadow, sunny day, fluffy dog, peaceful smile, blue bandana` |
| **`toto_20`** | **공중에 던져진 메이커 부품 토이를 날아올라 캐치하는 점프 컷** | `dynamic mid-air leap, catching a flying soft gear toy, airborne puppy, motion lines, white background` | `1dog, toto, puppy, mid-air, jumping, catching toy, flying paws, dynamic action, white background` |

---

## 🚀 2. 신규 기술 스택별 캐릭터 학습 이미지 기획 (20장)

### [카테고리 A: 엣지 AI & 분산 컴퓨팅]
1. **`dorothy_learn_01 (라즈베리파이 & 엣지 AI)`**
   * **장면:** 도로시가 라즈베리파이 4 모듈에 카메라를 연결하고, 파이썬 실시간 객체 검출(YOLO)로 주변 사물을 인식하며 신기해하는 장면.
   * **캡션:** `1girl, dorothy, raspberry pi, camera module, edge ai, computer vision, bounding boxes on monitor, maker lab, excited expression`
2. **`dorothy_learn_02 (연합학습 - Federated Learning)`**
   * **장면:** 세 대의 라즈베리파이가 이더넷 허브로 연결된 분산 클러스터 앞에서 도로시가 각 노드의 가중치(Gradient)가 중앙 서버로 취합되는 그래프를 가리키는 씬.
   * **캡션:** `1girl, dorothy, federated learning, raspberry pi cluster, decentralized network, ethernet cables, glowing leds, privacy preserving ai`
3. **`hojin_teach_01 (연합학습 수식 & FedAvg 강의)`**
   * **장면:** 이호진 교수님이 대형 칠판에 분산 클라이언트 노드 다이어그램과 FedAvg 수식을 분필로 필기하며 자상하게 설명하는 씬.
   * **캡션:** `1man, hojin, professor, blackboard, federated learning formula, fedavg, client nodes, chalkboard lecture, intellectual mentor`
4. **`toto_assist_01 (라즈베리파이 리본 케이블 조수)`**
   * **장면:** 토토가 라즈베리파이 카메라 리본 케이블을 입에 물고 도로시의 작업대로 조심스럽게 다가오는 귀여운 모습.
   * **캡션:** `1dog, toto, puppy, holding ribbon cable in mouth, raspberry pi, maker assistant, blue bandana, lab workbench`

### [카테고리 B: 컨테이너 가상화 & 데브옵스 (Docker & Linux)]
5. **`dorothy_learn_03 (도커 컨테이너 빌드 성공)`**
   * **장면:** 터미널 화면에 파란 도커 고래 아스키 아트와 `Successfully built container` 문구가 뜨자 도로시가 두 주먹을 불끈 쥐고 환호하는 씬.
   * **캡션:** `1girl, dorothy, cheering, docker, docker whale logo, successful build, dual monitors, developer desk, anime style`
6. **`jiny_review_01 (지니의 매서운 Dockerfile 감수)`**
   * **장면:** 조교 지니가 안경을 코끝에 걸치고 모니터의 Dockerfile 레이어 캐시 순서를 앞발로 콕 짚으며 훈수 두는 씬.
   * **캡션:** `1cat, jiny, tuxedo cat, glasses, inspecting code, dockerfile, terminal screen, sharp focus, technical reviewer cat`
7. **`dorothy_learn_04 (리눅스 CLI & Bash 마스터)`**
   * **장면:** 어두운 밤 연구실, 초록색 텍스트가 깜빡이는 리눅스 터미널 앞에서 도로시가 파이프라인(`grep | awk`) 쉘 스크립트를 능숙하게 입력하는 씬.
   * **캡션:** `1girl, dorothy, typing on keyboard, linux terminal, green text, bash script, dark mode, focused, glowing screen`
8. **`toto_mascot_01 (도커 고래 인형과 토토)`**
   * **장면:** 토토가 파란색 도커 고래 봉제인형 곁에 누워 인형 위에 턱을 괴고 낮잠을 청하는 사랑스러운 씬.
   * **캡션:** `1dog, toto, puppy, sleeping beside blue whale plush toy, docker mascot, cozy lab, warm light`

### [카테고리 C: 데이터베이스 & SQL (MySQL & PostgreSQL)]
9. **`dorothy_learn_05 (MySQL 테이블 설계 & ER 다이어그램)`**
   * **장면:** 화이트보드에 도로시가 컬러 마커로 학생-센서 데이터 ERD(개체 관계도)와 1:N 관계선, Primary Key를 직접 그리는 씬.
   * **캡션:** `1girl, dorothy, drawing erd diagram, whiteboard, relational database, mysql, primary key, colorful markers, thoughtful smile`
10. **`dorothy_learn_06 (PostgreSQL JSONB & 윈도우 함수)`**
    * **장면:** 도로시가 대형 모니터에서 복잡한 SQL 집계 쿼리와 JSONB 비정형 데이터 쿼리를 실행하고 인덱스 플랜을 분석하는 씬.
    * **캡션:** `1girl, dorothy, postgresql, database query, explain analyze, execution plan, dual screen, deep thinking`
11. **`hojin_teach_02 (ACID 트랜잭션과 B-Tree 인덱스 지도)`**
    * **장면:** 이호진 교수님이 모니터 옆에서 B-Tree 인덱스의 탐색 원리와 원자성(Atomicity)을 손가락으로 차근차근 짚어주는 씬.
    * **캡션:** `1man, hojin, professor, mentoring, b-tree index diagram, database architecture, explaining, gentle smile`
12. **`jiny_review_02 (지니와 PostgreSQL 코끼리 마스코트)`**
    * **장면:** 조교 지니가 작고 귀여운 파란 PostgreSQL 코끼리 피규어를 앞발로 툭 건드리며 만족스럽게 식빵을 굽는 씬.
    * **캡션:** `1cat, jiny, tuxedo cat, cat loaf, blue elephant figurine, postgresql mascot, cozy desk, purring`

### [카테고리 D: 엔터프라이즈 & 웹 프로그래밍 (Java, PHP, JavaScript, Python)]
13. **`dorothy_learn_07 (자바 객체지향 4대 원칙 UML)`**
    * **장면:** 도로시가 유리 칠판에 자바 상속(Inheritance), 캡슐화(Encapsulation), 다형성(Polymorphism) 클래스 구조를 그리며 뿌듯해하는 씬.
    * **캡션:** `1girl, dorothy, java oop, glass board, drawing class hierarchy, interfaces, spring boot book on desk`
14. **`dorothy_learn_08 (PHP 레거시 웹 리팩토링)`**
    * **장면:** 모니터 좌측에는 오래된 PHP 웹 게시판 코드, 우측에는 세련된 파이썬 FastAPI 코드를 띄워두고 현대적 API 구조로 전환하는 도로시.
    * **캡션:** `1girl, dorothy, code refactoring, php to modern api, split screen, side by side code, purple elephant toy`
15. **`dorothy_learn_09 (자바스크립트 인터랙티브 3D 대시보드)`**
    * **장면:** 브라우저 화면에 Three.js와 웹소켓(WebSocket)으로 아두이노 모형 로봇이 3D로 실시간 회전하는 대시보드를 완성하고 기뻐하는 씬.
    * **캡션:** `1girl, dorothy, javascript, threejs, web dashboard, real time robot telemetry, glowing browser, celebrating`
16. **`jiny_review_03 (지니의 비동기 코드 검수 - Promise & Async)`**
    * **장면:** 조교 지니가 자바스크립트 `Promise.all` 비동기 처리 다이어그램 화면 앞에서 고개를 끄덕이며 골골송을 부르는 씬.
    * **캡션:** `1cat, jiny, tuxedo cat, glasses, looking at async javascript flow, nodding, content expression`

### [카테고리 E: 종합 팀워크 & 모험 (Team Collaboration)]
17. **`team_lab_01 (4인방의 심야 해커톤)`**
    * **장면:** 교수님의 아늑한 연구실에서 4인방이 모여 라즈베리파이+도커+연합학습 로봇 프로젝트를 완성하고 밤하늘 창가 아래서 환하게 웃는 단체 씬.
    * **캡션:** `group of 4, hojin, dorothy, jiny, toto, robotics research lab, night window, starry sky, completed autonomous rover, unity, triumph`
18. **`dorothy_learn_10 (모바일 AI 비전 앱 필드 테스트)`**
    * **장면:** 도로시가 태블릿 카메라로 토토를 비추자 화면에 `[Bichon Mix: 99.8% - Happy Puppy]` AI 바운딩 박스가 뜨고 둘 다 활짝 웃는 씬.
    * **캡션:** `1girl, dorothy, holding tablet, object detection app, camera bounding box on puppy toto, outdoor sunshine, joyful bond`
19. **`jiny_toto_01 (지니와 토토의 하드웨어 페어 프로그래밍)`**
    * **장면:** 지니가 돋보기로 부품 라벨을 읽어주면 토토가 공구 가방에서 맞는 핀셋을 꺼내주는 환상의 동물 조수 듀오 씬.
    * **캡션:** `1cat jiny, 1dog toto, team work, cat pointing with paw, puppy holding tweezers, electronic parts, cute duo`
20. **`hojin_vision_01 (미래를 향한 컴퓨팅 과학 로드맵 발표)`**
    * **장면:** 이호진 교수님이 대형 디지털 홀로그램 스크린 앞에서 도로시, 지니, 토토에게 미래 양자 컴퓨팅과 우주 탐사 AI의 비전을 제시하는 씬.
    * **캡션:** `1man, hojin, professor, futuristic hologram screen, ai roadmap, mentoring young dorothy, inspiring vision, prestigious lab`

---

## ⚙️ 3. 자동화 생성 스크립트 구축
이미지 생성 API 쿼터가 리셋되는 즉시(약 2시간 50분 후) 위 24개 이미지 및 캡션을 일괄 생성하여 데이터셋 폴더에 자동 배치할 수 있도록 [`scripts/generate_learning_dataset.py`](file:///Users/hojin9/dev/projects/dorothy/scripts/generate_learning_dataset.py) 스크립트를 준비합니다.
