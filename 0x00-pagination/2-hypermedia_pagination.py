#!/usr/bin/env python3
"""This module implements a Server class to paginate a database of
popular baby names, and provides additionl pagination metadata.
"""

import csv
import math
from typing import List, Dict, Tuple, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate the start and end indices for a given page and page size"""
    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names"""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Constructor for the Server class"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""

        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of data based on the given page number and page size
        """
        assert isinstance(
            page, int) and page > 0, "page must be a positive integer"
        assert isinstance(
            page_size, int) and page_size > 0, "page_size must be positive"

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Return a dictionary containing pagination metadata"""

        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
