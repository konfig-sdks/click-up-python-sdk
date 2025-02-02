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

from click_up_python_sdk.type.key_result_subcategory_ids import KeyResultSubcategoryIds
from click_up_python_sdk.type.key_result_task_ids import KeyResultTaskIds
from click_up_python_sdk.type.last_action import LastAction
from click_up_python_sdk.type.owner import Owner

class RequiredKeyResult(TypedDict):
    id: str

    goal_id: str

    name: str

    type: str

    unit: str

    creator: int

    date_created: str

    goal_pretty_id: str

    percent_completed: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    completed: bool

    task_ids: KeyResultTaskIds

    subcategory_ids: KeyResultSubcategoryIds

    owners: typing.List[Owner]

    last_action: LastAction

class OptionalKeyResult(TypedDict, total=False):
    pass

class KeyResult(RequiredKeyResult, OptionalKeyResult):
    pass
