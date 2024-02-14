from PIL import Image
from io import BytesIO
from db import *
from gridfs import GridFS

# mongo_db : mongodb 객체
# mongo_db.collections -> fs.files, fs.chunks, user
# mongo_db.fs.files -> _id, filename, chunkSize, length, uploadDate

fs = GridFS(mongo_db)
get_docs= lambda tbl:[doc for doc in tbl.find()]
img_chunk_tbl, img_meta_tbl, text_tbl  = mongo_db["fs.chunks"], mongo_db["fs.files"], mongo_db["text"]

def get_prompt_from_db(tbl):
    texts=get_docs(tbl)
    prompt=texts[-1]['prompt']
    return prompt

def get_image_info_from_db(tbl):
    img_metas=get_docs(tbl)
    last_doc=img_metas[-1]
    img_file_name = last_doc['filename']
    return img_file_name

def get_img_from_db(img_file_tbl,img_meta_tbl):
    file_id=get_docs(img_meta_tbl)[-1]['_id']
    chunks=img_file_tbl.find({"files_id":file_id})
    img_bin = b''.join(chunk['data'] for chunk in chunks)
    img = Image.open(BytesIO(img_bin))
    return img

img_result=get_img_from_db(img_chunk_tbl,img_meta_tbl)
img_result.show()