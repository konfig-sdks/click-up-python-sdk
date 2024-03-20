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

from click_up_python_sdk.type.member4 import Member4
from click_up_python_sdk.type.role import Role

class RequiredTeam1(TypedDict):
    id: str

    name: str

    color: str

    avatar: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    members: typing.List[Member4]

    roles: typing.List[Role]

class OptionalTeam1(TypedDict, total=False):
    pass

class Team1(RequiredTeam1, OptionalTeam1):
    pass
