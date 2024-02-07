from abc import ABC

class BaseJsonMapper(ABC):
            def map_json_to_object(self, record:dict):
                    for key in record.keys():
                          if hasattr(self, key):
                                   setattr(self, key, record[key])
                   return self
                   