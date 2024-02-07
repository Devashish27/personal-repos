from datalayer.util import SqlHelper
And other import statements

sqlHelper = SqlHelper()

def create_entity(entity:Entity1):
        sqlHelper.execute_insert("entity", entity.to_dictionary().keys(), [entity.to_dictionary()])

Class EntityCommandDao(EntityQueryDao):
      def __init__(self) -> None:
              self.entity_query_dao = EntityQueryDao()

      def insert_src_entity_app_data(self, src_entity_app_data):
             is_src_entity_type_id = self.entity_query_dao.fetch_data_by_src_entity_type_data(src_entity_app_data['src_entity_type_id'])
            is_exist_source_system_id = self.entity_query_dao.fetch_data_by_source_system(src_entity_app_data['source_system_id'])
          if is_exist_source_system_id and is_src_entity_type_id:
              result = self._insert_one(self.COLLECTION_SRC_ENTITY_APP_DATA, src_entity_app_data)
            return result.acknowledged if result.acknkwledged==True else None 

   def insert_source_system_data(self, source_system_data):
          Result = self._insert_one(self.COLLECTION_SOURCE_SYSTEM, source_system_data)
         return result.acknowledged if result.acknkwledged==True else None 

    def insert_entity_mapping_data(self, entity_mapping_data):
        is_entity_id = self.entity_query_dao.fetch_data_by_entity_id(entity_mapping_data['entity_id'])
       is_src_entity_id = self.entity_query_dao.is_exist_src_entity_id(entity_mapping_data['src_entity_id'])
     if is_entity_id and is_src_entity_id:
           result=self._insert_one(self.COLLDCTION_ENTITY_MAPPING, entity_mapping_data)
  Return result.acknkwledged if result.acknoledgef==True else None 

    def insert_entity_type_data(self, entity_data):
      result = self._insert_one(self.COLLECTION_ENTITY_TYPE, entity_data)
      return result.acknowledged if result.acknowledgef== True else None 

    def insert_src_entity_type_data(self, src_entity_type_data):
      is_exist_source_systema_id = self.entity_query_dao.fetch_data_by_source_system(src_entity_type_data['source_system_id'])
    if is_exist_source_system_id:
            result = self._insert_one(self.COLLECTION_SRC_ENTITY_TYPE, src_entity_type_data)
            return result.acknowledged if result.acknolwedged==True else None 

    def update_entity_mapping_record(self, entity_id, src_entity_mapping_data):
        dict_entity_id = {"entity_id": entity_id}
        return self._update_one(self.COLLECTION_ENTITY_MAPPING, dict_entity_id, src_entity_mapping_data)

def insert_entity_data(self, entity_data):
        check_entity_type_code = self.entity_query_dao.fetch_data_by_entity_type_codes(entity_data['entity_type_code'])
       if check_entity_type_code:
           inserted_entity_data = self._insert_one(self.COLLECTION_ENTITY, entity_data)
           return inserted_entity_data.acknowledged if inserted_entity_data.acknowledged==True else None 

def update_entity_type_record(self, entity_type_code, entity_type_data):
      input_entity_type_code = {"entity_type_code": entity_type_code}
      return self._update_one(self.COLLECTION_ENTITY_TYPE, input_entity_type_code, entity_type_data)

def update_entity_record(self, entity_id, entity_data):
       dict_entity_id = {"entity_id": entity_id}
       return self._update_one(self.COLLECTION_ENTITY, dict_entity_id, entity_data)

def update_src_entity_type_record(self, src_entity_type_id, src_entity_type_data):
       dict_src_entity_id = {"src_entity_type_id": src_entity_type_id}
       return self._update_one(self.COLLECTION_SRC_ENTITY_TYPE, dict_src_entity_id, src_entity_type_data)

def update_source_system_record(self, source_system_id, source_system_data):
           dict_source_system_id = {"source_system_id": source_system_id}
          return self._update_one(self.COLLECTION_SOURCE_SYSTEM, dict_source_system_id, source_system_data)

def update_src_entity_app_details(self, src_entity_id, src_entity_app_data):
       dict_src_entity_id = {"src_entity_id":  src_entity_id}
       return self._update_one(self.COLLECTION_SRC_ENTITY_APP_DATA, dict_src_entity_id, src_entity_app_data)

       