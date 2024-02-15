from db import *
from gridfs import GridFS
import datetime

fs = GridFS(mongo_db)

def update_image_to_db(image_bytes,user_id:str,upload_time,isinput:bool=False):
    if isinput:
        mode=0
    else:
        mode=1
    fs.put(image_bytes, filename=f'{user_id}_{upload_time}_{mode}.jpg')

def update_text_to_db(prompt,user_id):
    coll=mongo_db["text"]
    doc={
        "prompt":prompt,
        "user_id":user_id,
        "date":datetime.datetime.now(tz=datetime.timezone.utc)
    }
    coll.insert_one(doc)