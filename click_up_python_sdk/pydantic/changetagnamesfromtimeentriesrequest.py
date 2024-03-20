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


class Changetagnamesfromtimeentriesrequest(BaseModel):
    name: str = Field(alias='name')

    new_name: str = Field(alias='new_name')

    tag_bg: str = Field(alias='tag_bg')

    tag_fg: str = Field(alias='tag_fg')
    class Config:
        arbitrary_types_allowed = True
