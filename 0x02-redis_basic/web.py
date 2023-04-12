#!/usr/bin/env python3
"""Allows Caching to Redis
"""
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()


def cache_response(method: Callable) -> Callable:
    """Decorator Caches the output of fetched data.
    """
    @wraps(method)
    def invoker(url) -> str:
        """The wrapper function for caching the output.
        """
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@cache_response
def get_page(url: str) -> str:
    """Caches the response from a request to
    the URL passed and returns
    """
    return requests.get(url).text
