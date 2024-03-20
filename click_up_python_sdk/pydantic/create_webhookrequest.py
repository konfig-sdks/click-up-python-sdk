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

from click_up_python_sdk.pydantic.create_webhookrequest_events import CreateWebhookrequestEvents

class CreateWebhookrequest(BaseModel):
    endpoint: str = Field(alias='endpoint')

    events: CreateWebhookrequestEvents = Field(alias='events')

    space_id: typing.Optional[int] = Field(None, alias='space_id')

    folder_id: typing.Optional[int] = Field(None, alias='folder_id')

    list_id: typing.Optional[int] = Field(None, alias='list_id')

    task_id: typing.Optional[str] = Field(None, alias='task_id')
    class Config:
        arbitrary_types_allowed = True
