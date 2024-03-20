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


class RequiredTypeConfig1(TypedDict):
    pass

class OptionalTypeConfig1(TypedDict, total=False):
    single_user: bool

    include_groups: bool

    include_guests: bool

    include_team_members: bool

class TypeConfig1(RequiredTypeConfig1, OptionalTypeConfig1):
    pass