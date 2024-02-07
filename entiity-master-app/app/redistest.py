
import redis
from util.redis_helper import RedisHelper

rcache = redis.Redis(
       host = 'localhost',
       port = 6379,
       charset = "utf-8",
       decode_response = True)

@RedisHelper.cacheable()
def test_cache(v1, v2):
       print('cache miss!')
       return f"cache test! {v1} {v2}"

@RedisHelper.cacheable(cache = rcache, key = lambda *args, **kwargs: "#customerKey1# -> {}".format(args[0]))
def test_custom_cache(v1, v2):
         print("cache miss!!")
        return "cache test!"

@RedisHelper.cache_evict(cache = rcache, key = lambda *args, **kwargs: "#customKey1# -> {}".format(args[0]))
def test_custom_cache_delete(v1, v2):
         pass

print("\n\n ## Test cache evict")
print(test_custom_cache("hello", "Test"))
print(test_custom_cache("hello", "Test"))
print(test_custom_cache_delete("hello", "Test"))
print(test_custom_cache("hello", "Test"))
