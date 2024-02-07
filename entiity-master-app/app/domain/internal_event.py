import json
from datetime import datetime
from util.cemh_util import generate_random_uuid, get_utc_time
from enum import Enum


class EventType(Enum):
         ENTITY_CREATED = "entity:created"
        ENTITY_UPDATED = "entity:updated"
        ENTITY_DELETED = "entity:deleted"
        DOCUMENT_CREATED = "document:created"
        DOCUMENT_UPDATED = "document:updated"
        DOCUMENT_DELETED = "document:deleted"

   class InternalEvent():
           event_id:str
           correlation_id: str
          event_type: EventType
          event_date: dict
         event_time: datetime

        def __init__(self, event_type:EventType) -> None:
               self.event_id = generate_random_uuid()
               self.correlation_id = generate_random_uuid()
               self.event_time = get_utc_time()
               self.event_type= event_type
               self.event_data = {}
 
      def to_json_string(self) -> str:
              return json.dumps({
                     "event_id": self.event_id,
                     "correlation_id": self.correlation_id,
                     "event_type": self.event_type.value,
                     "event_data": self.event_data,
                     "event_time": str(self.event_time)
})

    def to_dictionary(self) -> dict:
            return {"internal_event_id": self.event_id,
                            "event_data": self.to_json_string(),
                           "create_timestamp" : str(self.event_time)
                         }
