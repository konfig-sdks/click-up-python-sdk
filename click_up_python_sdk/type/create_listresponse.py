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

from click_up_python_sdk.type.assignee3 import Assignee3
from click_up_python_sdk.type.folder3 import Folder3
from click_up_python_sdk.type.priority1 import Priority1
from click_up_python_sdk.type.space2 import Space2
from click_up_python_sdk.type.status import Status
from click_up_python_sdk.type.status5 import Status5

class RequiredCreateListresponse(TypedDict):
    id: str

    name: str

    orderindex: int

    content: str

    status: Status5

    priority: Priority1

    assignee: Assignee3

    task_count: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    due_date: str

    due_date_time: bool

    start_date: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    start_date_time: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    folder: Folder3

    space: Space2

    statuses: typing.List[Status]

    inbound_address: str

class OptionalCreateListresponse(TypedDict, total=False):
    pass

class CreateListresponse(RequiredCreateListresponse, OptionalCreateListresponse):
    pass
