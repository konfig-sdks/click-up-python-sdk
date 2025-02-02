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

from click_up_python_sdk.pydantic.folder3 import Folder3
from click_up_python_sdk.pydantic.priority1 import Priority1
from click_up_python_sdk.pydantic.space2 import Space2
from click_up_python_sdk.pydantic.status import Status
from click_up_python_sdk.pydantic.status5 import Status5

class UpdateListresponse(BaseModel):
    id: str = Field(alias='id')

    name: str = Field(alias='name')

    orderindex: int = Field(alias='orderindex')

    content: str = Field(alias='content')

    status: Status5 = Field(alias='status')

    priority: Priority1 = Field(alias='priority')

    assignee: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='assignee')

    task_count: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='task_count')

    due_date: str = Field(alias='due_date')

    due_date_time: bool = Field(alias='due_date_time')

    start_date: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='start_date')

    start_date_time: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='start_date_time')

    folder: Folder3 = Field(alias='folder')

    space: Space2 = Field(alias='space')

    statuses: typing.List[Status] = Field(alias='statuses')

    inbound_address: str = Field(alias='inbound_address')
    class Config:
        arbitrary_types_allowed = True
