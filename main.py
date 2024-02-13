import time
from PIL import Image
from fastapi import FastAPI
from draw_image import *
from edit_image import *
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
    DALLE_img,DALLE_acc=draw_filtered_image_by_DALLE(prompt)
    SD_img=draw_image_by_SD(prompt)
    img_output=add_images(DALLE_img,SD_img)
    update_image(img_output,user_id,int(start))
    end=time.time()
    return {"DALLE_accuracy":f"{DALLE_acc:.2f}",
            "time_consumption":f"{end-start:.2f}"}