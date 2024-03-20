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


class UpdateSpacerequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "features",
            "private",
            "color",
            "name",
            "admin_can_manage",
            "multiple_assignees",
        }
        
        class properties:
            name = schemas.StrSchema
            color = schemas.StrSchema
            private = schemas.BoolSchema
            admin_can_manage = schemas.BoolSchema
            multiple_assignees = schemas.BoolSchema
        
            @staticmethod
            def features() -> typing.Type['Features']:
                return Features
            __annotations__ = {
                "name": name,
                "color": color,
                "private": private,
                "admin_can_manage": admin_can_manage,
                "multiple_assignees": multiple_assignees,
                "features": features,
            }
    
    features: 'Features'
    private: MetaOapg.properties.private
    color: MetaOapg.properties.color
    name: MetaOapg.properties.name
    admin_can_manage: MetaOapg.properties.admin_can_manage
    multiple_assignees: MetaOapg.properties.multiple_assignees
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["private"]) -> MetaOapg.properties.private: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["admin_can_manage"]) -> MetaOapg.properties.admin_can_manage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["multiple_assignees"]) -> MetaOapg.properties.multiple_assignees: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["features"]) -> 'Features': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "color", "private", "admin_can_manage", "multiple_assignees", "features", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["private"]) -> MetaOapg.properties.private: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["admin_can_manage"]) -> MetaOapg.properties.admin_can_manage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["multiple_assignees"]) -> MetaOapg.properties.multiple_assignees: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["features"]) -> 'Features': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "color", "private", "admin_can_manage", "multiple_assignees", "features", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        features: 'Features',
        private: typing.Union[MetaOapg.properties.private, bool, ],
        color: typing.Union[MetaOapg.properties.color, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        admin_can_manage: typing.Union[MetaOapg.properties.admin_can_manage, bool, ],
        multiple_assignees: typing.Union[MetaOapg.properties.multiple_assignees, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateSpacerequest':
        return super().__new__(
            cls,
            *args,
            features=features,
            private=private,
            color=color,
            name=name,
            admin_can_manage=admin_can_manage,
            multiple_assignees=multiple_assignees,
            _configuration=_configuration,
            **kwargs,
        )

from click_up_python_sdk.model.features import Features
