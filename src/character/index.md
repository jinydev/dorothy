---
layout: home
title: "공학 모험 연구실 캐릭터 5총사 & LoRA 데이터셋"
description: "이호진 교수님, 도로시, 지니(고양이), 토토(강아지), 티니(로봇)의 공식 프로필과 AI 학습 데이터셋 갤러리"
permalink: /character/
---

<style>
  .character-hero {
    background: linear-gradient(180deg, #f8faff 0%, #edf3fb 100%);
    padding: 4.5rem 1.5rem 3.5rem;
    margin-bottom: 3.5rem;
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
    max-width: 800px;
    margin: 1.25rem auto 2rem;
    line-height: 1.7;
  }
  .char-pill-btn {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    color: #334155;
    padding: 0.55rem 1.15rem;
    border-radius: 9999px;
    font-weight: 600;
    font-size: 0.92rem;
    text-decoration: none;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    box-shadow: 0 1px 2px rgba(0,0,0,0.04);
  }
  .char-pill-btn:hover {
    background: #0f172a;
    color: #ffffff !important;
    border-color: #0f172a;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
  }
  .hover-shadow {
    transition: transform 0.25s ease, box-shadow 0.25s ease;
  }
  .hover-shadow:hover {
    transform: translateY(-4px);
    box-shadow: 0 16px 32px -8px rgba(0, 0, 0, 0.1) !important;
  }
  .dataset-thumbnail-card {
    transition: all 0.2s ease;
    background: #ffffff;
  }
  .dataset-thumbnail-card:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 8px 20px rgba(0,0,0,0.12) !important;
    border-color: #3b82f6 !important;
  }
  .dataset-img-wrap {
    position: relative;
    width: 100%;
    padding-top: 100%; /* 1:1 Aspect Ratio */
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
  .char-section-card {
    border: 1px solid #e2e8f0;
    border-radius: 1.25rem;
    background: #ffffff;
    box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    margin-bottom: 4rem;
    overflow: hidden;
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
      공학 모험 연구실 캐릭터 5총사 & 데이터셋
    </h1>
    <p class="character-hero-subtitle">
      복잡하고 어려운 컴퓨터 공학과 하드웨어 이론을 쉽고 유쾌하게 전달하는 <strong>연구실 5총사</strong>를 소개합니다.<br class="d-none d-md-block">
      지브리풍 2D 애니메이션 화풍과 비주얼 일관성을 위해 정밀하게 큐레이션된 <strong>142장의 공식 학습 데이터셋</strong>을 캐릭터별로 감상해보세요.
    </p>

    <!-- 캐릭터 바로가기 퀵 네비게이션 필 -->
    <div class="d-flex flex-wrap justify-content-center gap-2 mt-4">
      <a href="#hojin" class="char-pill-btn">
        <span>👨‍🏫</span>
        <span>이호진 교수님 (30)</span>
      </a>
      <a href="#dorothy" class="char-pill-btn">
        <span>👧</span>
        <span>도로시 (42)</span>
      </a>
      <a href="#jiny" class="char-pill-btn">
        <span>🐱</span>
        <span>지니 (26)</span>
      </a>
      <a href="#toto" class="char-pill-btn">
        <span>🐶</span>
        <span>토토 (22)</span>
      </a>
      <a href="#tinny" class="char-pill-btn">
        <span>🤖</span>
        <span>티니 로봇 (22)</span>
      </a>
      <a href="#comparison" class="char-pill-btn">
        <span>📋</span>
        <span>속성 비교표</span>
      </a>
      <a href="#guides" class="char-pill-btn">
        <span>📐</span>
        <span>제작 가이드</span>
      </a>
    </div>

    <!-- 부가 정보 배지 -->
    <div class="mt-4 pt-2 d-flex flex-wrap justify-content-center gap-2">
      <span class="badge rounded-pill bg-white text-secondary border px-3 py-2 fw-medium">🌟 총 5개 핵심 캐릭터</span>
      <span class="badge rounded-pill bg-white text-secondary border px-3 py-2 fw-medium">🖼️ 총 142컷 고해상도 LoRA 데이터셋</span>
      <span class="badge rounded-pill bg-white text-secondary border px-3 py-2 fw-medium">🏷️ 상세 프롬프트 & 캡션 완비</span>
    </div>
  </div>
</div>

<!-- 본문 콘텐츠 영역 (사이드바 없는 풀 와이드 컨테이너) -->
<div class="container pb-5">

  {% for char in site.data.characters.characters %}
  <!-- 캐릭터 섹션: {{ char.name }} -->
  <section class="char-section-card" id="{{ char.id }}" style="border-top: 5px solid {{ char.theme_color }};">
    <!-- 캐릭터 프로필 상단 배너 -->
    <div class="p-4 p-md-5" style="background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);">
      <div class="row align-items-center">
        <!-- 아바타 이미지 -->
        <div class="col-md-3 col-lg-2 text-center mb-3 mb-md-0">
          <div class="position-relative d-inline-block p-2 rounded-4 bg-white shadow-sm border" style="border-color: {{ char.theme_color }} !important;">
            <img src="{{ char.avatar | relative_url }}"
                 alt="{{ char.name }}"
                 class="img-fluid rounded-3"
                 style="width: 140px; height: 140px; object-fit: cover;"
                 loading="lazy">
          </div>
        </div>

        <!-- 캐릭터 프로필 텍스트 -->
        <div class="col-md-9 col-lg-7 ps-md-4">
          <div class="d-flex flex-wrap align-items-center gap-2 mb-2">
            <span class="badge rounded-pill {{ char.role_badge }} px-3 py-1 fw-bold">{{ char.role }}</span>
            <span class="text-muted small fw-medium">{{ char.en_name }}</span>
            <span class="badge rounded-pill bg-light text-dark border px-2 py-1 small">
              📷 데이터셋 {{ char.image_count }}컷
            </span>
          </div>
          <h2 class="fs-2 fw-bold text-dark mb-2" style="letter-spacing: -0.02em;">
            {{ char.name }}
          </h2>
          <blockquote class="text-secondary fst-italic small mb-2 ps-3 border-start border-3" style="border-color: {{ char.theme_color }} !important;">
            "{{ char.quote }}"
          </blockquote>
          <p class="text-secondary mb-3 small leading-relaxed">
            {{ char.description }}
          </p>
          <!-- 시그니처 특징 태그 -->
          <div class="d-flex flex-wrap gap-1">
            {% for trait in char.traits %}
            <span class="badge bg-white text-secondary border px-2 py-1" style="font-size: 0.78rem;">#{{ trait }}</span>
            {% endfor %}
          </div>
        </div>

        <!-- 상세 페이지 바로가기 액션 버튼 -->
        <div class="col-lg-3 text-center text-lg-end mt-3 mt-lg-0">
          <a href="{{ char.profile_url }}" class="btn btn-outline-dark fw-bold rounded-pill px-4 py-2 shadow-sm d-inline-flex align-items-center gap-2">
            <span>상세 프로필 보기</span>
            <span>➔</span>
          </a>
        </div>
      </div>
    </div>

    <!-- 캐릭터 데이터셋 갤러리 영역 -->
    <div class="p-4 p-md-5 bg-light border-top">
      <div class="d-flex flex-wrap align-items-center justify-content-between mb-4">
        <div>
          <h3 class="fs-5 fw-bold text-dark mb-1 d-flex align-items-center gap-2">
            <span>🎨</span>
            <span>{{ char.name }} 학습 & 컨셉 데이터셋</span>
          </h3>
          <p class="text-secondary small mb-0">
            고유한 외형 특징과 다양한 앵글, 포즈, 표정을 담은 원본 훈련 이미지 모음입니다. (클릭 시 원본 이미지 확인)
          </p>
        </div>
        <span class="badge rounded-pill bg-white text-secondary border px-3 py-2 small shadow-sm mt-2 mt-md-0">
          총 {{ char.image_count }}장
        </span>
      </div>

      <!-- 이미지 썸네일 그리드 -->
      <div class="row row-cols-2 row-cols-sm-3 row-cols-md-4 row-cols-lg-6 g-3">
        {% for img in char.images %}
        <div class="col">
          <a href="{{ img.url | relative_url }}" target="_blank" rel="noopener" class="text-decoration-none text-dark">
            <div class="card h-100 border rounded-3 dataset-thumbnail-card shadow-sm overflow-hidden">
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
  </section>
  {% endfor %}

  <!-- 캐릭터 속성 비교표 섹션 -->
  <section class="char-section-card p-4 p-md-5 mb-5" id="comparison">
    <div class="d-flex align-items-center mb-4 pb-2 border-bottom">
      <span class="fs-2 me-3">📋</span>
      <div>
        <h2 class="fs-3 fw-bold mb-1 text-dark">캐릭터 핵심 속성 및 역할 비교표</h2>
        <span class="text-secondary small">연구실 5총사의 조형 비율, 시그니처 착장 및 기술 전문 분야 한눈에 보기</span>
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
            <th scope="col" class="text-center" style="min-width: 120px;">상세 페이지</th>
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
              <a href="/character/hojin/" class="btn btn-outline-success btn-sm rounded-pill fw-medium">상세보기 ➔</a>
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
              <a href="/character/dorothy/" class="btn btn-outline-warning btn-sm rounded-pill fw-medium">상세보기 ➔</a>
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
              <a href="/character/jiny/" class="btn btn-outline-primary btn-sm rounded-pill fw-medium">상세보기 ➔</a>
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
              <a href="/character/toto/" class="btn btn-outline-info btn-sm rounded-pill fw-medium">상세보기 ➔</a>
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
              <a href="/character/tinny/" class="btn btn-outline-secondary btn-sm rounded-pill fw-medium">상세보기 ➔</a>
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
