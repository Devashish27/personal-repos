from datalayer.entity_command_dao import EntityCommandDao
all other import statements...

class EntityCommandBll:

            def __init__(self) -> None:
                   self.logger = Logger().getLogger()
                   self.entity_command_dao = EntityCommandDao()
                   self.config_dao = ConfigDao()

           def update_src_entity_type_data(self, src_entity_type_id, src_entity_type_data):
                   response = ServiceResponse[SrcEntityTypeUpdateModel]()
                   try:
                       updated_src_entity_data = self.entity_command_dao.update_src_entity_type_record(src_entity_type_id, src_entity_type_data.dict())

                  response.data = updated_src_entity_data
                  response.statusCode = 200
                  response.statusMessage = "Source Entity type Document Updated Successfully!"

              except Exception as ex:
                           self.logger.exception(ex)
                           response.statusCode = 500
                           response.statusMessage = "Error in processing request. \nReason:{}". format(str(ex))
                           response.data = None
            return response

        def update_src_entity_app_record(self, src_entity_id, src_entity_app_data):
                response = ServiceResponse[SrcEntityAppDataUpdateModel]()
                try:
                     updated_src_entity_app_data = self.entity_command_dao.update_src_entity_app_details(src_entity_id, src_entity_app_data.dict())

                   response.data = updated_src_entity_app_data
                  response.statusCode = 200
                 response.statusMessage = "Source Entity App Data Document Updated Successfully!"
         
           except Exception as ex:
                      self.logger.exception(ex)
                      response.statusCode = 500
                     response.statusMessage = "Error in processing request. \nReason:{}".format(str(ex))
                     response.data = None
           return response

    def update_entity_data(self, entity_id, entity_data):
            response = ServiceResponse[EntityUpdateModel]()
            try:
                 updated_entity = self.entity_command_dao.update_entity_record(entity_id, entity_data.dict())
                response.data = updated_entity
                response.statusCode = 200
                response.statusMessage = "Entity Document Updated Successfully!!"

           except Excution as ex:
                 self.logger.exception(ex)
                 response.statusCode = 500
                 response.statusMessage = "Error in processing request. \n Reason:{}".format(str(ex))
                 response.data = None

          return response

     def update_source_system_data(self, source_system_id, source_system_data):
              response = ServiceResponse[SrcSystemUpdateModel]()
            try:
                 updated_source_system = self.entity_command_dao.update_source_system_record(source_system_id, source_system_data.dict())
                response.data = updated_source_system
                response.statusCode = 200
                response.statusMessage = "Source System Document Updated Successfully!!"

           except Excution as ex:
                 self.logger.exception(ex)
                 response.statusCode = 500
                 response.statusMessage = "Error in processing request. \n Reason:{}".format(str(ex))
                 response.data = None

          return response

      def update_entity_mapping_data(self, entity_id, entity_mapping_data):
              response = ServiceResponse[SrcSystemUpdateModel]()
            try:
                 updated_entity_mapping_data = self.entity_command_dao.update_entity_mapping_record(entity_id, entity_mapping_data.dict())
                response.data = updated_entity_mapping_data
                response.statusCode = 200
                response.statusMessage = "Entity Mapping Document Updated Successfully!!"

           except Excution as ex:
                 self.logger.exception(ex)
                 response.statusCode = 500
                 response.statusMessage = "Error in processing request. \n Reason:{}".format(str(ex))
                 response.data = None

          return response

      def update_entity_type_data(self, entity_type_code, entity_data):
              response = ServiceResponse[EntityTypeUpdate]()
            try:
                 updated_entity_type = self.entity_command_dao.update_entity_type_record(entity_type_code, entity_data.dict())
                response.data = updated_entity_type
                response.statusCode = 200
                response.statusMessage = "Entity Type Document Updated Successfully!!"

           except Excution as ex:
                 self.logger.exception(ex)
                 response.statusCode = 500
                 response.statusMessage = "Error in processing request. \n Reason:{}".format(str(ex))
                 response.data = None

          return response

        def create_entity_mapping_data(self, entity_id, src_entity_id, entity_mapping_data):
              response = ServiceResponse[EntityMappingModel]()
            try:
                  entity_,mapping_data['entity_id'] = entity_id
                   entity_mapping_data['src_entity_id'] = src_entity_id

                 entity_mapping_result = self.entity_command_dao.insert_entity_mapping_data(entity_mapping_data)
                response.data = entity_mapping_result
                response.statusCode = 500 if entity_mapping_result == None else 200
                response.statusMessage = "Entity Mapping Document Inserted Successfully!!" if response.statusCode==200 else "Does not exist in the collection!!"

           except Excution as ex:
                 self.logger.exception(ex)
                 response.statusCode = 500
                 response.statusMessage = "Error in processing request. \n Reason:{}".format(str(ex))
                 response.data = None

          return response

      def create_source_system_data(self, source_system_data, source_system_id, source_system_name):
              response = ServiceResponse[SrcSystemModel]()
            try:
                 source_system_data['source_system_id']  = source_system_id 
                source_system_data['source_system_name']  = source_system_name

source_system_result = self.entity_command_dao.insert_source_system_data(source_system_data)
                response.data = source_system_result
                response.statusCode = 200
                response.statusMessage = "Source System Document Inserted Successfully!!"

           except Excution as ex:
                 self.logger.exception(ex)
                 response.statusCode = 500
                 response.statusMessage = "Error in processing request. \n Reason:{}".format(str(ex))
                 response.data = None

          return response

          def create_entity_type_data(self, entity_data, entity_type_code, entity_type_name):
              response = ServiceResponse[EntityType]()
            try:
                 entity_data['entity_type_code']  = entity_type_code 
                 entity_data['entity_type_name']  = entity_type_name

entity_type_result = self.entity_command_dao.insert_entity_type_data(entity_data)
                response.data = entity_type_result
                response.statusCode = 200
                response.statusMessage = "Entity Type Document Inserted Successfully!!"

           except Excution as ex:
                 self.logger.exception(ex)
                 response.statusCode = 500
                 response.statusMessage = "Error in processing request. \n Reason:{}".format(str(ex))
                 response.data = None

          return response

            def create_src_entity_type_data(self, src_entity_data, src_entity_type_id, source_system_id, src_entity_type_name):
              response = ServiceResponse[SrcEntityTypeModel]()
            try:
                 src_entity_data['src_entity_type_id'] = src_entity_type_id
                 src_entity_data['source_system_id']  = source_system_id
                 src_entity_data['src_entity_type_name']  = src_entity_type_name

entity_type_result = self.entity_command_dao.insert_src_entity_type_data(src_entity_data)
                response.data = entity_type_result
                response.statusCode = 200
                response.statusMessage = "Source Entity Type Document Inserted Successfully!!"

           except Excution as ex:
                 self.logger.exception(ex)
                 response.statusCode = 500
                 response.statusMessage = "Error in processing request. \n Reason:{}".format(str(ex))
                 response.data = None

          return response

        def insert_src_entity_app_data(self, src_entity_app_data):
              response = ServiceResponse[SrcEntityAppDataModel]()
            try:
                 src_entity_app_data_response = self.entity_command_dao.insert_src_entity_app_data(src_entity_app_data.dict())           
                response.data = src_entity_app_data_response
                response.statusCode = 200
                response.statusMessage = "Source Entity App data Document Inserted Successfully!!"

           except Excution as ex:
                 self.logger.exception(ex)
                 response.statusCode = 500
                 response.statusMessage = "Error in processing request. \n Reason:{}".format(str(ex))
                 response.data = None

          return response

        def create_entity_data(self, entity_data):
              response = ServiceResponse[EntityModel]()
            try:
                entity_response = self.entity_command_dao.insert_entity_data(entity_data.dict())
               if entity_response
                    response.data = entity_response
                    response.statusCode = 200
                    response.statusMessage = "Entity Doucment inserted Successfully!!"
             else:
                 response.data = entity_response
                 response.statusCode = 400
                 response.statusMessage = "Entity type code does not exist!!"

         except Exception as ex:
                 self.logger.exception(ex)
                 response.statusCode = 500
                response.statusMessage = "Error in processing request. \nReason:{}".format(str(ex))
                 response.data = None

          return response
          