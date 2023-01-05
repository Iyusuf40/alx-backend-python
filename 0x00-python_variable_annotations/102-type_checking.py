#!/usr/bin/env python3
""" module doc """

from typing import List, Set, Dict, Tuple
import typing


def zoom_array(lst: List, factor: int = 2) -> List:
    """ function to annotate """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


if __name__ == "__main__":
    array = [12, 72, 91]

    zoom_2x = zoom_array(array)

    zoom_3x = zoom_array(array, 3)
