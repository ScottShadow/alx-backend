#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes the Server class.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves a subset of data based on the index and page size provided.

        Parameters:
            index (int): The starting index for the data subset. Default is
            None.
            page_size (int): The size of the page to be retrieved. Default
            is 10.

        Returns:
            Dict: A dictionary containing the retrieved data subset with
            keys "index", "next_index", "page_size", and "data".
        """
        assert index < len(self.dataset()) and index >= 0
        data = self.indexed_dataset()
        total_pages = len(self.dataset())
        data_list = []
        page_size = min(page_size, total_pages-index)
        next_index = index + page_size
        for key, val in data.items():
            if key < index:
                continue
            if key >= next_index:
                break
            data_list.append(val)

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data_list
        }
