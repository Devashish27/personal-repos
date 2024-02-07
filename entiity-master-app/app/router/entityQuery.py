from fastapi import APIRouter, Header, Query
from domain.service_response import ServiceResponse
from router.baseController import BaseController
from pydantic import schema
from typing import List, Union, Optional
from domain.entity1 import Entity1, BasicEntityInfo
from domain.entity_mapping import EntityMappingModel
from domain.entity import EntityModel
from domain.src_entity_type import SrcEntityTypeModel
from domain.src_system import SrcSystemModel
from domain.entity_type import EntityType
from domain.src_entity_app_data import SrcEntityAppDataModel
from datalayer.entity_query_dao import EntityQueryDao
from businesslayer import entity_query_bll

class EntityQueryController(BaseController):

           def __init__(self) -> None:
                   self._entityQueryBll = entity_query_bll.EntityQueryBLL()
                   self._entityQueryDao = EntityQueryDao()

                  self.router = APIRouter()
                 self.router.add_api_router("/id/{cemh_id}",
                        self.get_entity_by_cemh_id,
                        methods=["GET"],
                         name="Get entity by CEMH ID",
                        response_model=ServiceResponse[BasicEntityInfo])

                 self.router.add_api_router("/id/{src_system_id}/{src_entity_type}/{src_entity_id}",
                        self.get_entity_source_system_id,
                        methods=["GET"],
                         name="Get entity by Source System, Source Entity Type, Source System ID",
                        response_model=ServiceResponse[BasicEntityInfo])

             self.router.add_api_router("/src-system/data/{cemh_id}/{src_system}",
                        self.get_entity_source_system_id,
                        methods=["GET"],
                         name="Get entity data by CEMH ID and Source System",
                        response_model=ServiceResponse[Entity1])

            self.router.add_api_router("/src-system/data/{src_system_id}/{src_entity_type}/{src_entity_id}",
                        self.get_entity_source_system_id,
                        methods=["GET"],
                         name="Get entity data by Source System, Source Entity Type, Source System ID",
                        response_model=ServiceResponse[Entity1])

        self.router.add_api_router("/static-data/src-system/list",
                        self.list_all_src_system_data,
                        methods=["GET"],
                         name="Get all CEMH Source System",
                        response_model=ServiceResponse[List[SrcSystemModel]])

        self.router.add_api_router("/static-data/cemh_entity-type/list",
                        self.list_all_entity_types,
                        methods=["GET"],
                         name="Get All CEMH Entity Types",
                        response_model=ServiceResponse[List[EntityType]])

       self.router.add_api_router("/static-data/src-entity-type/list",
                        self.list_src_entity_type,
                        methods=["GET"],
                         name="Get All CEMH Source Entity Types",
                        response_model=ServiceResponse[List[SrcEntityTypeModel]])

      self.router.add_api_router("/static-data/entity/list",
                        self.list_all_entities,
                        methods=["GET"],
                         name="Get All CEMH Entites",
                        response_model=ServiceResponse[List[EntityModel]])

        self.router.add_api_router("/static-data/entity-mapping/list",
                        self.list_all_entity_mappings,
                        methods=["GET"],
                         name="Get All CEMH Entity Mappings",
                        response_model=ServiceResponse[List[EntityMappingModel]])

            self.router.add_api_router("/static-data/src_entity_app_data/list",
                        self.list_src_entity_app_data,
                        methods=["GET"],
                         name="Get All CEMH Source Entity Types",
                        response_model=ServiceResponse[List[SrcEntityAppDataModel]])

         def get_entity_source_system_id(self, src_system_id:str, src_id: str):
                     pass

          def list_src_entity_app_data(self, src_entity_id: List[str] = Query(None, description="Source Entity Id(optional)"),
                 sm_user: Union[str, None] = Header(default=None, convert_underscores=False, include_in_schema=False)) -> ServiceResponse[List[SrcEntityAppDataModel]]:
               return ServiceResponse[List[SrcEntityAppDataModel]](data=self._entityQueryBll.retrieve_src_entity_app_data(src_entity_id), statusCode=200, statusMessage="OK")

         @BaseController.methodLogger
             def list_src_entity_type(self, src_entity_type_id: List[str] = Query(None, description="Source Entity Type Id(optional)"),
                 sm_user: Union[str, None] = Header(default=None, convert_underscores=False, include_in_schema=False)) -> ServiceResponse[List[SrcEntityTypeModel]]:
               return ServiceResponse[List[SrcEntityTypeModel]](data=self._entityQueryBll.retrieve_src_entity_type_data(src_entity_type_id), statusCode=200, statusMessage="OK")

            @BaseController.methodLogger
             def list_all_src_system_data(self, src_system_id: List[str] = Query(None, description="Source System Id(optional)"),
                 sm_user: Union[str, None] = Header(default=None, convert_underscores=False, include_in_schema=False)) -> ServiceResponse[List[SrcSystemModel]]:
               return ServiceResponse[List[SrcSystemModel]](data=self._entityQueryBll.retrieve_source_system_data(src_system_id), statusCode=200, statusMessage="OK")

           @BaseController.methodLogger
             def list_all_entity_mappings(self, entity_id: List[int] = Query(None, description="Entity Id(optional)"),
                 sm_user: Union[str, None] = Header(default=None, convert_underscores=False, include_in_schema=False)) -> ServiceResponse[List[EntityMappingModel]]:
               return ServiceResponse[List[EntityMappingModel]](data=self._entityQueryBll.retrieve_all_entity_mapping_data(entity_id), statusCode=200, statusMessage="OK")

           @BaseController.methodLogger
             def list_all_entites(self, entity_id: List[str] = Query(None, description="Entity Id(optional)"),
                 sm_user: Union[str, None] = Header(default=None, convert_underscores=False, include_in_schema=False)) -> ServiceResponse[List[EntityModel]]:
               return ServiceResponse[List[EntityModel]](data=self._entityQueryBll.retrieve_all_entity_data(entity_id), statusCode=200, statusMessage="OK")

         @BaseController.methodLogger
             def list_all_entity_types(self, entity_type_codes: List[str] = Query(None, description="Entity Type code(optional)"),
                 sm_user: Union[str, None] = Header(default=None, convert_underscores=False, include_in_schema=False)) -> ServiceResponse[List[EntityType]]:
               return ServiceResponse[List[EntityType]](data=self._entityQueryBll.retrieve_all_entity_type_data(entity_type_codes), statusCode=200, statusMessage="OK")

          @BaseController.methodLogger
             def get_entity_by_cemh_id(self, cemh_id,
                 sm_user: Union[str, None] = Header(default=None, convert_underscores=False, include_in_schema=False)) -> ServiceResponse[BasicEntityInfo]:
               return ServiceResponse[BasicEntityInfo](data=self._entityQueryBll.retrieve_entity_by_cemh_id(cemh_id), statusCode=200, statusMessage="OK")
