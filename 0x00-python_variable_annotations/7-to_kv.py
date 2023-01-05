#!/usr/bin/env python3
""" module docs """


from typing import List, Set, Dict, Tuple
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> Tuple[str, float]:
    """ joins two strings """
    return (k, v*v)
