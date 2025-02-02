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


class List3(
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
            "override_statuses",
            "task_count",
            "archived",
            "permission_level",
            "name",
            "statuses",
            "assignee",
            "id",
            "start_date",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            orderindex = schemas.IntSchema
            status = schemas.AnyTypeSchema
            priority = schemas.AnyTypeSchema
            assignee = schemas.AnyTypeSchema
            task_count = schemas.StrSchema
            due_date = schemas.AnyTypeSchema
            start_date = schemas.AnyTypeSchema
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
                "status": status,
                "priority": priority,
                "assignee": assignee,
                "task_count": task_count,
                "due_date": due_date,
                "start_date": start_date,
                "archived": archived,
                "override_statuses": override_statuses,
                "statuses": statuses,
                "permission_level": permission_level,
            }
    
    orderindex: MetaOapg.properties.orderindex
    due_date: MetaOapg.properties.due_date
    priority: MetaOapg.properties.priority
    override_statuses: MetaOapg.properties.override_statuses
    task_count: MetaOapg.properties.task_count
    archived: MetaOapg.properties.archived
    permission_level: MetaOapg.properties.permission_level
    name: MetaOapg.properties.name
    statuses: MetaOapg.properties.statuses
    assignee: MetaOapg.properties.assignee
    id: MetaOapg.properties.id
    start_date: MetaOapg.properties.start_date
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orderindex"]) -> MetaOapg.properties.orderindex: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignee"]) -> MetaOapg.properties.assignee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["task_count"]) -> MetaOapg.properties.task_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["due_date"]) -> MetaOapg.properties.due_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
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
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "orderindex", "status", "priority", "assignee", "task_count", "due_date", "start_date", "archived", "override_statuses", "statuses", "permission_level", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orderindex"]) -> MetaOapg.properties.orderindex: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignee"]) -> MetaOapg.properties.assignee: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["task_count"]) -> MetaOapg.properties.task_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["due_date"]) -> MetaOapg.properties.due_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
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
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "orderindex", "status", "priority", "assignee", "task_count", "due_date", "start_date", "archived", "override_statuses", "statuses", "permission_level", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        orderindex: typing.Union[MetaOapg.properties.orderindex, decimal.Decimal, int, ],
        due_date: typing.Union[MetaOapg.properties.due_date, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        priority: typing.Union[MetaOapg.properties.priority, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        override_statuses: typing.Union[MetaOapg.properties.override_statuses, bool, ],
        task_count: typing.Union[MetaOapg.properties.task_count, str, ],
        archived: typing.Union[MetaOapg.properties.archived, bool, ],
        permission_level: typing.Union[MetaOapg.properties.permission_level, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        statuses: typing.Union[MetaOapg.properties.statuses, list, tuple, ],
        assignee: typing.Union[MetaOapg.properties.assignee, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        start_date: typing.Union[MetaOapg.properties.start_date, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        status: typing.Union[MetaOapg.properties.status, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'List3':
        return super().__new__(
            cls,
            *args,
            orderindex=orderindex,
            due_date=due_date,
            priority=priority,
            override_statuses=override_statuses,
            task_count=task_count,
            archived=archived,
            permission_level=permission_level,
            name=name,
            statuses=statuses,
            assignee=assignee,
            id=id,
            start_date=start_date,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from click_up_python_sdk.model.status import Status
