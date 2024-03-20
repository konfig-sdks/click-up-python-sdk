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

from click_up_python_sdk.pydantic.invited_by import InvitedBy
from click_up_python_sdk.pydantic.shared3 import Shared3
from click_up_python_sdk.pydantic.user7 import User7

class Guest3(BaseModel):
    user: User7 = Field(alias='user')

    invited_by: InvitedBy = Field(alias='invited_by')

    can_see_time_spent: bool = Field(alias='can_see_time_spent')

    can_see_time_estimated: bool = Field(alias='can_see_time_estimated')

    can_edit_tags: bool = Field(alias='can_edit_tags')

    shared: Shared3 = Field(alias='shared')
    class Config:
        arbitrary_types_allowed = True
