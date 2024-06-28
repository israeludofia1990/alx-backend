#!/usr/bin/python3
'''MRU Caching'''
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''MRU Caching system that inherits from BaseCaching'''
    def __init__(self):
        '''class constructor'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''put method for MRU CACHE'''
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.pop(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            MRU_item, _ = self.cache_data.popitem(last=True)
            print("DISCARD: {}".format(MRU_item))
        self.cache_data[key] = item

    def get(self, key):
        '''get method for MRU CACHING'''
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
