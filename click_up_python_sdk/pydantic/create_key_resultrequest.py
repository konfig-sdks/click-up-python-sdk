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

from click_up_python_sdk.pydantic.create_key_resultrequest_list_ids import CreateKeyResultrequestListIds
from click_up_python_sdk.pydantic.create_key_resultrequest_owners import CreateKeyResultrequestOwners
from click_up_python_sdk.pydantic.create_key_resultrequest_task_ids import CreateKeyResultrequestTaskIds

class CreateKeyResultrequest(BaseModel):
    name: str = Field(alias='name')

    owners: CreateKeyResultrequestOwners = Field(alias='owners')

    # Target (key result) types include: `number`, `currency`, `boolean`, `percentage`, or `automatic`.
    type: str = Field(alias='type')

    steps_start: int = Field(alias='steps_start')

    steps_end: int = Field(alias='steps_end')

    unit: str = Field(alias='unit')

    task_ids: CreateKeyResultrequestTaskIds = Field(alias='task_ids')

    list_ids: CreateKeyResultrequestListIds = Field(alias='list_ids')
    class Config:
        arbitrary_types_allowed = True