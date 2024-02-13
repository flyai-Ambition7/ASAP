import time
from PIL import Image
from fastapi import FastAPI
from draw_image import *
from eval_image import evalulate_image
from update_db import *

app=FastAPI()

@app.get("/")
async def root():
    return {"message":"hello world"}

@app.get("/draw")
def draw(user_id:str,prompt:str):
    start=time.time()
    top_img,top_score = 0,0
    for _ in range(5):
        img = draw_image_by_DALLE(prompt)
        score = evalulate_image(prompt,img)
        if top_score<score:
            top_img, top_score = img, score
            if score>0.99:
                break
    update_image(top_img,user_id,start)
    end=time.time()
    return {"img_info":Image.open(top_img),
            "score":f"{top_score:.2f}",
            "time_consumption":f"{end-start:.2f}"}