#!/usr/bin/env python3
"""
Module test cases.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''
    access_nested_map tests.
    '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        '''
            tests if access_nested_map function returns what it's supposed to.
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
