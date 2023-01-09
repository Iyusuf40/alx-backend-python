#!/usr/bin/env python3
""" module contains functions that demonstrate
coroutines with python's asyncio.
NOTE:  the coroutines have to be bound to an event
loop in order to work as expected. for example
Using a for _ in range and awaiting will instead of work
asynchroniously, work in a bocking manner.
making a tuple of the coroutines and passing it to a
asyncio.gather method ensures they are bound to an
event loop and in that way it works as expected """


import asyncio
import random
from typing import List, Callable


wait_random = __import__('0-basic_async_syntax').wait_random


async def wrapper(f: Callable, arg: int, lst: List[float]) -> None:
    """ wrapper function that takes a coroutines and awats its
    value before appending to a list"""
    x = await f(arg)
    lst.append(x)


async def wait_n(n: int, max_delay: int) -> List[float]:
    """demo of asyncio"""
    coros = []
    lst: List[float] = []
    for _ in range(n):
        coros.append(wrapper(wait_random, max_delay, lst))
    await asyncio.gather(*coros)
    return lst
