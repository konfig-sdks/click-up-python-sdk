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


class StatusHistory(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "color",
            "orderindex",
            "total_time",
            "type",
            "status",
        }
        
        class properties:
            status = schemas.StrSchema
            color = schemas.StrSchema
            type = schemas.StrSchema
        
            @staticmethod
            def total_time() -> typing.Type['TotalTime']:
                return TotalTime
            orderindex = schemas.IntSchema
            __annotations__ = {
                "status": status,
                "color": color,
                "type": type,
                "total_time": total_time,
                "orderindex": orderindex,
            }
    
    color: MetaOapg.properties.color
    orderindex: MetaOapg.properties.orderindex
    total_time: 'TotalTime'
    type: MetaOapg.properties.type
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_time"]) -> 'TotalTime': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orderindex"]) -> MetaOapg.properties.orderindex: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "color", "type", "total_time", "orderindex", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_time"]) -> 'TotalTime': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orderindex"]) -> MetaOapg.properties.orderindex: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "color", "type", "total_time", "orderindex", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        color: typing.Union[MetaOapg.properties.color, str, ],
        orderindex: typing.Union[MetaOapg.properties.orderindex, decimal.Decimal, int, ],
        total_time: 'TotalTime',
        type: typing.Union[MetaOapg.properties.type, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StatusHistory':
        return super().__new__(
            cls,
            *args,
            color=color,
            orderindex=orderindex,
            total_time=total_time,
            type=type,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from click_up_python_sdk.model.total_time import TotalTime
