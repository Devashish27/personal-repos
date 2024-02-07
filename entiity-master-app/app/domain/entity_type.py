from pydantic import BaseModel, Field
from typing import Optional

class EntityType(BaseModel):
           entity_type_code: str = Field(..., title="entity_type_code", description="Entity Type Code", min_length=3, max_length=50)
           entity_type_name: str = Field(default=None, title="entity_type_name", description="Entity Type Name", min_length=3, max_length=50)

class EntityTypeUpdate(BaseModel):
           entity_type_name: Optional[str] = Field(default=None, title="entity_type_name", description="Entity Type Name", min_length=3, max_length=30)