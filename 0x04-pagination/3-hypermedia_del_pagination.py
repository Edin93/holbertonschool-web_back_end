#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a dictionary containing the following information:
        - index: the current start index of the return page. That is the
            index of the first item in the current page. For example if
            requesting page 3 with page_size 20, and no data was removed from
            the dataset, the current index should be 60.
        - next_index: the next index to query with. That should be the index of
        the first item after the last item on the current page.
        - page_size: the current page size
        - data: the actual page of the dataset
        """
        dataset = self.indexed_dataset()
        data_keys = sorted(dataset.keys())
        data_amount = len(data_keys)
        assert index >= 0 and index < data_amount
        d_index = data_keys[index]
        d_next_index = None
        d_page_size = 0
        d_data = []
        i = 0
        while i < page_size:
            k = d_index + i
            d_data.append(dataset[k])
            i += 1
        if d_data:
            d_page_size = len(d_data)
        if index >= 0 and index + d_page_size < data_amount - 1:
            d_next_index = index + d_page_size
        d = {
            'index': index,
            'next_index': d_next_index,
            'page_size': d_page_size,
            'data': d_data
        }

        return d
