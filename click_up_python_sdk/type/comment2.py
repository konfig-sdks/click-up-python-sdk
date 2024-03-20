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

from click_up_python_sdk.type.comment1 import Comment1
from click_up_python_sdk.type.comment2_reactions import Comment2Reactions
from click_up_python_sdk.type.user2 import User2

class RequiredComment2(TypedDict):
    id: str

    comment: typing.List[Comment1]

    comment_text: str

    user: User2

    resolved: bool

    assignee: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    assigned_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    reactions: Comment2Reactions

    date: str

class OptionalComment2(TypedDict, total=False):
    pass

class Comment2(RequiredComment2, OptionalComment2):
    pass
