from PIL import Image
from io import BytesIO
from db import *

def read_docs(tbl):
    return [doc for doc in tbl.find()]

def read_latest_prompts_from_db(tbl):
    texts=read_docs(tbl)
    latest_text=texts[-1]
    text_prompt, bg_prompt = latest_text['text_prompt'], latest_text['bg_prompt']
    return (text_prompt, bg_prompt)

def read_latest_img_from_db(img_file_tbl,img_meta_tbl,isinput:bool):
    if isinput:
        metas=[doc for doc in img_meta_tbl.find() if '0.jpg' in doc['filename']]
    else:
        metas=[doc for doc in img_meta_tbl.find() if '1.jpg' in doc['filename']]
    latest_file_id=metas[-1]['_id']
    img_chunks=img_file_tbl.find({"files_id":latest_file_id})
    img_bin = b''.join(chunk['data'] for chunk in img_chunks)
    img = Image.open(BytesIO(img_bin))
    return img

def read_infos_from_db(img_data_tbl,img_meta_tbl,text_tbl,isinput:bool):
    if isinput:
        metas=[doc for doc in img_meta_tbl.find() if '0.jpg' in doc['filename']]
    else:
        metas=[doc for doc in img_meta_tbl.find() if '1.jpg' in doc['filename']]
    metas=read_docs(img_meta_tbl)
    latest_meta=metas[-1]
    img_file_name, img_file_id = latest_meta['filename'], latest_meta['_id']
    img_chunks=img_data_tbl.find({"files_id":img_file_id})
    img_bin=b''.join(chunk['data'] for chunk in img_chunks)
    img_file=Image.open(BytesIO(img_bin))
    text_prompt, bg_prompt = read_latest_prompts_from_db(text_tbl)
    return img_file, img_file_name, text_prompt, bg_prompt 

# img_result=get_img_from_db(img_chunk_tbl,img_meta_tbl)
# img_result.show()