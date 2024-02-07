import traceback
import logging
import boto3
import os
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

secret_name = "dev-entity-master-app-config"
region_name = "eu-west-1"
config_secret = dict()

def init_config_secret():
         session = boto3.session.Session()
         client = session.client(
                service_name = 'secretsmanager',
                region_name = region_name
)

         try:

                config_secret_value = client.get_secret_value(SecretId=secret_name)

               if 'SecretString' in config_secret_value:
                    global config_secret
                    config_secret = json.loads(config_secret_value['SecretString'])

             return config_secret
          except Exception as e:
                  logger.error('Error while retrieving secrets')
                  traceback.print_exc()

    def get_config_secret():
         if not bool(config_secret):
                  return init_config_secret()
         else:
                  return config_secret

  if __name__ == '__main__':
        print(get_config_secret())
        