#!/usr/bin/env python3
""" module contains unittest cases """


from parameterized import parameterized, parameterized_class
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
from fixtures import TEST_PAYLOAD
import requests
import client


org_payload = TEST_PAYLOAD[0][0]
repos_payload = TEST_PAYLOAD[0][1]
expected_repos = TEST_PAYLOAD[0][2]
apache2_repos = TEST_PAYLOAD[0][3]


class TestGithubOrgClient(unittest.TestCase):
    """ unittesT: GithubOrgClient test case """

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
        # import client  # to assert it was called
        with patch("client.get_json", return_value=org) as m_gt_json:
            self.assertEqual(client_inst.org, org)
            url = client_inst.ORG_URL.format(org=org)
            client.get_json.assert_called_once_with(url)

    def test_public_repos_url(self):
        """ tests org method of GithubOrgClient """
        org = "google"
        payload = {
            "repos_url": "https://api.github.com/orgs/{}/repos".format(
                org
            )
        }
        client_inst = GithubOrgClient(org)
        with patch(
            "client.GithubOrgClient.org",
             new_callable=PropertyMock,
             return_value=payload
             ) as m_org:
            self.assertEqual(client_inst._public_repos_url,
                             payload["repos_url"])

    # @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json")
    def test_public_repos(self, m_get_json):
        """ tests org method of GithubOrgClient """
        org = "google"
        payload = {
            "repos_url": "https://api.github.com/orgs/{}/repos".format(
                org
            )
        }
        m_get_json.return_value = payload
        client_inst = GithubOrgClient(org)
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock,
                   return_value=payload.get("repos_url")) as m_pru:
            self.assertEqual(client_inst._public_repos_url,
                             payload.get("repos_url"))
            m_pru.assert_called_once
            client.get_json.assert_called_once

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo, license, exp):
        """ tests org method of GithubOrgClient """
        client_inst = GithubOrgClient("no-org")
        self.assertEqual(client_inst.has_license(repo, license), exp)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [
        (org_payload, repos_payload, expected_repos, apache2_repos)
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ integration test on GithubOrgClient """

    @classmethod
    def setUpClass(cls) -> None:
        """ sets up TestIntegrationGithubOrgClient """
        m_req = MagicMock(json=MagicMock(side_effect=[TEST_PAYLOAD]))
        cls.patcher = patch("requests.get", return_value=m_req)
        cls.get_patcher = cls.patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """ tears down TestIntegrationGithubOrgClient """
        cls.patcher.stop()

    def test_req(self):
        """ test_req doc string """
        self.assertEqual(self.get_patcher("google").json(), TEST_PAYLOAD)

    @parameterized.expand([
        ("google", {"repos_url": "https://google.com"}),
        ("abc", {"repos_url": "https://abc.com"})
        ])
    @patch("client.get_json")
    def test_public_repos(self, org, payload, m_get_json):
        """ tests org method of GithubOrgClient """
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
    def test_public_repos_with_license(self, repo, license, exp):
        """ tests org method of GithubOrgClient """
        client_inst = GithubOrgClient("no-org")
        self.assertEqual(client_inst.has_license(repo, license), exp)


if __name__ == "__main__":
    unittest.main()
