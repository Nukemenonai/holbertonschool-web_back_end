#!/usr/bin/python3
""" Basic Cache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    Basic caching system
    '''
    MAX_ITEMS = None

    def put(self, key, item):
        """puts a value in self cache"""
        if not key or not item:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """returns value in self cache"""
        if not key:
            return None
        else:
            return self.cache_data.get(key)
