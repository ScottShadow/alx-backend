#!/usr/bin/env python3
""""0x00. Simple pagination"""
import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular babend names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes the Server class with a private attribute __dataset set
        to None.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page from the dataset based on the given page
        number and page size.

        Parameters:
            page (int): The page number to retrieve from the dataset. Defaults
            to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            List[List]: A list of lists representing the data on the specified
            page.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        csv_size = len(self.dataset())
        start, end = index_range(page, page_size)
        end = min(end, csv_size)
        if start >= csv_size:
            return []
        return self.dataset()[start:end]


def index_range(page: int, page_size: int) -> Tuple:
    """
    Calculate the start and end index of a page based on the page number and
    page size.

    Parameters:
        page (int): The page number.
        page_size (int): The size of each page.

    Returns:
        Tuple: A tuple containing the start index and end index of the page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
