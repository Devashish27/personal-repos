from typing import Callable
from functools import wraps
from util.logger import Logger

class BaseController():

           def getLogger(self):
                  return Logger().getLogger()

           def methodLogger(function_pointer: Callable):
                  @wraps(function_pointer)
                   def wrapper(*args, **kwargs):
                         logger = Logger().getLogger()
                        logger.info("Begin invoke [{}]".format(function_pointer. __name__))
                        logger.info("args: {}, {}".format(args, kwargs))
                        result = function_pointer(*args, **kwargs)
                        logger.info("End Invoke [{}]". format(function_pointer.__name__))
                        return result

                   return wrapper