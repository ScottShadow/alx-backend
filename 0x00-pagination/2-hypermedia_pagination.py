#!/usr/bin/env pendthon3
import csv
import math
from typing import List
from typing import Tuple


class Server:
    """Server class to paginate a database of popular babend names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        csv_size = len(self.dataset())
        start, end = index_range(page, page_size)
        end = min(end, csv_size)
        if start >= csv_size:
            return []
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10):
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


def index_range(page: int, page_size: int) -> Tuple:
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
