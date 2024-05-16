#!/usr/bin/env python3
'''request, cache and track.
'''
import redis
import requests
from functools import wraps


redis_store = redis.Redis()


def data_cacher(method):
    '''Caches the output of result.
    '''
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)

        store.incr(count_key)
        store.set(cached_key, html)
        store.expire(cached_key, 10)
        return html
    return wrapper

@data_cacher
def get_page(url: str) -> str:
    '''return URL after adding cache.
    '''
    return requests.get(url).text
