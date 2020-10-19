#!/usr/bin/env python3
'''
Contains a function.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Returns a tuple containing k and v squared.
    '''
    return (k, v**2)
