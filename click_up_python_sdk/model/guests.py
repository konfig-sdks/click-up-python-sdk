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


class Guests(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "empty_guest_seats",
            "total_guest_seats",
            "filled_guest_seats",
        }
        
        class properties:
            filled_guest_seats = schemas.IntSchema
            total_guest_seats = schemas.IntSchema
            empty_guest_seats = schemas.IntSchema
            __annotations__ = {
                "filled_guest_seats": filled_guest_seats,
                "total_guest_seats": total_guest_seats,
                "empty_guest_seats": empty_guest_seats,
            }
    
    empty_guest_seats: MetaOapg.properties.empty_guest_seats
    total_guest_seats: MetaOapg.properties.total_guest_seats
    filled_guest_seats: MetaOapg.properties.filled_guest_seats
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filled_guest_seats"]) -> MetaOapg.properties.filled_guest_seats: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_guest_seats"]) -> MetaOapg.properties.total_guest_seats: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["empty_guest_seats"]) -> MetaOapg.properties.empty_guest_seats: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["filled_guest_seats", "total_guest_seats", "empty_guest_seats", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filled_guest_seats"]) -> MetaOapg.properties.filled_guest_seats: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_guest_seats"]) -> MetaOapg.properties.total_guest_seats: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["empty_guest_seats"]) -> MetaOapg.properties.empty_guest_seats: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["filled_guest_seats", "total_guest_seats", "empty_guest_seats", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        empty_guest_seats: typing.Union[MetaOapg.properties.empty_guest_seats, decimal.Decimal, int, ],
        total_guest_seats: typing.Union[MetaOapg.properties.total_guest_seats, decimal.Decimal, int, ],
        filled_guest_seats: typing.Union[MetaOapg.properties.filled_guest_seats, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Guests':
        return super().__new__(
            cls,
            *args,
            empty_guest_seats=empty_guest_seats,
            total_guest_seats=total_guest_seats,
            filled_guest_seats=filled_guest_seats,
            _configuration=_configuration,
            **kwargs,
        )