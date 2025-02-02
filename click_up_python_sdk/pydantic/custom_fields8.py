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

from click_up_python_sdk.pydantic.type_config1 import TypeConfig1
from click_up_python_sdk.pydantic.value import Value
from click_up_python_sdk.pydantic.value1 import Value1
from click_up_python_sdk.pydantic.value2 import Value2

class CustomFields8(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    name: typing.Optional[str] = Field(None, alias='name')

    type: typing.Optional[str] = Field(None, alias='type')

    type_config: typing.Optional[TypeConfig1] = Field(None, alias='type_config')

    date_created: typing.Optional[str] = Field(None, alias='date_created')

    hide_from_guests: typing.Optional[bool] = Field(None, alias='hide_from_guests')

    value: typing.Optional[typing.Union[Value, Value1, Value2]] = Field(None, alias='value')

    required: typing.Optional[bool] = Field(None, alias='required')
    class Config:
        arbitrary_types_allowed = True
