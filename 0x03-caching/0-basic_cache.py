#!/usr/bin/python3
""" BasicCache """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class """
    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        the item value for the key key
        """
        if not (key is None and item is None):
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value of key in self.cache_data
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
