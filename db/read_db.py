from PIL import Image
from io import BytesIO
from db import *
from gridfs import GridFS

fs = GridFS(mongo_db)
get_docs= lambda tbl:[doc for doc in tbl.find()]
img_chunk_tbl, img_meta_tbl, text_tbl  = mongo_db["fs.chunks"], mongo_db["fs.files"], mongo_db["text"]

def get_prompt_from_db(tbl):
    texts=get_docs(tbl)
    prompt=texts[-1]['prompt']
    return prompt

def get_img_from_db(img_file_tbl,img_meta_tbl):
    file_id=get_docs(img_meta_tbl)[-1]['_id']
    chunks=img_file_tbl.find({"files_id":file_id})
    img_bin = b''.join(chunk['data'] for chunk in chunks)
    img = Image.open(BytesIO(img_bin))
    return img

def read_infos_from_db(img_data_tbl,img_meta_tbl,text_tbl):
    img_metas=get_docs(img_meta_tbl)
    meta=img_metas[-1]
    img_file_name, img_file_id = meta['filename'], meta['_id']
    img_chunks=img_data_tbl.find({"files_id":img_file_id})
    img_bin=b''.join(chunk['data'] for chunk in img_chunks)
    img_input=Image.open(BytesIO(img_bin))
    prompt=get_prompt_from_db(text_tbl)
    return img_input, img_file_name, prompt


img_result=get_img_from_db(img_chunk_tbl,img_meta_tbl)
img_result.show()