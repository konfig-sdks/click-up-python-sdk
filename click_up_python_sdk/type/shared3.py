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

from click_up_python_sdk.type.list3 import List3
from click_up_python_sdk.type.shared3_folders import Shared3Folders
from click_up_python_sdk.type.shared3_tasks import Shared3Tasks

class RequiredShared3(TypedDict):
    tasks: Shared3Tasks

    lists: typing.List[List3]

    folders: Shared3Folders

class OptionalShared3(TypedDict, total=False):
    pass

class Shared3(RequiredShared3, OptionalShared3):
    pass