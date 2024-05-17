#!/usr/bin/env python3
""" Server Class Module """

from typing import List, Tuple
import csv
import math


class Server:
    """
    This server class paginates a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        pass

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Paginates the dataset and returns a list of rows"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        rows = self.dataset()

        if start_index >= len(rows):
            return []

        return rows[start_index:end_index]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of start and end
    indexes for pagination.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
