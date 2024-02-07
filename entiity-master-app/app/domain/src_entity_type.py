from pydantic import BaseModel, Field
other import statements

class SrcEntityTypeModel(BaseModel):
           src_entity_type_id: str = Field(..., title="src_entity_type_id", description="Source Entity Type Id", min_length=3, max_length=50)
             src_system_id: str = Field(..., title="src_system_id", description="Source system Id", min_length=3, max_length=50)
     src_entity_type_name: str = Field(.default=None, title="src_entity_type_name", description="Source Entity Type Name", min_length=3, max_length=50)

class SrcEntityTypeUpdateModel(BaseModel):
       src_entity_type_name: str = Field(default=None, title+"src_entity_type_name", description="Source Entity Type Name", min_length=3, max_length=50)
       