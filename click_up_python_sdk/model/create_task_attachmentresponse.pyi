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


class CreateTaskAttachmentresponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "date",
            "thumbnail_small",
            "extension",
            "thumbnail_large",
            "id",
            "title",
            "version",
            "url",
        }
        
        class properties:
            title = schemas.StrSchema
            version = schemas.StrSchema
            id = schemas.StrSchema
            date = schemas.IntSchema
            extension = schemas.StrSchema
            thumbnail_small = schemas.StrSchema
            thumbnail_large = schemas.StrSchema
            url = schemas.StrSchema
            __annotations__ = {
                "title": title,
                "version": version,
                "id": id,
                "date": date,
                "extension": extension,
                "thumbnail_small": thumbnail_small,
                "thumbnail_large": thumbnail_large,
                "url": url,
            }
    
    date: MetaOapg.properties.date
    thumbnail_small: MetaOapg.properties.thumbnail_small
    extension: MetaOapg.properties.extension
    thumbnail_large: MetaOapg.properties.thumbnail_large
    id: MetaOapg.properties.id
    title: MetaOapg.properties.title
    version: MetaOapg.properties.version
    url: MetaOapg.properties.url
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extension"]) -> MetaOapg.properties.extension: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thumbnail_small"]) -> MetaOapg.properties.thumbnail_small: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thumbnail_large"]) -> MetaOapg.properties.thumbnail_large: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "version", "id", "date", "extension", "thumbnail_small", "thumbnail_large", "url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extension"]) -> MetaOapg.properties.extension: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thumbnail_small"]) -> MetaOapg.properties.thumbnail_small: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thumbnail_large"]) -> MetaOapg.properties.thumbnail_large: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "version", "id", "date", "extension", "thumbnail_small", "thumbnail_large", "url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date: typing.Union[MetaOapg.properties.date, decimal.Decimal, int, ],
        thumbnail_small: typing.Union[MetaOapg.properties.thumbnail_small, str, ],
        extension: typing.Union[MetaOapg.properties.extension, str, ],
        thumbnail_large: typing.Union[MetaOapg.properties.thumbnail_large, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        version: typing.Union[MetaOapg.properties.version, str, ],
        url: typing.Union[MetaOapg.properties.url, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateTaskAttachmentresponse':
        return super().__new__(
            cls,
            *args,
            date=date,
            thumbnail_small=thumbnail_small,
            extension=extension,
            thumbnail_large=thumbnail_large,
            id=id,
            title=title,
            version=version,
            url=url,
            _configuration=_configuration,
            **kwargs,
        )