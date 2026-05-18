# ROS2 Core Practice

Python과 turtlesim을 기반으로 ROS2 핵심 개념을 실습한 저장소이다.

이 저장소에서는 다음과 같은 ROS2 기본 통신 구조를 학습하고 실습하였다.

- Node
- Topic (Publisher / Subscriber)
- Service
- turtlesim 제어
- Custom ROS2 Package 구조

---

# 개발 환경

- Ubuntu 22.04 (WSL2)
- ROS2 Humble
- Python 3


---

# 주요 실습 내용

## Publisher / Subscriber

- ROS2 Topic 기반 메시지 송수신
- turtlesim pose topic 구독
- 실시간 데이터 통신 구조 실습

## Service

- ROS2 Service Server 생성
- Request / Response 기반 통신 실습

## turtlesim 실습

- 거북이 이동 제어
- 거북이 위치 데이터 수신
- 명령 토픽과 상태 토픽 연동

---

# 빌드 방법

```bash
colcon build
```

---

# Workspace Source

```bash
source install/setup.bash
```

---

# 실행 예시

## turtlesim 실행

```bash
ros2 run turtlesim turtlesim_node
```

## Subscriber 실행

```bash
ros2 run my_first_package my_subscriber
```

## Publisher 실행

```bash
ros2 run my_first_package my_publisher
```

## Service Server 실행

```bash
ros2 run my_first_package my_service_server
```

---

# 학습 목표

- ROS2 통신 구조 이해
- Node 기반 분산 시스템 구조 학습
- Topic 및 Service 통신 방식 이해
- 로봇 소프트웨어 기본 개발 흐름 실습