import time
from PIL import Image
from fastapi import FastAPI
from draw_image import *
from eval_image import evalulate_image
from update import *

app=FastAPI()

@app.get("/")
async def root():
    return {"message":"hello world"}

@app.get("/draw")
def draw(user_id:str,prompt:str):
    start=time.time()
    DALLE_img_1st,DALLE_score_1st = 0,0
    for _ in range(3):
        img = draw_image_by_DALLE(prompt)
        score = evalulate_image(prompt,img)
        if DALLE_score_1st<score:
            DALLE_img_1st, DALLE_score_1st = img, score
            if score>0.99:
                break
    SD_img=draw_image_by_SD(prompt)
    DALLE_img=Image.open(DALLE_img_1st)
    DALLE_img.save(f'DALLE_{int(start)}.jpg')
    SD_img.save(f'SD_{int(start)}.jpg')
    # update_image(DALLE_img_1st,user_id,start)
    end=time.time()
    return {"DALLE_img_info":Image.open(DALLE_img_1st),
            "SD_img_info":SD_img,
            "DALLE_score":f"{DALLE_score_1st:.2f}",
            "time_consumption":f"{end-start:.2f}"}