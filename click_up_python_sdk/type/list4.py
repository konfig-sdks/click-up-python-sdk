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

from click_up_python_sdk.type.folder3 import Folder3
from click_up_python_sdk.type.priority4 import Priority4
from click_up_python_sdk.type.space2 import Space2
from click_up_python_sdk.type.status11 import Status11

class RequiredList4(TypedDict):
    id: str

    name: str

    orderindex: int

    content: str

    status: typing.Union[Status11, typing.Union[bool, date, datetime, dict, float, int, list, str, None], typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    priority: typing.Union[Priority4, typing.Union[bool, date, datetime, dict, float, int, list, str, None], typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    assignee: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    task_count: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    due_date: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    start_date: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    folder: Folder3

    space: Space2

    archived: bool

    override_statuses: bool

    permission_level: str

class OptionalList4(TypedDict, total=False):
    pass

class List4(RequiredList4, OptionalList4):
    pass