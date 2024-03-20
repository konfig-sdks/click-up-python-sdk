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


class CreateTaskCommentrequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "comment_text",
            "assignee",
            "notify_all",
        }
        
        class properties:
            comment_text = schemas.StrSchema
            assignee = schemas.IntSchema
            notify_all = schemas.BoolSchema
            __annotations__ = {
                "comment_text": comment_text,
                "assignee": assignee,
                "notify_all": notify_all,
            }
    
    comment_text: MetaOapg.properties.comment_text
    assignee: MetaOapg.properties.assignee
    notify_all: MetaOapg.properties.notify_all
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment_text"]) -> MetaOapg.properties.comment_text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignee"]) -> MetaOapg.properties.assignee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notify_all"]) -> MetaOapg.properties.notify_all: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["comment_text", "assignee", "notify_all", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment_text"]) -> MetaOapg.properties.comment_text: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignee"]) -> MetaOapg.properties.assignee: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notify_all"]) -> MetaOapg.properties.notify_all: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["comment_text", "assignee", "notify_all", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        comment_text: typing.Union[MetaOapg.properties.comment_text, str, ],
        assignee: typing.Union[MetaOapg.properties.assignee, decimal.Decimal, int, ],
        notify_all: typing.Union[MetaOapg.properties.notify_all, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateTaskCommentrequest':
        return super().__new__(
            cls,
            *args,
            comment_text=comment_text,
            assignee=assignee,
            notify_all=notify_all,
            _configuration=_configuration,
            **kwargs,
        )
