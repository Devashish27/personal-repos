from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class EntityModel(BaseModel):
           entity_id:str = Field(..., title="entity_id", description="Entity Id")
           entity_type_code: str = Field(..., title="entity_type_code", description="Entity Type Code")
           entity_name: str = Field(default=None, title="entity_name", description="Entity Name", min_length=3, max_length=50)
           Create_date: datetime = Field(..., title="create_date", description="Create Date")
           created_by: str = Field(default=None, title="created_by", description="Created By", min_length=3, max_length=30)
           update_date:Optional[datetime] = Field(default=None, title="update_date", description="Updated Date")
           updated_by: Optional[str] = Field(default=None, title="updated_by", description="Updated_by", min_length=3, max_length=30)

class EntityUpdateModel(BaseModel):
           entity_name: str = Field(default=None, title="entity_name", description="Entity Name", min_length=3, max_length=50)
            update_date:Optional[datetime] = Field(default=None, title="update_date", description="Updated Date")
           updated_by: Optional[str] = Field(default=None, title="updated_by", description="Updated_by", min_length=3, max_length=30)

