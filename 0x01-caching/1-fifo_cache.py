#!/usr/bin/python3
'''FIFO caching'''
from collections import deque
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''a class FIFOCache that inherits from
    BaseCaching and is a caching system'''
    def __init__(self):
        '''FIFO class constructor'''
        super().__init__()
        self.order = deque()

    def put(self, key, item):
        '''assigns a value to a given key'''
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.order.popleft()
            del self.cache_data[oldest_key]
            print("DISCARD {}".format(oldest_key))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        '''return the value in `self.cache_data` linked to key '''
        if key is None:
            return None
        if key in self.cache_data:
            return self.cache_data[key]
        return None
