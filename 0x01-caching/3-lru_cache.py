#!/usr/bin/python3
'''LRU Caching'''
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''LRU Caching system that inherits from BaseCaching'''
    def __init__(self):
        '''class constructor'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''put method for LRU CACHE'''
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            LRU_item, _ = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(LRU_item))
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        '''get method for LRU CACHING'''
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
