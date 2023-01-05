#!/usr/bin/env python3
""" module docs """


from typing import List, Set, Dict, Tuple
import typing


def sum_mixed_list(lst: List[typing.Union[int, float]]) -> float:
    """ joins two strings """
    res = 0
    for i in lst:
        res += i

    return res
