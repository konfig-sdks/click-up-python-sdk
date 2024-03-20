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


class RequiredMembers3(TypedDict):
    id: int

    username: str

    email: str

    color: str

    initials: str

    profilePicture: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class OptionalMembers3(TypedDict, total=False):
    pass

class Members3(RequiredMembers3, OptionalMembers3):
    pass
