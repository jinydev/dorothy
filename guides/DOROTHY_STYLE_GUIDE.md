# 📘 도로시(Dorothy) 캐릭터 이미지 생성 스타일 가이드라인

본 가이드라인은 **도로시(Dorothy)** 및 동반 캐릭터(지니, 토토)가 등장하는 아두이노·과학 교육 콘텐츠 및 삽화에서 **외모, 의상, 색감, 화풍(Art Style)의 일관성(Consistency)**을 100% 유지하며 고품질 이미지를 생성하기 위한 표준 가이드입니다.

---

## 1. 캐릭터 디자인 표준 규격 (Character Specification)

### 👧 도로시 (Dorothy)
* **나이 및 체형:** 만 8~10세의 발랄하고 호기심 많은 소녀, 균형 잡힌 2D 애니메이션 비율 (약 4~5등신 치비/주니어 애니메이션 비율)
* **헤어스타일:**
  * 색상: 풍부하고 따뜻한 체스트넛 브라운 (Chestnut / Warm Brown)
  * 스타일: 볼륨감 있는 웨이브 양갈래 머리 (Twin wavy pigtails), 자연스럽게 이마를 덮는 뱅 스타일 앞머리 (Cute front bangs)
  * 액세서리: 양갈래 묶음 부분에 달린 **컬러풀 구슬 방울 머리끈 (Colorful round beads hair ties - 빨강/초록/노랑 구슬)**
* **얼굴 및 표정:**
  * 눈: 크고 또렷한 엠버 브라운/꿀색 눈동자 (Big warm amber-brown eyes), 맑은 하이라이트
  * 인상: 생기 넘치는 밝은 미소, 장난기와 호기심이 담긴 눈빛, 사랑스러운 홍조 (Soft pink rosy cheeks)
* **시그니처 복장 (Signature Outfit):**
  * **상의:** 산뜻한 주황색/노란색 가로 줄무늬 반팔 티셔츠 (Orange & yellow horizontal striped t-shirt)
  * **멜빵바지:** 미디엄 워싱의 클래식 블루 데님 오버롤 (Classic blue denim overalls / dungarees)
    * 앞가슴 포켓에 **"STEM HERO"** 원형 뱃지 부착
    * 앤틱 황동 버클 (Brass buttons/clasps)
    * 발목 위로 롤업된 밑단 (Rolled-up pant cuffs)
  * **신발 및 양말:** 깔끔한 흰색 발목 양말 (White ankle socks) + 캔버스 스타일의 **레드 스니커즈 (Ruby red canvas sneakers)**
* **대체 복장 (상황별 코스튬):**
  * **과학 실험 룩:** 오버롤 위에 흰색 미니 연구 가운 (White lab coat) 착용, 머리 위 또는 눈에 안전 고글 (Safety goggles) 착용
  * **메이커/엔지니어링 룩:** 허리 도구 벨트 (Tool belt), 드라이버 및 측정 도구 소지

---

### 🐾 동반 캐릭터 (Companions)

| 캐릭터 | 종/외형 | 핵심 시각 특징 | 프롬프트 키워드 |
| :--- | :--- | :--- | :--- |
| **지니 (Jiny)** | 연구실 수석 조교 고양이 (Lab Assistant Cat) | • 블랙&화이트 턱시도/젖소 무늬 코숏<br>• 지적인 올리브 그린 눈 & 핑크 코<br>• 빨간 방울 목걸이 & 미니 조교 안경<br>• 코드 디버깅 및 회로 감수 | `Jiny the lab assistant cat, tuxedo cat, black and white cow pattern, olive green eyes, pink nose, red collar with gold bell, tiny round spectacles on nose, intelligent feline TA` |
| **토토 (Toto)** | 메이커 강아지 (Maker Puppy) | • 복슬복슬한 크림 화이트 컬러 (비숑/말티즈 믹스)<br>• 반짝이는 검은 코와 순진무구한 눈<br>• 목에 두른 하늘색 반다나/스카프<br>• 점퍼선 물어오기 & 활기찬 꼬리 | `Toto the fluffy white puppy, cute bichon maltese mix, cream white fur, cheerful sky-blue neckerchief bandana around neck, wagging fluffy tail happily` |

> 💡 전체 캐릭터 페르소나 및 14대 기술 학습 매트릭스는 [CHARACTER_PERSONAS.md](file:///Users/hojin9/dev/projects/dorothy/guides/CHARACTER_PERSONAS.md)를 참고하세요.

## 2. 공통 아트 스타일 & 비주얼 톤 (Art Style & Aesthetics)

* **핵심 화풍:** 
  * 프리미엄 2D 교육 애니메이션 & 지브리 감성의 따뜻한 동화책 일러스트레이션 (High-end 2D storybook anime illustration)
  * 부드럽고 정교한 클린 라인아트 (Crisp clean anime lineart)
  * 맑고 화사한 셀 셰이딩 (Vibrant flat cel shading with soft gradient ambient occlusion)
  * 채도가 과하게 튀지 않으면서도 온화하고 따뜻한 색감 (Warm, inviting, harmonious color palette)
* **금지 스타일 (Negative Rules):**
  * ❌ 과도한 실사/CGI/3D 렌더링 (Photorealistic, uncanny 3D, CGI model)
  * ❌ 어둡거나 칙칙한 느와르/그로테스크 톤 (Grimdark, desaturated, moody noir)
  * ❌ 뭉개진 손가락, 잘못된 아두이노 부품 묘사 (Mutated hands, distorted pins)
  * ❌ 의도하지 않은 한자/일본어 왜곡 문자 (Garbled Asian text, random kanji)

---

## 3. 프롬프트 표준 템플릿 (Prompt Construction)

### ① 긍정 프롬프트 (Positive Prompt) 구조
프롬프트는 항상 아래의 5단 레이어로 조합하여 작성합니다:

```text
[1. 아트 스타일] + [2. 도로시 캐릭터 디테일] + [3. 상황 및 포즈(아두이노/실험)] + [4. 동반자/배경] + [5. 품질/렌더 옵션]
```

#### 표준 긍정 프롬프트 베이스 (Base Positive Prompt)
```text
2D premium anime storybook illustration, clean anime line art, vibrant soft cel shading, studio animation screenshot. 
Dorothy, an adorable 9-year-old girl, wavy chestnut brown hair in twin pigtails tied with colorful round beads, cute front bangs, large warm amber-brown eyes, rosy cheeks, cheerful bright smile. Wearing classic blue denim overalls with rolled cuffs and a "STEM HERO" badge on the chest pocket, orange and yellow horizontal striped t-shirt underneath, white socks, and red canvas sneakers.
[여기에 구체적인 동작 및 상황 묘사 삽입]
[배경 모드 선택: 순수 흰색 배경 or 따뜻한 메이커 실험실]
Highly detailed, masterwork, educational textbook asset, crisp focus, 8k resolution.
```

---

### ② 부정 프롬프트 (Negative Prompt) 표준 세트
일관성을 해치는 요소를 차단하기 위해 아래 내용을 항상 적용합니다:

```text
3d, photorealistic, realistic rendering, cgi, oil painting, rough sketch, grayscale, monochrome, deformed anatomy, bad hands, missing fingers, extra limbs, mutated fingers, poorly drawn face, blurry, low quality, artifact, text watermark, signature, garbled letters, kanji, hiragana, katakana, dark moody atmosphere, horrifying, horror
```

---

## 4. 상황별 프롬프트 추천 예시

### 1) 단독 캐릭터 소개 및 전신 스탠딩 (Cutout/Isolated White BG)
* **목적:** PPT 인트로, 웹사이트 소개, UI 아이콘, 스탠딩 캐릭터
```text
2D premium anime storybook illustration, clean anime line art, vibrant flat cel shading. Full-body character standing portrait of Dorothy, a cute 9-year-old girl with brown wavy twin pigtails with colorful beads hair ties, warm smiling brown eyes, wearing classic blue denim dungarees with "STEM HERO" badge, orange striped shirt, rolled pant cuffs, and red sneakers. Waving one hand cheerfully towards the viewer in a friendly greeting. Pure solid white background, isolated clean cutout, subtle soft contact shadow at feet, no background clutter.
```

### 2) 아두이노 보드 탐구 및 코딩 실습 (Hardware & Tinkering)
* **목적:** 하드웨어 조립, 핀 연결, 브레드보드 실습 설명
```text
2D premium anime storybook illustration, clean line art, soft cel shading. Dorothy sitting at a wooden maker workbench, curiously holding an official cyan-blue Arduino Uno board and inspecting the microcontroller chip with joyful wonder. On the desk are a neat white breadboard with colorful jumping wires, glowing LEDs, and a laptop with beginner C++ code. Floating beside her is Jiny, the cute lavender fairy cat with a glowing star wand. Toto the fluffy white puppy sits happily under the desk. Warm cozy workshop background with tool pegboards and warm sunlight, educational anime aesthetic.
```

### 3) 과학 원리 탐구 및 물리/에너지 실험 (Science & Physics)
* **목적:** 에너지 변환, 회로, 모터, 센서 작동 원리 설명
```text
2D studio anime illustration, crisp line art, vibrant educational visual. Dorothy wearing protective safety goggles on her forehead and a mini white lab coat over her denim overalls, excitedly pointing at an illuminated scientific demonstration apparatus showing glowing energy flows and rotating gears. Her expression is full of 'eureka' discovery and delight. Jiny the purple fairy cat casts sparkling magical stardust that traces the flow of electric current. Bright modern science laboratory background, chalkboard with neat physics diagrams.
```

---

## 5. 생성 모델별 권장 세팅값

### Stable Diffusion XL (SDXL) / ComfyUI / WebUI
* **Model ID:** `stabilityai/stable-diffusion-xl-base-1.0` (또는 애니메이션 특화 SDXL 모델)
* **Sampling Method:** DPM++ 2M Karras 또는 Euler a
* **Sampling Steps:** 28 ~ 35 steps
* **CFG Scale:** 7.0 ~ 8.0
* **해상도:** 
  * 가로형(16:9 슬라이드용): `1376 x 768` 또는 `1344 x 768`
  * 세로형(전신/포트레이트용): `896 x 1152` 또는 `768 x 1024`
  * 정방형(아이콘/카드용): `1024 x 1024`
* **Reference Image (IP-Adapter 사용 시):**
  * `/Users/hojin9/dev/projects/dorothy/data/images/dorothy_front_view.jpg`
  * `/Users/hojin9/dev/projects/dorothy/data/images/dorothy_character_sheet.jpg`

### Midjourney v6
* **파라미터 권장:**
  * `--ar 16:9` (또는 `--ar 3:4`)
  * `--style raw`
  * `--niji 6` (애니메이션 모드 활용 시 가장 안정적)
  * `--cref [dorothy_front_view_url]` (Character Reference 기능 활용 시 도로시 외모 고정)
  * `--cw 80` (의상과 헤어를 철저히 유지)

---

## 6. 품질 검수 체크리스트 (Quality Checklist)

이미지 생성 후 아래 6개 항목을 점검하세요:
- [ ] **헤어스타일:** 브라운 색상의 웨이브 양갈래 머리와 앞머리가 유지되었는가?
- [ ] **헤어 액세서리:** 양갈래 머리끈에 알록달록한 구슬 방울이 표현되었는가?
- [ ] **의상:** 데님 블루 멜빵바지 + 오렌지/옐로우 스트라이프 티셔츠 조합인가?
- [ ] **뱃지:** 멜빵바지 앞주머니에 'STEM HERO' 뱃지가 올바르게 표현되었는가?
- [ ] **신발:** 롤업된 밑단 아래로 흰색 양말과 빨간색 스니커즈가 착용되었는가?
- [ ] **화풍:** 사실적인 3D나 과도한 실사 없이 따뜻하고 깔끔한 2D 애니메이션 화풍인가?
