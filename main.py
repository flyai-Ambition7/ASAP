import time
from fastapi import FastAPI, UploadFile
from draw_image import draw_filtered_image_by_DALLE, draw_image_by_SD
from edit_image import add_images
from eval_image import evalulate_image
from db.update_db import update_text_to_db, update_image_to_db
from db.read_db import *
import numpy as np

app=FastAPI()
BASE_PATH="samples"
@app.get("/")
async def root():
    return {"message":"hello world"}

@app.post("/upload")
async def upload(user_id:str,text_prompt:str,bg_prompt:str,img_input:UploadFile):
    start = time.time()
    img_input = await img_input.read()
    update_image_to_db(img_input,
                       user_id,
                       upload_time=int(start),
                       isinput=True)
    update_text_to_db(text_prompt,bg_prompt,user_id)
    end=time.time()
    return {
        "time_consumption":f"{end-start:.2f}"
    }

@app.get("/read_text")
async def read_text():
    start = time.time()
    text_prompt, bg_prompt = read_latest_prompts_from_db(text_tbl)
    end=time.time()
    return {
        "text_prompt":text_prompt,
        "bg_prompt":bg_prompt,
        "time_consumption":f"{end-start:.2f}"
    }

@app.get("/read_img")
async def read_img(isinput:bool):
    start = time.time()
    img_output=read_latest_img_from_db(img_chunk_tbl,img_meta_tbl,isinput)
    img_output.show()
    img_output.save('sample_output.jpg')
    end=time.time()
    return {
        "img_size":img_output.size,
        "time_consumption":f"{end-start:.2f}"
    }

@app.post("/draw")
def draw():
    start=time.time()
    img_input, img_file_name, text_prompt, image_prompt = read_infos_from_db(img_chunk_tbl,img_meta_tbl,text_tbl,False)
    user_id = img_file_name.split('_')[0]
    DALLE_img, DALLE_acc = draw_filtered_image_by_DALLE(text_prompt)
    SD_img = draw_image_by_SD(img_input,image_prompt)
    img_output = add_images(DALLE_img,SD_img)
    update_image_to_db(img_output,
                       user_id,
                       upload_time=int(start),
                       isinput=False)
    end=time.time()
    return {
        "DALLE_accuracy":f"{DALLE_acc:.2f}",
        "time_consumption":f"{end-start:.2f}"
    }