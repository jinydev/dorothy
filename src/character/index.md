---
layout: home
title: "공학 모험 연구실 캐릭터 5총사 - 상세 프로필 & 데이터셋 갤러리"
description: "이호진 교수님, 도로시, 지니(고양이), 토토(강아지), 티니(로봇)의 상세 프로필 규격, 컬러 팔레트, AI 프롬프트 및 142컷 데이터셋 갤러리"
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
  
  /* 캐릭터 선택 네비게이션 탭 */
  .char-nav-tabs {
    border: none;
    gap: 0.75rem;
    justify-content: center;
    margin-bottom: 2.5rem;
  }
  .char-nav-tabs .nav-link {
    background: #ffffff;
    border: 1px solid #e2e8f0 !important;
    border-radius: 1rem !important;
    padding: 0.85rem 1.4rem;
    color: #475569;
    font-weight: 700;
    font-size: 1rem;
    display: inline-flex;
    align-items: center;
    gap: 0.65rem;
    transition: all 0.25s ease;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
  }
  .char-nav-tabs .nav-link:hover {
    background: #f8fafc;
    border-color: #cbd5e1 !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
  }
  .char-nav-tabs .nav-link.active {
    background: #0f172a !important;
    color: #ffffff !important;
    border-color: #0f172a !important;
    box-shadow: 0 8px 20px rgba(15, 23, 42, 0.25);
    transform: translateY(-2px);
  }
  .char-nav-tabs .nav-link .char-tab-badge {
    font-size: 0.75rem;
    padding: 0.2rem 0.55rem;
    border-radius: 9999px;
    background: #f1f5f9;
    color: #475569;
    transition: all 0.2s ease;
  }
  .char-nav-tabs .nav-link.active .char-tab-badge {
    background: rgba(255, 255, 255, 0.2);
    color: #ffffff;
  }

  /* 캐릭터 상세 프로필 카드 */
  .char-profile-banner {
    border-radius: 1.5rem;
    border: 1px solid #e2e8f0;
    background: #ffffff;
    box-shadow: 0 4px 15px -2px rgba(0,0,0,0.05);
    overflow: hidden;
    margin-bottom: 2.5rem;
  }
  
  /* 데이터셋 썸네일 그리드 */
  .dataset-thumbnail-card {
    transition: all 0.2s ease;
    background: #ffffff;
    border: 1px solid #e2e8f0;
  }
  .dataset-thumbnail-card:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 8px 20px rgba(0,0,0,0.12) !important;
    border-color: #3b82f6 !important;
  }
  .dataset-img-wrap {
    position: relative;
    width: 100%;
    padding-top: 100%;
    overflow: hidden;
    background: #f8fafc;
    border-radius: 0.65rem 0.65rem 0 0;
  }
  .dataset-img-wrap img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
  }
  .dataset-thumbnail-card:hover .dataset-img-wrap img {
    transform: scale(1.06);
  }

  /* 컬러 팔레트 칩 */
  .palette-chip {
    display: inline-block;
    width: 28px;
    height: 28px;
    border-radius: 6px;
    border: 1px solid rgba(0,0,0,0.15);
    box-shadow: inset 0 1px 2px rgba(0,0,0,0.1);
  }

  .hover-shadow {
    transition: transform 0.25s ease, box-shadow 0.25s ease;
  }
  .hover-shadow:hover {
    transform: translateY(-4px);
    box-shadow: 0 16px 32px -8px rgba(0, 0, 0, 0.1) !important;
  }
</style>

<!-- 상단 풀와이드 히어로 헤딩 영역 -->
<div class="character-hero">
  <div class="container text-center">
    <div class="d-inline-flex align-items-center gap-2 px-3 py-1 rounded-pill bg-white border text-secondary small fw-bold mb-3 shadow-sm">
      <span class="text-primary">🎨</span>
      <span>jiny.dev Characters & Concept Dataset</span>
    </div>
    <h1 class="character-hero-title mb-3">
      공학 모험 연구실 캐릭터 5총사 상세 프로필
    </h1>
    <p class="character-hero-subtitle">
      컴퓨터 공학과 하드웨어 이론을 흥미진진하게 풀어내는 <strong>연구실 5총사</strong>의 상세 프로필입니다.<br class="d-none d-md-block">
      아래에서 <strong>캐릭터를 선택</strong>하면 <strong>공식 조형 규격, 표준 컬러 팔레트, AI 프롬프트</strong>와 <strong>전체 데이터셋 갤러리</strong>를 바로 확인할 수 있습니다.
    </p>

    <!-- 부가 정보 배지 -->
    <div class="d-flex flex-wrap justify-content-center gap-2">
      <span class="badge rounded-pill bg-white text-secondary border px-3 py-2 fw-medium">🌟 총 5개 핵심 캐릭터 (142컷)</span>
      <span class="badge rounded-pill bg-white text-secondary border px-3 py-2 fw-medium">🧩 총 5대 파츠 & 환경 에셋 (44컷)</span>
      <span class="badge rounded-pill bg-white text-secondary border px-3 py-2 fw-medium">📐 조형 비례 & 컬러 팔레트 완비</span>
    </div>
  </div>
</div>

<!-- 본문 콘텐츠 영역 (사이드바 없는 풀 와이드 컨테이너) -->
<div class="container pb-5">

  <!-- 캐릭터 상세 프로필 선택 탭 (Bootstrap Nav Pills) -->
  <ul class="nav nav-pills char-nav-tabs" id="characterTabs" role="tablist">
    <li class="nav-item" role="presentation">
      <button class="nav-link active" id="tab-btn-hojin" data-bs-toggle="pill" data-bs-target="#tab-hojin" type="button" role="tab" aria-controls="tab-hojin" aria-selected="true">
        <span>👨‍🏫</span>
        <span>이호진 교수님</span>
        <span class="char-tab-badge">30컷</span>
      </button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link" id="tab-btn-dorothy" data-bs-toggle="pill" data-bs-target="#tab-dorothy" type="button" role="tab" aria-controls="tab-dorothy" aria-selected="false">
        <span>👧</span>
        <span>도로시</span>
        <span class="char-tab-badge">42컷</span>
      </button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link" id="tab-btn-jiny" data-bs-toggle="pill" data-bs-target="#tab-jiny" type="button" role="tab" aria-controls="tab-jiny" aria-selected="false">
        <span>🐱</span>
        <span>지니</span>
        <span class="char-tab-badge">26컷</span>
      </button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link" id="tab-btn-toto" data-bs-toggle="pill" data-bs-target="#tab-toto" type="button" role="tab" aria-controls="tab-toto" aria-selected="false">
        <span>🐶</span>
        <span>토토</span>
        <span class="char-tab-badge">22컷</span>
      </button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link" id="tab-btn-tinny" data-bs-toggle="pill" data-bs-target="#tab-tinny" type="button" role="tab" aria-controls="tab-tinny" aria-selected="false">
        <span>🤖</span>
        <span>티니 로봇</span>
        <span class="char-tab-badge">22컷</span>
      </button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link" id="tab-btn-parts" data-bs-toggle="pill" data-bs-target="#tab-parts" type="button" role="tab" aria-controls="tab-parts" aria-selected="false">
        <span>🧩</span>
        <span>파츠 & 배경 에셋</span>
        <span class="char-tab-badge">44컷</span>
      </button>
    </li>
  </ul>

  <!-- 탭 콘텐츠 영역 -->
  <div class="tab-content" id="characterTabContent">

    {% for char in site.data.characters.characters %}
    <!-- 개별 탭 패널: {{ char.name }} -->
    <div class="tab-pane fade {% if forloop.first %}show active{% endif %}" id="tab-{{ char.id }}" role="tabpanel" aria-labelledby="tab-btn-{{ char.id }}">
      
      <!-- 1. 캐릭터 마스터 헤더 배너 -->
      <div class="char-profile-banner" style="border-top: 6px solid {{ char.theme_color }};">
        <div class="p-4 p-md-5" style="background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);">
          <div class="row align-items-center">
            <!-- 아바타 이미지 -->
            <div class="col-md-3 col-lg-2 text-center mb-3 mb-md-0">
              <div class="position-relative d-inline-block p-2 rounded-4 bg-white shadow-sm border" style="border-color: {{ char.theme_color }} !important;">
                <img src="{{ char.avatar | relative_url }}"
                     alt="{{ char.name }}"
                     class="img-fluid rounded-3"
                     style="width: 150px; height: 150px; object-fit: cover;"
                     loading="lazy">
              </div>
            </div>

            <!-- 프로필 기본 정보 -->
            <div class="col-md-9 col-lg-7 ps-md-4">
              <div class="d-flex flex-wrap align-items-center gap-2 mb-2">
                <span class="badge rounded-pill {{ char.role_badge }} px-3 py-1 fw-bold">{{ char.role }}</span>
                <span class="text-muted small fw-medium">{{ char.en_name }}</span>
                <span class="badge rounded-pill bg-light text-dark border px-2 py-1 small">
                  📷 데이터셋 {{ char.image_count }}컷 완비
                </span>
              </div>
              <h2 class="display-6 fw-bold text-dark mb-2" style="letter-spacing: -0.02em;">
                {{ char.name }}
              </h2>
              <blockquote class="text-secondary fst-italic mb-3 ps-3 border-start border-3" style="border-color: {{ char.theme_color }} !important; font-size: 1.05rem;">
                "{{ char.quote }}"
              </blockquote>
              <p class="text-secondary mb-3 leading-relaxed">
                {{ char.description }}
              </p>
              <div class="d-flex flex-wrap gap-1">
                {% for trait in char.traits %}
                <span class="badge bg-white text-secondary border px-2 py-1" style="font-size: 0.82rem;">#{{ trait }}</span>
                {% endfor %}
              </div>
            </div>

            <!-- 단독 페이지 링크 -->
            <div class="col-lg-3 text-center text-lg-end mt-4 mt-lg-0">
              <a href="{{ char.profile_url }}" class="btn btn-dark fw-bold rounded-pill px-4 py-2 shadow-sm d-inline-flex align-items-center gap-2">
                <span>전용 상세페이지 이동</span>
                <span>➔</span>
              </a>
            </div>
          </div>
        </div>

        <!-- 2. 캐릭터 상세 정보 (해부학적 조형 규격 & 컬러 팔레트 & AI 프롬프트) -->
        <div class="p-4 p-md-5 border-top bg-white">
          <div class="row g-4">
            
            <!-- 왼쪽: 해부학적 형태 & 조형 규격 -->
            <div class="col-lg-7">
              <h3 class="fs-5 fw-bold text-dark mb-3 d-flex align-items-center gap-2">
                <span>📐</span>
                <span>공식 조형 및 신체 규격 (Anatomy & Proportions)</span>
              </h3>
              <div class="table-responsive border rounded-3 overflow-hidden">
                <table class="table table-hover align-middle mb-0" style="font-size: 0.9rem;">
                  <thead class="table-light">
                    <tr>
                      <th style="width: 25%;" class="ps-3">부위 / 항목</th>
                      <th>규격 및 조형 세부 원칙</th>
                    </tr>
                  </thead>
                  <tbody>
                    {% for item in char.anatomy %}
                    <tr>
                      <td class="fw-bold ps-3 text-dark bg-light">{{ item.part }}</td>
                      <td class="text-secondary" style="white-space: pre-line;">{{ item.detail }}</td>
                    </tr>
                    {% endfor %}
                  </tbody>
                </table>
              </div>
            </div>

            <!-- 오른쪽: 표준 컬러 팔레트 -->
            <div class="col-lg-5">
              <h3 class="fs-5 fw-bold text-dark mb-3 d-flex align-items-center gap-2">
                <span>🌈</span>
                <span>표준 컬러 팔레트 (Color Palette)</span>
              </h3>
              <div class="table-responsive border rounded-3 overflow-hidden">
                <table class="table table-hover align-middle mb-0" style="font-size: 0.88rem;">
                  <thead class="table-light">
                    <tr>
                      <th class="ps-3">항목</th>
                      <th>색상명</th>
                      <th>Hex</th>
                      <th class="text-center" style="width: 50px;">칩</th>
                    </tr>
                  </thead>
                  <tbody>
                    {% for p in char.palette %}
                    <tr>
                      <td class="ps-3 fw-medium text-dark">{{ p.item }}</td>
                      <td class="text-secondary small">{{ p.name }}</td>
                      <td><code>{{ p.hex }}</code></td>
                      <td class="text-center">
                        <span class="palette-chip" style="background-color: {{ p.hex }};"></span>
                      </td>
                    </tr>
                    {% endfor %}
                  </tbody>
                </table>
              </div>
            </div>

            <!-- 하단: AI 마스터 프롬프트 -->
            {% if char.prompt %}
            <div class="col-12 mt-4">
              <h3 class="fs-5 fw-bold text-dark mb-2 d-flex align-items-center gap-2">
                <span>💡</span>
                <span>표준 AI 생성 프롬프트 블록 (Master Formula)</span>
              </h3>
              <div class="bg-light p-3 rounded-3 border">
                <pre class="mb-0 text-dark small" style="white-space: pre-wrap; font-family: SFMono-Regular, Menlo, Monaco, Consolas, monospace;"><code>{{ char.prompt }}</code></pre>
              </div>
            </div>
            {% endif %}

          </div>
        </div>
      </div>

      <!-- 3. 캐릭터 전용 고해상도 학습 데이터셋 갤러리 -->
      <div class="char-profile-banner p-4 p-md-5">
        <div class="d-flex flex-wrap align-items-center justify-content-between mb-4 pb-2 border-bottom">
          <div>
            <h3 class="fs-4 fw-bold text-dark mb-1 d-flex align-items-center gap-2">
              <span>🖼️</span>
              <span>{{ char.name }} 공식 학습 & 컨셉 데이터셋 갤러리</span>
            </h3>
            <p class="text-secondary small mb-0">
              LoRA 훈련 및 캐릭터 일관성 검증에 사용되는 원본 컷입니다. (각 이미지를 클릭하면 고해상도 원본 확인)
            </p>
          </div>
          <span class="badge rounded-pill bg-primary px-3 py-2 fw-bold shadow-sm mt-2 mt-md-0">
            총 {{ char.image_count }}장
          </span>
        </div>

        <!-- 썸네일 그리드 (모바일 2열 ~ 데스크톱 6열) -->
        <div class="row row-cols-2 row-cols-sm-3 row-cols-md-4 row-cols-lg-6 g-3">
          {% for img in char.images %}
          <div class="col">
            <a href="{{ img.url | relative_url }}" target="_blank" rel="noopener" class="text-decoration-none text-dark">
              <div class="card h-100 dataset-thumbnail-card shadow-sm rounded-3 overflow-hidden">
                <div class="dataset-img-wrap">
                  <img src="{{ img.url | relative_url }}"
                       alt="{{ char.name }} - {{ img.title }}"
                       loading="lazy">
                </div>
                <div class="p-2 text-center bg-white">
                  <div class="text-truncate fw-semibold text-secondary" style="font-size: 0.78rem;" title="{{ img.title }}">
                    {{ img.title }}
                  </div>
                </div>
              </div>
            </a>
          </div>
          {% endfor %}
        </div>
      </div>

    </div>
    {% endfor %}

    <!-- 6번째 탭: 파츠 & 배경 에셋 데이터셋 (assets/dataset/parts) -->
    <div class="tab-pane fade" id="tab-parts" role="tabpanel" aria-labelledby="tab-btn-parts">
      <!-- 상단 인트로 헤더 -->
      <div class="char-profile-banner p-4 p-md-5 mb-5" style="border-top: 6px solid #6366f1;">
        <div class="d-flex flex-wrap align-items-center justify-content-between gap-3">
          <div>
            <div class="d-flex align-items-center gap-2 mb-2">
              <span class="badge rounded-pill bg-indigo text-white px-3 py-1 fw-bold" style="background-color: #6366f1;">Concept & Parts Dataset</span>
              <span class="badge rounded-pill bg-light text-dark border px-2 py-1 small">
                총 5개 카테고리 · 44컷 완비
              </span>
            </div>
            <h2 class="display-6 fw-bold text-dark mb-2" style="letter-spacing: -0.02em;">
              🧩 연구실 환경 · 하드웨어 · 소프트웨어 · AI 이론 · 로고 에셋
            </h2>
            <p class="text-secondary mb-0 leading-relaxed" style="max-width: 780px;">
              연구실의 주 무대가 되는 숲속 캠퍼스 배경부터 피지컬 아두이노/라즈베리파이 부품, 소프트웨어 시스템 아키텍처, 딥러닝 이론 다이어그램, 지브리 감성 테크 로고 엠블럼까지 세밀하게 구축된 공식 비주얼 에셋 모음입니다.
            </p>
          </div>
          <!-- 카테고리 퀵 점프 링크 -->
          <div class="d-flex flex-wrap gap-2">
            {% for cat in site.data.dataset_parts.categories %}
            <a href="#part-{{ cat.id }}" class="btn btn-outline-secondary btn-sm rounded-pill fw-medium">
              <span>{{ cat.icon }}</span>
              <span>{{ cat.name }} ({{ cat.count }})</span>
            </a>
            {% endfor %}
          </div>
        </div>
      </div>

      <!-- 5개 파츠 카테고리별 섹션 -->
      {% for cat in site.data.dataset_parts.categories %}
      <div class="char-profile-banner mb-5" id="part-{{ cat.id }}">
        <!-- 카테고리 헤더 -->
        <div class="p-4 bg-light border-bottom d-flex flex-wrap align-items-center justify-content-between gap-2">
          <div class="d-flex align-items-center gap-3">
            <span class="fs-2">{{ cat.icon }}</span>
            <div>
              <div class="d-flex align-items-center gap-2">
                <h3 class="fs-5 fw-bold text-dark mb-0">{{ cat.name }}</h3>
                <span class="badge rounded-pill {{ cat.badge }} small">{{ cat.en_name }}</span>
              </div>
              <p class="text-secondary small mb-0 mt-1">{{ cat.desc }}</p>
            </div>
          </div>
          <span class="badge rounded-pill bg-white text-secondary border px-3 py-2 small shadow-sm">
            총 {{ cat.count }}장
          </span>
        </div>

        <!-- 썸네일 그리드 -->
        <div class="p-4 p-md-5">
          <div class="row row-cols-2 row-cols-sm-3 row-cols-md-4 row-cols-lg-6 g-3">
            {% for img in cat.images %}
            <div class="col">
              <a href="{{ img.url | relative_url }}" target="_blank" rel="noopener" class="text-decoration-none text-dark">
                <div class="card h-100 dataset-thumbnail-card shadow-sm rounded-3 overflow-hidden">
                  <div class="dataset-img-wrap">
                    <img src="{{ img.url | relative_url }}"
                         alt="{{ img.title }}"
                         loading="lazy">
                  </div>
                  <div class="p-2 text-center bg-white">
                    <div class="text-truncate fw-semibold text-secondary" style="font-size: 0.78rem;" title="{{ img.title }}">
                      {{ img.title }}
                    </div>
                  </div>
                </div>
              </a>
            </div>
            {% endfor %}
          </div>
        </div>
      </div>
      {% endfor %}
    </div>

  </div>

  <!-- 캐릭터 속성 비교표 섹션 -->
  <section class="char-profile-banner p-4 p-md-5 mb-5" id="comparison">
    <div class="d-flex align-items-center mb-4 pb-2 border-bottom">
      <span class="fs-2 me-3">📋</span>
      <div>
        <h2 class="fs-3 fw-bold mb-1 text-dark">캐릭터 핵심 속성 및 역할 비교표</h2>
        <span class="text-secondary small">연구실 5총사의 조형 비율, 시그니처 착장 및 기술 전문 분야 한눈에 비교</span>
      </div>
    </div>

    <div class="table-responsive">
      <table class="table table-hover align-middle mb-0" style="font-size: 0.92rem;">
        <thead class="table-light">
          <tr>
            <th scope="col" style="min-width: 140px;">캐릭터</th>
            <th scope="col">역할 / 포지션</th>
            <th scope="col">연령 / 체형</th>
            <th scope="col">시그니처 아이템</th>
            <th scope="col">주요 전문 분야</th>
            <th scope="col" class="text-center" style="min-width: 120px;">상세보기</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <div class="d-flex align-items-center gap-2">
                <img src="{{ '/assets/img/hojin_thumbs_up.jpg' | relative_url }}" class="rounded-circle border" width="36" height="36" style="object-fit: cover;">
                <strong class="text-success">이호진 교수님</strong>
              </div>
            </td>
            <td>총괄 멘토 & 지도교수</td>
            <td>40대 초반 (6.5~7등신)</td>
            <td>실버 라운드 안경, 네이비 폴로</td>
            <td>컴퓨터 구조, 회로 설계, 원리 직관화</td>
            <td class="text-center">
              <button class="btn btn-outline-success btn-sm rounded-pill fw-medium" onclick="switchCharTab('hojin')">프로필 보기</button>
            </td>
          </tr>
          <tr>
            <td>
              <div class="d-flex align-items-center gap-2">
                <img src="{{ '/assets/img/dorothy_front_view_nobg.png' | relative_url }}" class="rounded-circle border" width="36" height="36" style="object-fit: cover;">
                <strong style="color: #ea580c;">도로시</strong>
              </div>
            </td>
            <td>주니어 메이커</td>
            <td>9세 (4.5등신)</td>
            <td>붉은 스니커즈, STEM HERO 멜빵</td>
            <td>피지컬 컴퓨팅 도전, 프로그래밍 입문</td>
            <td class="text-center">
              <button class="btn btn-outline-warning btn-sm rounded-pill fw-medium" onclick="switchCharTab('dorothy')">프로필 보기</button>
            </td>
          </tr>
          <tr>
            <td>
              <div class="d-flex align-items-center gap-2">
                <img src="{{ '/assets/img/jiny_profile.jpg' | relative_url }}" class="rounded-circle border" width="36" height="36" style="object-fit: cover;">
                <strong class="text-primary">지니 (Jiny)</strong>
              </div>
            </td>
            <td>AI & 테크 코치</td>
            <td>턱시도 코숏 고양이</td>
            <td>별빛 자수 마법 망토, 테크 고글</td>
            <td>신경망 수식, 알고리즘 최적화, 디버깅</td>
            <td class="text-center">
              <button class="btn btn-outline-primary btn-sm rounded-pill fw-medium" onclick="switchCharTab('jiny')">프로필 보기</button>
            </td>
          </tr>
          <tr>
            <td>
              <div class="d-flex align-items-center gap-2">
                <img src="{{ '/assets/img/toto_profile.jpg' | relative_url }}" class="rounded-circle border" width="36" height="36" style="object-fit: cover;">
                <strong style="color: #0d9488;">토토 (Toto)</strong>
              </div>
            </td>
            <td>메이커 서포터</td>
            <td>밀크 화이트 강아지</td>
            <td>하늘색 반다나, 단추 코</td>
            <td>부품 조달, 팀워크 사기 진작, 실습 도우미</td>
            <td class="text-center">
              <button class="btn btn-outline-info btn-sm rounded-pill fw-medium" onclick="switchCharTab('toto')">프로필 보기</button>
            </td>
          </tr>
          <tr>
            <td>
              <div class="d-flex align-items-center gap-2">
                <img src="{{ '/assets/img/robot_tinny_profile.jpg' | relative_url }}" class="rounded-circle border" width="36" height="36" style="object-fit: cover;">
                <strong class="text-secondary">티니 (Tinny)</strong>
              </div>
            </td>
            <td>데스크톱 보조 로봇</td>
            <td>소형 큐브 로봇</td>
            <td>전구 안테나, 블루 LED 눈</td>
            <td>전압/전류 계측, I2C/SPI 통신 피드백</td>
            <td class="text-center">
              <button class="btn btn-outline-secondary btn-sm rounded-pill fw-medium" onclick="switchCharTab('tinny')">프로필 보기</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- 가이드 & 세계관 안내 링크 카드 -->
  <section class="mb-5" id="guides">
    <div class="row row-cols-1 row-cols-md-2 g-4">
      <div class="col">
        <div class="card h-100 border rounded-4 shadow-sm p-4 bg-white hover-shadow" style="border-left: 5px solid #8b5cf6 !important;">
          <div class="d-flex align-items-center gap-3 mb-3">
            <span class="fs-1">📐</span>
            <div>
              <h3 class="fs-5 fw-bold mb-0 text-dark">캐릭터 제작 & AI 가이드</h3>
              <span class="text-muted small">AI 생성 규격, 프롬프트 블록, 컬러 코드</span>
            </div>
          </div>
          <p class="text-secondary small mb-4 flex-grow-1">
            일관된 지브리 화풍과 캐릭터 조형을 유지하기 위한 네거티브 프롬프트, LoRA 가중치, 전신 턴어라운드 및 파츠별 규격 가이드를 수록했습니다.
          </p>
          <a href="/character/guide/" class="btn btn-outline-dark fw-bold rounded-pill btn-sm align-self-start px-3 py-2">
            가이드 문서 살펴보기 ➔
          </a>
        </div>
      </div>

      <div class="col">
        <div class="card h-100 border rounded-4 shadow-sm p-4 bg-white hover-shadow" style="border-left: 5px solid #0284c7 !important;">
          <div class="d-flex align-items-center gap-3 mb-3">
            <span class="fs-1">🧭</span>
            <div>
              <h3 class="fs-5 fw-bold mb-0 text-dark">공학 모험의 세계관</h3>
              <span class="text-muted small">산골 연구실에서 펼쳐지는 피지컬 컴퓨팅 대모험</span>
            </div>
          </div>
          <p class="text-secondary small mb-4 flex-grow-1">
            숲속 연구실에서 도로시와 친구들이 왜 납땜 인두를 잡고 코딩을 시작하게 되었는지, 세계관 배경과 모험 스토리라인을 만나보세요.
          </p>
          <a href="/character/universe/" class="btn btn-outline-primary fw-bold rounded-pill btn-sm align-self-start px-3 py-2">
            세계관 스토리 읽기 ➔
          </a>
        </div>
      </div>
    </div>
  </section>

</div>

<script>
  function switchCharTab(charId) {
    const tabBtn = document.getElementById('tab-btn-' + charId);
    if (tabBtn) {
      const tab = new bootstrap.Tab(tabBtn);
      tab.show();
      tabBtn.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  }

  // URL hash (#dorothy, #jiny, etc.) 자동 탭 활성화 지원
  window.addEventListener('DOMContentLoaded', function() {
    const hash = window.location.hash.replace('#', '');
    if (hash) {
      switchCharTab(hash);
    }
  });
</script>
