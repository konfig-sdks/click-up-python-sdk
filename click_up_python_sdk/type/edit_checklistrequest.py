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


class RequiredEditChecklistrequest(TypedDict):
    pass

class OptionalEditChecklistrequest(TypedDict, total=False):
    name: str

    # Position refers to the order of appearance of checklists on a task.\\  \\ To set a checklist to appear at the top of the checklists section of a task, use `\"position\": 0`.
    position: int

class EditChecklistrequest(RequiredEditChecklistrequest, OptionalEditChecklistrequest):
    pass
