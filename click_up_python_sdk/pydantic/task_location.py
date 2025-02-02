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


class TaskLocation(BaseModel):
    list_id: int = Field(alias='list_id')

    folder_id: int = Field(alias='folder_id')

    space_id: int = Field(alias='space_id')

    list_name: str = Field(alias='list_name')

    folder_name: str = Field(alias='folder_name')

    space_name: str = Field(alias='space_name')
    class Config:
        arbitrary_types_allowed = True
