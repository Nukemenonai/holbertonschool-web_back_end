#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    First in First Out caching
    """
    def __init__(self):
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        '''
        Puts an item in the cache
        discards the first item put if the size of the cache
        > than the max number of items
        '''
        if not key or not item:
            pass
        else:
            self.cache_data[key] = item
            self.cache_order.append(key)
            if len(self.cache_data.values()) > BaseCaching.MAX_ITEMS:
                del self.cache_data[self.cache_order[0]]
                print(f"DISCARD: {self.cache_order[0]}")
                del self.cache_order[0]

    def get(self, key):
        """get an item from cache by key """
        if not key:
            return None
        else:
            return self.cache_data.get(key)
