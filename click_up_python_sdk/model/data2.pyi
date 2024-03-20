# coding: utf-8

"""
    ClickUp API Reference

    This is the ClickUp API Reference where you can learn about specific endpoints and parameters in detail.  Browse the available endpoints using the sidebar on the left.  **Not sure where to begin?** [Get Started with the ClickUp API](https://clickup.com/api) 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from click_up_python_sdk import schemas  # noqa: F401


class Data2(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "duration",
            "at",
            "task",
            "wid",
            "start",
            "description",
            "id",
            "billable",
            "user",
            "tags",
        }
        
        class properties:
        
            @staticmethod
            def tags() -> typing.Type['Data2Tags']:
                return Data2Tags
            description = schemas.StrSchema
            id = schemas.StrSchema
        
            @staticmethod
            def task() -> typing.Type['Task6']:
                return Task6
            wid = schemas.StrSchema
        
            @staticmethod
            def user() -> typing.Type['User2']:
                return User2
            billable = schemas.BoolSchema
            start = schemas.StrSchema
            duration = schemas.IntSchema
            at = schemas.IntSchema
            __annotations__ = {
                "tags": tags,
                "description": description,
                "id": id,
                "task": task,
                "wid": wid,
                "user": user,
                "billable": billable,
                "start": start,
                "duration": duration,
                "at": at,
            }
    
    duration: MetaOapg.properties.duration
    at: MetaOapg.properties.at
    task: 'Task6'
    wid: MetaOapg.properties.wid
    start: MetaOapg.properties.start
    description: MetaOapg.properties.description
    id: MetaOapg.properties.id
    billable: MetaOapg.properties.billable
    user: 'User2'
    tags: 'Data2Tags'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> 'Data2Tags': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["task"]) -> 'Task6': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wid"]) -> MetaOapg.properties.wid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'User2': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billable"]) -> MetaOapg.properties.billable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start"]) -> MetaOapg.properties.start: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["at"]) -> MetaOapg.properties.at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tags", "description", "id", "task", "wid", "user", "billable", "start", "duration", "at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> 'Data2Tags': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["task"]) -> 'Task6': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wid"]) -> MetaOapg.properties.wid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> 'User2': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billable"]) -> MetaOapg.properties.billable: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start"]) -> MetaOapg.properties.start: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["at"]) -> MetaOapg.properties.at: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tags", "description", "id", "task", "wid", "user", "billable", "start", "duration", "at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        duration: typing.Union[MetaOapg.properties.duration, decimal.Decimal, int, ],
        at: typing.Union[MetaOapg.properties.at, decimal.Decimal, int, ],
        task: 'Task6',
        wid: typing.Union[MetaOapg.properties.wid, str, ],
        start: typing.Union[MetaOapg.properties.start, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        billable: typing.Union[MetaOapg.properties.billable, bool, ],
        user: 'User2',
        tags: 'Data2Tags',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Data2':
        return super().__new__(
            cls,
            *args,
            duration=duration,
            at=at,
            task=task,
            wid=wid,
            start=start,
            description=description,
            id=id,
            billable=billable,
            user=user,
            tags=tags,
            _configuration=_configuration,
            **kwargs,
        )

from click_up_python_sdk.model.data2_tags import Data2Tags
from click_up_python_sdk.model.task6 import Task6
from click_up_python_sdk.model.user2 import User2
