rom pymongo import MongoClient

import asyncio
from util.logger import Logger

logger = Logger().getLogger()

class BaseMongoDbDao:

          CLIENT = MongoClient("mongodb://10.43.33.17:27017/")

          DB_CEMH = CLIENT["cemh"]

          COLLECTION_CFG_ENTITY_ATTRIBUTE = "config_entity_attribute"
          COLLECTION_CFG_SRC_ENTITY_ETL = "config_src_entity_etl"
          COLLECTION_CFG_APP = "config_app"
          COLLECTION_CFG_GOLDEN_DATA_ETL = "config_golden_data_etl"
          COLLECTION_ENTITY = "entity"
          COLLECTION_ENTITY_MAPPING = "entity_mapping"
          COLLECTION_SRC_ENTITY_TYPE = "src_entity_type"
          COLLECTION_SRC_ENTITY_APP_DATA = "src_entity_app_data"
          COLLECTION_ENTITY_TYPE = "entity_type"
          COLLECTION_SOURCE_SYSTEM = "source_system"

          entyty_type_collection = DB_CEMH[COLLECTION_ENTITY_TYPE]
          entyty_type_collection.create_index([("cemh_entity_type_id")], unique=True, sparse=False)

          entyty_collection = DB_CEMH[COLLECTION_ENTITY]
          entyty_collection.create_index([("cemh_id")], uniwue=True, sparse=False)
          entyty_collection.create_index([("cemh_entity_type_id")], sparse=False)

          src_entyty_type_collection = DB_CEMH[COLLECTION_SRC_ENTITY_TYPE]
          src_entyty_type_collection.create_index([("src_entity_type_id")], unique=True, sparse=False)
          src_entyty_type_collection.create_index([("src_entity_id")], sparse=False)

         source_system_collection = DB_CEMH[COLLECTION_SOURCE_SYSTEM]
         source_system_collection.create_index([("source_system_id")], unique=True, sparse=False)

        src_entity_app_data_collection = DB_CEMH[COLLECTION_SRC_ENTITY_APP_DATA]
        src_entity_app_data_collection.create_index([("src_entity_id")], unique=True, sparse=False)

        def __get_client(self):
                return self.CLIENT

        def __get_database(self):
                 return self.__get_client()[self.DB_CEMH.name]

        def _get_collection(self, collection_name:str):
                 return self.__get_database()[collection_name]

        def _insert_one(self, collection_name, data):
                return self._get_collection(collection_name).insert_one(data)

         def _find_one(self, collection_name, filter):
                  response = self._get_collection(collection_name).find_one(filter)
                  if response:
                      response.pop("_id", None)
                  return response

         def _find(self, collection_name, filter, filter2=None):
                  entity_types=[]
                  list_entity_types = self._get_collection(collection_name).find(filter)
                  for entity_type in list(list_entity_types):
                         entity_type.pop("_id", None)
                         entity_types.append(entity_type)

                 return entity_types

           def _update_one(self, collection_name, input_filter, filter):
                   updated_record = self._get_collection(collection_name).find_one_and_update(input_filter, {"$set":filter}, return_document=True)
                   if updated_record:
                          updated_record.pop("_id", None)
                  return updated_record

          def _exist_one(self, collection_name, filter):
                   is_exist = self._get_collection(collection_name).find_one({filter: {"$exists": True}})

