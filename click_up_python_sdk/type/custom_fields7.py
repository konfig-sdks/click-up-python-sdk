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

from click_up_python_sdk.type.type_config1 import TypeConfig1

class RequiredCustomFields7(TypedDict):
    id: str

    name: str

    type: str

    type_config: TypeConfig1

    date_created: str

    hide_from_guests: bool

    required: bool

class OptionalCustomFields7(TypedDict, total=False):
    value: str

class CustomFields7(RequiredCustomFields7, OptionalCustomFields7):
    pass
