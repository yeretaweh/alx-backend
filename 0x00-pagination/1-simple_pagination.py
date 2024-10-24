#!/usr/bin/env python3
"""This Module implements a Server class to paginate a dababase of
popular baby names.
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate the start and end indices for a given page and page size

    Args:
        page (int): The current page number (1-indexed)
        page_size (int): The number of items per page

    Returns:
        Tuple[int, int]: A tuple containing the start and end index
    """
    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Constructor for the Server class"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:  # If dataset is not cached
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)  # Read CSV file
                dataset = [row for row in reader]  # Convert to list
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset  # Return the cached dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of data based on the given page number and page size

        Args:
            page (int, optional): Current page number. Defaults to 1.
            page_size (int, optional): Number of items per page.
            Defaults to 10.

        Returns:
            List[List]: A list of rows corresponding to the specified page.
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
