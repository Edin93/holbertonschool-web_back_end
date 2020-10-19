#!/usr/bin/env python3
'''
Contains a function.
'''
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Return first of the arguments if it is a list otherwise None.
    '''
    if lst:
        return lst[0]
    else:
        return None
