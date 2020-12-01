#!/usr/bin/env python3
"""
Module test cases.
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import requests


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
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock
        ) as mock:
            mock.return_value = {'repos_url': 'http://mock.url'}
            gc = GithubOrgClient('xyz')
            r = gc._public_repos_url
            self.assertEqual(r, mock.return_value.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """ Tests if GithubOrgClient.public_repos result is as expected """
        get_json_mock.return_value = [
            {'name': 'my_repo_num_0'},
            {'name': 'my_repo_num_1'},
            {'name': 'my_repo_num_2'},
            {'name': 'my_repo_num_3'}
        ]
        get_json_mock()
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mocked_public_repos:
            mocked_public_repos.return_value = [
                {'name': 'random_name_0'},
                {'name': 'random_name_1'},
                {'name': 'random_name_2'},
                {'name': 'random_name_3'}
            ]
            gc = GithubOrgClient('abc')
            r = gc._public_repos_url
            self.assertEqual(r, mocked_public_repos.return_value)
            mocked_public_repos.assert_called_once()
            get_json_mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """ Tests GithubOrgClient.has_license """
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected_result
        )


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test Class for GithubOrgClient.public_repos method. """

    @classmethod
    def setUpClass(cls):
        """ setUpClass method. """
        cls.get_patcher = patch(
            'requests.get',
            side_effect=[
                org_payload,
                repos_payload
            ]
        )
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ tearDownClass method. """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Testing GithubOrgClient.public_repos """
        ghoc = GithubOrgClient('random')
        self.assertEqual(ghoc.org, self.org_payload)
        self.assertEqual(ghoc.repos_payload, self.repos_payload)

    def test_public_repos_with_license(self):
        """ Testing public_repos with the argument license="apache-2.0" """
        ghoc = client.GithubOrgClient('random')
        self.assertEqual(ghoc.public_repos('apache-2.0'), self.apache2_repos)
