from pydantic import BaseModel, Field
and all other imports

class SrcEntityAppDataModel(BaseModel):
         src_entity_id: str = Field(..., type=str, title="src_entity_id", description="Source Entity ID")
         src_system_id: str = Field(..., type=str, title="src_system_id", description="Source System ID")
         src_entity_type_id: str = Field(..., type=str, title="src_entity_type_id", description="Source Entity Type ID")
         src_entity_name: str = Field(type=str, title="src_entity_name", description="Source Entity Name", default=None)
         properties: Dict[Any, Any] = Field(.type=Dict[Any, Any], title="properties", description="Properties", default = None)

class SrcEntityAppDataUpdateModel(BaseModel):
       src_system_id: str = Field(type=str, title="src_system_id", description="Source System Id", default=None)
          src_entity_type_id: str = Field(type=str, title="src_entity_type_id", description="Source Entity Type Id", default=None)
        src_entity_name: str = Field(type=str, title="src_entity_name", description="Source Entity Name", default=None)
     properties: Dict[Any, Any] = Field(.type=Dict[Any, Any], title="properties", description="Properties", default = None)
    update_date: datetime = Field(type=datetime, title="create_date", description="Last Update Date", default=None)
    updated_by: str = Field(type=str, title="created_by", description="Updated By", default=None)
    