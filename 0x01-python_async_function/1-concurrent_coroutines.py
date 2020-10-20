#!/usr/bin/env python3
'''
Contains a coroutine.
'''
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Returns the list of all the delays.
    '''
    # r = []
    # for i in range(n):
    #     x = await wait_random(max_delay)
    #     r.append(x)
    # return sorted(r)
    r = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return sorted(r)
