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


class GetListresponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "orderindex",
            "due_date",
            "priority",
            "content",
            "space",
            "override_statuses",
            "archived",
            "permission_level",
            "folder",
            "due_date_time",
            "name",
            "statuses",
            "assignee",
            "id",
            "start_date_time",
            "inbound_address",
            "start_date",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            orderindex = schemas.IntSchema
            content = schemas.StrSchema
        
            @staticmethod
            def status() -> typing.Type['Status5']:
                return Status5
        
            @staticmethod
            def priority() -> typing.Type['Priority1']:
                return Priority1
            assignee = schemas.AnyTypeSchema
            due_date = schemas.StrSchema
            due_date_time = schemas.BoolSchema
            start_date = schemas.AnyTypeSchema
            start_date_time = schemas.AnyTypeSchema
        
            @staticmethod
            def folder() -> typing.Type['Folder3']:
                return Folder3
        
            @staticmethod
            def space() -> typing.Type['Space2']:
                return Space2
            inbound_address = schemas.StrSchema
            archived = schemas.BoolSchema
            override_statuses = schemas.BoolSchema
            
            
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
            permission_level = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "orderindex": orderindex,
                "content": content,
                "status": status,
                "priority": priority,
                "assignee": assignee,
                "due_date": due_date,
                "due_date_time": due_date_time,
                "start_date": start_date,
                "start_date_time": start_date_time,
                "folder": folder,
                "space": space,
                "inbound_address": inbound_address,
                "archived": archived,
                "override_statuses": override_statuses,
                "statuses": statuses,
                "permission_level": permission_level,
            }
    
    orderindex: MetaOapg.properties.orderindex
    due_date: MetaOapg.properties.due_date
    priority: 'Priority1'
    content: MetaOapg.properties.content
    space: 'Space2'
    override_statuses: MetaOapg.properties.override_statuses
    archived: MetaOapg.properties.archived
    permission_level: MetaOapg.properties.permission_level
    folder: 'Folder3'
    due_date_time: MetaOapg.properties.due_date_time
    name: MetaOapg.properties.name
    statuses: MetaOapg.properties.statuses
    assignee: MetaOapg.properties.assignee
    id: MetaOapg.properties.id
    start_date_time: MetaOapg.properties.start_date_time
    inbound_address: MetaOapg.properties.inbound_address
    start_date: MetaOapg.properties.start_date
    status: 'Status5'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orderindex"]) -> MetaOapg.properties.orderindex: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["content"]) -> MetaOapg.properties.content: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'Status5': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> 'Priority1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignee"]) -> MetaOapg.properties.assignee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["due_date"]) -> MetaOapg.properties.due_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["due_date_time"]) -> MetaOapg.properties.due_date_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date_time"]) -> MetaOapg.properties.start_date_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["folder"]) -> 'Folder3': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["space"]) -> 'Space2': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inbound_address"]) -> MetaOapg.properties.inbound_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["archived"]) -> MetaOapg.properties.archived: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["override_statuses"]) -> MetaOapg.properties.override_statuses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statuses"]) -> MetaOapg.properties.statuses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permission_level"]) -> MetaOapg.properties.permission_level: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "orderindex", "content", "status", "priority", "assignee", "due_date", "due_date_time", "start_date", "start_date_time", "folder", "space", "inbound_address", "archived", "override_statuses", "statuses", "permission_level", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orderindex"]) -> MetaOapg.properties.orderindex: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["content"]) -> MetaOapg.properties.content: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'Status5': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> 'Priority1': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignee"]) -> MetaOapg.properties.assignee: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["due_date"]) -> MetaOapg.properties.due_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["due_date_time"]) -> MetaOapg.properties.due_date_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date_time"]) -> MetaOapg.properties.start_date_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["folder"]) -> 'Folder3': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["space"]) -> 'Space2': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inbound_address"]) -> MetaOapg.properties.inbound_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["archived"]) -> MetaOapg.properties.archived: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["override_statuses"]) -> MetaOapg.properties.override_statuses: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statuses"]) -> MetaOapg.properties.statuses: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permission_level"]) -> MetaOapg.properties.permission_level: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "orderindex", "content", "status", "priority", "assignee", "due_date", "due_date_time", "start_date", "start_date_time", "folder", "space", "inbound_address", "archived", "override_statuses", "statuses", "permission_level", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        orderindex: typing.Union[MetaOapg.properties.orderindex, decimal.Decimal, int, ],
        due_date: typing.Union[MetaOapg.properties.due_date, str, ],
        priority: 'Priority1',
        content: typing.Union[MetaOapg.properties.content, str, ],
        space: 'Space2',
        override_statuses: typing.Union[MetaOapg.properties.override_statuses, bool, ],
        archived: typing.Union[MetaOapg.properties.archived, bool, ],
        permission_level: typing.Union[MetaOapg.properties.permission_level, str, ],
        folder: 'Folder3',
        due_date_time: typing.Union[MetaOapg.properties.due_date_time, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        statuses: typing.Union[MetaOapg.properties.statuses, list, tuple, ],
        assignee: typing.Union[MetaOapg.properties.assignee, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        start_date_time: typing.Union[MetaOapg.properties.start_date_time, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        inbound_address: typing.Union[MetaOapg.properties.inbound_address, str, ],
        start_date: typing.Union[MetaOapg.properties.start_date, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        status: 'Status5',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GetListresponse':
        return super().__new__(
            cls,
            *args,
            orderindex=orderindex,
            due_date=due_date,
            priority=priority,
            content=content,
            space=space,
            override_statuses=override_statuses,
            archived=archived,
            permission_level=permission_level,
            folder=folder,
            due_date_time=due_date_time,
            name=name,
            statuses=statuses,
            assignee=assignee,
            id=id,
            start_date_time=start_date_time,
            inbound_address=inbound_address,
            start_date=start_date,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from click_up_python_sdk.model.folder3 import Folder3
from click_up_python_sdk.model.priority1 import Priority1
from click_up_python_sdk.model.space2 import Space2
from click_up_python_sdk.model.status import Status
from click_up_python_sdk.model.status5 import Status5
