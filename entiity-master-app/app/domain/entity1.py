from pydantic import BaseModel, Field, ConfigDict
and all other imports

class Entity1(BaseModel):

           __name__ = "Entity1"

           cemh_id:str = Field(type=str, title="cemh_id", alias="cemh_id", description="CEMH Id", default=None)
           entity_name: str = Field(type=str, title="entity_name", description="CEMH Entity Name", default=None)
           cemh_entity_type_id: str = Field(type=str, title="cemh_entity_type_id", description="CEMH Entity Type Id", default=None)
           src_entity_app_data: SrcEntityAppDataModel = Field(title="src_entity_app_data", description="Entity Property", default=None)
           create_date: datetime = Field(type=datetime, title="create_date", description="Creation date", default=None)
           created_by: str = Field(type=str, title="created_by", description="Created By", default=None)
           update_date: datetime = Field(type=datetime, title="create_date", description="Last Update Date", default=None)
           updated_by: str = Field(type=str, title="created_by", description="Updated By", default=None)

class BasicEnityInfo(BaseModel):
                 __name__ = "BasicEnityInfo"

           cemh_id:str = Field(type=str, title="cemh_id", alias="cemh_id", description="CEMH Id", default=None)
           entity_name: str = Field(type=str, title="entity_name", description="CEMH Entity Name", default=None)
           cemh_entity_type_id: str = Field(type=str, title="cemh_entity_type_id", description="CEMH Entity Type Id", default=None)
           entity_mapping: List[EntityMappingModel] = Field(title="entity_mapping", description="Entity Mapping", default=None)
           create_date: datetime = Field(type=datetime, title="create_date", description="Creation date", default=None)
           created_by: str = Field(type=str, title="created_by", description="Created By", default=None)
           update_date: datetime = Field(type=datetime, title="create_date", description="Last Update Date", default=None)
           updated_by: str = Field(type=str, title="created_by", description="Updated By", default=None)

