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


class User13(BaseModel):
    id: int = Field(alias='id')

    username: str = Field(alias='username')

    email: str = Field(alias='email')

    color: str = Field(alias='color')

    initials: str = Field(alias='initials')

    profile_picture: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='profilePicture')
    class Config:
        arbitrary_types_allowed = True
