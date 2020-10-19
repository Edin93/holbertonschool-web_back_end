#!/usr/bin/env python3
'''
Contains a function.
'''
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Returns a list.
    '''
    return [(i, len(i)) for i in lst]
