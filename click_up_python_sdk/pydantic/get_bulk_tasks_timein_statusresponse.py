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

from click_up_python_sdk.pydantic.model20bbn28 import Model20bbn28
from click_up_python_sdk.pydantic.model27075wz import Model27075wz

class GetBulkTasksTimeinStatusresponse(BaseModel):
    27075wz_: Model27075wz = Field(alias='27075wz')

    20bbn28_: Model20bbn28 = Field(alias='20bbn28')
    class Config:
        arbitrary_types_allowed = True
