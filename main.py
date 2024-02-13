import time
from PIL import Image
from fastapi import FastAPI
from draw_image import *
from eval_image import evalulate_image
from update_db import *
import cv2

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
    # DALLE_img.save(f'{BASE_PATH}/DALLE_{int(start)}.jpg')
    # SD_img.save(f'{BASE_PATH}/SD_{int(start)}.jpg')
    img_output=cv2.add(DALLE_img,SD_img)
    img_output.save(f'{BASE_PATH}/RESULT_{int(start)}')
    # update_image(DALLE_img,user_id,start)
    end=time.time()
    return {
            "output_img_info":img_output.size(),
            "DALLE_score":f"{DALLE_score:.2f}",
            "time_consumption":f"{end-start:.2f}"}