#!/usr/bin/env python3
"""
Redis caching module.
"""
import redis
from typing import Union
import uuid


class Cache:
    """ Redis caching class. """

    def __init__(self):
        """ Cache class initialization. """
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Stores the input data in Redis under a randomly generated key. """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
