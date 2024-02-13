from PIL import Image
from io import BytesIO
from db import client, mongo_db
from gridfs import GridFS

# mongo_db : mongodb 객체
# mongo_db.collections -> fs.files, fs.chunks, user
# mongo_db.fs.files -> _id, filename, chunkSize, length, uploadDate

fs = GridFS(mongo_db)
chunk_table, meta_table = mongo_db["fs.chunks"], mongo_db["fs.files"]
chunks, metas = [chunk for chunk in chunk_table.find()], [doc for doc in meta_table.find()]
last_file_name=metas[-1]['filename']

'''
find(read) generated file by name
'''
# 1. name으로부터 file_id 찾기
file_id = meta_table.find_one({"filename": last_file_name})['_id']
# 2. file_id로부터 chunks 찾기
chunks=chunk_table.find({"files_id":file_id})
# 3. 이미지 출력
img = b''.join(chunk['data'] for chunk in chunks)
img_output = Image.open(BytesIO(img))
img_output.show()  # 이미지를 보여줍니다.