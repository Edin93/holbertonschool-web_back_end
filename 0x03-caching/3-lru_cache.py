#!/usr/bin/python3
"""
LRUCache module.
"""
from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
        LRUCache class.
    """

    def __init__(self):
        """
            Initialize.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
            Add an item in the cache.
        """
        if not (key is None or item is None):
            if (
                len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS and
                (key not in self.cache_data.keys())
            ):
                lru = list(self.cache_data.keys())[0]
                print('DISCARD: {}'.format(lru))
                del self.cache_data[lru]
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """
            Get an item by key.
        """
        if key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
