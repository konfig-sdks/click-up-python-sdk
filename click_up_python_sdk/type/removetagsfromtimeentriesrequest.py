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

from click_up_python_sdk.type.removetagsfromtimeentriesrequest_time_entry_ids import RemovetagsfromtimeentriesrequestTimeEntryIds
from click_up_python_sdk.type.tags10 import Tags10

class RequiredRemovetagsfromtimeentriesrequest(TypedDict):
    tags: typing.List[Tags10]

    time_entry_ids: RemovetagsfromtimeentriesrequestTimeEntryIds

class OptionalRemovetagsfromtimeentriesrequest(TypedDict, total=False):
    pass

class Removetagsfromtimeentriesrequest(RequiredRemovetagsfromtimeentriesrequest, OptionalRemovetagsfromtimeentriesrequest):
    pass
