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


class RequiredCreateFolderlessListrequest(TypedDict):
    name: str

class OptionalCreateFolderlessListrequest(TypedDict, total=False):
    content: str

    due_date: int

    due_date_time: bool

    priority: int

    # Include a `user_id` to add a List owner.
    assignee: int

    # **Status** refers to the List color rather than the task Statuses available in the List.
    status: str

class CreateFolderlessListrequest(RequiredCreateFolderlessListrequest, OptionalCreateFolderlessListrequest):
    pass