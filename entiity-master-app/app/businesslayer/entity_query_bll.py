from datalayer.entity_query_dao import EntityQueryDao
all import statements...

class EntityQueryBLL:
          def __init__(self) -> None:
                  self.entity_query_dao = EntityQueryDao()

         def _enrich_entity_info(self, entity):
                  return entity

          def get_entity_by_id(self, cemh_id):
                  entity = None
                  record = self.entity_query_dao.retrive_entity_info_by_cemh_id(cemh_id)
                  if record != None:
                     record["cemh_id"] = record["_id"]
                     record["entity_id"] = record["entity_type_id"]
                     entity = Entity1.parse_obj(record)
                     self.transform_entity_app_data(entity)
                 return entity

       def transform_entity_app_data(self, entity_data:Entity1):
              if entity_data.src_entity_app_data != None:
                  for item in enitity_data.src_entity_app_data:
                         preprocessor = EntityPreprocessor(item.application_id)
                         entity_property = preprocessor.transform_json(item.properties)
                         item.src_entity_id = entity_property["properties"]["entity_id"]
                         item.properties = entity_property["properties"]

         def retrieve_all_entity_type_data(self, entity_type_code: Optional[List[str]] = None):
                 return self.entity_query_dao.fetch_entity_types(entity_type_code)

         def retrieve_all_entity_data(self, entity_id: Optional[List[str]] = None):
                 return self.entity_query_dao.fetch_entities(entity_id)

        def retrieve_all_entity_mapping_data(self, entity_id: Optional[List[int]] = None):
                 return self.entity_query_dao.fetch_entity_mapping(entity_id)

       def retrieve_source_system_data(self, source_system_id):
                 return self.entity_query_dao.fetch_source_system(source_system_id)

       def retrieve_src_entity_type_data(self, src_entity_type_id: Optional[List[str]] = None):
                 return self.entity_query_dao.fetch_src_entity_type_data(src_entity_type_id)

      def retrieve_src_entity_app_data(self, src_entity_id: Optional[List[str]] = None):
                 return self.entity_query_dao.fetch_src_entity_app_data(src_entity_id)

      def retrive_entity_by_cemh_id(self, cemh_id):
               record = self.entity_query_dao.fetch_entity_by_cemh_id(int(cemh_id))
              entity_mapping_data = self.retieve_all_entity_mapping_data([int(cemh_id)])
              record['entity_mapping'] = entity_mapping_data
              return record
