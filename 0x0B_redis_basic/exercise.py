#!/usr/bin/env python3
"""
Redis caching module.
"""
import redis
from typing import Union, Callable, Optional
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
        Counts how many times methods of the Cache class are called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ Wrapper function. """
        method_name = method.__qualname__
        self._redis.incr(method_name)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
        Stores the history of inputs and outputs for a particular function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ Wrapper function. """
        method_name = method.__qualname__
        data = str(args)
        method_result = method(self, data)
        self._redis.rpush("{}:inputs".format(method_name), data)
        self._redis.rpush("{}:outputs".format(method_name), method_result)
        return method_result
    return wrapper


def replay(func: Callable):
    """
        Displays the history of calls of the passed func.
    """
    r = redis.Redis()
    method_name = func.__qualname__
    inputs = r.lrange("{}:inputs".format(method_name), 0, -1)
    outputs = r.lrange("{}:outputs".format(method_name), 0, -1)
    calls_number = len(inputs)
    msg = '{} was called {} times:\n'.format(method_name, calls_number)
    for i in range(calls_number):
        k = inputs[i]
        v = outputs[i]
        msg += '{}(*{}) -> {}'.format(
            method_name,
            k.decode('utf-8'),
            v.decode('utf-8')
        )
        if i < calls_number - 1:
            msg += '\n'
    print(msg)


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

    @call_history
    @count_calls
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
