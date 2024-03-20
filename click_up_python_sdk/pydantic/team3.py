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

from click_up_python_sdk.pydantic.members5 import Members5
from click_up_python_sdk.pydantic.role import Role

class Team3(BaseModel):
    id: str = Field(alias='id')

    name: str = Field(alias='name')

    color: str = Field(alias='color')

    avatar: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='avatar')

    members: typing.List[Members5] = Field(alias='members')

    roles: typing.List[Role] = Field(alias='roles')
    class Config:
        arbitrary_types_allowed = True