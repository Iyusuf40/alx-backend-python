#!/usr/bin/env python3
""" module doc str """


import asyncio
from typing import List, Iterator, Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """ yields a random int """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
