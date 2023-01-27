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
from unittest.mock import MagicMock, PropertyMock
from unittest.mock import patch
from unittest import mock
from utils import (
    get_json,
    access_nested_map,
    memoize,
)
from client import GithubOrgClient


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
        self.assertEqual(access_nested_map(map, seq), exp)

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


class TestGetJson(unittest.TestCase):
    """ tests the get_json function """
    # @parameterized.expand(
    #     [
    #         ("http://example.com", {"payload": True}),
    #         ("http://holberton.io", {"payload": False})
    #     ]
    # )
    # @patch("utils.get_json")
    # def test_get_json(self, url, payload, get_json_mock):
    #     """ mocks http request to url """
    #     get_json_mock.json = MagicMock(return_value=payload)
    #     self.assertEqual(get_json_mock.json(url), payload)
    #     get_json_mock.json.assert_called_once_with(url)
    #     return get_json_mock
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]
    )
    @patch("utils.requests.get")
    def test_get_json(self, url, payload, get_json_mock):
        """ mocks http request to url """
        resp_obj = MagicMock(json=MagicMock(return_value=payload))
        get_json_mock.return_value = resp_obj
        self.assertEqual(get_json(url), payload)
        get_json_mock.assert_called_once_with(url)
        return get_json_mock


class TestMemoize(unittest.TestCase):
    """ tests memoize decorator """

    def test_memoize(self):
        """ tests memoize decorator """
        class TestClass:
            """ used for testing """

            def a_method(self):
                """ a_method is memoized """
                return 42

            @memoize
            def a_property(self):
                """ sets to a readonly property of
                TestClass instance """
                return self.a_method()

        global testInstance  # hack to allow access from toplevel
        # module name. easier alternative is patch.object to pacth
        # TestClass testInsatnce directly
        testInstance = TestClass()
        with patch("__main__.testInstance.a_method",
                   return_value=42) as mocked_method:
            self.assertEqual(testInstance.a_property, 42)
            self.assertEqual(testInstance.a_property, 42)
            testInstance.a_method.assert_called_once


class TestGithubOrgClient(unittest.TestCase):
    """ Tests GithubOrgClient """

    @parameterized.expand([("google",),  ("abc",)])
    def test_org(self, org):
        """ tests org method of GithubOrgClient """
        client_inst = GithubOrgClient(org)
        # NOTE: see the patch target "client.get_json"
        # Always the exact object is patched based on
        # the module it resides in.
        # patching utils.get_json will fail mocking because
        # the get get_json object of interest is the one
        # imported in client module
        import client  # to assert it was called
        with patch("client.get_json", return_value=org) as m_gt_json:
            self.assertEqual(client_inst.org, org)
            url = client_inst.ORG_URL.format(org=org)
            client.get_json.assert_called_once_with(url)

    @parameterized.expand([
        ("google", {"repos_url": "https://google.com"}),
        ("abc", {"repos_url": "https://abc.com"})
        ])
    def test_public_repos_url(self, org, payload):
        """ tests org method of GithubOrgClient """
        client_inst = GithubOrgClient(org)
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock,
                   return_value=payload) as m_org:
            self.assertEqual(client_inst._public_repos_url,
                             payload.get("repos_url"))

    @parameterized.expand([
        ("google", {"repos_url": "https://google.com"}),
        ("abc", {"repos_url": "https://abc.com"})
        ])
    @patch("client.get_json")
    def test_public_repos(self, org, payload, m_get_json):
        """ tests org method of GithubOrgClient """
        import client
        client_inst = GithubOrgClient(org)
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock,
                   return_value=payload.get("repos_url")) as m_pru:
            self.assertEqual(client_inst._public_repos_url,
                             payload.get("repos_url"))
            client.get_json.assert_called_once
            m_pru.assert_called_once

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo, license, exp):
        """ tests org method of GithubOrgClient """
        client_inst = GithubOrgClient("no-org")
        self.assertEqual(client_inst.has_license(repo, license), exp)


if __name__ == "__main__":
    unittest.main()
