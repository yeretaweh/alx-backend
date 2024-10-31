#!/usr/bin/env python3
""" This module defines a class FIFOCache that inherits from BaseCaching
and is a caching system using the logic of First In First Out"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache is a caching system that follows
        FIFO (First-In, First-Out)
    """

    def __init__(self):
        """ Initialize the cache system """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache following FIFO rules """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Remove the first item added (FIFO)
                    first_key = self.order.pop(0)
                    del self.cache_data[first_key]
                    print(f"DISCARD: {first_key}")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
