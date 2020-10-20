#!/usr/bin/env python3
'''
Contains a coroutine.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    Returns the given argument.
    '''
    n = random.uniform(0, max_delay)
    await asyncio.sleep(n)
    return n
