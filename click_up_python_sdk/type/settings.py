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


class RequiredSettings(TypedDict):
    show_task_locations: bool

    # Acceptable values are `1`, `2`, or `3`, which show subtasks separate, expanded, or collapsed.
    show_subtasks: int

    show_subtask_parent_names: bool

    show_closed_subtasks: bool

    show_assignees: bool

    show_images: bool

    collapse_empty_columns: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    me_comments: bool

    me_subtasks: bool

    me_checklists: bool

class OptionalSettings(TypedDict, total=False):
    pass

class Settings(RequiredSettings, OptionalSettings):
    pass
