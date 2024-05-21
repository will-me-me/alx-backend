#!/usr/bin/env python3
""" FIFOCache Class Module """

from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Data structure - implements a First-In-First-Out (FIFO)
    algorithm for storing and retrieving items from a cache (dictionary)
    """
    def __init__(self):
        """Initializes the cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item to the cache using key"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves an item from the cache using key"""
        return self.cache_data.get(key)
