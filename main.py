import time
from PIL import Image
from fastapi import FastAPI
from draw_img import *
from update import *

app=FastAPI()

@app.get("/")
async def root():
    return {"message":"hello world"}

@app.get("/draw")
def draw(user_id:str,image_id:int,prompt:str):
    start=time.time()
    image_bytes = draw_by_DALLE(prompt)
    update_image(image_bytes,user_id,image_id)
    end=time.time()
    return {"image_info":Image.open(image_bytes),
            "time_consumption":f"{end-start:.2f}"}