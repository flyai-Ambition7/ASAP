import time
from PIL import Image
from fastapi import FastAPI, UploadFile
from draw_image import *
from edit_image import *
from eval_image import evalulate_image
from db.update_db import *
from db.read_db import *

app=FastAPI()
BASE_PATH="samples"
@app.get("/")
async def root():
    return {"message":"hello world"}

@app.post("/upload")
async def upload(user_id:str,prompt:str,input_img:UploadFile):
    start=time.time()
    img = await input_img.read()
    update_image(img,user_id,int(start),"I")
    update_text(prompt,user_id)
    end=time.time()
    return {
        "time_consumption":f"{end-start:.2f}"
    }

@app.get("/read")
async def read():
    start=time.time()
    img_file_name=get_image_name_from_db(img_meta_tbl)
    prompt=get_prompt_from_db(text_tbl)
    end=time.time()
    return {
        "img_file_name":img_file_name,
        "prompt":prompt,
        "time_consumption":f"{end-start:.2f}"
    }
@app.get("/draw")
async def draw(user_id:str,prompt:str):
    start=time.time()
    DALLE_img,DALLE_acc=draw_filtered_image_by_DALLE(prompt)
    SD_img=draw_image_by_SD(prompt)
    img_output=await add_images(DALLE_img,SD_img)
    file_id=await update_image(img_output,user_id,int(start),"O")
    end=time.time()
    return {
        "file_id":str(file_id),
        "DALLE_accuracy":f"{DALLE_acc:.2f}",
        "time_consumption":f"{end-start:.2f}"
    }