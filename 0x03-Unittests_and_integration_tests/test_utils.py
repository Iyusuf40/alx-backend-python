#!/usr/bin/env python3
""" module contains unittest cases """


from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
import unittest
from utils import (
    get_json,
    access_nested_map,
    memoize,
)
from nose.tools import assert_equal


class TestAccessNestedMap(unittest.TestCase):
    """ tests utils.access_nested_map function """
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, map, seq, exp):
        """ tests for expected outcomes """
        assert_equal(access_nested_map(map, seq), exp)

    @parameterized.expand(
        [
            ({}, ("a",)),
            ({"a": 1}, ("a", "b"))
        ]
    )
    def test_access_nested_map_exception(self, map, seq):
        """ tests for expected exceptions """
        with self.assertRaises(KeyError):
            access_nested_map(map, seq)


if __name__ == "__main__":
    unittest.main()
