#!/usr/bin/env python3
"""
Simple helper module.
"""
import csv
import math
from typing import List, Tuple


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
            pass


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size 2 containing a start index and an end index
    orresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    t0 = page * page_size - page_size
    t1 = t0 + page_size
    return (t0, t1)
