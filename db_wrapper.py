import os 
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

uri = os.getenv('MONGODB_URI')
class DBWrapper:
    def __init__(self):
        self.client = MongoClient(uri)
        self.db = self.client['air']
        self.collection = self.db['air']

    def insert_data(self, data):
        self.collection.insert_one(data)