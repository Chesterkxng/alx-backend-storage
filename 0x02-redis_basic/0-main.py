#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"Chester"
key = cache.store(data)
local_redis = redis.Redis()
print("the data : {} is stored under key: {}".format(local_redis.get(key), key))


data = b"king"
key = cache.store(data)
print("the data : {} is stored under key: {}".format(local_redis.get(key), key))
