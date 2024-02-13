from PIL import Image
from io import BytesIO
from pymongo import MongoClient
from db import client, mongo_db
from gridfs import GridFS
fs = GridFS(mongo_db)
print(mongo_db.list_collection_names())
chunk_docs, meta_docs = mongo_db["fs.chunks"], mongo_db["fs.files"]
metas=[doc for doc in meta_docs.find()]
file=metas[-1]
print(file)

# chunks=[doc for doc in chunk_docs.find()]
# print(chunks)
# for doc in docs:
    # print(doc)

# name='yaong_0.jpg'
# file_id = meta_docs.find_one({"filename": name})['_id']
# chunks=chunk_docs.find({"files_id":file_id})
# img=b''
# for chunk in chunks:
#     img+=chunk['data']
# print(img)
# result = Image.open(BytesIO(img))
# result.show()  # 이미지를 보여줍니다.