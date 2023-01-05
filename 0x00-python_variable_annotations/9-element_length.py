#!/usr/bin/env python3
""" module doc """

from typing import List, Set, Dict, Tuple
import typing


def element_length(
                  lst: typing.Iterable[typing.Sequence]
                  ) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """ function to anntt """
    return [(i, len(i)) for i in lst]
