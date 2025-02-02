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

from click_up_python_sdk.pydantic.goal_history import GoalHistory
from click_up_python_sdk.pydantic.goal_key_results import GoalKeyResults
from click_up_python_sdk.pydantic.goal_members import GoalMembers
from click_up_python_sdk.pydantic.owner import Owner

class Goal(BaseModel):
    description: str = Field(alias='description')

    id: str = Field(alias='id')

    name: str = Field(alias='name')

    team_id: str = Field(alias='team_id')

    date_created: str = Field(alias='date_created')

    start_date: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='start_date')

    due_date: str = Field(alias='due_date')

    private: bool = Field(alias='private')

    archived: bool = Field(alias='archived')

    creator: int = Field(alias='creator')

    color: str = Field(alias='color')

    pretty_id: str = Field(alias='pretty_id')

    multiple_owners: bool = Field(alias='multiple_owners')

    folder_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='folder_id')

    members: GoalMembers = Field(alias='members')

    owners: typing.List[Owner] = Field(alias='owners')

    key_results: GoalKeyResults = Field(alias='key_results')

    percent_completed: int = Field(alias='percent_completed')

    history: GoalHistory = Field(alias='history')

    pretty_url: str = Field(alias='pretty_url')
    class Config:
        arbitrary_types_allowed = True
