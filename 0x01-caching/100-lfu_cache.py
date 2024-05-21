#!/usr/bin/env python3
""" LFUCache Cahcing Module """

from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    A data structure that implements a Least Frequently Used
    (LFU) algorithm for storing and retrieving items from a cache (dictionary)
    """
    def __init__(self):
        """Initializes the caching instance."""
        super().__init__()
        self.cache_data = OrderedDict()
        self.key_freq = {}

    def __reorder_items(self, mru_key):
        """
        Reorders the items cache based on the most recently used item.
        """
        if mru_key in self.key_freq:
            self.key_freq[mru_key] += 1
            self.cache_data.move_to_end(mru_key, last=False)

    def put(self, key, item):
        """Adds an item to the cache."""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > self.MAX_ITEMS:
                lfu_key = min(self.key_freq, key=self.key_freq.get)
                del self.cache_data[lfu_key]
                del self.key_freq[lfu_key]
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            self.key_freq[key] = 0
        else:
            self.cache_data[key] = item
        self.__reorder_items(key)

    def get(self, key):
        """Retrieves an item from the cache"""
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
