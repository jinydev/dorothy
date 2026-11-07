---
layout: docs
title: "jiny.dev 공학 강좌 서브도메인 포털"
description: "인공지능, 아두이노, 도커, 리눅스, 모던 웹 등 분야별 독립 서브도메인 포털 안내"
permalink: /courses/
---

<!-- 상단 히어로 배너 -->
<div class="p-4 p-md-5 mb-5 rounded-4 shadow-sm" style="background: linear-gradient(135deg, #eff6ff 0%, #f0fdf4 100%); border: 1px solid #bfdbfe;">
  <div class="row align-items-center">
    <div class="col-lg-8">
      <span class="badge rounded-pill bg-primary px-3 py-2 fw-bold mb-3">Subdomain Directory</span>
      <h1 class="display-6 fw-bold mb-3" style="color: #0f172a; letter-spacing: -0.02em;">
        🌐 분야별 특화 심층 강좌 포털
      </h1>
      <p class="fs-5 text-secondary mb-3 leading-relaxed">
        <strong>jiny.dev</strong>의 모든 심층 강좌는 분야별 특성에 맞추어 최적화된 <strong>독립 서브도메인(***.jiny.dev)</strong>으로 서비스됩니다. 원하는 분야를 선택하여 바로 학습을 시작하세요!
      </p>
      <div class="d-flex flex-wrap gap-2">
        <span class="badge rounded-pill bg-white text-dark border px-3 py-2 fw-semibold">독립 서브도메인 아키텍처</span>
        <span class="badge rounded-pill bg-white text-dark border px-3 py-2 fw-semibold">YAML 데이터 중앙 집중 관리</span>
        <span class="badge rounded-pill bg-white text-dark border px-3 py-2 fw-semibold">원클릭 포털 이동</span>
      </div>
    </div>
    <div class="col-lg-4 text-center mt-4 mt-lg-0">
      <img src="{{ '/assets/img/robot_ecosystem_lab.jpg' | relative_url }}"
           alt="공학 생태계 연구실"
           class="img-fluid rounded-4 shadow-sm"
           style="max-height: 240px; object-fit: cover; border: 1px solid #cbd5e1;">
      <p class="small text-muted mt-2 mb-0">▲ 소프트웨어와 하드웨어가 융합된 첨단 랩</p>
    </div>
  </div>
</div>

---

{% for category in site.data.courses.categories %}
<div class="mb-5 pb-3" id="{{ category.id }}">
  <!-- 카테고리 헤더 -->
  <div class="d-flex align-items-center mb-4 pb-2 border-bottom">
    <span class="fs-2 me-3">{{ category.icon }}</span>
    <div>
      <h2 class="fs-3 fw-bold mb-1 text-dark">{{ category.name }}</h2>
      <span class="text-secondary small">{{ category.en_name }} — {{ category.description }}</span>
    </div>
  </div>

  <div class="row row-cols-1 row-cols-md-2 g-4 mb-4">
    {% for course in category.courses %}
    <div class="col">
      <div class="card h-100 border rounded-4 shadow-sm bg-white" style="border-color: #e2e8f0 !important;">
        <!-- 카드 상단 이미지 -->
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

          <h3 class="fs-5 fw-bold text-dark mb-2">
            <span class="me-1">{{ course.icon }}</span>
            {{ course.title }}
          </h3>

          <p class="text-secondary small mb-3 flex-grow-1" style="line-height: 1.55;">
            {{ course.summary }}
          </p>

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
    </div>
    {% endfor %}
  </div>
</div>
{% endfor %}
