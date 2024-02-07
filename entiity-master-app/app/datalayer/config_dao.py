from datalayer.base_mongodb_dao import BaseMongoDbDao

Class ConfigDao(BaseMongoDbDao):

         def get_etl_config_by_application(self, application_id:str):

         etl_config_collection = self._get_collection(self.COLLECTION_VW_CFG_SRC_ENTITY_ETL)
        For item in etl_config_collection.find({"application_id": application_id}):
          return item 

       raise Exception("No ETL configuration found for application I'd ""{}""". format (application _id))

def get_app_config_by_name(self, config_name):
        etl_config_collection = self._get_collection(self.COLLECTION_CFG_APP)
        for item in etl_config_collection.find({"config_name" : config_name}):
            return item["config_value"]

      raise Exception ("No Application Configuration found for config name ""{}""".format(config_name)) 