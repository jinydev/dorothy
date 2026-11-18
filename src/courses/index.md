---
layout: home
title: "분야별 전문 심층 강좌 포털 - jiny.dev"
description: "인공지능, 아두이노, 도커, 리눅스, 모던 웹 등 분야별 독립 서브도메인 포털 안내"
permalink: /courses/
---

<style>
  .courses-hero {
    background: linear-gradient(180deg, #f8faff 0%, #edf3fb 100%);
    padding: 4.5rem 1.5rem 3.5rem;
    margin-bottom: 3.5rem;
    border-bottom: 1px solid #e2e8f0;
  }
  .courses-hero-title {
    font-size: 2.75rem;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.03em;
    line-height: 1.25;
  }
  .courses-hero-subtitle {
    font-size: 1.15rem;
    color: #64748b;
    max-width: 760px;
    margin: 1.25rem auto 2rem;
    line-height: 1.7;
  }
  .category-pill-btn {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    color: #334155;
    padding: 0.55rem 1.1rem;
    border-radius: 9999px;
    font-weight: 600;
    font-size: 0.92rem;
    text-decoration: none;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    box-shadow: 0 1px 2px rgba(0,0,0,0.04);
  }
  .category-pill-btn:hover {
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
</style>

<!-- 상단 풀와이드 히어로 헤딩 영역 -->
<div class="courses-hero">
  <div class="container text-center">
    <div class="d-inline-flex align-items-center gap-2 px-3 py-1 rounded-pill bg-white border text-secondary small fw-bold mb-3 shadow-sm">
      <span class="text-primary">🌐</span>
      <span>jiny.dev 공학 강좌 서브도메인 포털</span>
    </div>
    <h1 class="courses-hero-title mb-3">
      분야별 특화 심층 강좌 포털
    </h1>
    <p class="courses-hero-subtitle">
      <strong>jiny.dev</strong>의 모든 심층 기술 강좌는 분야별 특성에 맞추어 최적화된 <strong>독립 서브도메인(***.jiny.dev)</strong>으로 서비스됩니다.<br class="d-none d-md-block">
      체계적인 이론과 실전 코드로 무장한 원하는 과정을 선택하여 바로 학습을 시작하세요!
    </p>

    <!-- 분야별 바로가기 퀵 네비게이션 필 -->
    <div class="d-flex flex-wrap justify-content-center gap-2 mt-4">
      {% for category in site.data.courses.categories %}
      <a href="#{{ category.id }}" class="category-pill-btn">
        <span>{{ category.icon }}</span>
        <span>{{ category.name }}</span>
      </a>
      {% endfor %}
    </div>

    <!-- 부가 정보 배지 -->
    <div class="mt-4 pt-2 d-flex flex-wrap justify-content-center gap-2">
      <span class="badge rounded-pill bg-white text-secondary border px-3 py-2 fw-medium">🚀 15개 독립 전문 도메인</span>
      <span class="badge rounded-pill bg-white text-secondary border px-3 py-2 fw-medium">✨ 이호진 교수 & 도로시 멘토링</span>
      <span class="badge rounded-pill bg-white text-secondary border px-3 py-2 fw-medium">🎯 기초부터 심화까지 전 커리큘럼 완비</span>
    </div>
  </div>
</div>

<!-- 분야별 심층강좌 카드 그리드 (홈 스타일 3열 나열) -->
<div class="container pb-5">
  {% for category in site.data.courses.categories %}
  <div class="mb-5 pb-3" id="{{ category.id }}">
    <!-- 카테고리 헤더 -->
    <div class="d-flex align-items-center mb-4 pb-2 border-bottom">
      <span class="fs-2 me-3">{{ category.icon }}</span>
      <div>
        <h2 class="fs-3 fw-bold mb-1 text-dark" style="letter-spacing: -0.01em;">{{ category.name }}</h2>
        <span class="text-secondary small">{{ category.en_name }} — {{ category.description }}</span>
      </div>
    </div>

    <!-- 강좌 그리드 카드 (홈 스타일 3열 그리드) -->
    <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
      {% for course in category.courses %}
      <div class="col">
        <div class="card h-100 border rounded-4 shadow-sm hover-shadow bg-white" style="border-color: #e2e8f0 !important;">
          <!-- 카드 상단 이미지 / 썸네일 -->
          {% if course.logo %}
          <div class="overflow-hidden rounded-top-4 position-relative" style="height: 160px; background-color: #f8fafc;">
            <img src="{{ course.logo | relative_url }}"
                 alt="{{ course.title }}"
                 class="w-100 h-100"
                 style="object-fit: cover;">
            <div class="position-absolute top-0 end-0 m-3">
              <span class="badge rounded-pill bg-{{ course.badge_color }} shadow-sm fw-bold px-3 py-1">
                {{ course.badge }}
              </span>
            </div>
            <div class="position-absolute bottom-0 start-0 m-3">
              <span class="badge rounded-pill bg-dark bg-opacity-75 text-white px-2 py-1 small">
                난이도: {{ course.level }}
              </span>
            </div>
          </div>
          {% endif %}

          <div class="card-body p-4 d-flex flex-column">
            <!-- 도메인 주소 배지 -->
            <div class="mb-2">
              <span class="badge font-monospace text-primary bg-primary-subtle border border-primary-subtle px-2 py-1">
                {{ course.subdomain }}
              </span>
            </div>

            <!-- 제목 -->
            <h3 class="card-title fs-5 fw-bold text-dark mb-2">
              <span class="me-1">{{ course.icon }}</span>
              {{ course.title }}
            </h3>

            <!-- 요약 설명 -->
            <p class="card-text text-secondary small flex-grow-1 mb-3" style="line-height: 1.55;">
              {{ course.summary }}
            </p>

            <!-- 멘토 & 태그 -->
            <div class="pt-2 border-top">
              <div class="d-flex align-items-center justify-content-between mb-2 small text-muted">
                <span><strong>멘토:</strong> {{ course.mentor }}</span>
              </div>
              <div class="d-flex flex-wrap gap-1 mb-3">
                {% for tag in course.tags %}
                <span class="badge rounded-pill bg-light text-secondary border px-2 py-1" style="font-size: 0.72rem;">
                  #{{ tag }}
                </span>
                {% endfor %}
              </div>
            </div>

            <!-- 이동 버튼 -->
            <a href="{{ course.url }}"
               target="_blank"
               rel="noopener"
               class="btn btn-outline-dark w-100 fw-bold rounded-3 d-flex align-items-center justify-content-center gap-2 mt-auto">
              <span>{{ course.subdomain }} 입장하기</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" class="bi bi-box-arrow-up-right" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8.636 3.5a.5.5 0 0 0-.5-.5H1.5A1.5 1.5 0 0 0 0 4.5v10A1.5 1.5 0 0 0 1.5 16h10a1.5 1.5 0 0 0 1.5-1.5V7.864a.5.5 0 0 0-1 0V14.5a.5.5 0 0 1-.5.5h-10a.5.5 0 0 1-.5-.5v-10a.5.5 0 0 1 .5-.5h6.636a.5.5 0 0 0 .5-.5z"/>
                <path fill-rule="evenodd" d="M16 .5a.5.5 0 0 0-.5-.5h-5a.5.5 0 0 0 0 1h3.793L6.146 9.146a.5.5 0 1 0 .708.708L15 1.707V5.5a.5.5 0 0 0 1 0v-5z"/>
              </svg>
            </a>
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
  {% endfor %}
</div>
