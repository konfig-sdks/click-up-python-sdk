# coding: utf-8

"""
    ClickUp API Reference

    This is the ClickUp API Reference where you can learn about specific endpoints and parameters in detail.  Browse the available endpoints using the sidebar on the left.  **Not sure where to begin?** [Get Started with the ClickUp API](https://clickup.com/api) 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import click_up_python_sdk
from click_up_python_sdk.paths.team_team_id_time_entries_timer_id import delete
from click_up_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestTeamTeamIdTimeEntriesTimerId(ApiTestMixin, unittest.TestCase):
    """
    TeamTeamIdTimeEntriesTimerId unit test stubs
        Delete a time Entry
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
