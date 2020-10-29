#!/usr/bin/env python3
"""
Simple helper module.
"""
import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a list of inner lists, where each inner list represents
        a data row from the dataset.
        """
        assert type(page_size) is int and type(page) is int
        assert page > 0
        assert page_size > 0
        if self.__dataset is None:
            self.dataset()
        r = index_range(page, page_size)
        if r[0] >= len(self.__dataset):
            return []
        else:
            return self.__dataset[r[0]:r[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a dictionary containing the following information:
        - page_size: the length of the returned dataset page
        - page: the current page number
        - data: the dataset page (equivalent to return from previous task)
        - next_page: number of the next page, None if no next page
        - prev_page: number of the previous page, None if no previous page
        - total_pages: the total number of pages in the dataset as an integer
        """
        dataset = self.dataset()
        data = self.get_page(page, page_size)
        page = page
        total_pages = math.ceil(len(dataset) / page_size)
        page_size = len(data)
        next_page = None
        prev_page = None
        if page > 1:
            prev_page = page - 1
        if page < total_pages:
            next_page = page + 1

        d = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
        return d


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size 2 containing a start index and an end index
    orresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    t0 = page * page_size - page_size
    t1 = t0 + page_size
    return (t0, t1)
