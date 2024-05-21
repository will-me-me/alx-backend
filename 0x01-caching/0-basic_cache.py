#!/usr/bin/env python3
""" BasicCache Class Module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Represents an object that for storing and retrieving
    items from a dictionary.
    """

    def put(self, key, item):
        """Adds an item to the cache using key."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves a cached item from the cache using key."""
        return self.cache_data.get(key)
