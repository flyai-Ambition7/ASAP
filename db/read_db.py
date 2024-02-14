from PIL import Image
from io import BytesIO
from db import *
from gridfs import GridFS

# mongo_db : mongodb 객체
# mongo_db.collections -> fs.files, fs.chunks, user
# mongo_db.fs.files -> _id, filename, chunkSize, length, uploadDate

fs = GridFS(mongo_db)
tolist = lambda tbl:[doc for doc in tbl.find()]
img_chunk_tbl, img_meta_tbl, text_tbl  = mongo_db["fs.chunks"], mongo_db["fs.files"], mongo_db["text"]

# # 1. filename으로 file_id 쿼리
# last_file_name=metas[-1]['filename']
# last_file_id = img_meta_tbl.find_one({"filename": last_file_name})['_id']
# # 2. file_id로 chunks(이미지 데이터) 쿼리
# chunks=img_chunk_tbl.find({"files_id":last_file_id})
# # 3. 이미지 출력
# img = b''.join(chunk['data'] for chunk in chunks)
# img_output = Image.open(BytesIO(img))

def get_prompt_from_db(tbl):
    texts=tolist(tbl)
    prompt=texts[-1]['prompt']
    return prompt

def get_image_name_from_db(tbl):
    img_metas=tolist(tbl)
    img_name=img_metas[-1]['filename']
    return img_name