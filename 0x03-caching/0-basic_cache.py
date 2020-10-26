#!/usr/bin/python3
"""
BasicCache module.
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
        BasicCache class.
    """

    def put(self, key, item):
        """
            Add an item in the cache.
        """
        if not (key is None and item is None):
            self.cache_data[key] = item

    def get(self, key):
        """
            Get an item by key.
        """
        if (key is None or key not in self.cache_data.keys()):
            return None
        else:
            return self.cache_data[key]
