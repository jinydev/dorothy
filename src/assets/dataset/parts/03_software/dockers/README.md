# 🐳 도커 강의 데이터셋 파츠 (Docker Dataset Parts)

본 디렉토리([`dockers/`](.))는 도로시(Dorothy) Multi-Concept LoRA 학습 및 도커 강의 교재 제작을 위해 구축된 총 20종(로고 1종 + 아키텍처 다이어그램 19종)의 고해상도(1024×1024) 데이터셋 파츠 모음입니다.

모든 이미지는 도로시 프로젝트의 **지브리 애니메이션 교육용 스타일(Ghibli Anime Educational Style, 에스프레소 브라운 `#26211E` 라인아트, 순백색 `#FFFFFF` 배경)** 가이드를 엄격히 준수합니다.

---

## 📂 파일 목록 및 프롬프트 명세 (총 20종)

| 파일명 (ID) | 명칭 | 원본 챕터 | LoRA 캡션 프롬프트 요약 |
| :--- | :--- | :--- | :--- |
| `logo_10_docker` | 도커 인프라 로고 | 사용자 제공 애셋 | `logo, docker infrastructure logo, friendly blue whale swimming carrying colorful containers, ghibli anime style, clean line art, pure white background` |
| `docker_01_cloud_migration_legacy` | 클라우드 이주 & 레거시 현대화 | Part 01 - 001장 | `diagram, educational graphic, docker cloud migration and legacy modernization architecture, monolithic application containerization, lift and shift strategy, strangler fig pattern, clean line art, ghibli anime educational style, pure white background` |
| `docker_02_msa_devops_containers` | MSA & 데브옵스 컨테이너 | Part 01 - 002장 | `diagram, educational graphic, microservices architecture and devops pipeline with docker, decoupled service containers, continuous integration and deployment loop, clean line art, ghibli anime educational style, pure white background` |
| `docker_03_hello_world_workflow` | Build-Share-Run 워크플로 | Part 01 - 005장 | `diagram, educational graphic, standard docker build share run workflow, docker client cli, docker daemon engine, registry repository, clean vector graphic, ghibli anime educational style, pure white background` |
| `docker_04_dockerfile_syntax` | Dockerfile 기본 문법 해부 | Part 02 - 016장 | `diagram, educational graphic, dockerfile instruction syntax anatomy, FROM base image, ENV variables, WORKDIR, COPY source files, CMD execution command, clean line art, ghibli anime educational style, pure white background` |
| `docker_05_layer_immutability` | 이미지 레이어 아키텍처 & 불변성 | Part 02 - 018장 | `diagram, educational graphic, docker image layered architecture and immutability, stacked read-only layers, sha256 layer cache, union filesystem, clean line art, ghibli anime educational style, pure white background` |
| `docker_06_multistage_build` | 멀티스테이지 빌드 패턴 | Part 02 - 021장 | `diagram, educational graphic, docker multistage build pattern, heavy build environment stage, lean minimal production artifact, alpine scratch base image, clean line art, ghibli anime educational style, pure white background` |
| `docker_07_registry_push_pull` | 도커 레지스트리 Push & Pull | Part 02 - 027장 | `diagram, educational graphic, docker image distribution and registry push pull flow, local engine to docker hub and ghcr repository, semantic tag versioning, clean line art, ghibli anime educational style, pure white background` |
| `docker_08_storage_volumes` | 퍼시스턴트 도커 볼륨 | Part 03 - 033장 | `diagram, educational graphic, docker persistent volume architecture, decoupling storage lifecycle from ephemeral container, named volume mount, clean line art, ghibli anime educational style, pure white background` |
| `docker_09_bind_mount_development` | 바인드 마운트 실시간 동기화 | Part 03 - 036장 | `diagram, educational graphic, docker bind mount development workflow, live source code sync between host directory and container filesystem, instant reload, clean line art, ghibli anime educational style, pure white background` |
| `docker_10_compose_declarative_stack` | 도커 컴포즈 선언적 스택 | Part 04 - 042장 | `diagram, educational graphic, docker compose declarative multi-container stack, compose yaml specification, orchestrating web server, application was, database and cache, clean line art, ghibli anime educational style, pure white background` |
| `docker_11_compose_internal_dns` | 내장 DNS 및 서비스 디스커버리 | Part 04 - 044장 | `diagram, educational graphic, docker embedded dns server and service discovery, container name resolution, round-robin load balancing, clean line art, ghibli anime educational style, pure white background` |
| `docker_12_container_healthcheck` | 헬스체크 프로브 아키텍처 | Part 04 - 047장 | `diagram, educational graphic, docker container healthcheck probe mechanism, process status vs service availability, interval retries and timeout, clean line art, ghibli anime educational style, pure white background` |
| `docker_13_multi_environment_workflow` | 다중 환경(Dev/Test/Prod) 설계 | Part 05 - 067장 | `diagram, educational graphic, docker multi-environment deployment workflow, dev test prod configuration parity, compose override inheritance and secret injection, clean line art, ghibli anime educational style, pure white background` |
| `docker_14_swarm_cluster_nodes` | 도커 스웜 클러스터 매니저/워커 | Part 06 - 077장 | `diagram, educational graphic, docker swarm cluster architecture, manager nodes raft consensus quorum, worker nodes task scheduling, clean line art, ghibli anime educational style, pure white background` |
| `docker_15_swarm_vs_kubernetes` | 스웜 vs 쿠버네티스 아키텍처 비교 | Part 06 - 080장 | `diagram, educational graphic, container orchestration comparison, docker swarm simplicity vs kubernetes enterprise ecosystem, clean line art, ghibli anime educational style, pure white background` |
| `docker_16_mtls_docker_security` | 상호 TLS(mTLS) 도커 데몬 보안 | Part 07 - 097장 | `diagram, educational graphic, docker mutual tls mtls security architecture, certificate authority ca, server and client public keys, encrypted daemon endpoint, clean line art, ghibli anime educational style, pure white background` |
| `docker_17_centralized_fluentd_logging` | 중앙 집중식 Fluentd 로그 파이프라인 | Part 08 - 116장 | `diagram, educational graphic, centralized docker container logging pipeline, stdout stderr stream, fluentd log aggregator, opensearch and loki search visualization, clean line art, ghibli anime educational style, pure white background` |
| `docker_18_reverse_proxy_loadbalancing` | Nginx/Traefik 리버스 프록시 & 로드밸런싱 | Part 08 - 119장 | `diagram, educational graphic, reverse proxy architecture with nginx and traefik, ssl tls termination, upstream server load balancing, clean line art, ghibli anime educational style, pure white background` |
| `docker_19_async_redis_messaging` | Redis 비동기 이벤트 큐 시스템 | Part 08 - 122장 | `diagram, educational graphic, asynchronous event-driven messaging queue, dockerized redis pub sub broker, worker task queues and background processing, clean line art, ghibli anime educational style, pure white background` |

