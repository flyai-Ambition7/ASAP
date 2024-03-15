# 생성형 AI 기반 홍보물 제작 서비스
### [SKT FLY AI Challenger 4기] 패기 7조 ASAP 프로젝트 

<p align="center">
  <br>
  <img src="./images/service_video.gif" width="640" height="360">
  <br>
</p>

## 👨🏼‍💻 프로젝트 소개
- 자영업자들이 홍보물 제작 과정에서 겪는 **시간과 비용을 절감**시켜 주는 서비스
- 사용자가 **글과 이미지만 입력**하면 현수막, 전단지, SNS게시물 등에서 사용 가능한 다양한 홍보물 이미지를 생성해주는 서비스
  <br></br>

## 🧑‍🤝‍🧑 팀 구성

| <img src="https://avatars.githubusercontent.com/u/113690378?v=4" width="140">   | <img src="https://avatars.githubusercontent.com/u/149135459?v=4" width="140"> | <img src="https://avatars.githubusercontent.com/u/43908014?v=4" width="140"> | <img src="https://avatars.githubusercontent.com/u/149581532?v=4" width="140"> | <img src="https://avatars.githubusercontent.com/u/83653380?v=4" width="140"> |
| :--------: | :--------: | :-------:| :-----: | :-----: |
|   [정유진](https://github.com/yujin45)   |   [옥창희](https://github.com/okchangheeok)    |  [최지안](https://github.com/choijian) |  [정민수](https://github.com/dbp-jack) |  [이현성](https://github.com/jodog0412) |  
| 팀장, 프론트엔드, 영상처리| 영상처리, AI | 디자인, 백엔드, 프롬프트 튜닝 | 백엔드 | AI, 클라우드|

<br></br>
  
## 📅 개발 기간
2024.01.02 ~ 2024.02.28  
### [세부 일정]

2024.01.02 ~ 2024.01.29 
- 프로젝트 기획 및 설계
- AI Process 설계
- UI/UX 설계
<br></br>

2024.01.29 ~ 2024.02.28
- API 명세서, DB 설계
- 프론트엔드 개발
- 백엔드 개발
- 클라우드 개발
- MVP 구축 및 테스트
- PPT, 영상 제작, 발표
  

  <br></br>
  
## 🔧 기술 스택
### Frontend
<div>
  <img src="https://img.shields.io/badge/java-007396?style=for-the-badge&logo=OpenJDK&logoColor=white">
  <img src="https://img.shields.io/badge/kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white">
  <img src="https://img.shields.io/badge/android-34A853?style=for-the-badge&logo=android&logoColor=white">
</div>

### Backend
<div>
  <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=Django&logoColor=white">
  <img src="https://img.shields.io/badge/mongodb-47A248?style=for-the-badge&logo=MongoDB&logoColor=white">
</div>

### AI
<div>
  <img src="https://img.shields.io/badge/openai-412991?style=for-the-badge&logo=OpenAI&logoColor=white">
</div>

### Image Processing
<div>
  <img src="https://img.shields.io/badge/opencv-5C3EE8?style=for-the-badge&logo=OpenCV&logoColor=white">
</div>
  <br></br>
  
## 🐣 구현 기능

### 1. GPT를 이용한 홍보문구 생성
<img src="./documents/flow/text_generate.png" width="600" height="300">

### 2. Dalle, OCR을 이용한 텍스트 이미지 생성 및 정확도 계산
<img src="./documents/flow/text_generate2.png" width="600" height="300">
  
### 3. OpenCV, Stable Diffusion을 이용한 배경 이미지 생성
<img src="./documents/flow/image_generate.png" width="600" height="300">
  
### 4. OpenCV를 이용한 마스킹 처리 및 이미지 합성
<img src="./documents/flow/image_synthesize.png" width="600" height="300">
<br></br>

## 🎨 화면 구성
<img src="./documents/ui/슬라이드6.PNG" width="700" height="400">
<img src="./documents/ui/슬라이드7.PNG" width="700" height="400">
<img src="./documents/ui/슬라이드8.PNG" width="700" height="400">
<img src="./documents/ui/슬라이드9.PNG" width="700" height="400">
<img src="./documents/ui/슬라이드10.PNG" width="700" height="400">
<img src="./documents/ui/슬라이드11.PNG" width="700" height="400">
<img src="./documents/ui/슬라이드12.PNG" width="700" height="400">
<img src="./documents/ui/슬라이드13.PNG" width="700" height="400">
<img src="./documents/ui/슬라이드14.PNG" width="700" height="400">
<img src="./documents/ui/슬라이드15.PNG" width="700" height="400">
<img src="./documents/ui/슬라이드16.PNG" width="700" height="400">

## 기대효과 및 활용방안  
### 🍃 ESG  
- **소상공인** 홍보물 제작 지원을 통한 **지역경제 활성화**
- 공익 캠페인, 국가 등에 홍보물 제작에 지원해 줌으로써 **사회 메시지 전달**이나 **특산물 홍보**에 기여  

### 💰 비즈니스 모델 
- **인쇄 업체나 옥외광고 업체와 제휴**를 맺어 소비자에게 또 하나의 편리한 서비스 프로세스 제공
- 홍보 디자인을 활용할 수 있는 모든 업체와 **상호 보완적인 혜택** 마련  
  
### 🦄 확장성  
- **사용자로부터 결과물에 대한 피드백**을 받아 다음 생성에서 더 높은 퀄리티의 맞춤형 결과물을 내도록 **AI모델 성능을 개선**
- 영상을 자동 생성해주는 API를 이용하여 **유튜브 쇼츠 형태**로 확장  
