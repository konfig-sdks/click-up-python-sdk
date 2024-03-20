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

from click_up_python_sdk.type.checklists import Checklists
from click_up_python_sdk.type.custom_fields import CustomFields
from click_up_python_sdk.type.dependency_warning import DependencyWarning
from click_up_python_sdk.type.due_dates import DueDates
from click_up_python_sdk.type.portfolios import Portfolios
from click_up_python_sdk.type.remap_dependencies import RemapDependencies
from click_up_python_sdk.type.tags import Tags
from click_up_python_sdk.type.time_estimates import TimeEstimates
from click_up_python_sdk.type.time_tracking import TimeTracking

class RequiredFeatures4(TypedDict):
    tags: Tags

    due_dates: DueDates

    time_tracking: TimeTracking

    time_estimates: TimeEstimates

    checklists: Checklists

class OptionalFeatures4(TypedDict, total=False):
    custom_fields: CustomFields

    remap_dependencies: RemapDependencies

    dependency_warning: DependencyWarning

    portfolios: Portfolios

class Features4(RequiredFeatures4, OptionalFeatures4):
    pass