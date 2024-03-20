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
from pydantic import BaseModel, Field, RootModel

from click_up_python_sdk.pydantic.assigned_by import AssignedBy
from click_up_python_sdk.pydantic.assignee import Assignee
from click_up_python_sdk.pydantic.comment1 import Comment1
from click_up_python_sdk.pydantic.comment_reactions import CommentReactions
from click_up_python_sdk.pydantic.user2 import User2

class Comment(BaseModel):
    id: str = Field(alias='id')

    comment: typing.List[Comment1] = Field(alias='comment')

    comment_text: str = Field(alias='comment_text')

    user: User2 = Field(alias='user')

    resolved: bool = Field(alias='resolved')

    assignee: Assignee = Field(alias='assignee')

    assigned_by: AssignedBy = Field(alias='assigned_by')

    reactions: CommentReactions = Field(alias='reactions')

    date: str = Field(alias='date')
    class Config:
        arbitrary_types_allowed = True