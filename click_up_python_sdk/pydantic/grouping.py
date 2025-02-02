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

from click_up_python_sdk.pydantic.grouping_collapsed import GroupingCollapsed

class Grouping(BaseModel):
    # Set the field to group by.\\  \\ Options include: `none`, `status`, `priority`, `assignee`, `tag`, or `dueDate`.
    field: str = Field(alias='field')

    # Set a group sort order using `1` or `-1`.\\  \\ For example, use `1`show tasks with urgent priority at the top of your view, and tasks with no priority at the bottom.\\  \\ Use `-1` to reverse the order to show tasks with no priority at the top of your view.
    dir: int = Field(alias='dir')

    collapsed: GroupingCollapsed = Field(alias='collapsed')

    ignore: bool = Field(alias='ignore')
    class Config:
        arbitrary_types_allowed = True
