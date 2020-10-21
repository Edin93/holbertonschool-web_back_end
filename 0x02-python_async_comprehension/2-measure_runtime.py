#!/usr/bin/env python3
'''
Contains a coroutine.
'''
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    It will execute async_comprehension four times in parallel.
    Then return the total runtime of it.
    '''
    s = time.perf_counter()
    r = await asyncio.gather(*(async_comprehension() for i in range(4)))
    e = time.perf_counter() - s
    return e
