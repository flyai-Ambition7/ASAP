from db import client, mongo_db
from gridfs import GridFS

def update_image(image_bytes,user_id,image_id):
    fs = GridFS(mongo_db)
    fs.put(image_bytes, filename=f'{user_id}_{image_id}.jpg')