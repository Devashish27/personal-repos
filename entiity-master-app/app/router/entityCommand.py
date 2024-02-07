from typing import Union, Dict, Any
from fastapi import APIRouter, Header
from domain.service_response import ServiceResponse
from domain.entity_command_response import CreateEntityResponse
from domain.entity_type import EntityType, EntityTypeUpdate
from domain.entity_mapping import EntityMappingModel, EntityMappingUpdateModel
from domain.entity import EntityModel, EntityUpdateModel
from domain.src_entity_app_data import SrcEntityAppDataModel, SrcEntityAppDataUpdateModel
from domain.src_system import SrcSystemModel, SrcSystemUpdateModel
from domain.src_entity_type import SrcEntityTypeModel, SrcEntityTypeUpdateModel
from businesslayer.entity_command_bll import EntityCommandBll
from router.baseController import BaseController
import logging
import traceback
import sys

class EntityCommandController(BaseController):
         def __init__(self) -> None:
                 self.entity_command_bll = EntityCommandBll()
                self.router = APIRouter()

                self.router.add_api_route("/src_entity_app_data/create",
                         self.create_src_entity_app_data,
                         methods=["POST"],
                         name = "Create New Source Entity App Data",
                         response_model = ServiceResponse[SrcEntityAppDataModel])

                    self.router.add_api_route("/src_entity_app_data/update",
                         self.update_src_entity_app_data,
                         methods=["POST"],
                         name = "Update Exisitng Source Entity App Data",
                         response_model = ServiceResponse[SrcEntityAppDataUpdateModel])

                        self.router.add_api_route("/entity/create",
                         self.create_entity,
                         methods=["POST"],
                         name = "Create New Entity ",
                         response_model = ServiceResponse[EntityModel])

                          self.router.add_api_route("/entity_type/create",
                         self.create_entity_type,
                         methods=["POST"],
                         name = "Create New Entity Type",
                         response_model = ServiceResponse[EntityType])

                              self.router.add_api_route("/entity_mapping/create",
                         self.create_entity_mapping,
                         methods=["POST"],
                         name = "Create New Entity Mapping",
                         response_model = ServiceResponse[EntityMappingModel])

                       self.router.add_api_route("/entity_mapping/update",
                         self.create_entity_mapping,
                         methods=["POST"],
                         name = "Update Existing Entity Mapping",
                         response_model = ServiceResponse[EntityMappingUpdateModel])

                         self.router.add_api_route("/src_entity_type/create",
                         self.create_src_entity_type,
                         methods=["POST"],
                         name = "Create New Source Entity Type",
                         response_model = ServiceResponse[SrcEntityTypeModel])
           
                        self.router.add_api_route("/src_entity_type/update",
                         self.update_src_entity_type,
                         methods=["POST"],
                         name = "Update Existing Source Entity Type",
                         response_model = ServiceResponse[SrcEntityTypeUpdateModel])

                        self.router.add_api_route("/entity_type/update",
                         self.update_entity_type,
                         methods=["POST"],
                         name = "Update Existing Entity Type",
                         response_model = ServiceResponse[EntityTypeUpdate])
 
                        self.router.add_api_route("/entity/update",
                         self.update_entity,
                         methods=["POST"],
                         name = "update Existing Entity",
                         response_model = ServiceResponse[EntityUpdateModel])

                        self.router.add_api_route("/src_system/create",
                         self.create_source_system,
                         methods=["POST"],
                         name = "Create New Source System",
                         response_model = ServiceResponse[SrcSystemModel])

                       self.router.add_api_route("/src_system/update",
                         self.update_source_system,
                         methods=["POST"],
                         name = "Update Existing Source System",
                         response_model = ServiceResponse[SrcSystemUpdateModel])

        @BaseController.methodLogger
          def create_entity_type(self, entity_data:Dict[Any, Any], entity_type_code: str, entity_type_name: str, sm_user: Union[str, None] = Header(default=None, convert_underscores=False, include_in_schema=False)) -> ServiceResponse[EntityType]:
                 entity_type_result = self.entity_command_bll.create_entty_type_data(entity_data, entity_type_code, entity_type_name)
             return entity_type_result

       @BaseController.methodLogger
          def create_src_entity_type(self, src_entity_data:Dict[Any, Any], src_entity_type_id: str, source_id: str, src_entity_type_name: str, sm_user: Union[str, None] = Header(default=None, convert_underscores=False, include_in_schema=False)) -> ServiceResponse[SrcEntityTypeModel]:
                 src_entity_type_result = self.entity_command_bll.create_src_entty_type_data(src_entity_data, src_entity_type_id, source_id, src_entity_type_name)
             return src_entity_type_result

       @BaseController.methodLogger
          def create_entity(self, entity_data:EntityModel, sm_user: Union[str, None] = Header(default=None, convert_underscores=False, include_in_schema=False)) -> ServiceResponse[EntityModel]:
                 entity_result = self.entity_command_bll.create_entty_data(entity_data)
             return entity_result

       @BaseController.methodLogger
          def create_src_entity_app_data(self, src_entity_data:SrcEntityAppDataModel, sm_user: Union[str, None] = Header(default=None, convert_underscores=False, include_in_schema=False)) -> ServiceResponse[SrcEntityAppDataModel]:
                 src_entity_app_data_result = self.entity_command_bll.insert_src_entity_app_data(src_entity_app_data)
             return src_entity_app_data_result

       @BaseController.methodLogger
          def update_entity_type(self, entity_type_code: str, entity_type_data: EntityTypeData, sm_user: Union[str, None] = Header(default=None, convert_underscores=False, include_in_schema=False)) -> ServiceResponse[EntityTypeUpdate]:
                 entity_type_response = self.entity_command_bll.update_entty_type_data(entity_type_code, entity_type_data)
             return entity_type_response

       @BaseController.methodLogger
          def update_entity(self, entity_id: str, entity_data: EntityUpdateModel, sm_user: Union[str, None] = Header(default=None, convert_underscores=False, include_in_schema=False)) -> ServiceResponse[EntityUpdateModel]:
                 entity_response = self.entity_command_bll.update_entity_data(entity_id, entity_data)
             return entity_response

       @BaseController.methodLogger
          def update_src_entity_app_data(self, src_entity_id : str, src_entity_app_record: SrcEntityAppDataUpdateModel, sm_user: Union[str, None] = Header(default=None, convert_underscores=False, include_in_schema=False)) -> ServiceResponse[SrcEntityAppDataUpdateModel]:
                 src_entity_app_data_response = self.entity_command_bll.update_src_entity_app_record(src_entity_id, src_entity_app_record)
             return src_entity_app_data_response

       @BaseController.methodLogger
          def update_src_entity_type(self, src_entity_type_id: str, src_entity_type_data: SrcEntityTypeUpdateModel, sm_user: Union[str, None] = Header(default=None, convert_underscores=False, include_in_schema=False)) -> ServiceResponse[SrcEntityTypeUpdateModel]:
                 entity_response = self.entity_command_bll.update_src_entity_type_data(src_entity_type_id, src_entity_type_data)
             return entity_response

       @BaseController.methodLogger
          def create_source_system(self, source_system_data:Dict[Any, Any], source_system_id: str, source_system_name: str, sm_user: Union[str, None] = Header(default=None, convert_underscores=False, include_in_schema=False)) -> ServiceResponse[SrcSystemModel]:
                 source_system_result = self.entity_command_bll.create_source_system_data(source_system_data, source_system_id, source_system_name)
             return source_system_result

       @BaseController.methodLogger
          def update_source_system(self, source_system_id: str, source_system_data: SrcSystemUpdateModel, sm_user: Union[str, None] = Header(default=None, convert_underscores=False, include_in_schema=False)) -> ServiceResponse[SrcSystemUpdateModel]:
                 entity_response = self.entity_command_bll.update_source_system_data(source_system_id, source_system_data)
             return entity_resoinse

   @BaseController.methodLogger
          def create_entity_mapping(self, entity_id: str, src_entity_id: str, entity_mapping_data: Dict[Any, Any], sm_user: Union[str, None] = Header(default=None, convert_underscores=False, include_in_schema=False)) -> ServiceResponse[EntityMappingModel]:
                 entity_response = self.entity_command_bll.create_entity_mapping_data(entity_id, src_entity_id, entity_mapping_data)
             return entity_resoinse

   @BaseController.methodLogger
          def update_entity_mapping(self, entity_id: str, entity_mapping_data: EntityMappingUpdateModel, sm_user: Union[str, None] = Header(default=None, convert_underscores=False, include_in_schema=False)) -> ServiceResponse[EntityMappingUpdateModel]:
                 entity_response = self.entity_command_bll.update_entity_mapping_data(entity_id, entity_mapping_data)
             return entity_response


