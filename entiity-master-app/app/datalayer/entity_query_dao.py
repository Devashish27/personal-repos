from datalayer.util import QueryHelper
from datalayer.base_mongodb_dao import BaseMongoDbDao
from domain.entity1 import Entity1, BasicERnityInfo
from domain.entity import EntityModel
from domain.src_entity_type import SrcEntityTypeModel
from domain.src_system import SrcSystemModel
from domain.src_entity_app_data import SrcEntityAppDataModel
from domain.entity_type import EntityType
from domain.entity_mapping import EntityMappingModel
from typing import List

from bson import ObjectId

class EntityQueryDao(BaseMongoDbDao):
      def fetch_src_entity_app_data(self, src_entity_id) -> List[SrcEntityAppDataModel]:
              src_entity_id = {"src_entity_id" : {"$in": src_entity_id}} if src_entity_id else {}
              return self._find(self.COLLECTION_SRC_ENTITY_APP_DATA, src_entity_id)

       def fetch_src_entity_type_data(self, src_entity_type_id) -> List[SrcEntityTypeModel]:
              src_entity_type_id = {"src_entity_type_id" : {"$in": src_entity_type_id}} if src_entity_type_id else {}
              return self._find(self.COLLECTION_SRC_ENTITY_TYPE, src_entity_type_id)

     def fetch_source_systems(self, source_system_id) -> List[SrcSystemModel]:
              source_system_id = {"source_system_id" : {"$in": source_system_id}} if source_system_id else {}
              return self._find(self.COLLECTION_SOURCE_SYSTEM, source_system_id)

def fetch_entity_mappings(self, entity_ids) -> List[EntityMappingModel]:
              entity_ids = {"cemh_id" : {"$in": entity_ids}} if entity_ids else {}
              return self._find(self.COLLECTION_ENTITY_MAPPING, entity_ids)

def fetch_entity_types(self, entity_type_code) -> List[EntityType]:
              entity_type_codes = {"entity_type_code" : {"$in": entity_type_code}} if entity_type_code else {}
              return self._find(self.COLLECTION_ENTITY_TYPE, entity_type_codes)

def fetch_entities(self, entity_ids) -> List[EntityModel]:
              entity_ids= {"entity_id" : {"$in": entity_ids}} if entity_ids else {}
              return self._find(self.COLLECTION_ENTITY, entity_ids)

def fetch_src_entity_app_data(self, src_entity_id) -> List[SrcEntityAppDataModel]:
              src_entity_id = {"src_entity_id" : {"$in": src_entity_id}} if src_entity_id else {}
              return self._find(self.COLLECTION_SRC_ENTITY_APP_DATA, src_entity_id)

def is_exist_src_entity_id(self, src_entity_id) -> SrcEntityAppDataModel:
              return self._find_one(self.COLLECTION_SRC_ENTITY_APP_DATA, {"src_entity_id": src_entity_id})

def fetch_data_by_source_system(self, source_system_id) -> SrcSystemModel:
              return self._find_one(self.COLLECTION_SOURCE_SYSTEM, {"source_system_id": source_system_id})

def fetch_data_by_entity_type_codes(self, entity_type_code) -> EntityType:
              return self._find_one(self.COLLECTION_ENTITY_TYPE, {"entity_type_code": entity_type_code})

def fetch_data_by_src_entity_type_data(self, src_entity_type_id) -> SrcEntityTypeModel:
              return self._find_one(self.COLLECTION_SRC_ENTITY_TYPE, {"src_entity_type_id": src_entity_type_id})

def retrieve_entity_info_by_cemh_id(self, cemh_id) -> Entity1:
       return self._find_one(self.COLLECTION_ENTITY_TYPE, {"_id": cemh_id})

def retrieve_entity_by_cemh_id(self, cemh_id) -> Entity1:
       return self._find_one(self.COLLECTION_ENTITY_TYPE, {"_id": cemh_id})

def fetch_entity_by_cemh_id(self, cemh_id) -> BasicEnityInfo:
       return self._find_one(self.COLLECTION_ENTITY, {"cemh_id": cemh_id})
