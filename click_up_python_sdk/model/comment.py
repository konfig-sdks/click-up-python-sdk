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


class Comment(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "date",
            "comment_text",
            "comment",
            "reactions",
            "assigned_by",
            "assignee",
            "id",
            "user",
            "resolved",
        }
        
        class properties:
            id = schemas.StrSchema
            
            
            class comment(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Comment1']:
                        return Comment1
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Comment1'], typing.List['Comment1']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'comment':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Comment1':
                    return super().__getitem__(i)
            comment_text = schemas.StrSchema
        
            @staticmethod
            def user() -> typing.Type['User2']:
                return User2
            resolved = schemas.BoolSchema
        
            @staticmethod
            def assignee() -> typing.Type['Assignee']:
                return Assignee
        
            @staticmethod
            def assigned_by() -> typing.Type['AssignedBy']:
                return AssignedBy
        
            @staticmethod
            def reactions() -> typing.Type['CommentReactions']:
                return CommentReactions
            date = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "comment": comment,
                "comment_text": comment_text,
                "user": user,
                "resolved": resolved,
                "assignee": assignee,
                "assigned_by": assigned_by,
                "reactions": reactions,
                "date": date,
            }
    
    date: MetaOapg.properties.date
    comment_text: MetaOapg.properties.comment_text
    comment: MetaOapg.properties.comment
    reactions: 'CommentReactions'
    assigned_by: 'AssignedBy'
    assignee: 'Assignee'
    id: MetaOapg.properties.id
    user: 'User2'
    resolved: MetaOapg.properties.resolved
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment_text"]) -> MetaOapg.properties.comment_text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'User2': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resolved"]) -> MetaOapg.properties.resolved: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignee"]) -> 'Assignee': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assigned_by"]) -> 'AssignedBy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reactions"]) -> 'CommentReactions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "comment", "comment_text", "user", "resolved", "assignee", "assigned_by", "reactions", "date", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment_text"]) -> MetaOapg.properties.comment_text: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> 'User2': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resolved"]) -> MetaOapg.properties.resolved: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignee"]) -> 'Assignee': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assigned_by"]) -> 'AssignedBy': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reactions"]) -> 'CommentReactions': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "comment", "comment_text", "user", "resolved", "assignee", "assigned_by", "reactions", "date", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date: typing.Union[MetaOapg.properties.date, str, ],
        comment_text: typing.Union[MetaOapg.properties.comment_text, str, ],
        comment: typing.Union[MetaOapg.properties.comment, list, tuple, ],
        reactions: 'CommentReactions',
        assigned_by: 'AssignedBy',
        assignee: 'Assignee',
        id: typing.Union[MetaOapg.properties.id, str, ],
        user: 'User2',
        resolved: typing.Union[MetaOapg.properties.resolved, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Comment':
        return super().__new__(
            cls,
            *args,
            date=date,
            comment_text=comment_text,
            comment=comment,
            reactions=reactions,
            assigned_by=assigned_by,
            assignee=assignee,
            id=id,
            user=user,
            resolved=resolved,
            _configuration=_configuration,
            **kwargs,
        )

from click_up_python_sdk.model.assigned_by import AssignedBy
from click_up_python_sdk.model.assignee import Assignee
from click_up_python_sdk.model.comment1 import Comment1
from click_up_python_sdk.model.comment_reactions import CommentReactions
from click_up_python_sdk.model.user2 import User2
