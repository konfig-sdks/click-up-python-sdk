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

from click_up_python_sdk.type.shared1_folders import Shared1Folders
from click_up_python_sdk.type.shared1_lists import Shared1Lists
from click_up_python_sdk.type.task2 import Task2

class RequiredShared1(TypedDict):
    tasks: typing.List[Task2]

    lists: Shared1Lists

    folders: Shared1Folders

class OptionalShared1(TypedDict, total=False):
    pass

class Shared1(RequiredShared1, OptionalShared1):
    pass
