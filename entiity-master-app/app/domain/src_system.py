from pydantic import BaseModel, Field
from typing import Optional

class SrcSystemModel(BaseModel):
    src_system_id: str = Field(..., title="src_system_id", description="Source System Id", min_length=3, max_length=50)
    src_system_name: str = Field(default=None, title="src_system_name", description="Source System Name", min_length=3, max_length=50)

class SrcSystemUpdateModel(BaseModel):
    src_system_name: Optional[str] = Field(default=None, title="src_system_name", description="Source System Name", min_length=3, max_length=30)
