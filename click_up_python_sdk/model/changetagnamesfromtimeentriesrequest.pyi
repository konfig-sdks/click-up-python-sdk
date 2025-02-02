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


class Changetagnamesfromtimeentriesrequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "tag_bg",
            "name",
            "new_name",
            "tag_fg",
        }
        
        class properties:
            name = schemas.StrSchema
            new_name = schemas.StrSchema
            tag_bg = schemas.StrSchema
            tag_fg = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "new_name": new_name,
                "tag_bg": tag_bg,
                "tag_fg": tag_fg,
            }
    
    tag_bg: MetaOapg.properties.tag_bg
    name: MetaOapg.properties.name
    new_name: MetaOapg.properties.new_name
    tag_fg: MetaOapg.properties.tag_fg
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["new_name"]) -> MetaOapg.properties.new_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag_bg"]) -> MetaOapg.properties.tag_bg: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag_fg"]) -> MetaOapg.properties.tag_fg: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "new_name", "tag_bg", "tag_fg", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["new_name"]) -> MetaOapg.properties.new_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag_bg"]) -> MetaOapg.properties.tag_bg: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag_fg"]) -> MetaOapg.properties.tag_fg: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "new_name", "tag_bg", "tag_fg", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tag_bg: typing.Union[MetaOapg.properties.tag_bg, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        new_name: typing.Union[MetaOapg.properties.new_name, str, ],
        tag_fg: typing.Union[MetaOapg.properties.tag_fg, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Changetagnamesfromtimeentriesrequest':
        return super().__new__(
            cls,
            *args,
            tag_bg=tag_bg,
            name=name,
            new_name=new_name,
            tag_fg=tag_fg,
            _configuration=_configuration,
            **kwargs,
        )
