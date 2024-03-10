<img src="https://github.com/jodog0412/ASAP_AI/assets/83653380/9b4717b7-07ef-4af8-be24-19a2a76abfaa" width="60%" height="60%">  

# 1. AI-pipeline
## 1) text2img
* [SDXL-Refiner](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0)
  * 2023, Stability AI
  * 높은 품질의 디테일한 이미지 생성 
* [DALL-E-3](https://openai.com/dall-e-3)
  * 2023, OpenAI
  * 빠른 생성 속도, 텍스트 이미지 생성 가능
## 2) text-embedding
* [all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) : 텍스트 임베딩 → 문장 간의 cosine-similarity 측정 가능
## 3) OCR(Optical Character Recognition)
* [Microsoft Azure, OCR](https://azure.microsoft.com/ko-kr/products/ai-services/ai-vision) : 이미지로부터 텍스트를 추출 

# 2. AI-server
* workstaion : Azure Virtual Machine (Nvidia, T4 GPU)
* server-development
  * read & update DB with AI-pipeline
  * `MongoDB`, `FastAPI`
* test
  * check client↔server connection 
  * `ngrok` 

※ .env 파일은 보안상의 이유로 github에 업로드하지 않았습니다.
