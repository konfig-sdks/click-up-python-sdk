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

from click_up_python_sdk.type.datum1_tags import Datum1Tags
from click_up_python_sdk.type.task4 import Task4
from click_up_python_sdk.type.task_location import TaskLocation
from click_up_python_sdk.type.task_tag import TaskTag
from click_up_python_sdk.type.user2 import User2

class RequiredDatum1(TypedDict):
    tags: Datum1Tags

    description: str

    id: str

    task: Task4

    wid: str

    user: User2

    billable: bool

    start: str

    end: str

    duration: str

    source: str

    at: str

    task_location: TaskLocation

    task_tags: typing.List[TaskTag]

    task_url: str

class OptionalDatum1(TypedDict, total=False):
    pass

class Datum1(RequiredDatum1, OptionalDatum1):
    pass