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


class RequiredEditGuestOnWorkspacerequest(TypedDict):
    username: str

    can_edit_tags: bool

    can_see_time_spent: bool

    can_see_time_estimated: bool

    can_create_views: bool

    custom_role_id: int

class OptionalEditGuestOnWorkspacerequest(TypedDict, total=False):
    pass

class EditGuestOnWorkspacerequest(RequiredEditGuestOnWorkspacerequest, OptionalEditGuestOnWorkspacerequest):
    pass
