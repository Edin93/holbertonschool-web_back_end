#!/usr/bin/env python3
"""
Module test cases.
"""
import requests
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    '''
    utils.access_nested_map tests.
    '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        '''
            Tests if access_nested_map function returns what it's supposed to.
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''
            Tests access_nested_map for raised expections.
        '''
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    '''
    utils.get_json tests.
    '''

    @parameterized.expand([
        ('http://example.com', {"test_payload": True}),
        ('http://holberton.io', {"test_payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        '''
            Tests if get_json function returns the expected result.
        '''
        with patch('requests.get') as mock:
            mock.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock.assert_called_once()


class TestMemoize(unittest.TestCase):
    """
    utils.memoize tests.
    """
    def test_memoize(self):
        '''
            Test memoize function for functional memoization.
        '''
        class TestClass:
            ''' TestClass for memoize testing. '''
            def a_method(self):
                ''' Returns 42. '''
                return 42

            @memoize
            def a_property(self):
                ''' Returns the class a_method result. '''
                return self.a_method()

        with patch.object(TestClass, 'a_method') as am:
            am.return_value = 42
            tc = TestClass()
            self.assertEqual(tc.a_property, am.return_value)
            self.assertEqual(tc.a_property, am.return_value)
            am.assert_called_once()
