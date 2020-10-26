#!/usr/bin/python3
"""
LRUCache module.
"""

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
        self.ordered_cache_keys = []

    def put(self, key, item):
        """
            Add an item in the cache.
        """
        if not (key is None or item is None):
            if (
                len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS and
                (key not in self.cache_data.keys())
            ):
                lru = self.ordered_cache_keys[0]
                print('DISCARD: {}'.format(lru))
                self.ordered_cache_keys.pop(0)
                del self.cache_data[lru]
                self.cache_data[key] = item
                self.ordered_cache_keys.append(key)
            if (
                len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS and
                (key in self.cache_data.keys())
            ):

                self.ordered_cache_keys.remove(key)
                self.ordered_cache_keys.append(key)
                self.cache_data[key] = item
            else:
                self.ordered_cache_keys.append(key)
                self.cache_data[key] = item

    def get(self, key):
        """
            Get an item by key.
        """
        if key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
