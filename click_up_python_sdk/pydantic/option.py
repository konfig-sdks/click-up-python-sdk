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


class Option(BaseModel):
    id: str = Field(alias='id')

    color: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='color')

    label: typing.Optional[str] = Field(None, alias='label')

    name: typing.Optional[str] = Field(None, alias='name')

    value: typing.Optional[int] = Field(None, alias='value')

    type: typing.Optional[str] = Field(None, alias='type')

    orderindex: typing.Optional[int] = Field(None, alias='orderindex')
    class Config:
        arbitrary_types_allowed = True
