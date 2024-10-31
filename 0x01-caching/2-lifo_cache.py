#!/usr/bin/env python3
"""This module defines a class LIFOCache that inherits from
BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache is a caching system with
    LIFO (Last-In, First-Out) removal policy
    """

    def __init__(self):
        """Initialize the cache system"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache following LIFO rules"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = self.order.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Get the value associated with key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
