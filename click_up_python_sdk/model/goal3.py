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


class Goal3(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "pinned",
            "private",
            "date_updated",
            "color",
            "group_members",
            "description",
            "owners",
            "team_id",
            "editor_token",
            "archived",
            "folder_access",
            "last_update",
            "members",
            "id",
            "pretty_id",
            "start_date",
            "owner",
            "key_result_count",
            "creator",
            "multiple_owners",
            "date_created",
            "due_date",
            "percent_completed",
            "name",
            "folder_id",
        }
        
        class properties:
            description = schemas.StrSchema
            id = schemas.StrSchema
            pretty_id = schemas.StrSchema
            name = schemas.StrSchema
            team_id = schemas.StrSchema
            creator = schemas.IntSchema
            owner = schemas.AnyTypeSchema
            color = schemas.StrSchema
            date_created = schemas.StrSchema
            start_date = schemas.AnyTypeSchema
            due_date = schemas.StrSchema
            private = schemas.BoolSchema
            archived = schemas.BoolSchema
            multiple_owners = schemas.BoolSchema
            editor_token = schemas.StrSchema
            date_updated = schemas.StrSchema
            last_update = schemas.StrSchema
            folder_id = schemas.StrSchema
            folder_access = schemas.BoolSchema
            pinned = schemas.BoolSchema
        
            @staticmethod
            def owners() -> typing.Type['Goal3Owners']:
                return Goal3Owners
            key_result_count = schemas.IntSchema
            
            
            class members(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Member1']:
                        return Member1
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Member1'], typing.List['Member1']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'members':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Member1':
                    return super().__getitem__(i)
        
            @staticmethod
            def group_members() -> typing.Type['Goal3GroupMembers']:
                return Goal3GroupMembers
            percent_completed = schemas.IntSchema
            __annotations__ = {
                "description": description,
                "id": id,
                "pretty_id": pretty_id,
                "name": name,
                "team_id": team_id,
                "creator": creator,
                "owner": owner,
                "color": color,
                "date_created": date_created,
                "start_date": start_date,
                "due_date": due_date,
                "private": private,
                "archived": archived,
                "multiple_owners": multiple_owners,
                "editor_token": editor_token,
                "date_updated": date_updated,
                "last_update": last_update,
                "folder_id": folder_id,
                "folder_access": folder_access,
                "pinned": pinned,
                "owners": owners,
                "key_result_count": key_result_count,
                "members": members,
                "group_members": group_members,
                "percent_completed": percent_completed,
            }
    
    pinned: MetaOapg.properties.pinned
    private: MetaOapg.properties.private
    date_updated: MetaOapg.properties.date_updated
    color: MetaOapg.properties.color
    group_members: 'Goal3GroupMembers'
    description: MetaOapg.properties.description
    owners: 'Goal3Owners'
    team_id: MetaOapg.properties.team_id
    editor_token: MetaOapg.properties.editor_token
    archived: MetaOapg.properties.archived
    folder_access: MetaOapg.properties.folder_access
    last_update: MetaOapg.properties.last_update
    members: MetaOapg.properties.members
    id: MetaOapg.properties.id
    pretty_id: MetaOapg.properties.pretty_id
    start_date: MetaOapg.properties.start_date
    owner: MetaOapg.properties.owner
    key_result_count: MetaOapg.properties.key_result_count
    creator: MetaOapg.properties.creator
    multiple_owners: MetaOapg.properties.multiple_owners
    date_created: MetaOapg.properties.date_created
    due_date: MetaOapg.properties.due_date
    percent_completed: MetaOapg.properties.percent_completed
    name: MetaOapg.properties.name
    folder_id: MetaOapg.properties.folder_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pretty_id"]) -> MetaOapg.properties.pretty_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["team_id"]) -> MetaOapg.properties.team_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creator"]) -> MetaOapg.properties.creator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner"]) -> MetaOapg.properties.owner: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_created"]) -> MetaOapg.properties.date_created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["due_date"]) -> MetaOapg.properties.due_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["private"]) -> MetaOapg.properties.private: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["archived"]) -> MetaOapg.properties.archived: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["multiple_owners"]) -> MetaOapg.properties.multiple_owners: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["editor_token"]) -> MetaOapg.properties.editor_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_updated"]) -> MetaOapg.properties.date_updated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_update"]) -> MetaOapg.properties.last_update: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["folder_id"]) -> MetaOapg.properties.folder_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["folder_access"]) -> MetaOapg.properties.folder_access: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pinned"]) -> MetaOapg.properties.pinned: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owners"]) -> 'Goal3Owners': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key_result_count"]) -> MetaOapg.properties.key_result_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["members"]) -> MetaOapg.properties.members: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["group_members"]) -> 'Goal3GroupMembers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["percent_completed"]) -> MetaOapg.properties.percent_completed: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "id", "pretty_id", "name", "team_id", "creator", "owner", "color", "date_created", "start_date", "due_date", "private", "archived", "multiple_owners", "editor_token", "date_updated", "last_update", "folder_id", "folder_access", "pinned", "owners", "key_result_count", "members", "group_members", "percent_completed", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pretty_id"]) -> MetaOapg.properties.pretty_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["team_id"]) -> MetaOapg.properties.team_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creator"]) -> MetaOapg.properties.creator: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner"]) -> MetaOapg.properties.owner: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_created"]) -> MetaOapg.properties.date_created: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["due_date"]) -> MetaOapg.properties.due_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["private"]) -> MetaOapg.properties.private: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["archived"]) -> MetaOapg.properties.archived: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["multiple_owners"]) -> MetaOapg.properties.multiple_owners: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["editor_token"]) -> MetaOapg.properties.editor_token: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_updated"]) -> MetaOapg.properties.date_updated: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_update"]) -> MetaOapg.properties.last_update: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["folder_id"]) -> MetaOapg.properties.folder_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["folder_access"]) -> MetaOapg.properties.folder_access: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pinned"]) -> MetaOapg.properties.pinned: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owners"]) -> 'Goal3Owners': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key_result_count"]) -> MetaOapg.properties.key_result_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["members"]) -> MetaOapg.properties.members: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["group_members"]) -> 'Goal3GroupMembers': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["percent_completed"]) -> MetaOapg.properties.percent_completed: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "id", "pretty_id", "name", "team_id", "creator", "owner", "color", "date_created", "start_date", "due_date", "private", "archived", "multiple_owners", "editor_token", "date_updated", "last_update", "folder_id", "folder_access", "pinned", "owners", "key_result_count", "members", "group_members", "percent_completed", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        pinned: typing.Union[MetaOapg.properties.pinned, bool, ],
        private: typing.Union[MetaOapg.properties.private, bool, ],
        date_updated: typing.Union[MetaOapg.properties.date_updated, str, ],
        color: typing.Union[MetaOapg.properties.color, str, ],
        group_members: 'Goal3GroupMembers',
        description: typing.Union[MetaOapg.properties.description, str, ],
        owners: 'Goal3Owners',
        team_id: typing.Union[MetaOapg.properties.team_id, str, ],
        editor_token: typing.Union[MetaOapg.properties.editor_token, str, ],
        archived: typing.Union[MetaOapg.properties.archived, bool, ],
        folder_access: typing.Union[MetaOapg.properties.folder_access, bool, ],
        last_update: typing.Union[MetaOapg.properties.last_update, str, ],
        members: typing.Union[MetaOapg.properties.members, list, tuple, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        pretty_id: typing.Union[MetaOapg.properties.pretty_id, str, ],
        start_date: typing.Union[MetaOapg.properties.start_date, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        owner: typing.Union[MetaOapg.properties.owner, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        key_result_count: typing.Union[MetaOapg.properties.key_result_count, decimal.Decimal, int, ],
        creator: typing.Union[MetaOapg.properties.creator, decimal.Decimal, int, ],
        multiple_owners: typing.Union[MetaOapg.properties.multiple_owners, bool, ],
        date_created: typing.Union[MetaOapg.properties.date_created, str, ],
        due_date: typing.Union[MetaOapg.properties.due_date, str, ],
        percent_completed: typing.Union[MetaOapg.properties.percent_completed, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        folder_id: typing.Union[MetaOapg.properties.folder_id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Goal3':
        return super().__new__(
            cls,
            *args,
            pinned=pinned,
            private=private,
            date_updated=date_updated,
            color=color,
            group_members=group_members,
            description=description,
            owners=owners,
            team_id=team_id,
            editor_token=editor_token,
            archived=archived,
            folder_access=folder_access,
            last_update=last_update,
            members=members,
            id=id,
            pretty_id=pretty_id,
            start_date=start_date,
            owner=owner,
            key_result_count=key_result_count,
            creator=creator,
            multiple_owners=multiple_owners,
            date_created=date_created,
            due_date=due_date,
            percent_completed=percent_completed,
            name=name,
            folder_id=folder_id,
            _configuration=_configuration,
            **kwargs,
        )

from click_up_python_sdk.model.goal3_group_members import Goal3GroupMembers
from click_up_python_sdk.model.goal3_owners import Goal3Owners
from click_up_python_sdk.model.member1 import Member1