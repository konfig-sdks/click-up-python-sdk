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

from click_up_python_sdk.type.goal3_group_members import Goal3GroupMembers
from click_up_python_sdk.type.goal3_owners import Goal3Owners
from click_up_python_sdk.type.member1 import Member1

class RequiredGoal3(TypedDict):
    description: str

    id: str

    pretty_id: str

    name: str

    team_id: str

    creator: int

    owner: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    color: str

    date_created: str

    start_date: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    due_date: str

    private: bool

    archived: bool

    multiple_owners: bool

    editor_token: str

    date_updated: str

    last_update: str

    folder_id: str

    folder_access: bool

    pinned: bool

    owners: Goal3Owners

    key_result_count: int

    members: typing.List[Member1]

    group_members: Goal3GroupMembers

    percent_completed: int

class OptionalGoal3(TypedDict, total=False):
    pass

class Goal3(RequiredGoal3, OptionalGoal3):
    pass