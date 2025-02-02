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


class User21(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.IntSchema
            username = schemas.StrSchema
            email = schemas.StrSchema
            color = schemas.AnyTypeSchema
            profilePicture = schemas.AnyTypeSchema
            initials = schemas.StrSchema
            role = schemas.IntSchema
        
            @staticmethod
            def custom_role() -> typing.Type['CustomRole']:
                return CustomRole
            last_active = schemas.AnyTypeSchema
            date_joined = schemas.AnyTypeSchema
            date_invited = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "username": username,
                "email": email,
                "color": color,
                "profilePicture": profilePicture,
                "initials": initials,
                "role": role,
                "custom_role": custom_role,
                "last_active": last_active,
                "date_joined": date_joined,
                "date_invited": date_invited,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profilePicture"]) -> MetaOapg.properties.profilePicture: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["initials"]) -> MetaOapg.properties.initials: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_role"]) -> 'CustomRole': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_active"]) -> MetaOapg.properties.last_active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_joined"]) -> MetaOapg.properties.date_joined: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_invited"]) -> MetaOapg.properties.date_invited: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "username", "email", "color", "profilePicture", "initials", "role", "custom_role", "last_active", "date_joined", "date_invited", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profilePicture"]) -> typing.Union[MetaOapg.properties.profilePicture, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["initials"]) -> typing.Union[MetaOapg.properties.initials, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role"]) -> typing.Union[MetaOapg.properties.role, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_role"]) -> typing.Union['CustomRole', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_active"]) -> typing.Union[MetaOapg.properties.last_active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_joined"]) -> typing.Union[MetaOapg.properties.date_joined, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_invited"]) -> typing.Union[MetaOapg.properties.date_invited, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "username", "email", "color", "profilePicture", "initials", "role", "custom_role", "last_active", "date_joined", "date_invited", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        color: typing.Union[MetaOapg.properties.color, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        profilePicture: typing.Union[MetaOapg.properties.profilePicture, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        initials: typing.Union[MetaOapg.properties.initials, str, schemas.Unset] = schemas.unset,
        role: typing.Union[MetaOapg.properties.role, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        custom_role: typing.Union['CustomRole', schemas.Unset] = schemas.unset,
        last_active: typing.Union[MetaOapg.properties.last_active, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        date_joined: typing.Union[MetaOapg.properties.date_joined, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        date_invited: typing.Union[MetaOapg.properties.date_invited, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'User21':
        return super().__new__(
            cls,
            *args,
            id=id,
            username=username,
            email=email,
            color=color,
            profilePicture=profilePicture,
            initials=initials,
            role=role,
            custom_role=custom_role,
            last_active=last_active,
            date_joined=date_joined,
            date_invited=date_invited,
            _configuration=_configuration,
            **kwargs,
        )

from click_up_python_sdk.model.custom_role import CustomRole
