from util import secretHelper

import redis

class AppConfig:

         def getAppConfig(self):
                 return secretHelper.get_config_secret()

         def getConnectionString(self):
                appConfig = self.getAppConfig()
                return "{}://{}:{}@{}/entity_master".format(appConfig["dialect"],
                           appConfig["user_name"],
                           appConfig["password"],
                           appConfig["host"])

          def getRedisConfig(self):
                  return redis.Redis(
                                    host='localhost',
                                     port=6379,
                                     decode_responses=True)

          def get_kafka_config(self):
                  return {
                          "bootstrap_servers" : ['localhost:9092']
                  }
                  return "{}://{}:{}@{}/{}".format(appConfig["dialect"],
                           appConfig["db_user"],
                           appConfig["db_password"],
                           appConfig["db_host"],
                           appConfig["db_name"])

