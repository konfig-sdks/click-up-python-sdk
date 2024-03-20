# coding: utf-8

"""
    ClickUp API Reference

    This is the ClickUp API Reference where you can learn about specific endpoints and parameters in detail.  Browse the available endpoints using the sidebar on the left.  **Not sure where to begin?** [Get Started with the ClickUp API](https://clickup.com/api) 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredLastAction(TypedDict):
    id: str

    key_result_id: str

    userid: int

    date_modified: str

    steps_taken: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    note: str

    steps_before: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    steps_current: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class OptionalLastAction(TypedDict, total=False):
    pass

class LastAction(RequiredLastAction, OptionalLastAction):
    pass