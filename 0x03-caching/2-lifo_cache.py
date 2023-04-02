#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    caching system that implements LIFO algo
    """
    def __init__(self):
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        '''
        Puts an item in the cache
        discards the last item put if the size of the cache
        > than the max number of items
        '''
        if not key or not item:
            pass
        else:
            if len(self.cache_data.values()) > BaseCaching.MAX_ITEMS:
                last = self.cache_order.pop()
                del self.cache_data[last]
                print(f"DISCARD: {last}")
            self.cache_data[key] = item
            self.cache_order.append(key)

    def get(self, key):
        """get an item from cache by key """
        if not key:
            return None
        else:
            return self.cache_data.get(key)
