import sys
from typing import Optional

from usa_visa.configuration.mongo_db_connection import MongoDBClient
from usa_visa.constants import DATABASE_NAME
from usa_visa.exception import AydieException
import pandas as pd
import numpy as np


class USvisaData:
    """
        This class helps us to export entire MongoDB record into pandas dataframe.
    """
    
    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name = DATABASE_NAME)
        except Exception as e:
            raise AydieException(e, sys)
        
        
    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            if database_name:
                collection = self.mongo_client[database_name][collection_name]
            else:
                collection = self.mongo_client.database[collection_name]
                 
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.tolist():
                df = df.drop(columns=['_id'], axis = 1)
            df.replace({"na":np.nan}, inplace = True)
            return df
            
        except Exception as e:
            raise AydieException(e, sys)                