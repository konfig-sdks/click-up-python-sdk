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

from click_up_python_sdk.type.assignees import Assignees

class RequiredUpdateTaskrequest(TypedDict):
    pass

class OptionalUpdateTaskrequest(TypedDict, total=False):
    # To clear the task description, include `Description` with `\" \"`.
    description: str

    # To convert an item using a custom task type into a task, send `'null'`. \\  \\ To update this task to be a Milestone, send a value of `1`. \\  \\ To use a custom task type, send the custom task type ID as defined in your Workspace, such as `2`.
    custom_item_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    name: str

    status: str

    priority: int

    due_date: int

    due_date_time: bool

    # You can move a subtask to another parent task by including `\"parent\"` with a valid `task id`.\\  \\ You cannot convert a subtask to a task by setting `\"parent\"` to `null`.
    parent: str

    time_estimate: int

    start_date: int

    start_date_time: bool

    assignees: Assignees

    archived: bool

class UpdateTaskrequest(RequiredUpdateTaskrequest, OptionalUpdateTaskrequest):
    pass
