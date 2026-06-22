# Smart-Grip-Car-v1.1

<p align="center">
  <img src="https://github.com/user-attachments/assets/fc9d76bf-851d-4538-a262-0100c8b3d112" width="500">
</p>

<h3 align="center">
YOLOv8 기반 실시간 객체 인식 및 웹 UI 원격 제어 자율 이송 로봇
</h3>

---

# 프로젝트 소개

Smart-Grip-Car-v1.1은 Raspberry Pi 4와 STM32F103을 연동하여 개발한 AI 기반 자율 이송 로봇 시스템입니다.

YOLOv8 객체 인식 모델을 활용하여 실시간으로 물체를 탐지하고, 웹 브라우저 기반 UI를 통해 차량 제어 및 센서 상태를 모니터링할 수 있도록 구현하였습니다.

기존 Smart-Grip-Car 프로젝트를 확장하여 AI 비전 기술과 임베디드 제어 기술을 하나의 시스템으로 통합하였습니다.

---

# 개발 기간

* 2026.03.25 ~ 2026.04.01

---

# 기술 스택

| 구분            | 기술                         |
| ------------- | -------------------------- |
| MCU           | STM32F103                  |
| SBC           | Raspberry Pi 4             |
| Language      | C, Python                  |
| AI            | YOLOv8, OpenCV             |
| Server        | Flask, Node.js             |
| Communication | UART, I2C                  |
| Control       | PWM, ADC                   |
| Tool          | STM32CubeIDE, Google Colab |

---

# 시스템 아키텍처

<p align="center">
  <img src="https://github.com/user-attachments/assets/821aaf61-8285-4012-bf39-b4227fa9dbae" width="800">
</p>

## 데이터 흐름

1. Raspberry Pi 4 카메라 영상 수집
2. YOLOv8 객체 인식 수행
3. 객체 인식 결과 분석
4. UART 통신을 통해 STM32로 제어 명령 전송
5. STM32가 모터 및 센서 제어 수행
6. 웹 UI를 통해 실시간 상태 모니터링

---

# 주요 기능

## 1. YOLOv8 객체 인식

<p align="center">
  <img src="https://github.com/user-attachments/assets/5a6ce5b3-dda4-47e3-b51b-90680a3db6ac" width="45%">
  <img src="https://github.com/user-attachments/assets/4c91fc3b-771e-494b-a66f-f0e2d3e0181f" width="45%">
</p>

### 구현 내용

- YOLOv8 기반 실시간 객체 탐지
- Paper, Plastic Bag, Carton 등 객체 분류
- TACO Dataset 기반 커스텀 학습
- Raspberry Pi 기반 실시간 추론 수행

---

## 2. 웹 UI 기반 원격 제어
<p align="center">
  <img src="https://github.com/user-attachments/assets/210ba3bd-1771-4c43-ab47-2206bb19a9ed" width="800">
</p>

### 구현 내용

* 실시간 영상 스트리밍
* 차량 이동 제어
* 초음파 센서 데이터 확인
* 시스템 상태 모니터링

---

## 3. STM32 기반 하드웨어 제어

### 구현 내용

* PWM 기반 DC 모터 제어
* Servo Motor 제어
* 초음파 거리 측정
* 조도 기반 LED 제어
* UART 기반 Raspberry Pi 연동

---

# 프로젝트 성과

* Raspberry Pi 4와 STM32F103 간 UART 통신 구현
* YOLOv8 기반 객체 인식 기능 구현
* Flask 및 Node.js 기반 웹 UI 구축
* AI + Embedded + Web 기술 통합 시스템 개발
* 실시간 객체 인식 및 원격 제어 기능 구현

---

# 문제 해결 경험

## 문제 1 : UART 통신 안정성 문제

### 문제 상황

조이스틱 입력 및 센서 데이터 처리 과정에서 통신 누락과 응답 지연이 발생하였습니다.

### 해결 방법

* Polling 구조 제거
* Interrupt 기반 구조 적용
* Ring Buffer 적용

### 결과

통신 안정성을 향상시키고 데이터 누락 문제를 해결하였습니다.

---

## 문제 2 : 객체 인식 성능 저하

### 문제 상황

실제 환경에서 객체 인식률이 낮아지는 문제가 발생하였습니다.

### 원인

TACO 데이터셋과 실제 환경 간 차이

### 해결 방법

* 국내 환경 데이터 추가 수집
* 데이터셋 보강
* YOLOv8 파라미터 최적화

### 결과

실제 환경에서의 객체 인식 성능을 향상시켰습니다.

---

# 프로젝트를 통해 배운 점

* Raspberry Pi와 STM32 통합 제어 구조 이해
* YOLOv8 객체 인식 모델 적용 경험
* UART 기반 임베디드 통신 경험
* AI, Embedded, Web 기술 통합 경험
* 시스템 통합 과정에서의 문제 해결 능력 향상

---

# 향후 개선 계획

* ROS2 연동
* Object Tracking 기능 추가
* 자율주행 기능 구현
* 실시간 경로 계획 기능 적용
* AI 기반 자동 물체 집기 기능 개발

---

# 시연 영상

YouTube 링크 추가 예정

---

# 개발자

임청수

GitHub
https://github.com/koonie404
