---
layout: home
title: "공학 모험 연구실 파츠 & 배경 에셋 데이터셋 (138컷)"
description: "연구실 환경, 아두이노·센서 키트, 컴퓨팅·반도체 & 하드웨어 장비, 3D프린터·공구, 소프트웨어/IDE, AI/수학 이론 도식, 개발 로고 엠블럼 등 5대 카테고리 138종의 공식 에셋 데이터셋"
permalink: /character/parts/
---

<style>
  .parts-hero {
    background: linear-gradient(180deg, #f8faff 0%, #edf3fb 100%);
    padding: 3.5rem 1.5rem 2.5rem;
    margin-bottom: 2rem;
    border-bottom: 1px solid #e2e8f0;
  }
  .parts-hero-title {
    font-size: 2.5rem;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.03em;
  }
  .parts-hero-subtitle {
    font-size: 1.15rem;
    color: #64748b;
    max-width: 820px;
    margin: 1rem auto 1.5rem;
    line-height: 1.7;
  }
  
  .category-anchor-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.45rem 0.9rem;
    border-radius: 9999px;
    font-size: 0.88rem;
    font-weight: 600;
    color: #334155;
    background: #ffffff;
    border: 1px solid #cbd5e1;
    text-decoration: none;
    transition: all 0.2s ease;
  }
  .category-anchor-pill:hover {
    background: #0f172a;
    color: #ffffff;
    border-color: #0f172a;
    transform: translateY(-2px);
  }

  .part-card {
    transition: all 0.25s ease;
    background: #ffffff;
    border: 1px solid #e2e8f0;
  }
  .part-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 24px rgba(0,0,0,0.08) !important;
    border-color: #3b82f6 !important;
  }
  .part-img-wrap {
    position: relative;
    width: 100%;
    padding-top: 80%;
    overflow: hidden;
    background: #f8fafc;
    border-radius: 0.75rem 0.75rem 0 0;
  }
  .part-img-wrap img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
  }
  .part-card:hover .part-img-wrap img {
    transform: scale(1.05);
  }
</style>

<!-- 상단 풀와이드 히어로 영역 -->
<div class="parts-hero text-center">
  <div class="container">
    <div class="d-inline-flex align-items-center gap-2 px-3 py-1 rounded-pill bg-white border text-secondary small fw-bold mb-3 shadow-sm">
      <span class="text-primary">🧩</span>
      <span>Laboratory Parts & Assets Dataset</span>
    </div>
    <h1 class="parts-hero-title mb-3">
      공학 모험 연구실 파츠 & 배경 에셋 (138컷)
    </h1>
    <p class="parts-hero-subtitle">
      캐릭터뿐만 아니라, 캐릭터가 머무는 <strong>연구실 환경, 아두이노(우노·나노·메가) 및 40여종 센서·액추에이터 실습 키트, ESP32, CPU·RAM·SSD·메인보드 등 반도체 부품, 3D 프린터, TV, 헤드셋, 충전기, 정밀공구, 파워서플라이, 웨어러블 디바이스, IDE/코드 비주얼, 시그모이드·ReLU 및 AI/수학 기호, 개발 기술 로고</strong>까지 완벽한 세계관 일관성을 유지할 수 있도록 정교하게 조형된 <strong>138컷의 공식 보조 데이터셋</strong>입니다.
    </p>

    <!-- 빠른 카테고리 이동 앵커 바 -->
    <div class="d-flex flex-wrap justify-content-center gap-2 pt-2">
      <a href="#environments" class="category-anchor-pill shadow-sm">🏛️ 연구실 & 캠퍼스 환경 (6컷)</a>
      <a href="#hardware" class="category-anchor-pill shadow-sm">⚡ 컴퓨팅·반도체 & 하드웨어 (88컷)</a>
      <a href="#software" class="category-anchor-pill shadow-sm">💻 소프트웨어 & IDE 코드 (6컷)</a>
      <a href="#ai_theory" class="category-anchor-pill shadow-sm">🧠 AI & 수학 이론 도식 (14컷)</a>
      <a href="#logos" class="category-anchor-pill shadow-sm">🛡️ 기술 로고 & 엠블럼 (24컷)</a>
    </div>
  </div>
</div>

<div class="container pb-5">
  <!-- 공통 서브 네비게이션 -->
  {% include character_nav_bar.html %}

  <!-- 카테고리별 데이터셋 섹션 렌더링 -->
  {% for cat in site.data.dataset_parts.categories %}
  <section id="{{ cat.id }}" class="mb-5 pt-3">
    <div class="d-flex flex-wrap align-items-center justify-content-between pb-3 mb-4 border-bottom">
      <div>
        <div class="d-flex align-items-center gap-2 mb-1">
          <span class="fs-4">{{ cat.icon }}</span>
          <h2 class="h3 fw-bold mb-0 text-dark">{{ cat.name }}</h2>
          <span class="badge rounded-pill {{ cat.badge }} px-3 py-1 ms-2">{{ cat.images.size }}컷</span>
        </div>
        <p class="text-muted small mb-0">{{ cat.en_name }} · {{ cat.desc }}</p>
      </div>
      <a href="#top" class="btn btn-sm btn-outline-secondary rounded-pill mt-2 mt-sm-0">↑ 맨 위로</a>
    </div>

    <!-- 이미지 카드 그리드 -->
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 g-4">
      {% for img in cat.images %}
      <div class="col">
        <div class="card h-100 part-card shadow-sm rounded-4 overflow-hidden">
          <a href="{{ img.url | relative_url }}" target="_blank" rel="noopener" class="d-block overflow-hidden">
            <div class="part-img-wrap">
              <img src="{{ img.url | relative_url }}" 
                   alt="{{ img.title }}" 
                   loading="lazy">
            </div>
          </a>
          <div class="card-body p-3 d-flex flex-column justify-content-between">
            <div>
              <div class="d-flex align-items-center justify-content-between mb-2">
                <span class="badge bg-light text-secondary border font-monospace small px-2 py-1">{{ img.filename }}</span>
                <span class="small text-muted">원화</span>
              </div>
              <h5 class="fw-bold fs-6 text-dark mb-2">{{ img.title }}</h5>
              <p class="small text-muted mb-0 text-truncate-2" style="font-size: 0.8rem; line-height: 1.5;" title="{{ img.caption }}">
                {{ img.caption }}
              </p>
            </div>
            <div class="pt-3 mt-2 border-top">
              <a href="{{ img.url | relative_url }}" target="_blank" rel="noopener" class="btn btn-outline-primary btn-sm w-100 rounded-pill fw-medium">
                고해상도 원본 보기 ↗
              </a>
            </div>
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
  </section>
  {% endfor %}

  <!-- 하단 안내 배너 -->
  <div class="p-4 rounded-4 bg-light border text-center my-5 shadow-sm">
    <h4 class="fw-bold mb-2">🎨 LoRA 및 멀티컨셉 AI 학습에 파츠 데이터셋 활용하기</h4>
    <p class="text-muted mb-3 max-w-700 mx-auto">
      캐릭터 LoRA 학습 시 본 에셋 데이터셋을 정규화 데이터(Regularization Data) 또는 보조 토큰 데이터로 함께 학습하면 캐릭터가 배경이나 도구에 오염되지 않고 일관된 고품질 삽화를 생성할 수 있습니다.
    </p>
    <div class="d-flex justify-content-center gap-2">
      <a href="{{ '/character/guide/' | relative_url }}" class="btn btn-primary rounded-pill px-4 fw-bold">
        📐 제작 가이드 확인하기
      </a>
      <a href="{{ '/character/' | relative_url }}" class="btn btn-outline-secondary rounded-pill px-4 fw-bold">
        👨‍🏫 캐릭터 포털로 가기
      </a>
    </div>
  </div>
</div>
