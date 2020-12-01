#!/usr/bin/env python3
"""
Redis caching module.
"""
import redis
from typing import Union
import uuid


class Cache:
    """ Redis caching class. """

    def __init__(self) -> None:
        """ Cache class initialization. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Stores the input data in Redis under a randomly generated key. """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
