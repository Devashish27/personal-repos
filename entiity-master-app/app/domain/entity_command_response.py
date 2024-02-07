rom pydantic import BaseModel, Field
from domain.entity1 import Entity1

class BaseEventTracker(BaseModel):
            __name__ = "BaseEventTracker"
             correlation_id: str = Field(type=str, title="correlation_id", description="The vent correlation ID for this request", default=None)

class CreateEntityResponse(BaseEventTracker, Entity1):
           __name__ = "CreateEntityResponse"

           def set_entity(self, entity:Entity1):
                   self.cemh_id = entity.cemh_id
                   self.cemh_entity_name = entity.cemh_entity_name
                   self.cemh_entity_type = entity.cemh_entity_type
                   self.entity_app_data = entity.entity_app_data
                   return self
                   