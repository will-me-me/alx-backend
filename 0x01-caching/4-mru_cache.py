#!/usr/bin/env python3
""" MRUCache Caching Module """

from base_caching import BaseCaching
from typing import Union, Any
from collections import deque


class MRUCache(BaseCaching):
    """
    A data structure that implements a Most Recently Used (LRU)
    algorithm for storing and retrieving items from a cache (dictionary)
    """

    def __init__(self) -> None:
        """Initialize the caching instance"""
        super().__init__()
        self.queue = deque()

    def put(self, key, item) -> None:
        """Adds an item to the cachhe"""
        if not key or not item:
            return
        if len(self.cache_data) < self.MAX_ITEMS or key in self.cache_data:
            if key not in self.cache_data:
                self.queue.append(key)
            self.cache_data[key] = item
        else:
            k = self.queue.pop()
            del self.cache_data[k]
            print('DISCARD:', k)
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key) -> Union[Any, None]:
        """Retrieves an item from the cache"""
        item = self.cache_data.get(key)
        if item and key in self.queue:
            self.queue.remove(key)
            self.queue.append(key)
        return item
