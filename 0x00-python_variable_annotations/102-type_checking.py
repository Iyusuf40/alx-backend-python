#!/usr/bin/env python3
""" module used to test mypy """

from typing import List, Set, Dict, Tuple
import typing


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ function to annotate """
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 9)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
