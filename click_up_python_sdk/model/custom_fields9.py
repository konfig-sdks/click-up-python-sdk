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


class CustomFields9(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "date_created",
            "hide_from_guests",
            "name",
            "type_config",
            "id",
            "type",
            "required",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            type = schemas.StrSchema
            type_config = schemas.DictSchema
            date_created = schemas.StrSchema
            hide_from_guests = schemas.BoolSchema
            required = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "type": type,
                "type_config": type_config,
                "date_created": date_created,
                "hide_from_guests": hide_from_guests,
                "required": required,
            }
    
    date_created: MetaOapg.properties.date_created
    hide_from_guests: MetaOapg.properties.hide_from_guests
    name: MetaOapg.properties.name
    type_config: MetaOapg.properties.type_config
    id: MetaOapg.properties.id
    type: MetaOapg.properties.type
    required: MetaOapg.properties.required
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type_config"]) -> MetaOapg.properties.type_config: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_created"]) -> MetaOapg.properties.date_created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hide_from_guests"]) -> MetaOapg.properties.hide_from_guests: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "type", "type_config", "date_created", "hide_from_guests", "required", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type_config"]) -> MetaOapg.properties.type_config: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_created"]) -> MetaOapg.properties.date_created: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hide_from_guests"]) -> MetaOapg.properties.hide_from_guests: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "type", "type_config", "date_created", "hide_from_guests", "required", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date_created: typing.Union[MetaOapg.properties.date_created, str, ],
        hide_from_guests: typing.Union[MetaOapg.properties.hide_from_guests, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        type_config: typing.Union[MetaOapg.properties.type_config, dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        required: typing.Union[MetaOapg.properties.required, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomFields9':
        return super().__new__(
            cls,
            *args,
            date_created=date_created,
            hide_from_guests=hide_from_guests,
            name=name,
            type_config=type_config,
            id=id,
            type=type,
            required=required,
            _configuration=_configuration,
            **kwargs,
        )
