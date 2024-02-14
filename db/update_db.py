from db import *
from gridfs import GridFS
import datetime

fs = GridFS(mongo_db)

def update_image(image_bytes,user_id:str,image_id,isinput:bool=False):
    if isinput:
        mode=0
    else:
        mode=1
    fs.put(image_bytes, filename=f'{user_id}_{image_id}_{mode}.jpg')

def update_text(prompt,user_id):
    coll=mongo_db["text"]
    doc={
        "prompt":prompt,
        "user_id":user_id,
        "date":datetime.datetime.now(tz=datetime.timezone.utc)
    }
    coll.insert_one(doc)