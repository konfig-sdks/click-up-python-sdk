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


class Removetagsfromtimeentriesrequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "time_entry_ids",
            "tags",
        }
        
        class properties:
            
            
            class tags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Tags10']:
                        return Tags10
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Tags10'], typing.List['Tags10']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tags':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Tags10':
                    return super().__getitem__(i)
        
            @staticmethod
            def time_entry_ids() -> typing.Type['RemovetagsfromtimeentriesrequestTimeEntryIds']:
                return RemovetagsfromtimeentriesrequestTimeEntryIds
            __annotations__ = {
                "tags": tags,
                "time_entry_ids": time_entry_ids,
            }
    
    time_entry_ids: 'RemovetagsfromtimeentriesrequestTimeEntryIds'
    tags: MetaOapg.properties.tags
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_entry_ids"]) -> 'RemovetagsfromtimeentriesrequestTimeEntryIds': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tags", "time_entry_ids", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_entry_ids"]) -> 'RemovetagsfromtimeentriesrequestTimeEntryIds': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tags", "time_entry_ids", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        time_entry_ids: 'RemovetagsfromtimeentriesrequestTimeEntryIds',
        tags: typing.Union[MetaOapg.properties.tags, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Removetagsfromtimeentriesrequest':
        return super().__new__(
            cls,
            *args,
            time_entry_ids=time_entry_ids,
            tags=tags,
            _configuration=_configuration,
            **kwargs,
        )

from click_up_python_sdk.model.removetagsfromtimeentriesrequest_time_entry_ids import RemovetagsfromtimeentriesrequestTimeEntryIds
from click_up_python_sdk.model.tags10 import Tags10
