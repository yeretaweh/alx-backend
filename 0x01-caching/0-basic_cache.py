#!/usr/bin/env python3
"""This module defines a class BasicCache that inherits from
BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache is a caching system with no limits"""

    def __init__(self):
        """Initialize the cache system from the base class"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get the value associated with key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
