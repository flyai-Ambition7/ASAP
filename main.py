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
    update_image(img,user_id,int(start),True)
    update_text(prompt,user_id)
    end=time.time()
    return {
        "time_consumption":f"{end-start:.2f}"
    }

@app.get("/read")
async def read():
    start=time.time()
    img_file_name = get_image_info_from_db(img_meta_tbl)
    prompt=get_prompt_from_db(text_tbl)
    end=time.time()
    return {
        "img_file_name":img_file_name,
        "prompt":prompt,
        "time_consumption":f"{end-start:.2f}"
    }

@app.get("/draw")
async def draw():
    start=time.time()
    img_file_name = get_image_info_from_db(img_meta_tbl)
    user_id = img_file_name.split('_')[0]
    img_input = get_img_from_db(img_chunk_tbl,img_meta_tbl) 
    prompt=get_prompt_from_db(text_tbl)
    DALLE_img,DALLE_acc=draw_filtered_image_by_DALLE(prompt)
    SD_img=draw_image_by_SD(img_input,prompt)
    img_output=add_images(DALLE_img,SD_img)
    update_image(img_output,user_id,int(start),False)
    end=time.time()
    return {
        "DALLE_accuracy":f"{DALLE_acc:.2f}",
        "time_consumption":f"{end-start:.2f}"
    }