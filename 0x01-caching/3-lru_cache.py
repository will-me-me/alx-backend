#!/usr/bin/env python3
""" LRUCache Module """

from base_caching import BaseCaching
from typing import Union, Any
from collections import deque


class LRUCache(BaseCaching):
    """
    A data structure that implements a Least Recently Used (LRU)
    mechanism for storing and retrieving items from a cache (dictionary)
    """
    def __init__(self) -> None:
        """Initializes the cache instance."""
        super().__init__()
        self.queue = deque()

    def put(self, key, item) -> None:
        """Adds an item to the cache."""
        if not key or not item:
            return
        if len(self.cache_data) < self.MAX_ITEMS or key in self.cache_data:
            if key not in self.cache_data:
                self.queue.appendleft(key)
            self.cache_data[key] = item
        else:
            k = self.queue.pop()
            del self.cache_data[k]
            print('DISCARD:', k)
            self.cache_data[key] = item
            self.queue.appendleft(key)

    def get(self, key) -> Union[Any, None]:
        """Retrieves an item from the cache"""
        val = self.cache_data.get(key)
        if val and key in self.queue:
            self.queue.remove(key)
            self.queue.appendleft(key)
        return val
