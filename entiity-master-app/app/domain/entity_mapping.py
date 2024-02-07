from pydantic import BaseModel, Field
from typing import Optional

class EntityMappingModel(BaseModel):
           cemh_id: str = Field(..., title="cemh_id", description="CEMH Entity Id", min_length=3, max_length=50)
           src_entity_id: str = Field(..., title="src_entity_id", description="Source Entity Id", min_length=3, max_length=50)
         src_system_id: str = Field(..., title="src_system_id", description="Source System Id", min_length=3, max_length=50)
         src_entity_type_id: str = Field(..., title="src_entity_type_id", description="Source Entity Type id", min_length=3, max_length=50)


class EntityMappingUpdateModel(BaseModel):
           entity_id: str = Field(..., title="entity_id", description="Entity Id", min_length=3, max_length=50)
           src_entity_id: str = Field(..., title="src_entity_id", description="Source Entity Id", min_length=3, max_length=50)
           