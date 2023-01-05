#!/usr/bin/env python3
""" module doc """

from typing import List, Set, Dict, Tuple
import typing


Type = typing.Union[typing.Any, None]


def safe_first_element(lst: typing.Sequence[typing.Any]) -> Type:
    """ function to anotate """
    if lst:
        return lst[0]
    else:
        return None
