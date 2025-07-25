import sys

from usa_visa.exception import AydieException
from usa_visa.logger import logging

import os
from usa_visa.constants import DATABASE_NAME, MONGODB_URL_KEY
import pymongo
import certifi

ca = certifi.where()

class MongoDBClient:
    client = None
    
    def __init__(self, database_name = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f'Environment Key: mongo_db_url is not set')
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile = ca)
                
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection succesfull")               
                
        except Exception as e:
            raise AydieException(e, sys)