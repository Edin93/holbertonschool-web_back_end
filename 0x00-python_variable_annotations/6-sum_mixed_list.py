#!/usr/bin/env python3
'''
Contains a function.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Return the sum of the argument items as a float.
    '''
    return sum(mxd_lst)
