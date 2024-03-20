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


class Guest5(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "shared",
            "can_see_time_estimated",
            "can_edit_tags",
            "can_see_time_spent",
            "invited_by",
            "user",
        }
        
        class properties:
        
            @staticmethod
            def user() -> typing.Type['User7']:
                return User7
        
            @staticmethod
            def invited_by() -> typing.Type['InvitedBy']:
                return InvitedBy
            can_see_time_spent = schemas.BoolSchema
            can_see_time_estimated = schemas.BoolSchema
            can_edit_tags = schemas.BoolSchema
        
            @staticmethod
            def shared() -> typing.Type['Shared5']:
                return Shared5
            __annotations__ = {
                "user": user,
                "invited_by": invited_by,
                "can_see_time_spent": can_see_time_spent,
                "can_see_time_estimated": can_see_time_estimated,
                "can_edit_tags": can_edit_tags,
                "shared": shared,
            }
    
    shared: 'Shared5'
    can_see_time_estimated: MetaOapg.properties.can_see_time_estimated
    can_edit_tags: MetaOapg.properties.can_edit_tags
    can_see_time_spent: MetaOapg.properties.can_see_time_spent
    invited_by: 'InvitedBy'
    user: 'User7'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'User7': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invited_by"]) -> 'InvitedBy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["can_see_time_spent"]) -> MetaOapg.properties.can_see_time_spent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["can_see_time_estimated"]) -> MetaOapg.properties.can_see_time_estimated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["can_edit_tags"]) -> MetaOapg.properties.can_edit_tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shared"]) -> 'Shared5': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["user", "invited_by", "can_see_time_spent", "can_see_time_estimated", "can_edit_tags", "shared", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> 'User7': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invited_by"]) -> 'InvitedBy': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["can_see_time_spent"]) -> MetaOapg.properties.can_see_time_spent: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["can_see_time_estimated"]) -> MetaOapg.properties.can_see_time_estimated: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["can_edit_tags"]) -> MetaOapg.properties.can_edit_tags: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shared"]) -> 'Shared5': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["user", "invited_by", "can_see_time_spent", "can_see_time_estimated", "can_edit_tags", "shared", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        shared: 'Shared5',
        can_see_time_estimated: typing.Union[MetaOapg.properties.can_see_time_estimated, bool, ],
        can_edit_tags: typing.Union[MetaOapg.properties.can_edit_tags, bool, ],
        can_see_time_spent: typing.Union[MetaOapg.properties.can_see_time_spent, bool, ],
        invited_by: 'InvitedBy',
        user: 'User7',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Guest5':
        return super().__new__(
            cls,
            *args,
            shared=shared,
            can_see_time_estimated=can_see_time_estimated,
            can_edit_tags=can_edit_tags,
            can_see_time_spent=can_see_time_spent,
            invited_by=invited_by,
            user=user,
            _configuration=_configuration,
            **kwargs,
        )

from click_up_python_sdk.model.invited_by import InvitedBy
from click_up_python_sdk.model.shared5 import Shared5
from click_up_python_sdk.model.user7 import User7