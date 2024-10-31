#!/usr/bin/env python3
"""This module defines a class LRUCahe that inherits from BaseCaching
    and is a caching system using the LRU algorithm
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Implements an LRU caching algorithm

    Args:
        BaseCaching (class): The Base Caching class
    """

    def __init__(self):
        """Initialize the LRUCache
        """
        super().__init__()
        self.order = []  # This will track the order of access to implement LRU

    def put(self, key, item):
        """Add an item in the cache, using LRU if the cache exceetds the limit
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If the key already exists, remove it from current position
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # If the cache exceeds MAX_ITEMS, remove the least recetly used
            lru_key = self.order.pop(0)  # Remove the LRU item
            del self.cache_data[lru_key]  # Delete the LRU item from the cache
            print(f"DISCARD: {lru_key}")  # Print the LRU item

        # Add the item to the cache and update the order
        self.cache_data[key] = item
        self.order.append(key)  # Append to order to mark as most recently used

    def get(self, key):
        """Get the value associated with the key and update its access in
        the cache
        """

        if key is None or key not in self.cache_data:
            return None

        # Since the key was accessed, move it to the end of the order list
        self.order.remove(key)  # Remove from current position
        self.order.append(key)  # Mark as most recently used

        return self.cache_data[key]
