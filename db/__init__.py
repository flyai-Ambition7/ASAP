from pymongo import MongoClient
from dotenv import load_dotenv
import os
from gridfs import GridFS

def get_env(env_list):
    return [os.getenv(env_var) for env_var in env_list]

load_dotenv(verbose=True)
HOST, PORT, DB_NAME, IMAGE_FILE_TABLE_NAME, IMAGE_META_TABLE_NAME, TEXT_TABLE_NAME = get_env(["HOST", 
                                                                                              "PORT", 
                                                                                              "DB_NAME", 
                                                                                              "IMAGE_FILE_TABLE_NAME", 
                                                                                              "IMAGE_META_TABLE_NAME", 
                                                                                              "TEXT_TABLE_NAME"])

client = MongoClient(HOST,int(PORT))
db = client[DB_NAME]
fs = GridFS(db)
img_chunk_tbl=db[IMAGE_FILE_TABLE_NAME]
img_meta_tbl=db[IMAGE_META_TABLE_NAME]
text_tbl=db[TEXT_TABLE_NAME]