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

from click_up_python_sdk.type.folder4 import Folder4
from click_up_python_sdk.type.shared5_lists import Shared5Lists
from click_up_python_sdk.type.shared5_tasks import Shared5Tasks

class RequiredShared5(TypedDict):
    tasks: Shared5Tasks

    lists: Shared5Lists

    folders: typing.List[Folder4]

class OptionalShared5(TypedDict, total=False):
    pass

class Shared5(RequiredShared5, OptionalShared5):
    pass