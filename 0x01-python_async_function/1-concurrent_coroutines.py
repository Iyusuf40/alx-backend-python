#!/usr/bin/env python3
""" module's doc string """


import asyncio
import random
from typing import List, Callable


wait_random = __import__('0-basic_async_syntax').wait_random


async def wrapper(f: Callable, arg: int, lst: List[float]) -> None:
    x = await f(arg)
    lst.append(x)


async def wait_n(n: int, max_delay: int) -> str:
    """demo of asyncio"""
    coros = []
    lst: List[float] = []
    for _ in range(n):
        coros.append(wrapper(wait_random, max_delay, lst))
    await asyncio.gather(*coros)
    return lst
