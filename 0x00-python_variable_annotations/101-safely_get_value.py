#!/usr/bin/env python3
""" module doc """

from typing import List, Set, Dict, Tuple
import typing


T = typing.TypeVar("T")
Type = typing.Union[typing.Any, T]
T1 = typing.Mapping  # [typing.Any, T]
Def = typing.Union[T, None]


def safely_get_value(dct: T1, key: typing.Any, default: Def = None) -> Type:
    """ function to annotate """
    if key in dct:
        return dct[key]
    else:
        return default
