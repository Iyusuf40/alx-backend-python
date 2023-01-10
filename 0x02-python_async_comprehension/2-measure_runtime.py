#!/usr/bin/env python3
""" module doc str """


import asyncio
from typing import List, Iterator, Generator
import random
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measures time of exec of an async coroutine"""
    start = time.perf_counter()
    x = await asyncio.gather(async_comprehension(), async_comprehension(),
                             async_comprehension(), async_comprehension())
    # print(x)
    return time.perf_counter() - start
