#!/usr/bin/env python3
"""
Module to count how many times a particular URL was accessed.
"""
import requests
import redis


r = redis.Redis()


def get_page(url: str) -> str:
    """
        Returns the HTML of a particular URL.
    """
    name = 'count: ' + '{' + url + '}'
    r.incr(name, amount=1)
    r.expire(name, 10)
    response = requests.get(url)
    return response.text
