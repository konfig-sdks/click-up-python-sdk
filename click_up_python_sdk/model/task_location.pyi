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


class TaskLocation(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "list_id",
            "space_name",
            "folder_name",
            "list_name",
            "folder_id",
            "space_id",
        }
        
        class properties:
            list_id = schemas.IntSchema
            folder_id = schemas.IntSchema
            space_id = schemas.IntSchema
            list_name = schemas.StrSchema
            folder_name = schemas.StrSchema
            space_name = schemas.StrSchema
            __annotations__ = {
                "list_id": list_id,
                "folder_id": folder_id,
                "space_id": space_id,
                "list_name": list_name,
                "folder_name": folder_name,
                "space_name": space_name,
            }
    
    list_id: MetaOapg.properties.list_id
    space_name: MetaOapg.properties.space_name
    folder_name: MetaOapg.properties.folder_name
    list_name: MetaOapg.properties.list_name
    folder_id: MetaOapg.properties.folder_id
    space_id: MetaOapg.properties.space_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["list_id"]) -> MetaOapg.properties.list_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["folder_id"]) -> MetaOapg.properties.folder_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["space_id"]) -> MetaOapg.properties.space_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["list_name"]) -> MetaOapg.properties.list_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["folder_name"]) -> MetaOapg.properties.folder_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["space_name"]) -> MetaOapg.properties.space_name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["list_id", "folder_id", "space_id", "list_name", "folder_name", "space_name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["list_id"]) -> MetaOapg.properties.list_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["folder_id"]) -> MetaOapg.properties.folder_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["space_id"]) -> MetaOapg.properties.space_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["list_name"]) -> MetaOapg.properties.list_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["folder_name"]) -> MetaOapg.properties.folder_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["space_name"]) -> MetaOapg.properties.space_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["list_id", "folder_id", "space_id", "list_name", "folder_name", "space_name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        list_id: typing.Union[MetaOapg.properties.list_id, decimal.Decimal, int, ],
        space_name: typing.Union[MetaOapg.properties.space_name, str, ],
        folder_name: typing.Union[MetaOapg.properties.folder_name, str, ],
        list_name: typing.Union[MetaOapg.properties.list_name, str, ],
        folder_id: typing.Union[MetaOapg.properties.folder_id, decimal.Decimal, int, ],
        space_id: typing.Union[MetaOapg.properties.space_id, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TaskLocation':
        return super().__new__(
            cls,
            *args,
            list_id=list_id,
            space_name=space_name,
            folder_name=folder_name,
            list_name=list_name,
            folder_id=folder_id,
            space_id=space_id,
            _configuration=_configuration,
            **kwargs,
        )
