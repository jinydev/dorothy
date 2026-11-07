---
layout: docs
title: "컴퓨터 공학 & 피지컬 AI 학습 로드맵"
description: "기초 프로그래밍부터 하드웨어 회로, 클라우드 가상화, 딥러닝과 로보틱스까지 단계별 학습 경로"
permalink: /roadmap/
---

<!-- 상단 히어로 배너 -->
<div class="p-4 p-md-5 mb-5 rounded-4 shadow-sm" style="background: linear-gradient(135deg, #fdf4ff 0%, #ede9fe 100%); border: 1px solid #f0abfc;">
  <div class="row align-items-center">
    <div class="col-lg-8">
      <span class="badge rounded-pill bg-purple text-white px-3 py-2 fw-bold mb-3" style="background-color: #9333ea;">Master Roadmap</span>
      <h1 class="display-6 fw-bold mb-3" style="color: #3b0764; letter-spacing: -0.02em;">
        🗺️ 엔지니어링 마스터 클래스 로드맵
      </h1>
      <p class="fs-5 text-secondary mb-3 leading-relaxed">
        프로그래밍 기초 문법부터 물리 법칙을 다루는 전자 회로, 서버 가상화 인프라, 최신 인공지능과 자율 제어 로봇팔까지! <strong>jiny.dev</strong>가 제안하는 체계적인 공학 학습 로드맵입니다.
      </p>
      <div class="d-flex flex-wrap gap-2">
        <span class="badge rounded-pill bg-white text-dark border px-3 py-2 fw-semibold">기초부터 실전까지</span>
        <span class="badge rounded-pill bg-white text-dark border px-3 py-2 fw-semibold">소프트웨어 + 하드웨어 융합</span>
        <span class="badge rounded-pill bg-white text-dark border px-3 py-2 fw-semibold">독립 서브도메인 실습 연계</span>
      </div>
    </div>
    <div class="col-lg-4 text-center mt-4 mt-lg-0">
      <img src="{{ '/assets/img/robot_arm_learning_with_hojin.jpg' | relative_url }}"
           alt="로봇팔 학습 현장"
           class="img-fluid rounded-4 shadow-sm"
           style="max-height: 240px; object-fit: cover; border: 1px solid #cbd5e1;">
      <p class="small text-muted mt-2 mb-0">▲ 단계별 성장을 통해 도달하는 피지컬 AI 현장</p>
    </div>
  </div>
</div>

---

<div id="stage-1"></div>

## 📌 01단계: 프로그래밍 기본기 & 컴퓨터 원리 (Foundations)

<div class="card border rounded-4 p-4 mb-4 shadow-sm bg-white" style="border-left: 6px solid #6366f1 !important;">
  <div class="d-flex align-items-center justify-content-between mb-2">
    <span class="badge rounded-pill bg-primary-subtle text-primary border px-3 py-1 fw-bold">Stage 01</span>
    <span class="font-monospace small text-muted">python.jiny.dev</span>
  </div>
  <h3 class="fs-4 fw-bold text-dark mb-2">컴퓨터의 구조와 알고리즘적 사고의 시작</h3>
  <p class="text-secondary small mb-3 leading-relaxed">
    컴퓨터가 0과 1로 데이터를 표현하고 연산하는 기본 원리를 배웁니다. 파이썬과 C/C++ 기초 문법을 통해 변수, 조건문, 반복문, 함수, 자료구조(배열, 리스트, 딕셔너리)를 완벽히 이해합니다.
  </p>
  <div class="bg-light p-3 rounded-3 mb-3">
    <h6 class="fw-bold text-dark mb-2">핵심 습득 기술:</h6>
    <ul class="text-secondary small mb-0 ps-3">
      <li>컴퓨터 구조(CPU, 메모리, I/O)와 2진법 표현</li>
      <li>Python 3 기초 문법 및 함수형 프로그래밍</li>
      <li>C 언어 기본 문법 및 메모리 포인터 개념 입문</li>
      <li>기본 알고리즘(탐색, 정렬) 및 시간 복잡도($O(N)$)</li>
    </ul>
  </div>
  <a href="https://python.jiny.dev" target="_blank" rel="noopener" class="btn btn-outline-primary btn-sm rounded-3 align-self-start fw-bold">
    파이썬 포털 입장하기 ↗
  </a>
</div>

---

<div id="stage-2"></div>

## 📌 02단계: 전자회로 & 피지컬 임베디드 (Physical Computing)

<div class="card border rounded-4 p-4 mb-4 shadow-sm bg-white" style="border-left: 6px solid #059669 !important;">
  <div class="d-flex align-items-center justify-content-between mb-2">
    <span class="badge rounded-pill bg-success-subtle text-success border px-3 py-1 fw-bold">Stage 02</span>
    <span class="font-monospace small text-muted">arduino.jiny.dev / pi.jiny.dev</span>
  </div>
  <h3 class="fs-4 fw-bold text-dark mb-2">모니터 밖 현실 세계와 상호작용하는 하드웨어 제어</h3>
  <p class="text-secondary small mb-3 leading-relaxed">
    전압($V$), 전류($I$), 저항($R$)의 옴의 법칙부터 아두이노 우노/메가와 브레드보드로 다양한 디지털/아날로그 센서를 제어합니다. 서보모터, DC모터, OLED 디스플레이, 블루투스/Wi-Fi 통신을 직접 회로로 꾸밉니다.
  </p>
  <div class="bg-light p-3 rounded-3 mb-3">
    <h6 class="fw-bold text-dark mb-2">핵심 습득 기술:</h6>
    <ul class="text-secondary small mb-0 ps-3">
      <li>기초 전자물리, 옴의 법칙, 브레드보드 배선 및 계측</li>
      <li>디지털 입출력, PWM 펄스폭 변조, 아날로그 ADC 변환</li>
      <li>온습도/조도/초음파 센서 계측 및 모터(서보, 스텝, DC) 구동</li>
      <li>라즈베리파이 엣지 컴퓨팅 및 센서 클라우드 연동</li>
    </ul>
  </div>
  <a href="https://arduino.jiny.dev" target="_blank" rel="noopener" class="btn btn-outline-success btn-sm rounded-3 align-self-start fw-bold">
    아두이노 193강 포털 입장하기 ↗
  </a>
</div>

---

<div id="stage-3"></div>

## 📌 03단계: 시스템 인프라 & 클라우드 배포 (Infrastructure & DevOps)

<div class="card border rounded-4 p-4 mb-4 shadow-sm bg-white" style="border-left: 6px solid #0284c7 !important;">
  <div class="d-flex align-items-center justify-content-between mb-2">
    <span class="badge rounded-pill bg-info-subtle text-info-emphasis border px-3 py-1 fw-bold">Stage 03</span>
    <span class="font-monospace small text-muted">docker.jiny.dev / linux.jiny.dev</span>
  </div>
  <h3 class="fs-4 fw-bold text-dark mb-2">안정적인 서버 운영과 컨테이너 격리 배포 환경 구축</h3>
  <p class="text-secondary small mb-3 leading-relaxed">
    서버의 기본 운영체제인 리눅스(Ubuntu)의 파일 시스템, 프로세스 구조, 권한 관리, 쉘 스크립트를 마스터하고, 도커(Docker)를 통해 애플리케이션을 환경에 구애받지 않고 언제 어디서든 일관되게 배포하는 파이프라인을 구축합니다.
  </p>
  <div class="bg-light p-3 rounded-3 mb-3">
    <h6 class="fw-bold text-dark mb-2">핵심 습득 기술:</h6>
    <ul class="text-secondary small mb-0 ps-3">
      <li>Linux OS 구조, Bash 커맨드라인, 네트워크 설정 및 방화벽</li>
      <li>Docker 컨테이너 가상화 원리, Dockerfile 이미지 빌드</li>
      <li>Docker Compose 멀티 컨테이너 오케스트레이션</li>
      <li>Git 협업 브랜치 전략 및 GitHub Actions CI/CD</li>
    </ul>
  </div>
  <a href="https://docker.jiny.dev" target="_blank" rel="noopener" class="btn btn-outline-info btn-sm rounded-3 align-self-start fw-bold">
    도커 컨테이너 대항해 입장하기 ↗
  </a>
</div>

---

<div id="stage-4"></div>

## 📌 04단계: 인공지능 & 딥러닝 강화학습 (AI & Deep RL)

<div class="card border rounded-4 p-4 mb-4 shadow-sm bg-white" style="border-left: 6px solid #8b5cf6 !important;">
  <div class="d-flex align-items-center justify-content-between mb-2">
    <span class="badge rounded-pill bg-purple-subtle text-purple border px-3 py-1 fw-bold">Stage 04</span>
    <span class="font-monospace small text-muted">ai.jiny.dev / rl.jiny.dev</span>
  </div>
  <h3 class="fs-4 fw-bold text-dark mb-2">스스로 학습하고 최적의 의사결정을 내리는 지능형 알고리즘</h3>
  <p class="text-secondary small mb-3 leading-relaxed">
    행렬 연산과 경사 하강법을 기초로 DeZero 프레임워크를 밑바닥부터 구축하며 딥러닝 역전파(Backpropagation)의 본질을 깨닫습니다. 마르코프 결정 과정(MDP), 벨만 방정식, DQN 및 Actor-Critic 정책 경사법을 정복합니다.
  </p>
  <div class="bg-light p-3 rounded-3 mb-3">
    <h6 class="fw-bold text-dark mb-2">핵심 습득 기술:</h6>
    <ul class="text-secondary small mb-0 ps-3">
      <li>선형대수학, 미적분, 확률 통계 기초 수학</li>
      <li>PyTorch 딥러닝 프레임워크 실전 활용</li>
      <li>MDP, 가치 반복법, Q-러닝, 시간차 학습(TD)</li>
      <li>심층 Q-네트워크(DQN), 정책 경사법(Policy Gradient), PPO</li>
    </ul>
  </div>
  <a href="https://rl.jiny.dev" target="_blank" rel="noopener" class="btn btn-outline-primary btn-sm rounded-3 align-self-start fw-bold">
    강화학습 마법 여정 입장하기 ↗
  </a>
</div>

---

<div id="stage-5"></div>

## 📌 05단계: 피지컬 AI & 로보틱스 자율 제어 (Robotics & Physical AI)

<div class="card border rounded-4 p-4 mb-4 shadow-sm bg-white" style="border-left: 6px solid #ec4899 !important;">
  <div class="d-flex align-items-center justify-content-between mb-2">
    <span class="badge rounded-pill bg-danger-subtle text-danger border px-3 py-1 fw-bold">Stage 05</span>
    <span class="font-monospace small text-muted">robot.jiny.dev</span>
  </div>
  <h3 class="fs-4 fw-bold text-dark mb-2">학습된 AI 두뇌와 로봇 하드웨어의 완전한 융합</h3>
  <p class="text-secondary small mb-3 leading-relaxed">
    인공지능 모델이 센서 데이터(카메라, 라이다, IMU)를 실시간으로 인지하고, ROS2(Robot Operating System) 기반으로 6축 다관절 로봇팔과 보조 로봇 티니(Tinny)의 관절 모터를 정밀 제어하는 공학의 정점에 도달합니다.
  </p>
  <div class="bg-light p-3 rounded-3 mb-3">
    <h6 class="fw-bold text-dark mb-2">핵심 습득 기술:</h6>
    <ul class="text-secondary small mb-0 ps-3">
      <li>ROS2 노드 통신, 토픽/서비스/액션 구조</li>
      <li>기구학(Kinematics) 및 역기구학(Inverse Kinematics) 모션 궤적 생성</li>
      <li>비전 AI 객체 인식 기반 픽앤플레이스(Pick and Place)</li>
      <li>데스크톱 지능형 인터랙티브 에이전트 구축</li>
    </ul>
  </div>
  <a href="https://robot.jiny.dev" target="_blank" rel="noopener" class="btn btn-outline-danger btn-sm rounded-3 align-self-start fw-bold">
    피지컬 AI 로보틱스 입장하기 ↗
  </a>
</div>
