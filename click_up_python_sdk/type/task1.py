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
from click_up_python_sdk.type.folder import Folder
from click_up_python_sdk.type.model_list import ModelList
from click_up_python_sdk.type.space import Space
from click_up_python_sdk.type.status import Status
from click_up_python_sdk.type.task1_assignees import Task1Assignees
from click_up_python_sdk.type.task1_checklists import Task1Checklists
from click_up_python_sdk.type.task1_linked_tasks import Task1LinkedTasks
from click_up_python_sdk.type.task1_tags import Task1Tags

RequiredTask1 = TypedDict("RequiredTask1", {
    "tags": Task1Tags,

    "id": str,

    "name": str,

    "status": Status,

    "orderindex": str,

    "date_created": str,

    "date_updated": str,

    "date_closed": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "creator": Creator,

    "assignees": Task1Assignees,

    "checklists": Task1Checklists,

    "parent": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "priority": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "due_date": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "start_date": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "time_estimate": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "time_spent": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "list": ModelList,

    "folder": Folder,

    "space": Space,

    "linked_tasks": Task1LinkedTasks,

    "url": str,
    })

OptionalTask1 = TypedDict("OptionalTask1", {
    }, total=False)

class Task1(RequiredTask1, OptionalTask1):
    pass