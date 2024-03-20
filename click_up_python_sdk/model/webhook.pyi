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


class Webhook(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "endpoint",
            "list_id",
            "health",
            "task_id",
            "id",
            "secret",
            "team_id",
            "folder_id",
            "space_id",
            "userid",
            "client_id",
            "events",
        }
        
        class properties:
            id = schemas.StrSchema
            userid = schemas.IntSchema
            team_id = schemas.IntSchema
            endpoint = schemas.StrSchema
            client_id = schemas.StrSchema
        
            @staticmethod
            def events() -> typing.Type['WebhookEvents']:
                return WebhookEvents
            task_id = schemas.AnyTypeSchema
            list_id = schemas.AnyTypeSchema
            folder_id = schemas.AnyTypeSchema
            space_id = schemas.AnyTypeSchema
        
            @staticmethod
            def health() -> typing.Type['Health']:
                return Health
            secret = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "userid": userid,
                "team_id": team_id,
                "endpoint": endpoint,
                "client_id": client_id,
                "events": events,
                "task_id": task_id,
                "list_id": list_id,
                "folder_id": folder_id,
                "space_id": space_id,
                "health": health,
                "secret": secret,
            }
    
    endpoint: MetaOapg.properties.endpoint
    list_id: MetaOapg.properties.list_id
    health: 'Health'
    task_id: MetaOapg.properties.task_id
    id: MetaOapg.properties.id
    secret: MetaOapg.properties.secret
    team_id: MetaOapg.properties.team_id
    folder_id: MetaOapg.properties.folder_id
    space_id: MetaOapg.properties.space_id
    userid: MetaOapg.properties.userid
    client_id: MetaOapg.properties.client_id
    events: 'WebhookEvents'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userid"]) -> MetaOapg.properties.userid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["team_id"]) -> MetaOapg.properties.team_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endpoint"]) -> MetaOapg.properties.endpoint: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events"]) -> 'WebhookEvents': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["task_id"]) -> MetaOapg.properties.task_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["list_id"]) -> MetaOapg.properties.list_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["folder_id"]) -> MetaOapg.properties.folder_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["space_id"]) -> MetaOapg.properties.space_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["health"]) -> 'Health': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secret"]) -> MetaOapg.properties.secret: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "userid", "team_id", "endpoint", "client_id", "events", "task_id", "list_id", "folder_id", "space_id", "health", "secret", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userid"]) -> MetaOapg.properties.userid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["team_id"]) -> MetaOapg.properties.team_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endpoint"]) -> MetaOapg.properties.endpoint: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events"]) -> 'WebhookEvents': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["task_id"]) -> MetaOapg.properties.task_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["list_id"]) -> MetaOapg.properties.list_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["folder_id"]) -> MetaOapg.properties.folder_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["space_id"]) -> MetaOapg.properties.space_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["health"]) -> 'Health': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secret"]) -> MetaOapg.properties.secret: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "userid", "team_id", "endpoint", "client_id", "events", "task_id", "list_id", "folder_id", "space_id", "health", "secret", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        endpoint: typing.Union[MetaOapg.properties.endpoint, str, ],
        list_id: typing.Union[MetaOapg.properties.list_id, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        health: 'Health',
        task_id: typing.Union[MetaOapg.properties.task_id, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        secret: typing.Union[MetaOapg.properties.secret, str, ],
        team_id: typing.Union[MetaOapg.properties.team_id, decimal.Decimal, int, ],
        folder_id: typing.Union[MetaOapg.properties.folder_id, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        space_id: typing.Union[MetaOapg.properties.space_id, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        userid: typing.Union[MetaOapg.properties.userid, decimal.Decimal, int, ],
        client_id: typing.Union[MetaOapg.properties.client_id, str, ],
        events: 'WebhookEvents',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Webhook':
        return super().__new__(
            cls,
            *args,
            endpoint=endpoint,
            list_id=list_id,
            health=health,
            task_id=task_id,
            id=id,
            secret=secret,
            team_id=team_id,
            folder_id=folder_id,
            space_id=space_id,
            userid=userid,
            client_id=client_id,
            events=events,
            _configuration=_configuration,
            **kwargs,
        )

from click_up_python_sdk.model.health import Health
from click_up_python_sdk.model.webhook_events import WebhookEvents