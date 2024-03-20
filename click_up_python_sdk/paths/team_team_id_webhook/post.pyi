# coding: utf-8

"""
    ClickUp API Reference

    This is the ClickUp API Reference where you can learn about specific endpoints and parameters in detail.  Browse the available endpoints using the sidebar on the left.  **Not sure where to begin?** [Get Started with the ClickUp API](https://clickup.com/api) 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from click_up_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from click_up_python_sdk.api_response import AsyncGeneratorResponse
from click_up_python_sdk import api_client, exceptions
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

from click_up_python_sdk.model.create_webhookrequest_events import CreateWebhookrequestEvents as CreateWebhookrequestEventsSchema
from click_up_python_sdk.model.create_webhookrequest import CreateWebhookrequest as CreateWebhookrequestSchema
from click_up_python_sdk.model.create_webhookresponse import CreateWebhookresponse as CreateWebhookresponseSchema

from click_up_python_sdk.type.create_webhookrequest_events import CreateWebhookrequestEvents
from click_up_python_sdk.type.create_webhookresponse import CreateWebhookresponse
from click_up_python_sdk.type.create_webhookrequest import CreateWebhookrequest

from ...api_client import Dictionary
from click_up_python_sdk.pydantic.create_webhookresponse import CreateWebhookresponse as CreateWebhookresponsePydantic
from click_up_python_sdk.pydantic.create_webhookrequest import CreateWebhookrequest as CreateWebhookrequestPydantic
from click_up_python_sdk.pydantic.create_webhookrequest_events import CreateWebhookrequestEvents as CreateWebhookrequestEventsPydantic

# Path params
TeamIdSchema = schemas.NumberSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'team_id': typing.Union[TeamIdSchema, decimal.Decimal, int, float, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_team_id = api_client.PathParameter(
    name="team_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TeamIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = CreateWebhookrequestSchema


request_body_create_webhookrequest = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = CreateWebhookresponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CreateWebhookresponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CreateWebhookresponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_webhook_mapped_args(
        self,
        endpoint: str,
        events: CreateWebhookrequestEvents,
        team_id: typing.Union[int, float],
        space_id: typing.Optional[int] = None,
        folder_id: typing.Optional[int] = None,
        list_id: typing.Optional[int] = None,
        task_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if endpoint is not None:
            _body["endpoint"] = endpoint
        if events is not None:
            _body["events"] = events
        if space_id is not None:
            _body["space_id"] = space_id
        if folder_id is not None:
            _body["folder_id"] = folder_id
        if list_id is not None:
            _body["list_id"] = list_id
        if task_id is not None:
            _body["task_id"] = task_id
        args.body = _body
        if team_id is not None:
            _path_params["team_id"] = team_id
        args.path = _path_params
        return args

    async def _acreate_webhook_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create Webhook
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_team_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/team/{team_id}/webhook',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_webhookrequest.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_webhook_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create Webhook
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_team_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/team/{team_id}/webhook',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_webhookrequest.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateWebhookRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_webhook(
        self,
        endpoint: str,
        events: CreateWebhookrequestEvents,
        team_id: typing.Union[int, float],
        space_id: typing.Optional[int] = None,
        folder_id: typing.Optional[int] = None,
        list_id: typing.Optional[int] = None,
        task_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_webhook_mapped_args(
            endpoint=endpoint,
            events=events,
            team_id=team_id,
            space_id=space_id,
            folder_id=folder_id,
            list_id=list_id,
            task_id=task_id,
        )
        return await self._acreate_webhook_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_webhook(
        self,
        endpoint: str,
        events: CreateWebhookrequestEvents,
        team_id: typing.Union[int, float],
        space_id: typing.Optional[int] = None,
        folder_id: typing.Optional[int] = None,
        list_id: typing.Optional[int] = None,
        task_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_webhook_mapped_args(
            endpoint=endpoint,
            events=events,
            team_id=team_id,
            space_id=space_id,
            folder_id=folder_id,
            list_id=list_id,
            task_id=task_id,
        )
        return self._create_webhook_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreateWebhook(BaseApi):

    async def acreate_webhook(
        self,
        endpoint: str,
        events: CreateWebhookrequestEvents,
        team_id: typing.Union[int, float],
        space_id: typing.Optional[int] = None,
        folder_id: typing.Optional[int] = None,
        list_id: typing.Optional[int] = None,
        task_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> CreateWebhookresponsePydantic:
        raw_response = await self.raw.acreate_webhook(
            endpoint=endpoint,
            events=events,
            team_id=team_id,
            space_id=space_id,
            folder_id=folder_id,
            list_id=list_id,
            task_id=task_id,
            **kwargs,
        )
        if validate:
            return CreateWebhookresponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CreateWebhookresponsePydantic, raw_response.body)
    
    
    def create_webhook(
        self,
        endpoint: str,
        events: CreateWebhookrequestEvents,
        team_id: typing.Union[int, float],
        space_id: typing.Optional[int] = None,
        folder_id: typing.Optional[int] = None,
        list_id: typing.Optional[int] = None,
        task_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> CreateWebhookresponsePydantic:
        raw_response = self.raw.create_webhook(
            endpoint=endpoint,
            events=events,
            team_id=team_id,
            space_id=space_id,
            folder_id=folder_id,
            list_id=list_id,
            task_id=task_id,
        )
        if validate:
            return CreateWebhookresponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CreateWebhookresponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        endpoint: str,
        events: CreateWebhookrequestEvents,
        team_id: typing.Union[int, float],
        space_id: typing.Optional[int] = None,
        folder_id: typing.Optional[int] = None,
        list_id: typing.Optional[int] = None,
        task_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_webhook_mapped_args(
            endpoint=endpoint,
            events=events,
            team_id=team_id,
            space_id=space_id,
            folder_id=folder_id,
            list_id=list_id,
            task_id=task_id,
        )
        return await self._acreate_webhook_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        endpoint: str,
        events: CreateWebhookrequestEvents,
        team_id: typing.Union[int, float],
        space_id: typing.Optional[int] = None,
        folder_id: typing.Optional[int] = None,
        list_id: typing.Optional[int] = None,
        task_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_webhook_mapped_args(
            endpoint=endpoint,
            events=events,
            team_id=team_id,
            space_id=space_id,
            folder_id=folder_id,
            list_id=list_id,
            task_id=task_id,
        )
        return self._create_webhook_oapg(
            body=args.body,
            path_params=args.path,
        )

