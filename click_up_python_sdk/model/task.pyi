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


class Task(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "checklists",
            "parent",
            "creator",
            "date_updated",
            "orderindex",
            "date_created",
            "due_date",
            "assignees",
            "list",
            "priority",
            "space",
            "url",
            "tags",
            "time_spent",
            "time_estimate",
            "linked_tasks",
            "folder",
            "date_closed",
            "name",
            "id",
            "start_date",
            "status",
        }
        
        class properties:
        
            @staticmethod
            def tags() -> typing.Type['TaskTags']:
                return TaskTags
            id = schemas.StrSchema
            name = schemas.StrSchema
        
            @staticmethod
            def status() -> typing.Type['Status']:
                return Status
            orderindex = schemas.StrSchema
            date_created = schemas.StrSchema
            date_updated = schemas.StrSchema
            date_closed = schemas.AnyTypeSchema
        
            @staticmethod
            def creator() -> typing.Type['Creator']:
                return Creator
        
            @staticmethod
            def assignees() -> typing.Type['TaskAssignees']:
                return TaskAssignees
        
            @staticmethod
            def checklists() -> typing.Type['TaskChecklists']:
                return TaskChecklists
            parent = schemas.AnyTypeSchema
            priority = schemas.AnyTypeSchema
            due_date = schemas.AnyTypeSchema
            start_date = schemas.AnyTypeSchema
            time_estimate = schemas.AnyTypeSchema
            time_spent = schemas.AnyTypeSchema
        
            @staticmethod
            def _list() -> typing.Type['ModelList']:
                return ModelList
        
            @staticmethod
            def folder() -> typing.Type['Folder']:
                return Folder
        
            @staticmethod
            def space() -> typing.Type['Space']:
                return Space
            
            
            class linked_tasks(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['LinkedTask']:
                        return LinkedTask
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['LinkedTask'], typing.List['LinkedTask']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'linked_tasks':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'LinkedTask':
                    return super().__getitem__(i)
            url = schemas.StrSchema
            __annotations__ = {
                "tags": tags,
                "id": id,
                "name": name,
                "status": status,
                "orderindex": orderindex,
                "date_created": date_created,
                "date_updated": date_updated,
                "date_closed": date_closed,
                "creator": creator,
                "assignees": assignees,
                "checklists": checklists,
                "parent": parent,
                "priority": priority,
                "due_date": due_date,
                "start_date": start_date,
                "time_estimate": time_estimate,
                "time_spent": time_spent,
                "list": _list,
                "folder": folder,
                "space": space,
                "linked_tasks": linked_tasks,
                "url": url,
            }
    
    checklists: 'TaskChecklists'
    parent: MetaOapg.properties.parent
    creator: 'Creator'
    date_updated: MetaOapg.properties.date_updated
    orderindex: MetaOapg.properties.orderindex
    date_created: MetaOapg.properties.date_created
    due_date: MetaOapg.properties.due_date
    assignees: 'TaskAssignees'
    priority: MetaOapg.properties.priority
    space: 'Space'
    url: MetaOapg.properties.url
    tags: 'TaskTags'
    time_spent: MetaOapg.properties.time_spent
    time_estimate: MetaOapg.properties.time_estimate
    linked_tasks: MetaOapg.properties.linked_tasks
    folder: 'Folder'
    date_closed: MetaOapg.properties.date_closed
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    start_date: MetaOapg.properties.start_date
    status: 'Status'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> 'TaskTags': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'Status': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orderindex"]) -> MetaOapg.properties.orderindex: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_created"]) -> MetaOapg.properties.date_created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_updated"]) -> MetaOapg.properties.date_updated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_closed"]) -> MetaOapg.properties.date_closed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creator"]) -> 'Creator': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignees"]) -> 'TaskAssignees': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["checklists"]) -> 'TaskChecklists': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent"]) -> MetaOapg.properties.parent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["due_date"]) -> MetaOapg.properties.due_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_estimate"]) -> MetaOapg.properties.time_estimate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_spent"]) -> MetaOapg.properties.time_spent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["list"]) -> 'ModelList': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["folder"]) -> 'Folder': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["space"]) -> 'Space': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linked_tasks"]) -> MetaOapg.properties.linked_tasks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tags", "id", "name", "status", "orderindex", "date_created", "date_updated", "date_closed", "creator", "assignees", "checklists", "parent", "priority", "due_date", "start_date", "time_estimate", "time_spent", "list", "folder", "space", "linked_tasks", "url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> 'TaskTags': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'Status': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orderindex"]) -> MetaOapg.properties.orderindex: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_created"]) -> MetaOapg.properties.date_created: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_updated"]) -> MetaOapg.properties.date_updated: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_closed"]) -> MetaOapg.properties.date_closed: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creator"]) -> 'Creator': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignees"]) -> 'TaskAssignees': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["checklists"]) -> 'TaskChecklists': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent"]) -> MetaOapg.properties.parent: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["due_date"]) -> MetaOapg.properties.due_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_estimate"]) -> MetaOapg.properties.time_estimate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_spent"]) -> MetaOapg.properties.time_spent: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["list"]) -> 'ModelList': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["folder"]) -> 'Folder': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["space"]) -> 'Space': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linked_tasks"]) -> MetaOapg.properties.linked_tasks: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tags", "id", "name", "status", "orderindex", "date_created", "date_updated", "date_closed", "creator", "assignees", "checklists", "parent", "priority", "due_date", "start_date", "time_estimate", "time_spent", "list", "folder", "space", "linked_tasks", "url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        checklists: 'TaskChecklists',
        parent: typing.Union[MetaOapg.properties.parent, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        creator: 'Creator',
        date_updated: typing.Union[MetaOapg.properties.date_updated, str, ],
        orderindex: typing.Union[MetaOapg.properties.orderindex, str, ],
        date_created: typing.Union[MetaOapg.properties.date_created, str, ],
        due_date: typing.Union[MetaOapg.properties.due_date, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        assignees: 'TaskAssignees',
        priority: typing.Union[MetaOapg.properties.priority, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        space: 'Space',
        url: typing.Union[MetaOapg.properties.url, str, ],
        tags: 'TaskTags',
        time_spent: typing.Union[MetaOapg.properties.time_spent, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        time_estimate: typing.Union[MetaOapg.properties.time_estimate, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        linked_tasks: typing.Union[MetaOapg.properties.linked_tasks, list, tuple, ],
        folder: 'Folder',
        date_closed: typing.Union[MetaOapg.properties.date_closed, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        start_date: typing.Union[MetaOapg.properties.start_date, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        status: 'Status',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Task':
        return super().__new__(
            cls,
            *args,
            checklists=checklists,
            parent=parent,
            creator=creator,
            date_updated=date_updated,
            orderindex=orderindex,
            date_created=date_created,
            due_date=due_date,
            assignees=assignees,
            priority=priority,
            space=space,
            url=url,
            tags=tags,
            time_spent=time_spent,
            time_estimate=time_estimate,
            linked_tasks=linked_tasks,
            folder=folder,
            date_closed=date_closed,
            name=name,
            id=id,
            start_date=start_date,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from click_up_python_sdk.model.creator import Creator
from click_up_python_sdk.model.folder import Folder
from click_up_python_sdk.model.linked_task import LinkedTask
from click_up_python_sdk.model.model_list import ModelList
from click_up_python_sdk.model.space import Space
from click_up_python_sdk.model.status import Status
from click_up_python_sdk.model.task_assignees import TaskAssignees
from click_up_python_sdk.model.task_checklists import TaskChecklists
from click_up_python_sdk.model.task_tags import TaskTags