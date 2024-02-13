import time
from PIL import Image
from fastapi import FastAPI
from draw_image import *
from eval_image import evalulate_image
from update_db import *

app=FastAPI()
BASE_PATH="samples"
@app.get("/")
async def root():
    return {"message":"hello world"}

@app.get("/draw")
def draw(user_id:str,prompt:str):
    start=time.time()
    DALLE_img,DALLE_score=draw_filtered_image_by_DALLE(prompt)
    SD_img=draw_image_by_SD(prompt)
    DALLE_img.save(f'{BASE_PATH}/DALLE_{int(start)}.jpg')
    SD_img.save(f'{BASE_PATH}/SD_{int(start)}.jpg')
    # update_image(DALLE_img,user_id,start)
    end=time.time()
    return {
            "DALLE_img_info":DALLE_img.size,
            "SD_img_info":SD_img.size,
            "DALLE_score":f"{DALLE_score:.2f}",
            "time_consumption":f"{end-start:.2f}"}