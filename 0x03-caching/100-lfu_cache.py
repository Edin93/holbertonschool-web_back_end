#!/usr/bin/python3
"""
LFUCache module.
"""
import time


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
        LFUCache class.
    """

    def __init__(self):
        """
            Initialize.
        """
        super().__init__()
        self.keys_usage_frequency = {}

    def put(self, key, item):
        """
            Add an item in the cache.
        """
        if not (key is None or item is None):
            if (
                len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS and
                (key not in self.cache_data.keys())
            ):
                ordered_keys_by_value = {
                    k: v for k, v in sorted(
                        self.keys_usage_frequency.items(), key=lambda el: el['usage'][1]
                    )
                }
                lfu = list(ordered_keys_by_value.keys())[0]
                print('DISCARD: {}'.format(lfu))
                del self.keys_usage_frequency[lfu]
                del self.cache_data[lfu]
                self.keys_usage_frequency[key] = {
                    'time': time.time(),
                    'usage': 1
                }
                self.cache_data[key] = item
            elif (
                len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS and
                (key in self.cache_data.keys())
            ):
                self.keys_usage_frequency[key] = {
                    'time': time.time(),
                    'usage': self.keys_usage_frequency[key]['usage'] + 1
                }
                self.cache_data[key] = item
            else:
                self.keys_usage_frequency[key] = {
                    'time': time.time(),
                    'usage': 1
                }
                self.cache_data[key] = item

    def get(self, key):
        """
            Get an item by key.
        """
        if key not in self.cache_data.keys():
            return None
        else:
            self.keys_usage_frequency[key] = {
                'time': time.time(),
                'usage': self.keys_usage_frequency[key]['usage'] + 1
            }
            return self.cache_data[key]
