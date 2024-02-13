from PIL import Image
from io import BytesIO
from db import client, mongo_db
from gridfs import GridFS

# mongo_db : mongodb 객체
# mongo_db.collections -> fs.files, fs.chunks, user
# mongo_db.fs.files -> _id, filename, chunkSize, length, uploadDate

fs = GridFS(mongo_db)
chunk_docs, meta_docs = mongo_db["fs.chunks"], mongo_db["fs.files"]
chunks, metas = [chunk for chunk in chunk_docs.find()], [doc for doc in meta_docs.find()]
last_meta_doc=metas[-1]

# find(read) generated file by name 
name='xxx_0.jpg'
# 1. name으로부터 file_id 찾기
file_id = meta_docs.find_one({"filename": name})['_id']
# 2. file_id로부터 chunks 찾기
chunks=chunk_docs.find({"files_id":file_id})
# 3. 이미지 출력
img = b''.join(chunk['data'] for chunk in chunks)
img_output = Image.open(BytesIO(img))
img_output.show()  # 이미지를 보여줍니다.