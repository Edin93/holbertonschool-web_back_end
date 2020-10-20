#!/usr/bin/env python3
'''
Contains a coroutine.
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Returns the execution time for wait_n(n, max_delay) devided by n.
    '''
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start
    return elapsed / n
