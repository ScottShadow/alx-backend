#!/usr/bin/env pendthon3
import csv
import math
from typing import List
from typing import Tuple


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

        Args:
            page (int, optional): The page number to retrieve from the
            dataset. Defaults to 1.
            page_size (int, optional): The number of items per page. Defaults
            to 10.

        Returns:
            List[List]: A list of lists representing the data on the specified
            page.

        Raises:
            AssertionError: If the page or page_size is not an integer or if
            the page is less than or equal to 0 or if the page_size is less
            than or equal to 0.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        csv_size = len(self.dataset())
        start, end = index_range(page, page_size)
        end = min(end, csv_size)
        if start >= csv_size:
            return []
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """
        Calculates the total number of pages based on the dataset length and
        age size.

        Retrieves the data for the specified page using the get_page method.

        Returns a dictionary containing:
        - "page_size": The size of the data on the current page.
        - "page": The current page number.
        - "data": The data on the current page.
        - "next_page": The next page number if it exists, None otherwise.
        - "prev_page": The previous page number if it exists, None if on the
        first page.
        - "total_pages": The total number of pages in the dataset.
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        data = self.get_page(page, page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page + 1 < total_pages else None,
            "prev_page": None if page < 1 else page - 1,
            "total_pages": total_pages
        }
