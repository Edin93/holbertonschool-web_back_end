#!/usr/bin/env python3
'''
Contains a function.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Return a function that multiplies a float by the argument.
    '''
    def multi_func(x: float) -> float:
        '''
        Return float.
        '''
        return x * multiplier
    return multi_func
