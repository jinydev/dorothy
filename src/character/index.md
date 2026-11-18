---
layout: home
title: "공학 모험 연구실 캐릭터 5총사 - 공식 프로필 & 데이터셋 갤러리"
description: "이호진 교수님, 도로시, 지니(고양이), 토토(강아지), 티니(로봇)의 공식 디자인 규격, 컬러 팔레트, AI 프롬프트 및 142컷 데이터셋 갤러리 포털"
permalink: /character/
---

<style>
  .character-hero {
    background: linear-gradient(180deg, #f8faff 0%, #edf3fb 100%);
    padding: 4.5rem 1.5rem 3rem;
    margin-bottom: 2.5rem;
    border-bottom: 1px solid #e2e8f0;
  }
  .character-hero-title {
    font-size: 2.75rem;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.03em;
    line-height: 1.25;
  }
  .character-hero-subtitle {
    font-size: 1.15rem;
    color: #64748b;
    max-width: 820px;
    margin: 1.25rem auto 1.75rem;
    line-height: 1.7;
  }

  /* 캐릭터 카드 스타일 */
  .char-portal-card {
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 1.5rem;
    overflow: hidden;
  }
  .char-portal-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 35px -10px rgba(0, 0, 0, 0.12) !important;
    border-color: #3b82f6 !important;
  }
  .char-portal-img-wrap {
    background: linear-gradient(180deg, #f8fafc 0%, #edf2f7 100%);
    height: 240px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    position: relative;
    border-bottom: 1px solid #e2e8f0;
  }
  .char-portal-img-wrap img {
    max-height: 210px;
    width: auto;
    object-fit: contain;
    transition: transform 0.35s ease;
  }
  .char-portal-card:hover .char-portal-img-wrap img {
    transform: scale(1.08);
  }

  .hover-shadow {
    transition: transform 0.25s ease, box-shadow 0.25s ease;
  }
  .hover-shadow:hover {
    transform: translateY(-4px);
    box-shadow: 0 16px 32px -8px rgba(0, 0, 0, 0.1) !important;
  }
</style>

<!-- 상단 풀와이드 히어로 영역 -->
<div class="character-hero">
  <div class="container text-center">
    <div class="d-inline-flex align-items-center gap-2 px-3 py-1 rounded-pill bg-white border text-secondary small fw-bold mb-3 shadow-sm">
      <span class="text-primary">🎨</span>
      <span>jiny.dev Characters & Concept Dataset</span>
    </div>
    <h1 class="character-hero-title mb-3">
      공학 모험 연구실 캐릭터 5총사
    </h1>
    <p class="character-hero-subtitle">
      컴퓨터 공학과 하드웨어 이론을 흥미진진하게 풀어내는 <strong>연구실 5총사</strong>의 개별 프로필 허브입니다.<br class="d-none d-md-block">
      각 캐릭터를 선택하면 <strong>공식 조형 규격, 표준 컬러 팔레트, AI 프롬프트</strong>와 <strong>전체 고해상도 데이터셋 갤러리</strong> 페이지로 바로 이동합니다.
    </p>

    <!-- 부가 정보 배지 -->
    <div class="d-flex flex-wrap justify-content-center gap-2">
      <span class="badge rounded-pill bg-white text-secondary border px-3 py-2 fw-medium">🌟 총 5개 핵심 캐릭터 (142컷)</span>
      <span class="badge rounded-pill bg-white text-secondary border px-3 py-2 fw-medium">🧩 총 5대 파츠 & 환경 에셋 (67컷)</span>
      <span class="badge rounded-pill bg-white text-secondary border px-3 py-2 fw-medium">📐 조형 비례 & 컬러 팔레트 완비</span>
      <span class="badge rounded-pill bg-white text-secondary border px-3 py-2 fw-medium">🎨 100% 지브리풍 2D 애니메이션 화풍</span>
    </div>
  </div>
</div>

<!-- 본문 콘텐츠 영역 -->
<div class="container pb-5">
  <!-- 공통 서브 네비게이션 -->
  {% include character_nav_bar.html %}

  <!-- 캐릭터 5총사 카드 그리드 -->
  <div class="row row-cols-1 row-cols-md-2 row-cols-xl-3 g-4 mb-5">
    {% for char in site.data.characters.characters %}
    <div class="col">
      <div class="card h-100 char-portal-card shadow-sm d-flex flex-column justify-content-between">
        <div>
          <!-- 상단 아바타 썸네일 영역 -->
          <div class="char-portal-img-wrap">
            <img src="{{ char.avatar | relative_url }}" alt="{{ char.name }}" loading="lazy">
            <span class="position-absolute top-0 end-0 m-3 badge rounded-pill bg-white text-dark border shadow-sm px-3 py-2 fw-bold">
              📸 {{ char.image_count }}컷
            </span>
          </div>

          <!-- 카드 본문 정보 영역 -->
          <div class="card-body p-4">
            <div class="d-flex align-items-center gap-2 mb-2">
              <span class="badge rounded-pill {{ char.role_badge }} px-3 py-1 fw-bold">{{ char.role }}</span>
              <span class="text-muted small font-monospace">{{ char.en_name }}</span>
            </div>
            
            <h3 class="h4 fw-bold text-dark mb-2">
              <a href="{{ char.profile_url | relative_url }}" class="text-decoration-none text-dark hover-primary">
                {{ char.name }}
              </a>
            </h3>

            <!-- 인용구 -->
            <div class="p-3 rounded-3 bg-light border-start border-3 my-3" style="border-left-color: {{ char.theme_color }} !important;">
              <p class="fst-italic text-secondary small mb-0 leading-relaxed">
                "{{ char.quote }}"
              </p>
            </div>

            <!-- 설명 -->
            <p class="text-secondary small leading-relaxed mb-3">
              {{ char.description }}
            </p>

            <!-- 특징 태그 뱃지 -->
            <div class="d-flex flex-wrap gap-1 mb-2">
              {% for trait in char.traits %}
              <span class="badge bg-light text-secondary border fw-normal" style="font-size: 0.76rem;">{{ trait }}</span>
              {% endfor %}
            </div>
          </div>
        </div>

        <!-- 하단 바로가기 버튼 영역 -->
        <div class="card-footer bg-white border-0 px-4 pb-4 pt-0">
          <a href="{{ char.profile_url | relative_url }}" class="btn btn-outline-dark w-100 rounded-pill py-2 fw-bold shadow-sm d-flex align-items-center justify-content-center gap-2">
            <span>{{ char.name }} 상세 프로필 & 갤러리</span>
            <span>➔</span>
          </a>
        </div>
      </div>
    </div>
    {% endfor %}

    <!-- 6번째 카드: 파츠 & 배경 에셋 데이터셋 67컷 안내 카드 -->
    <div class="col">
      <div class="card h-100 char-portal-card shadow-sm d-flex flex-column justify-content-between" style="border: 2px dashed #93c5fd !important; background: linear-gradient(180deg, #ffffff 0%, #f0f7ff 100%);">
        <div>
          <div class="char-portal-img-wrap" style="background: linear-gradient(135deg, #e0f2fe 0%, #dbeafe 100%);">
            <div class="text-center p-3">
              <span class="display-3 d-block mb-1">🧩</span>
              <span class="badge bg-primary text-white rounded-pill px-3 py-1 fw-bold">보조 데이터셋 67종</span>
            </div>
            <span class="position-absolute top-0 end-0 m-3 badge rounded-pill bg-white text-primary border shadow-sm px-3 py-2 fw-bold">
              5개 카테고리
            </span>
          </div>

          <div class="card-body p-4">
            <div class="d-flex align-items-center gap-2 mb-2">
              <span class="badge rounded-pill bg-info text-dark px-3 py-1 fw-bold">Environments & Parts</span>
              <span class="text-muted small font-monospace">Parts Dataset</span>
            </div>
            
            <h3 class="h4 fw-bold text-dark mb-2">
              <a href="{{ '/character/parts/' | relative_url }}" class="text-decoration-none text-dark">
                파츠 & 배경 에셋 데이터셋
              </a>
            </h3>

            <div class="p-3 rounded-3 bg-white border-start border-3 my-3" style="border-left-color: #0284c7 !important;">
              <p class="fst-italic text-secondary small mb-0 leading-relaxed">
                "노트북·PC·GPU, 시그모이드/ReLU, 시그마·적분·나블라 수학 기호, 연구실 배경 및 최신 프레임워크 로고까지 온전한 지브리 스타일 에셋 완비!"
              </p>
            </div>

            <p class="text-secondary small leading-relaxed mb-3">
              연구실 환경(6컷), 컴퓨팅 디바이스 & 하드웨어(17컷), 소프트웨어(6컷), AI 수학 도식(14컷), 기술 로고 엠블럼(24컷) 등 총 67컷의 고해상도 에셋을 제공합니다.
            </p>

            <div class="d-flex flex-wrap gap-1 mb-2">
              <span class="badge bg-white text-secondary border fw-normal" style="font-size: 0.76rem;">🏛️ 연구실 환경</span>
              <span class="badge bg-white text-secondary border fw-normal" style="font-size: 0.76rem;">💻 디바이스 & HW</span>
              <span class="badge bg-white text-secondary border fw-normal" style="font-size: 0.76rem;">💾 IDE/코드</span>
              <span class="badge bg-white text-secondary border fw-normal" style="font-size: 0.76rem;">🧠 AI/수학 기호</span>
              <span class="badge bg-white text-secondary border fw-normal" style="font-size: 0.76rem;">🛡️ 기술 로고</span>
            </div>
          </div>
        </div>

        <div class="card-footer bg-transparent border-0 px-4 pb-4 pt-0">
          <a href="{{ '/character/parts/' | relative_url }}" class="btn btn-primary w-100 rounded-pill py-2 fw-bold shadow-sm d-flex align-items-center justify-content-center gap-2">
            <span>파츠 & 에셋 67컷 전체보기</span>
            <span>➔</span>
          </a>
        </div>
      </div>
    </div>
  </div>

  ---

  <!-- 캐릭터 5총사 조형 및 스펙 비교 매트릭스 표 -->
  <div class="my-5">
    <div class="d-flex align-items-center justify-content-between mb-4 pb-2 border-bottom">
      <div>
        <h2 class="h3 fw-bold mb-1 text-dark">📊 캐릭터 5총사 공식 조형 및 스펙 비교표</h2>
        <p class="text-muted small mb-0">각 캐릭터의 신체 비례, 대표 장비, 기술 분야 및 상호 보완 관계 한눈에 보기</p>
      </div>
    </div>

    <div class="table-responsive rounded-4 border shadow-sm">
      <table class="table table-hover align-middle mb-0 text-center" style="font-size: 0.92rem;">
        <thead class="table-light">
          <tr>
            <th class="py-3 text-start ps-4" style="min-width: 140px;">캐릭터</th>
            <th class="py-3" style="min-width: 130px;">역할 & 포지션</th>
            <th class="py-3" style="min-width: 120px;">신체 비례</th>
            <th class="py-3" style="min-width: 160px;">시그니처 장비/소품</th>
            <th class="py-3" style="min-width: 180px;">주요 기술 스택</th>
            <th class="py-3" style="min-width: 160px;">핵심 성격 및 매력</th>
            <th class="py-3 pe-4" style="min-width: 110px;">상세 페이지</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="text-start ps-4 fw-bold">
              <a href="{{ '/character/hojin/' | relative_url }}" class="text-decoration-none text-dark d-flex align-items-center gap-2">
                <span class="fs-5">👨‍🏫</span>
                <span>이호진 교수님</span>
              </a>
            </td>
            <td><span class="badge rounded-pill bg-success px-3 py-1">총괄 멘토</span></td>
            <td>6.5 ~ 7.0등신</td>
            <td>와이어 라운드 안경, 태블릿</td>
            <td>컴퓨터 구조, 회로 설계, 어셈블리</td>
            <td>지적이고 인자함, 원리주의</td>
            <td class="pe-4">
              <a href="{{ '/character/hojin/' | relative_url }}" class="btn btn-sm btn-outline-success rounded-pill px-3">보기</a>
            </td>
          </tr>
          <tr>
            <td class="text-start ps-4 fw-bold">
              <a href="{{ '/character/dorothy/' | relative_url }}" class="text-decoration-none text-dark d-flex align-items-center gap-2">
                <span class="fs-5">👧</span>
                <span>도로시</span>
              </a>
            </td>
            <td><span class="badge rounded-pill bg-warning text-dark px-3 py-1">주니어 메이커</span></td>
            <td>4.5등신</td>
            <td>청 멜빵바지, 붉은 스니커즈, 납땜기</td>
            <td>파이썬, 아두이노, 3D 프린팅</td>
            <td>호기심 폭발, 두려움 없는 도전</td>
            <td class="pe-4">
              <a href="{{ '/character/dorothy/' | relative_url }}" class="btn btn-sm btn-outline-warning text-dark rounded-pill px-3">보기</a>
            </td>
          </tr>
          <tr>
            <td class="text-start ps-4 fw-bold">
              <a href="{{ '/character/jiny/' | relative_url }}" class="text-decoration-none text-dark d-flex align-items-center gap-2">
                <span class="fs-5">🐱</span>
                <span>지니</span>
              </a>
            </td>
            <td><span class="badge rounded-pill bg-indigo text-white px-3 py-1" style="background-color: #6366f1;">AI 테크 코치</span></td>
            <td>2.0 ~ 2.5등신</td>
            <td>초소형 무선 헤드셋, 레이저 포인터</td>
            <td>딥러닝, PyTorch, 강화학습</td>
            <td>차분하고 냉철함, 완벽주의 츤데레</td>
            <td class="pe-4">
              <a href="{{ '/character/jiny/' | relative_url }}" class="btn btn-sm btn-outline-primary rounded-pill px-3">보기</a>
            </td>
          </tr>
          <tr>
            <td class="text-start ps-4 fw-bold">
              <a href="{{ '/character/toto/' | relative_url }}" class="text-decoration-none text-dark d-flex align-items-center gap-2">
                <span class="fs-5">🐶</span>
                <span>토토</span>
              </a>
            </td>
            <td><span class="badge rounded-pill bg-amber text-dark px-3 py-1" style="background-color: #f59e0b;">하드웨어 서포터</span></td>
            <td>2.0등신</td>
            <td>툴 벨트, 몽키스패너, 부품 바구니</td>
            <td>전원 관리, 센서 연결, 장비 조립</td>
            <td>충성심 가득, 무한한 활력, 긍정 에너지</td>
            <td class="pe-4">
              <a href="{{ '/character/toto/' | relative_url }}" class="btn btn-sm btn-outline-warning text-dark rounded-pill px-3">보기</a>
            </td>
          </tr>
          <tr>
            <td class="text-start ps-4 fw-bold">
              <a href="{{ '/character/tinny/' | relative_url }}" class="text-decoration-none text-dark d-flex align-items-center gap-2">
                <span class="fs-5">🤖</span>
                <span>티니 로봇</span>
              </a>
            </td>
            <td><span class="badge rounded-pill bg-cyan text-dark px-3 py-1" style="background-color: #06b6d4;">임베디드 로봇</span></td>
            <td>2.5등신</td>
            <td>도트 매트릭스 LED 눈, 전력 게이지</td>
            <td>C/C++, FreeRTOS, GPIO/PWM/I2C</td>
            <td>기계적 논리, 호기심 많은 사랑스러움</td>
            <td class="pe-4">
              <a href="{{ '/character/tinny/' | relative_url }}" class="btn btn-sm btn-outline-info text-dark rounded-pill px-3">보기</a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 하단 퀵 링크 카드 (가이드 및 세계관) -->
  <div class="row g-4 my-4">
    <div class="col-md-6">
      <div class="card h-100 border-0 rounded-4 p-4 shadow-sm" style="background: linear-gradient(135deg, #fdf4ff 0%, #fae8ff 100%);">
        <div class="d-flex align-items-center gap-3 mb-3">
          <div class="p-3 bg-white rounded-circle shadow-sm fs-3">📐</div>
          <div>
            <h4 class="fw-bold mb-1 text-dark">캐릭터 제작 & AI 데이터셋 가이드</h4>
            <p class="text-muted small mb-0">Multi-Concept LoRA 학습 규칙 및 AI 프롬프트 가이드</p>
          </div>
        </div>
        <p class="text-secondary small leading-relaxed mb-4">
          공식 139MB 데이터셋의 폴더 구조, 태그 표기법, AI 모델별 최적의 프롬프트 공식 및 다각도 일관성 유지 테크닉을 상세히 제공합니다.
        </p>
        <a href="{{ '/character/guide/' | relative_url }}" class="btn btn-outline-primary rounded-pill fw-bold px-4 py-2 mt-auto align-self-start">
          가이드 문서 읽기 ➔
        </a>
      </div>
    </div>

    <div class="col-md-6">
      <div class="card h-100 border-0 rounded-4 p-4 shadow-sm" style="background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);">
        <div class="d-flex align-items-center gap-3 mb-3">
          <div class="p-3 bg-white rounded-circle shadow-sm fs-3">🌌</div>
          <div>
            <h4 class="fw-bold mb-1 text-dark">공학 모험 세계관 & 교육 철학</h4>
            <p class="text-muted small mb-0">jiny.dev 세계관 배경 스토리 및 원리 우선주의 STEM 교육 철학</p>
          </div>
        </div>
        <p class="text-secondary small leading-relaxed mb-4">
          '두려워 말고 질문하고, 코드를 작성하며, 직접 손으로 만들어 보라!' jiny.dev 연구실의 탄생 배경과 캐릭터 간의 상호작용 스토리를 확인하세요.
        </p>
        <a href="{{ '/character/universe/' | relative_url }}" class="btn btn-primary rounded-pill fw-bold px-4 py-2 mt-auto align-self-start">
          세계관 스토리 읽기 ➔
        </a>
      </div>
    </div>
  </div>
</div>
