#!/usr/bin/env python3
""" module docs """


from typing import List, Set, Dict, Tuple
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """ joins two strings """
    def f(x: float) -> float:
        """ multiplies n by a number from parent function """
        return multiplier * x
    return f
