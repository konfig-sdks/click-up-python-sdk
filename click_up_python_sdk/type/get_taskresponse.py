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
from click_up_python_sdk.type.custom_fields8 import CustomFields8
from click_up_python_sdk.type.folder import Folder
from click_up_python_sdk.type.get_taskresponse_assignees import GetTaskresponseAssignees
from click_up_python_sdk.type.get_taskresponse_checklists import GetTaskresponseChecklists
from click_up_python_sdk.type.get_taskresponse_tags import GetTaskresponseTags
from click_up_python_sdk.type.model_list import ModelList
from click_up_python_sdk.type.space import Space
from click_up_python_sdk.type.status import Status

RequiredGetTaskresponse = TypedDict("RequiredGetTaskresponse", {
    })

OptionalGetTaskresponse = TypedDict("OptionalGetTaskresponse", {
    "tags": GetTaskresponseTags,

    "description": str,

    "id": str,

    "custom_id": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    # A `null` value means this item is a task. A value of `1` is a Milestone. Any other number is a custom task type.
    "custom_item_id": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "name": str,

    "text_content": str,

    "status": Status,

    "orderindex": str,

    "date_created": str,

    "date_updated": str,

    "date_closed": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "creator": Creator,

    "assignees": GetTaskresponseAssignees,

    "checklists": GetTaskresponseChecklists,

    "parent": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "priority": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "due_date": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "start_date": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "time_estimate": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "time_spent": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "custom_fields": typing.List[CustomFields8],

    "list": ModelList,

    "folder": Folder,

    "space": Space,

    "url": str,

    "markdown_description": str,
    }, total=False)

class GetTaskresponse(RequiredGetTaskresponse, OptionalGetTaskresponse):
    pass
