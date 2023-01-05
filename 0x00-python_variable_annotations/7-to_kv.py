#!/usr/bin/env python3
""" module docs """


from typing import List, Set, Dict, Tuple
import typing


def to_kv(k: str, r: typing.Union[int, float]) -> Tuple[str, float]:
    """ joins two strings """
    return k, r*r
