from datalayer.util import SqlHelper
from domain.internal_event import InternalEvent

SqlHelper = SqlHelper()

def create_internal_event(internal_event: InternalEvent):
        sqlHelper.execute_insert("event_projector.internal_event", internal_event.to_dictionary(). keys(), [internal_event.to_dictionary()])
        