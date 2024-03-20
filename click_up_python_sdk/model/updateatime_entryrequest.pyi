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


class UpdateatimeEntryrequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "tags",
        }
        
        class properties:
            
            
            class tags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Tags6']:
                        return Tags6
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Tags6'], typing.List['Tags6']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tags':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Tags6':
                    return super().__getitem__(i)
            description = schemas.StrSchema
            tag_action = schemas.StrSchema
            start = schemas.IntSchema
            end = schemas.IntSchema
            tid = schemas.StrSchema
            billable = schemas.BoolSchema
            duration = schemas.IntSchema
            __annotations__ = {
                "tags": tags,
                "description": description,
                "tag_action": tag_action,
                "start": start,
                "end": end,
                "tid": tid,
                "billable": billable,
                "duration": duration,
            }
    
    tags: MetaOapg.properties.tags
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag_action"]) -> MetaOapg.properties.tag_action: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start"]) -> MetaOapg.properties.start: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end"]) -> MetaOapg.properties.end: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tid"]) -> MetaOapg.properties.tid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billable"]) -> MetaOapg.properties.billable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tags", "description", "tag_action", "start", "end", "tid", "billable", "duration", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag_action"]) -> typing.Union[MetaOapg.properties.tag_action, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start"]) -> typing.Union[MetaOapg.properties.start, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end"]) -> typing.Union[MetaOapg.properties.end, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tid"]) -> typing.Union[MetaOapg.properties.tid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billable"]) -> typing.Union[MetaOapg.properties.billable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration"]) -> typing.Union[MetaOapg.properties.duration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tags", "description", "tag_action", "start", "end", "tid", "billable", "duration", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tags: typing.Union[MetaOapg.properties.tags, list, tuple, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        tag_action: typing.Union[MetaOapg.properties.tag_action, str, schemas.Unset] = schemas.unset,
        start: typing.Union[MetaOapg.properties.start, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        end: typing.Union[MetaOapg.properties.end, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tid: typing.Union[MetaOapg.properties.tid, str, schemas.Unset] = schemas.unset,
        billable: typing.Union[MetaOapg.properties.billable, bool, schemas.Unset] = schemas.unset,
        duration: typing.Union[MetaOapg.properties.duration, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateatimeEntryrequest':
        return super().__new__(
            cls,
            *args,
            tags=tags,
            description=description,
            tag_action=tag_action,
            start=start,
            end=end,
            tid=tid,
            billable=billable,
            duration=duration,
            _configuration=_configuration,
            **kwargs,
        )

from click_up_python_sdk.model.tags6 import Tags6