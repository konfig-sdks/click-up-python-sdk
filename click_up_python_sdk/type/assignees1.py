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


class RequiredAssignees1(TypedDict):
    id: int

    username: str

    color: str

    email: str

    profilePicture: str

class OptionalAssignees1(TypedDict, total=False):
    pass

class Assignees1(RequiredAssignees1, OptionalAssignees1):
    pass
