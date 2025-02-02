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

from click_up_python_sdk.pydantic.assignees import Assignees

class UpdateTaskrequest(BaseModel):
    # To clear the task description, include `Description` with `\" \"`.
    description: typing.Optional[str] = Field(None, alias='description')

    # To convert an item using a custom task type into a task, send `'null'`. \\  \\ To update this task to be a Milestone, send a value of `1`. \\  \\ To use a custom task type, send the custom task type ID as defined in your Workspace, such as `2`.
    custom_item_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='custom_item_id')

    name: typing.Optional[str] = Field(None, alias='name')

    status: typing.Optional[str] = Field(None, alias='status')

    priority: typing.Optional[int] = Field(None, alias='priority')

    due_date: typing.Optional[int] = Field(None, alias='due_date')

    due_date_time: typing.Optional[bool] = Field(None, alias='due_date_time')

    # You can move a subtask to another parent task by including `\"parent\"` with a valid `task id`.\\  \\ You cannot convert a subtask to a task by setting `\"parent\"` to `null`.
    parent: typing.Optional[str] = Field(None, alias='parent')

    time_estimate: typing.Optional[int] = Field(None, alias='time_estimate')

    start_date: typing.Optional[int] = Field(None, alias='start_date')

    start_date_time: typing.Optional[bool] = Field(None, alias='start_date_time')

    assignees: typing.Optional[Assignees] = Field(None, alias='assignees')

    archived: typing.Optional[bool] = Field(None, alias='archived')
    class Config:
        arbitrary_types_allowed = True
