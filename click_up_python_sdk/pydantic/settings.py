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


class Settings(BaseModel):
    show_task_locations: bool = Field(alias='show_task_locations')

    # Acceptable values are `1`, `2`, or `3`, which show subtasks separate, expanded, or collapsed.
    show_subtasks: int = Field(alias='show_subtasks')

    show_subtask_parent_names: bool = Field(alias='show_subtask_parent_names')

    show_closed_subtasks: bool = Field(alias='show_closed_subtasks')

    show_assignees: bool = Field(alias='show_assignees')

    show_images: bool = Field(alias='show_images')

    collapse_empty_columns: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='collapse_empty_columns')

    me_comments: bool = Field(alias='me_comments')

    me_subtasks: bool = Field(alias='me_subtasks')

    me_checklists: bool = Field(alias='me_checklists')
    class Config:
        arbitrary_types_allowed = True
