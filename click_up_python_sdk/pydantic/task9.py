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

from click_up_python_sdk.pydantic.creator import Creator
from click_up_python_sdk.pydantic.folder import Folder
from click_up_python_sdk.pydantic.model_list import ModelList
from click_up_python_sdk.pydantic.space import Space
from click_up_python_sdk.pydantic.status import Status
from click_up_python_sdk.pydantic.task9_assignees import Task9Assignees
from click_up_python_sdk.pydantic.task9_checklists import Task9Checklists
from click_up_python_sdk.pydantic.task9_tags import Task9Tags

class Task9(BaseModel):
    tags: Task9Tags = Field(alias='tags')

    id: str = Field(alias='id')

    custom_item_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='custom_item_id')

    name: str = Field(alias='name')

    status: Status = Field(alias='status')

    orderindex: str = Field(alias='orderindex')

    date_created: str = Field(alias='date_created')

    date_updated: str = Field(alias='date_updated')

    date_closed: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='date_closed')

    date_done: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='date_done')

    creator: Creator = Field(alias='creator')

    assignees: Task9Assignees = Field(alias='assignees')

    checklists: Task9Checklists = Field(alias='checklists')

    parent: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='parent')

    priority: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='priority')

    due_date: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='due_date')

    start_date: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='start_date')

    time_estimate: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='time_estimate')

    time_spent: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='time_spent')

    list_: ModelList = Field(alias='list')

    folder: Folder = Field(alias='folder')

    space: Space = Field(alias='space')

    url: str = Field(alias='url')

    markdown_description: typing.Optional[str] = Field(None, alias='markdown_description')
    class Config:
        arbitrary_types_allowed = True