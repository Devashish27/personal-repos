import uuid
import pytz
from datetime import datetime

def generate_random_uuid() -> str:
          return str(uuid.uuid4())

def get_utc_time() -> datetime:
        return datetime.now(pytz.UTC)
        