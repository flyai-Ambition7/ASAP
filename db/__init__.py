from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv(verbose=True)
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DB_NAME = os.getenv("DB_NAME")

client = MongoClient(HOST,int(PORT))
mongo_db = client[DB_NAME]