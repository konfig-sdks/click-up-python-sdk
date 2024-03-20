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


class Item1(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "parent",
            "orderindex",
            "children",
            "date_created",
            "name",
            "assignee",
            "id",
            "resolved",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            orderindex = schemas.IntSchema
            assignee = schemas.AnyTypeSchema
            resolved = schemas.BoolSchema
            parent = schemas.AnyTypeSchema
            date_created = schemas.StrSchema
        
            @staticmethod
            def children() -> typing.Type['Item1Children']:
                return Item1Children
            __annotations__ = {
                "id": id,
                "name": name,
                "orderindex": orderindex,
                "assignee": assignee,
                "resolved": resolved,
                "parent": parent,
                "date_created": date_created,
                "children": children,
            }
    
    parent: MetaOapg.properties.parent
    orderindex: MetaOapg.properties.orderindex
    children: 'Item1Children'
    date_created: MetaOapg.properties.date_created
    name: MetaOapg.properties.name
    assignee: MetaOapg.properties.assignee
    id: MetaOapg.properties.id
    resolved: MetaOapg.properties.resolved
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orderindex"]) -> MetaOapg.properties.orderindex: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignee"]) -> MetaOapg.properties.assignee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resolved"]) -> MetaOapg.properties.resolved: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent"]) -> MetaOapg.properties.parent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_created"]) -> MetaOapg.properties.date_created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["children"]) -> 'Item1Children': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "orderindex", "assignee", "resolved", "parent", "date_created", "children", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orderindex"]) -> MetaOapg.properties.orderindex: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignee"]) -> MetaOapg.properties.assignee: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resolved"]) -> MetaOapg.properties.resolved: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent"]) -> MetaOapg.properties.parent: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_created"]) -> MetaOapg.properties.date_created: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["children"]) -> 'Item1Children': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "orderindex", "assignee", "resolved", "parent", "date_created", "children", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        parent: typing.Union[MetaOapg.properties.parent, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        orderindex: typing.Union[MetaOapg.properties.orderindex, decimal.Decimal, int, ],
        children: 'Item1Children',
        date_created: typing.Union[MetaOapg.properties.date_created, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        assignee: typing.Union[MetaOapg.properties.assignee, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        resolved: typing.Union[MetaOapg.properties.resolved, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Item1':
        return super().__new__(
            cls,
            *args,
            parent=parent,
            orderindex=orderindex,
            children=children,
            date_created=date_created,
            name=name,
            assignee=assignee,
            id=id,
            resolved=resolved,
            _configuration=_configuration,
            **kwargs,
        )

from click_up_python_sdk.model.item1_children import Item1Children