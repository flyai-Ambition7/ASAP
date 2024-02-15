from PIL import Image
from io import BytesIO
from db import *

def get_docs(tbl):
    return [doc for doc in tbl.find()]

def get_prompts_from_db(tbl):
    texts=get_docs(tbl)
    text_prompt=texts[-1]['text_prompt']
    bg_prompt=texts[-1]['bg_prompt']
    return (text_prompt, bg_prompt)

def get_img_from_db(img_file_tbl,img_meta_tbl):
    latest_file_id=get_docs(img_meta_tbl)[-1]['_id']
    chunks=img_file_tbl.find({"files_id":latest_file_id})
    img_bin = b''.join(chunk['data'] for chunk in chunks)
    img = Image.open(BytesIO(img_bin))
    return img

def read_infos_from_db(img_data_tbl,img_meta_tbl,text_tbl):
    img_metas=get_docs(img_meta_tbl)
    latest_meta=img_metas[-1]
    img_file_name, img_file_id = latest_meta['filename'], latest_meta['_id']
    img_chunks=img_data_tbl.find({"files_id":img_file_id})
    img_bin=b''.join(chunk['data'] for chunk in img_chunks)
    img_file=Image.open(BytesIO(img_bin))
    text_prompt, bg_prompt = get_prompts_from_db(text_tbl)
    return img_file, img_file_name, text_prompt, bg_prompt 

# img_result=get_img_from_db(img_chunk_tbl,img_meta_tbl)
# img_result.show()