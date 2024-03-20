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


class ProfileInfo(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "viewed_top_tier_user",
            "verified_ambassador",
            "viewed_verified_consultant",
            "verified_consultant",
            "viewed_verified_ambassador",
            "display_profile",
            "top_tier_user",
        }
        
        class properties:
            display_profile = schemas.AnyTypeSchema
            verified_ambassador = schemas.AnyTypeSchema
            verified_consultant = schemas.AnyTypeSchema
            top_tier_user = schemas.AnyTypeSchema
            viewed_verified_ambassador = schemas.AnyTypeSchema
            viewed_verified_consultant = schemas.AnyTypeSchema
            viewed_top_tier_user = schemas.AnyTypeSchema
            __annotations__ = {
                "display_profile": display_profile,
                "verified_ambassador": verified_ambassador,
                "verified_consultant": verified_consultant,
                "top_tier_user": top_tier_user,
                "viewed_verified_ambassador": viewed_verified_ambassador,
                "viewed_verified_consultant": viewed_verified_consultant,
                "viewed_top_tier_user": viewed_top_tier_user,
            }
    
    viewed_top_tier_user: MetaOapg.properties.viewed_top_tier_user
    verified_ambassador: MetaOapg.properties.verified_ambassador
    viewed_verified_consultant: MetaOapg.properties.viewed_verified_consultant
    verified_consultant: MetaOapg.properties.verified_consultant
    viewed_verified_ambassador: MetaOapg.properties.viewed_verified_ambassador
    display_profile: MetaOapg.properties.display_profile
    top_tier_user: MetaOapg.properties.top_tier_user
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_profile"]) -> MetaOapg.properties.display_profile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verified_ambassador"]) -> MetaOapg.properties.verified_ambassador: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verified_consultant"]) -> MetaOapg.properties.verified_consultant: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["top_tier_user"]) -> MetaOapg.properties.top_tier_user: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["viewed_verified_ambassador"]) -> MetaOapg.properties.viewed_verified_ambassador: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["viewed_verified_consultant"]) -> MetaOapg.properties.viewed_verified_consultant: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["viewed_top_tier_user"]) -> MetaOapg.properties.viewed_top_tier_user: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["display_profile", "verified_ambassador", "verified_consultant", "top_tier_user", "viewed_verified_ambassador", "viewed_verified_consultant", "viewed_top_tier_user", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_profile"]) -> MetaOapg.properties.display_profile: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verified_ambassador"]) -> MetaOapg.properties.verified_ambassador: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verified_consultant"]) -> MetaOapg.properties.verified_consultant: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["top_tier_user"]) -> MetaOapg.properties.top_tier_user: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["viewed_verified_ambassador"]) -> MetaOapg.properties.viewed_verified_ambassador: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["viewed_verified_consultant"]) -> MetaOapg.properties.viewed_verified_consultant: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["viewed_top_tier_user"]) -> MetaOapg.properties.viewed_top_tier_user: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["display_profile", "verified_ambassador", "verified_consultant", "top_tier_user", "viewed_verified_ambassador", "viewed_verified_consultant", "viewed_top_tier_user", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        viewed_top_tier_user: typing.Union[MetaOapg.properties.viewed_top_tier_user, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        verified_ambassador: typing.Union[MetaOapg.properties.verified_ambassador, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        viewed_verified_consultant: typing.Union[MetaOapg.properties.viewed_verified_consultant, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        verified_consultant: typing.Union[MetaOapg.properties.verified_consultant, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        viewed_verified_ambassador: typing.Union[MetaOapg.properties.viewed_verified_ambassador, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        display_profile: typing.Union[MetaOapg.properties.display_profile, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        top_tier_user: typing.Union[MetaOapg.properties.top_tier_user, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProfileInfo':
        return super().__new__(
            cls,
            *args,
            viewed_top_tier_user=viewed_top_tier_user,
            verified_ambassador=verified_ambassador,
            viewed_verified_consultant=viewed_verified_consultant,
            verified_consultant=verified_consultant,
            viewed_verified_ambassador=viewed_verified_ambassador,
            display_profile=display_profile,
            top_tier_user=top_tier_user,
            _configuration=_configuration,
            **kwargs,
        )