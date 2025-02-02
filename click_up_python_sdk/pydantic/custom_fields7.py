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

class CustomFields7(BaseModel):
    id: str = Field(alias='id')

    name: str = Field(alias='name')

    type: str = Field(alias='type')

    type_config: TypeConfig1 = Field(alias='type_config')

    date_created: str = Field(alias='date_created')

    hide_from_guests: bool = Field(alias='hide_from_guests')

    required: bool = Field(alias='required')

    value: typing.Optional[str] = Field(None, alias='value')
    class Config:
        arbitrary_types_allowed = True
