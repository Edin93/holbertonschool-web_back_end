#!/usr/bin/env python3
'''
Contains a coroutine.
'''
import asyncio
import random


async def async_generator():
    '''
    Loops 10 times and yield a random number between 0 and 10.
    '''
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
