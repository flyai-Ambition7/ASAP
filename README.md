<img src="https://github.com/jodog0412/ASAP_AI/assets/83653380/9b4717b7-07ef-4af8-be24-19a2a76abfaa" width="60%" height="60%">  

# 1. AI-pipeline
## 1) image-generation(text2img)
* [SDXL-Refiner](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0)
  * 2023, Stability AI
  * 높은 품질의 디테일한 이미지 생성 
* [DALL-E-3](https://openai.com/dall-e-3)
  * 2023, OpenAI
  * 빠른 생성 속도, 텍스트 이미지 생성 가능
## 2) text-accuracy-inspection
* [all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) : 텍스트 임베딩
* [Microsoft Azure OCR](https://azure.microsoft.com/ko-kr/products/ai-services/ai-vision) : 이미지로부터 텍스트 추출
1. `Microsoft Azure OCR` → 생성된 이미지에서 텍스트를 추출 
2. `all-mpnet-base-v2` → target_text, generated_text를 임베딩
3. cosine similarity → 두 embedded_text 사이의 유사도 계산

# 2. AI-server
* 워크스테이션 : Azure Virtual Machine (Nvidia, T4 GPU)
* 서버 개발
  * DB ↔ AI-pipeline 연동
  * `MongoDB`, `FastAPI`
* 서버 테스트
  * client ↔ server 연결 확인 
  * `ngrok` 

※ .env 파일은 보안상의 이유로 github에 업로드하지 않았습니다.
