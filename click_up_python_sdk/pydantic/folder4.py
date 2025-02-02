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

from click_up_python_sdk.pydantic.folder4_lists import Folder4Lists
from click_up_python_sdk.pydantic.status import Status

class Folder4(BaseModel):
    id: str = Field(alias='id')

    name: str = Field(alias='name')

    orderindex: int = Field(alias='orderindex')

    override_statuses: bool = Field(alias='override_statuses')

    hidden: bool = Field(alias='hidden')

    task_count: str = Field(alias='task_count')

    archived: bool = Field(alias='archived')

    statuses: typing.List[Status] = Field(alias='statuses')

    lists: Folder4Lists = Field(alias='lists')

    permission_level: str = Field(alias='permission_level')
    class Config:
        arbitrary_types_allowed = True
