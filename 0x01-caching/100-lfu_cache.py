#!/usr/bin/env python3
"""LFU Cache module that implements the LFU cache algorithm.
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache defines a caching system
    with a Least Frequently Used eviction policy.
    """

    def __init__(self):
        """Initialize the LFUCache"""
        super().__init__()
        self.freq = {}  # Dictionary to store the frequency of each key
        self.order = []  # List to maintain the order of keys based on usage

    def put(self, key, item):
        """Add an item in the cache using LFU algorithm"""
        if key is None or item is None:
            return

        # If the key already exists, update the item and frequency
        if key in self.cache_data:
            self.cache_data[key] = item  # Update the item
            self.freq[key] += 1  # Increment the frequency
            self.order.remove(key)
            self.order.append(key)  # Update the order
        else:
            # If the cache is full, evict the least frequently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used item(s)
                min_freq = min(self.freq.values())
                lfu_keys = [k for k, v in self.freq.items() if v == min_freq]

                # If there's a tie, use LRU to decide which to evict
                if len(lfu_keys) > 1:
                    # The first key in order list that matches
                    # the min frequency
                    for k in self.order:
                        if k in lfu_keys:
                            lfu_key = k  # Evict the LRU item
                            break  # Exit the loop
                else:
                    lfu_key = lfu_keys[0]

                # Evict the LFU item
                del self.cache_data[lfu_key]
                del self.freq[lfu_key]
                self.order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")

            # Add the new key-value pair and update frequency and order
            self.cache_data[key] = item
            self.freq[key] = 1
            self.order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Update the frequency and order to reflect access
        self.freq[key] += 1
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
