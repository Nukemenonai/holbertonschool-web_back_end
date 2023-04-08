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
            return 
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.cache_order:
                last = self.cache_order.pop()
                del self.cache_data[last]
                print('DISCARD: {}'.format(last))
        
        if key not in self.cache_order:
            self.cache_order.append(key)
        else:
            self.add_to_cache_order(key)

    def get(self, key):
        """get an item from cache by key """
        if not key or key not in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)

    def add_to_cache_order(self, key):
        """add key to cache order if not already in cache order"""
        length = len(self.cache_order)
        if self.cache_order[length - 1] != key:
            self.cache_order.remove(key)
            self.cache_order.append(key)
