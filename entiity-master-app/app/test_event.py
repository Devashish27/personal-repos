from domain.internal_event import InternalEvent, EventType

evt = InternalEvent(event_type=EventType.ENTITY_CREATED)
evt.event_data = {
          "en" : "english"
}
print(evt.to_json_string())
