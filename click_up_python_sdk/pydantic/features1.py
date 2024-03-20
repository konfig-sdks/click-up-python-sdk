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

from click_up_python_sdk.pydantic.checklists import Checklists
from click_up_python_sdk.pydantic.custom_fields import CustomFields
from click_up_python_sdk.pydantic.custom_items import CustomItems
from click_up_python_sdk.pydantic.dependency_warning import DependencyWarning
from click_up_python_sdk.pydantic.due_dates import DueDates
from click_up_python_sdk.pydantic.emails import Emails
from click_up_python_sdk.pydantic.milestones import Milestones
from click_up_python_sdk.pydantic.multiple_assignees import MultipleAssignees
from click_up_python_sdk.pydantic.points import Points
from click_up_python_sdk.pydantic.portfolios import Portfolios
from click_up_python_sdk.pydantic.remap_dependencies import RemapDependencies
from click_up_python_sdk.pydantic.sprints import Sprints
from click_up_python_sdk.pydantic.tags import Tags
from click_up_python_sdk.pydantic.time_estimates import TimeEstimates
from click_up_python_sdk.pydantic.zoom import Zoom

class Features1(BaseModel):
    tags: Tags = Field(alias='tags')

    due_dates: DueDates = Field(alias='due_dates')

    sprints: Sprints = Field(alias='sprints')

    points: Points = Field(alias='points')

    custom_items: CustomItems = Field(alias='custom_items')

    time_estimates: TimeEstimates = Field(alias='time_estimates')

    checklists: Checklists = Field(alias='checklists')

    zoom: Zoom = Field(alias='zoom')

    milestones: Milestones = Field(alias='milestones')

    custom_fields: CustomFields = Field(alias='custom_fields')

    remap_dependencies: RemapDependencies = Field(alias='remap_dependencies')

    dependency_warning: DependencyWarning = Field(alias='dependency_warning')

    multiple_assignees: MultipleAssignees = Field(alias='multiple_assignees')

    portfolios: Portfolios = Field(alias='portfolios')

    emails: Emails = Field(alias='emails')
    class Config:
        arbitrary_types_allowed = True