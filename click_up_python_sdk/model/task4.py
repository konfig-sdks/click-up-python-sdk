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


class Task4(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "custom_type",
            "custom_id",
            "name",
            "id",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
            custom_id = schemas.StrSchema
            name = schemas.StrSchema
        
            @staticmethod
            def status() -> typing.Type['Status']:
                return Status
            custom_type = schemas.AnyTypeSchema
            __annotations__ = {
                "id": id,
                "custom_id": custom_id,
                "name": name,
                "status": status,
                "custom_type": custom_type,
            }
    
    custom_type: MetaOapg.properties.custom_type
    custom_id: MetaOapg.properties.custom_id
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    status: 'Status'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_id"]) -> MetaOapg.properties.custom_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'Status': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_type"]) -> MetaOapg.properties.custom_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "custom_id", "name", "status", "custom_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_id"]) -> MetaOapg.properties.custom_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'Status': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_type"]) -> MetaOapg.properties.custom_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "custom_id", "name", "status", "custom_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        custom_type: typing.Union[MetaOapg.properties.custom_type, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        custom_id: typing.Union[MetaOapg.properties.custom_id, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        status: 'Status',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Task4':
        return super().__new__(
            cls,
            *args,
            custom_type=custom_type,
            custom_id=custom_id,
            name=name,
            id=id,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from click_up_python_sdk.model.status import Status