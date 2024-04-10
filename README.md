# 🟪 Upstage Post OCR Parsing Project (명함 정보 추출)

## Introduction

### 🤪 Team 유쾌한 반란

### 🔅 Members

김준석|서인범|송영준|심효은|정시현|
:-:|:-:|:-:|:-:|:-:
<img src='https://avatars.githubusercontent.com/u/71753257?v=4' height=80 width=80px></img>|<img src='https://avatars.githubusercontent.com/u/92137358?v=4' height=80 width=80px></img>|<img src='https://avatars.githubusercontent.com/u/55626702?v=4' height=80 width=80px></img>|<img src='https://avatars.githubusercontent.com/u/62679143?v=4' height=80 width=80px></img>|<img src='https://user-images.githubusercontent.com/46811558/157460704-6a5ac09f-fe71-4dd3-b30a-f2fa347b08d2.jpg' height=80 width=80px></img>
[Github](https://github.com/junseok0408)|[Github](https://github.com/inbeomi)|[Github](https://github.com/addadda15)|[Github](https://github.com/hyoeun98)|[Github](https://github.com/jungsiroo)

## Project Outline

### 🎯 프로젝트 목표

> OCR API를 활용하여 **명함의 정보(이름, 직책, 주소, 회사명, 전화번호, 이메일) 추출**
> 

### 📍 프로젝트 Challenges

- **불완전한 OCR API** : 주어지는 OCR 정보는 정렬되지 않은 글자와 좌표값 뿐
- **정의하기 힘든 문제** : 목적함수는 무엇으로 설정하며 그에 따른 데이터는 어떻게 구성하는가?

**Solution : `명함 도메인 특성에 집중!`**

- **불완전한 OCR API** : 좌표값을 통해 기울기를 계산하고 이미지를 정방향으로 조정해 **글자 정렬 및 클러스터링**
- **정의하기 힘든 문제** : 명함 이미지는 개인 정보이기에, 명함 이미지 학습이나 생성이 아닌 명함 내 **글자들의 개채명 인식 문제로 변경**

### 🏭 프로젝트 전체 구조

![image](https://github.com/jungsiroo/boostcamp_final_project/assets/54366260/7d46e77d-1d6f-46e9-b6fe-b269ca6a87b0)


### 🔈 업무 분담

![image](https://github.com/jungsiroo/boostcamp_final_project/assets/54366260/841de1ab-fb3e-44fb-99b8-775a739fb78c)


## 🖍️ 프로젝트 기여

### Serialization

실제 데이터를 전달했을 때 **단어가 따로 따로 추출이 되고 순서도 뒤죽박죽**이라 직렬화가 필요

1. 좌표의 중심값에서 오차범위 이내의 y축 값들을 묶어준다.
2. 같은 y축 범위에 속해 있는 값들을 x축 기준으로 정렬한다.
3. OCR API를 통해 얻은 좌표의 크기를 10% 정도 늘려 겹치게 만든 후 BFS방식으로 Clustering을 진행한다.
4. 분류된 Cluster들을 JSON 형태로 전달한다.

![image](https://github.com/jungsiroo/boostcamp_final_project/assets/54366260/0371ca97-16b2-4baf-92d5-9ba9ee4babe3)


**DBSCAN 클러스터링 방식과 자체 클러스터링 비교**

![image](https://github.com/jungsiroo/boostcamp_final_project/assets/54366260/474f9ee4-23a7-4a1a-b64f-64f9e628d22e)

- DBSCAN 사용 후 정성적으로 평가 시 **너무 후하게 클러스터링**이 되는 모습 발견
- 자체적으로 좌표 크기를 늘린 후 **BFS를 통한 클러스터링 기법**을 통해 더 세부적으로 가능해짐

### Text pre & post process

- 직렬화 프로세스 전 OCR API의 좌표값을 통해 각 **Text를 방향에 맞게 정렬**
- **`PyKo-Spacing`** 을 활용하여 직렬화된 텍스트의 띄어쓰기 후처리 진행
- 모델의 성능 / 정확도 측면보다는 **유저 경험**을 고려하여 진행된 프로세스

## 📕 프로젝트 아쉬운 점

- 명함 도메인에 최적화된 데이터셋 구축 및 활용하지 못한 것
    - 개인정보와 관련 데이터 수집에 대한 어려움을 느낄 수 있었음
    - 추후 Masking 혹은 익명화 고려
- 서비스 관점에서 사용자가 정보를 수정할 수 있는 기능 등과 같은 고도화 기법 적용 못 해본점
- 실제 서비스 운영하면서 유저들의 실시간 피드백 수용해보지 못한 것

## 🔎 성장한 역량

- **문제 정의, 데이터 구축, 지표 설정, 프로덕트 서빙**까지 A부터 Z까지 경험
- 문제 정의 과정에서 **각자 다른 의견들을 하나로 좁혀가는 과정**에서 ”진정한 협업” 경험
- 프로덕트 서빙 시 **latency와 정확도 간의 trade-off** 를 고민하여 **지표 설정**
- 실제 명함 서비스 운영 중인 회사에게 자문을 구해 **현업 OCR 직렬화에 대한 조언**을 통해 문제 scope를 줄일 수 있었음
- 활용했던 **PyKo-Spacing** 의 경우 사소하지만 **Contributor로 활동**하여 오픈소스 생태계 기여

## Demo

### 👀 명함 인식 앱 구동 예시

![ezgif-4-e56ff915ab](https://user-images.githubusercontent.com/54366260/172990038-4fafa836-0f55-4d15-87d7-feb230b7a3a6.gif)
