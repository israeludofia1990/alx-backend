#!/usr/bin/python3
'''Basic dictionary'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''Basic_caching class that inherites from BaseCaching'''

    def put(self, key, item):
        '''puts item value in dictionary given the key'''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''returns the value of an item in the dictionary given the key'''
        if key is None:
            return None
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            None
