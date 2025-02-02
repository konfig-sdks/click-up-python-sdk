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

from click_up_python_sdk.pydantic.goal3 import Goal3
from click_up_python_sdk.pydantic.member2 import Member2

class Folder2(BaseModel):
    id: str = Field(alias='id')

    name: str = Field(alias='name')

    team_id: str = Field(alias='team_id')

    private: bool = Field(alias='private')

    date_created: str = Field(alias='date_created')

    creator: int = Field(alias='creator')

    goal_count: int = Field(alias='goal_count')

    members: typing.List[Member2] = Field(alias='members')

    goals: typing.List[Goal3] = Field(alias='goals')
    class Config:
        arbitrary_types_allowed = True
