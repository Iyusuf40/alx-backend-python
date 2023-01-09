#!/usr/bin/env python3
""" module doc string """


import asyncio
import random
from typing import List, Callable
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures time of execution and returns a
       total_time / n"""
    start = start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start
    return n / elapsed
