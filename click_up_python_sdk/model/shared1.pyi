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


class Shared1(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "folders",
            "lists",
            "tasks",
        }
        
        class properties:
            
            
            class tasks(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Task2']:
                        return Task2
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Task2'], typing.List['Task2']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tasks':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Task2':
                    return super().__getitem__(i)
        
            @staticmethod
            def lists() -> typing.Type['Shared1Lists']:
                return Shared1Lists
        
            @staticmethod
            def folders() -> typing.Type['Shared1Folders']:
                return Shared1Folders
            __annotations__ = {
                "tasks": tasks,
                "lists": lists,
                "folders": folders,
            }
    
    folders: 'Shared1Folders'
    lists: 'Shared1Lists'
    tasks: MetaOapg.properties.tasks
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tasks"]) -> MetaOapg.properties.tasks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lists"]) -> 'Shared1Lists': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["folders"]) -> 'Shared1Folders': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tasks", "lists", "folders", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tasks"]) -> MetaOapg.properties.tasks: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lists"]) -> 'Shared1Lists': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["folders"]) -> 'Shared1Folders': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tasks", "lists", "folders", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        folders: 'Shared1Folders',
        lists: 'Shared1Lists',
        tasks: typing.Union[MetaOapg.properties.tasks, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Shared1':
        return super().__new__(
            cls,
            *args,
            folders=folders,
            lists=lists,
            tasks=tasks,
            _configuration=_configuration,
            **kwargs,
        )

from click_up_python_sdk.model.shared1_folders import Shared1Folders
from click_up_python_sdk.model.shared1_lists import Shared1Lists
from click_up_python_sdk.model.task2 import Task2
