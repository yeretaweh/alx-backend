#!/usr/bin/env python3
"""MRU Cache module implementation
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache defines a caching system with a
    Most Recently Used eviction policy.
    """

    def __init__(self):
        """Initialize the MRUCache"""
        super().__init__()
        self.order = []  # List to track the order of keys for MRU

    def put(self, key, item):
        """Add an item in the cache using MRU algorithm"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the most recently used item
            most_recent_key = self.order.pop()
            del self.cache_data[most_recent_key]
            print(f"DISCARD: {most_recent_key}")

        # Add the new key-value pair and update order
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Update the order to reflect the most recent access
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
