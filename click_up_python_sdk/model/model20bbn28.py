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


class Model20bbn28(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "status_history",
            "current_status",
        }
        
        class properties:
        
            @staticmethod
            def current_status() -> typing.Type['CurrentStatus']:
                return CurrentStatus
            
            
            class status_history(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['StatusHistory']:
                        return StatusHistory
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['StatusHistory'], typing.List['StatusHistory']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'status_history':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'StatusHistory':
                    return super().__getitem__(i)
            __annotations__ = {
                "current_status": current_status,
                "status_history": status_history,
            }
    
    status_history: MetaOapg.properties.status_history
    current_status: 'CurrentStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_status"]) -> 'CurrentStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status_history"]) -> MetaOapg.properties.status_history: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["current_status", "status_history", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_status"]) -> 'CurrentStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status_history"]) -> MetaOapg.properties.status_history: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["current_status", "status_history", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        status_history: typing.Union[MetaOapg.properties.status_history, list, tuple, ],
        current_status: 'CurrentStatus',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Model20bbn28':
        return super().__new__(
            cls,
            *args,
            status_history=status_history,
            current_status=current_status,
            _configuration=_configuration,
            **kwargs,
        )

from click_up_python_sdk.model.current_status import CurrentStatus
from click_up_python_sdk.model.status_history import StatusHistory
