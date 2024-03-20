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

from click_up_python_sdk.type.assigned_by import AssignedBy
from click_up_python_sdk.type.assignee import Assignee
from click_up_python_sdk.type.comment1 import Comment1
from click_up_python_sdk.type.comment_reactions import CommentReactions
from click_up_python_sdk.type.user2 import User2

class RequiredComment(TypedDict):
    id: str

    comment: typing.List[Comment1]

    comment_text: str

    user: User2

    resolved: bool

    assignee: Assignee

    assigned_by: AssignedBy

    reactions: CommentReactions

    date: str

class OptionalComment(TypedDict, total=False):
    pass

class Comment(RequiredComment, OptionalComment):
    pass