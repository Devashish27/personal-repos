
from sqlalchemy import create_engine 
from sqlalchemy.sql import text
from typing import Callable
from config.appconfig import AppConfig

class SessionHelper(object):
        engine = None

        def __new__(cls):
                 if not hasattr(cls, 'instance'):
                        cls.instance = super(SessionHelper, cls).__new__(cls)
                return cls.instance

        def get_engine(self):
               if self.engine == None:
                      self.engine = create_engine(AppConfig().getConnectionString(), echo=False)
               return self.engine

class SqlHelper(object):
          def execute_raw_query(self, query, parameters, handler=None, collector=None):
                   engine = SessionHelper().get_engine()

                 with engine.connect() as connection:
                         statement = text(query)
                         if parameters != None:
                               result = connection.execute(statement, parameters)
                        else:
                               result = connection.execute(statement)

                       if handler != None:
                             for row in result:
                                    handler(row, collector)
                     else:
                              rows = []
                              for row in result:
                                    rows.append(row)
                              return rows

           def execute_insert(self, table, columns, record_values):
                   engine = SessionHelper().get_engine()
                   with engine.connect() as connection:
                             statement = text(self.prepare_insert_template(table, columns))
                              for record in record_values:
                                     connection.execute(statement, record)
                             connection.commit()

           def prepare_insert_template(self, table, columns):
                   template = "insert into {table} ({columns}) values ({values})"
                   values_template = ":" + ', :'.join(columns)
                  print(values_template)
                 return template.format(table = table, columns = ',  '.join(columns),
                                        values = values_template)

class QueryHelper():
           def query(query, targetEntity=None, mapping=None):
                
            def query_wrapper(function_pointer: Callable):
                 def row_mapper(row, collector):
                         index = 0
                         cls = targetEntity()
                         for properties in mappng:
                                setattr(cls, properties, row[index])
                                index += 1
                         collector.append(cls)

                 def wrapper_function(parameters=None, *args, **kwargs):
                        sqlHelper = SqlHelper()
                         if targetEntity != None:
                               mapped_results = []
                               sqlHelper.execute_raw_query(query, parameters, row_mapper, mapped_results)
                               return function_pointer(mapped_results)
                         else:
                               result = sqlHelper.execute_raw_query(query, parameters)
                              return function_pointer(result)
               return wrapper_function
          return query_wrapper

            def query2(query, targetEntity=None, mapper=None):
                    def query_wrapper(function_pointer: Callable):
                        def row_mapper(row, collector):
                                 cls = targetEntity()
                                 mapperfunc = getattr(cls, mapper)
                                 mapperfunc(row)
                                 collector.append(cls)

                       def wrapper_function(parameters=None, *args, **kwargs):
                              sqlHelper = SqlHelper()
                              if targetEntity != None:
                                  mapped_results = []
                                  sqlHelper.execute_raw_query(query, parameters, row_mapper, mapped_results)
                                  return function_pointer(mapped_results)
                             else:
                                    result = sqlHelper.execute_raw_query(query, parameters)
                                    return function_pointer(result)                     
               return wrapper_function
          return query_wrapper
