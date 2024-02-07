import json 
and other import commands

class EntityPreprocessor:

          def __init__(self, application) -> None:
                   self.application = application
                   self.config_dao = ConfigDao()

          def get_data_transformer(self):
                  etl_config = self.config_dao.get_etl_config_by_application(self.application)
                  return etl_config['transform_config']

          def update_json_value(self, json_data: json, json_path: str, new_value):
                  json_exp = jsonpath.parse(json_path)
                  json_exp.update_or_create(json_data, new_value)

          def get_entity_property_structure(self, application_id, cemh_id=None):
                  template = self.config_dao.get_app_config_by_name("src_entity_app_data_template")
                 template["_id"] = cemh_id
                 template["application_id"] = application_id
                 template["create_date"] = get_utc_time()
                 return template

          def get_json_values(self, json_object, json_path):
                  result = []
                 exp = jsonpath.parse(json_path)
                 for match in exp.find(json_object):
                         result.append(match.value)
                return result

           def get_src_json_collection_value(self, json_data, src_json_path):
                    result = []
                     values = self.get_json_values(json_data, src_json_path)
                    if len(values) != 0:
                          for match in values:
                               for key in match.keys():
                                       result.append(match[key]['properties'])
                          return result
                    else:
                          return None

           def get_src_json_single_value(self, json_data, src_json_path):
                  values = self.get_json_values(json_data, src_json_path)
                  if len(values) != 0:
                       for match in self.get_json_values(json_data, src_json_path):
                              return match
                  else:
                       return None

         def transform_json(self, json_data, cemh_id = None):
                  entity_property_json = self.get_entity_property_structure(self.application, cemg_id)
                   for config_item in self.get_data_transformer():
                          if config_item["source_attribute_type"] == "collection":
                                value = self.get_src_json_collection_value(json_data, config_item["source_json_path"] )
                          elif config_item["source_attribute_type"] == "single":
                                    value = self.get_src_json_single_value(json_data, config_item["source_json_path"] )

                        if value == None and config_item["required"]:
                            raise Exception("Validation failure. Entity property name {} is required but is nt supplied".format(
                                  config_item["attribute_name"]
                       ))

                else:
                          self.update_json_value(entity_property_json,
                                                                  config_item["target_json_path"],
                                                                   value)

return entity_property_json
