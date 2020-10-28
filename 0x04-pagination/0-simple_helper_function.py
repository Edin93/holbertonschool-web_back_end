#!/usr/bin/env python3
"""
Simple helper module.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size 2 containing a start index and an end index
    orresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    t0 = page * page_size - page_size
    t1 = t0 + page_size
    return (t0, t1)
