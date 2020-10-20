#!/usr/bin/env python3
'''
Contains a coroutine.
'''
import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Returns the list of all the delays.
    '''
    r = await asyncio.gather(*(task_wait_random(max_delay) for i in range(n)))
    return sorted(r)
