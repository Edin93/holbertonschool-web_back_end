#!/usr/bin/env python3
"""
Module test cases.
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ client.GithubOrgClient tests. """

    @parameterized.expand([
        ('google', {}),
        ('abc', {})
    ])
    @patch('client.get_json')
    def test_org(self, url, expected, mock):
        """ Tests if GithubOrgClient.org returns the correct value. """
        mock.return_value = {}
        r = GithubOrgClient(url)
        self.assertEqual(r.org, expected)
        mock.assert_called_once()

    def test_public_repos_url(self):
        """ Tests if GithubOrgClient._public_repos_url result is correct """
        with patch('client.GithubOrgClient.org',
             new_callable=PropertyMock) as mock:
            mock.return_value = {'repos_url': 'http://mock.url'}
            gc = GithubOrgClient('xyz')
            r = gc._public_repos_url
            self.assertEqual(r, mock.return_value.get('repos_url'))
