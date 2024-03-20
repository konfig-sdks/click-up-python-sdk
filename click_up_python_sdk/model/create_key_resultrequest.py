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


class CreateKeyResultrequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "steps_start",
            "unit",
            "name",
            "steps_end",
            "owners",
            "task_ids",
            "type",
            "list_ids",
        }
        
        class properties:
            name = schemas.StrSchema
        
            @staticmethod
            def owners() -> typing.Type['CreateKeyResultrequestOwners']:
                return CreateKeyResultrequestOwners
            type = schemas.StrSchema
            steps_start = schemas.IntSchema
            steps_end = schemas.IntSchema
            unit = schemas.StrSchema
        
            @staticmethod
            def task_ids() -> typing.Type['CreateKeyResultrequestTaskIds']:
                return CreateKeyResultrequestTaskIds
        
            @staticmethod
            def list_ids() -> typing.Type['CreateKeyResultrequestListIds']:
                return CreateKeyResultrequestListIds
            __annotations__ = {
                "name": name,
                "owners": owners,
                "type": type,
                "steps_start": steps_start,
                "steps_end": steps_end,
                "unit": unit,
                "task_ids": task_ids,
                "list_ids": list_ids,
            }
    
    steps_start: MetaOapg.properties.steps_start
    unit: MetaOapg.properties.unit
    name: MetaOapg.properties.name
    steps_end: MetaOapg.properties.steps_end
    owners: 'CreateKeyResultrequestOwners'
    task_ids: 'CreateKeyResultrequestTaskIds'
    type: MetaOapg.properties.type
    list_ids: 'CreateKeyResultrequestListIds'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owners"]) -> 'CreateKeyResultrequestOwners': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["steps_start"]) -> MetaOapg.properties.steps_start: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["steps_end"]) -> MetaOapg.properties.steps_end: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unit"]) -> MetaOapg.properties.unit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["task_ids"]) -> 'CreateKeyResultrequestTaskIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["list_ids"]) -> 'CreateKeyResultrequestListIds': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "owners", "type", "steps_start", "steps_end", "unit", "task_ids", "list_ids", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owners"]) -> 'CreateKeyResultrequestOwners': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["steps_start"]) -> MetaOapg.properties.steps_start: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["steps_end"]) -> MetaOapg.properties.steps_end: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unit"]) -> MetaOapg.properties.unit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["task_ids"]) -> 'CreateKeyResultrequestTaskIds': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["list_ids"]) -> 'CreateKeyResultrequestListIds': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "owners", "type", "steps_start", "steps_end", "unit", "task_ids", "list_ids", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        steps_start: typing.Union[MetaOapg.properties.steps_start, decimal.Decimal, int, ],
        unit: typing.Union[MetaOapg.properties.unit, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        steps_end: typing.Union[MetaOapg.properties.steps_end, decimal.Decimal, int, ],
        owners: 'CreateKeyResultrequestOwners',
        task_ids: 'CreateKeyResultrequestTaskIds',
        type: typing.Union[MetaOapg.properties.type, str, ],
        list_ids: 'CreateKeyResultrequestListIds',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateKeyResultrequest':
        return super().__new__(
            cls,
            *args,
            steps_start=steps_start,
            unit=unit,
            name=name,
            steps_end=steps_end,
            owners=owners,
            task_ids=task_ids,
            type=type,
            list_ids=list_ids,
            _configuration=_configuration,
            **kwargs,
        )

from click_up_python_sdk.model.create_key_resultrequest_list_ids import CreateKeyResultrequestListIds
from click_up_python_sdk.model.create_key_resultrequest_owners import CreateKeyResultrequestOwners
from click_up_python_sdk.model.create_key_resultrequest_task_ids import CreateKeyResultrequestTaskIds
