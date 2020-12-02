#!/usr/bin/env python3
"""
Module to count how many times a particular URL was accessed.
"""
import requests
import redis
from functools import wraps
from typing import Callable


r = redis.Redis()


def count_url_requests(method: Callable) -> Callable:
    """
        Counts how many times a url has been requested.
        Cache it in redis under the key 'count: {url}'
        with an expiration time of 10 seconds.
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        """ Function wrapper """
        url = args[0]
        name = 'count: ' + '{' + url + '}'
        r.incrby(name, 1)
        r.expire(name, 10)
        return method(url)
    return wrapper


@count_url_requests
def get_page(url: str) -> str:
    """
        Returns the HTML of a particular URL.
    """
    response = requests.get(url)
    return response.text
