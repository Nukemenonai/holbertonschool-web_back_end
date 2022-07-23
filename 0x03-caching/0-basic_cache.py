#!/usr/bin/python3
""" Basic Cache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    Basic caching system
    '''

    def put(self, key, item):
        if not key or not item:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        if not key:
            return None
        return self.cache_data.get(key)
