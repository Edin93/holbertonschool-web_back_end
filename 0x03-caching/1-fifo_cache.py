#!/usr/bin/python3
"""
FIFOCache module.
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
        FIFOCache class.
    """

    def __init__(self):
        """
            Initialize.
        """
        super().__init__()

    def put(self, key, item):
        """
            Add an item in the cache.
        """
        if not (key is None or item is None):
            if (
                len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS and
                (key not in self.cache_data.keys())
            ):
                first = sorted(self.cache_data.keys())[0]
                print('DISCARD: {}'.format(first))
                del self.cache_data[first]
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
