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


class UpdateSpaceresponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "features",
            "private",
            "name",
            "statuses",
            "id",
            "multiple_assignees",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            private = schemas.BoolSchema
            
            
            class statuses(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Status']:
                        return Status
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Status'], typing.List['Status']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'statuses':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Status':
                    return super().__getitem__(i)
            multiple_assignees = schemas.BoolSchema
        
            @staticmethod
            def features() -> typing.Type['Features']:
                return Features
            __annotations__ = {
                "id": id,
                "name": name,
                "private": private,
                "statuses": statuses,
                "multiple_assignees": multiple_assignees,
                "features": features,
            }
    
    features: 'Features'
    private: MetaOapg.properties.private
    name: MetaOapg.properties.name
    statuses: MetaOapg.properties.statuses
    id: MetaOapg.properties.id
    multiple_assignees: MetaOapg.properties.multiple_assignees
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["private"]) -> MetaOapg.properties.private: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statuses"]) -> MetaOapg.properties.statuses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["multiple_assignees"]) -> MetaOapg.properties.multiple_assignees: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["features"]) -> 'Features': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "private", "statuses", "multiple_assignees", "features", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["private"]) -> MetaOapg.properties.private: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statuses"]) -> MetaOapg.properties.statuses: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["multiple_assignees"]) -> MetaOapg.properties.multiple_assignees: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["features"]) -> 'Features': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "private", "statuses", "multiple_assignees", "features", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        features: 'Features',
        private: typing.Union[MetaOapg.properties.private, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        statuses: typing.Union[MetaOapg.properties.statuses, list, tuple, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        multiple_assignees: typing.Union[MetaOapg.properties.multiple_assignees, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateSpaceresponse':
        return super().__new__(
            cls,
            *args,
            features=features,
            private=private,
            name=name,
            statuses=statuses,
            id=id,
            multiple_assignees=multiple_assignees,
            _configuration=_configuration,
            **kwargs,
        )

from click_up_python_sdk.model.features import Features
from click_up_python_sdk.model.status import Status