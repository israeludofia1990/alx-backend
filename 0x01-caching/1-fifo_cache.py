#!/usr/bin/python3
'''FIFO caching'''
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''a class FIFOCache that inherits from
    BaseCaching and is a caching system'''
    def __init__(self):
        '''FIFO class constructor'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''assign to the dictionary `self.cache_data` the
           `item` value for the key `key`
        '''

        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        '''return the value in `self.cache_data` linked to key '''
        if key is None:
            return None
        if key in self.cache_data:
            return self.cache_data[key]
        return None
