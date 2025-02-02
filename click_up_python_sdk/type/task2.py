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

from click_up_python_sdk.type.creator import Creator
from click_up_python_sdk.type.folder3 import Folder3
from click_up_python_sdk.type.list2 import List2
from click_up_python_sdk.type.priority import Priority
from click_up_python_sdk.type.space import Space
from click_up_python_sdk.type.status import Status
from click_up_python_sdk.type.task2_assignees import Task2Assignees
from click_up_python_sdk.type.task2_checklists import Task2Checklists
from click_up_python_sdk.type.task2_custom_fields import Task2CustomFields
from click_up_python_sdk.type.task2_dependencies import Task2Dependencies
from click_up_python_sdk.type.task2_tags import Task2Tags

RequiredTask2 = TypedDict("RequiredTask2", {
    "tags": Task2Tags,

    "id": str,

    "name": str,

    "status": Status,

    "orderindex": str,

    "date_created": str,

    "date_updated": str,

    "date_closed": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "archived": bool,

    "creator": Creator,

    "assignees": Task2Assignees,

    "checklists": Task2Checklists,

    "parent": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "priority": Priority,

    "due_date": str,

    "start_date": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "points": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "time_estimate": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "custom_fields": Task2CustomFields,

    "dependencies": Task2Dependencies,

    "team_id": str,

    "url": str,

    "permission_level": str,

    "list": List2,

    "folder": Folder3,

    "space": Space,
    })

OptionalTask2 = TypedDict("OptionalTask2", {
    }, total=False)

class Task2(RequiredTask2, OptionalTask2):
    pass
