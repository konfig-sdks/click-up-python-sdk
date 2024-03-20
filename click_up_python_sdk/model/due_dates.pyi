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


class DueDates(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "remap_due_dates",
            "remap_closed_due_date",
            "enabled",
            "start_date",
        }
        
        class properties:
            enabled = schemas.BoolSchema
            start_date = schemas.BoolSchema
            remap_due_dates = schemas.BoolSchema
            remap_closed_due_date = schemas.BoolSchema
            __annotations__ = {
                "enabled": enabled,
                "start_date": start_date,
                "remap_due_dates": remap_due_dates,
                "remap_closed_due_date": remap_closed_due_date,
            }
    
    remap_due_dates: MetaOapg.properties.remap_due_dates
    remap_closed_due_date: MetaOapg.properties.remap_closed_due_date
    enabled: MetaOapg.properties.enabled
    start_date: MetaOapg.properties.start_date
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["remap_due_dates"]) -> MetaOapg.properties.remap_due_dates: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["remap_closed_due_date"]) -> MetaOapg.properties.remap_closed_due_date: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["enabled", "start_date", "remap_due_dates", "remap_closed_due_date", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["remap_due_dates"]) -> MetaOapg.properties.remap_due_dates: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["remap_closed_due_date"]) -> MetaOapg.properties.remap_closed_due_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["enabled", "start_date", "remap_due_dates", "remap_closed_due_date", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        remap_due_dates: typing.Union[MetaOapg.properties.remap_due_dates, bool, ],
        remap_closed_due_date: typing.Union[MetaOapg.properties.remap_closed_due_date, bool, ],
        enabled: typing.Union[MetaOapg.properties.enabled, bool, ],
        start_date: typing.Union[MetaOapg.properties.start_date, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DueDates':
        return super().__new__(
            cls,
            *args,
            remap_due_dates=remap_due_dates,
            remap_closed_due_date=remap_closed_due_date,
            enabled=enabled,
            start_date=start_date,
            _configuration=_configuration,
            **kwargs,
        )