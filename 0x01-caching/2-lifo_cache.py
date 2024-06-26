#!/usr/bin/python3
'''FIFO caching'''
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''a class FIFOCache that inherits from
    BaseCaching and is a caching system'''
    def __init__(self):
        '''FIFO class constructor'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Adds an item in the cache.'''
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        '''return the value in `self.cache_data` linked to key '''
        if key is None:
            return None
        if key in self.cache_data:
            return self.cache_data[key]
        return None
