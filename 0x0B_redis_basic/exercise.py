#!/usr/bin/env python3
"""
Redis caching module.
"""
import redis
from typing import Union, Callable, Optional
import uuid


class Cache:
    """
        Redis caching class.
    """

    def __init__(self):
        """
            Cache class initialization.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            Stores the input data in Redis under a randomly generated key
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(
        self,
        key: str,
        fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """
            Return the key's value, if fn is passed it'll convert it.
        """
        result = self._redis.get(key)
        if fn:
            return fn(result)
        return result

    def get_str(self, key):
        """
            Return key value as a string.
        """
        return get(key, str)

    def get_int(self, key):
        """
            Return key value as an integer.
        """
        return get(key, int)
