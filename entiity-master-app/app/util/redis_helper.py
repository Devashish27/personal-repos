from typing import Callable
from redis.client import Redis
import pickle, base64

class RedisHelper():
      cache_client:Redis = None

       @staticmethod
        def configure(cache:Redis):
                RedisHelper.cache_client = cache

        def __get_key(function_pointer:Callable, key:Callable, *args, **kwargs):
                 if key == None:
                     return "#{}# -> {}".format(function_pointer.__qualname__, args)
               else:
                    return "#custom# -> {}".format(key(*args, **kwargs))

       def cacheable(cache:Redis=None, key:Callable=None, ttl=300):
             def cache_wrapper(function_pointer:Callable):
               def wrapper_function(*args, **kwargs):
                   cache_key = RedisHelper.__get_key(function_pointer, key, *args, **kwargs)
                   client = RedisHelper.cache_client if cache == None else cache
                   cached_value = client.get(cache_key)
                   if cached_value == None:
                       cached_value = base64.b64encode(pickle.dumps(function_pointer(*args, **kwargs)))
                        client.set(cache_key, cached_value)
                        client.expire(cache_key, ttl)
                  return pickle.loads(base64.b64decode(cached_value))
               return wrapper_function
             return cache_wrapper

        def cache_evict(cache:Redis=None, key:Callable=None):
              def cache_wrapper(function_pointer: Callable):
                  def wrapper_function(*args, **kwargs):
                         cache_key = RedisHelper.__get_key(function_pointer, key, *args, **kwargs)
                        client = RedisHelper.cache_client if cache == None else cache
                        client.delete(cache_key)
                   return wrapper_function
             return cache_wrapper
