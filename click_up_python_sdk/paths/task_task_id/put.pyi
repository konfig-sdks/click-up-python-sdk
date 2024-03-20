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

from click_up_python_sdk.model.update_taskresponse import UpdateTaskresponse as UpdateTaskresponseSchema
from click_up_python_sdk.model.update_taskrequest import UpdateTaskrequest as UpdateTaskrequestSchema
from click_up_python_sdk.model.assignees import Assignees as AssigneesSchema

from click_up_python_sdk.type.update_taskrequest import UpdateTaskrequest
from click_up_python_sdk.type.update_taskresponse import UpdateTaskresponse
from click_up_python_sdk.type.assignees import Assignees

from ...api_client import Dictionary
from click_up_python_sdk.pydantic.update_taskrequest import UpdateTaskrequest as UpdateTaskrequestPydantic
from click_up_python_sdk.pydantic.assignees import Assignees as AssigneesPydantic
from click_up_python_sdk.pydantic.update_taskresponse import UpdateTaskresponse as UpdateTaskresponsePydantic

# Query params
CustomTaskIdsSchema = schemas.BoolSchema
TeamIdSchema = schemas.NumberSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'custom_task_ids': typing.Union[CustomTaskIdsSchema, bool, ],
        'team_id': typing.Union[TeamIdSchema, decimal.Decimal, int, float, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_custom_task_ids = api_client.QueryParameter(
    name="custom_task_ids",
    style=api_client.ParameterStyle.FORM,
    schema=CustomTaskIdsSchema,
    explode=True,
)
request_query_team_id = api_client.QueryParameter(
    name="team_id",
    style=api_client.ParameterStyle.FORM,
    schema=TeamIdSchema,
    explode=True,
)
# Path params
TaskIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'task_id': typing.Union[TaskIdSchema, str, ],
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


request_path_task_id = api_client.PathParameter(
    name="task_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TaskIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = UpdateTaskrequestSchema


request_body_update_taskrequest = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = UpdateTaskresponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: UpdateTaskresponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: UpdateTaskresponse


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

    def _update_task_fields_mapped_args(
        self,
        task_id: str,
        description: typing.Optional[str] = None,
        custom_item_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        priority: typing.Optional[int] = None,
        due_date: typing.Optional[int] = None,
        due_date_time: typing.Optional[bool] = None,
        parent: typing.Optional[str] = None,
        time_estimate: typing.Optional[int] = None,
        start_date: typing.Optional[int] = None,
        start_date_time: typing.Optional[bool] = None,
        assignees: typing.Optional[Assignees] = None,
        archived: typing.Optional[bool] = None,
        custom_task_ids: typing.Optional[bool] = None,
        team_id: typing.Optional[typing.Union[int, float]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if description is not None:
            _body["description"] = description
        if custom_item_id is not None:
            _body["custom_item_id"] = custom_item_id
        if name is not None:
            _body["name"] = name
        if status is not None:
            _body["status"] = status
        if priority is not None:
            _body["priority"] = priority
        if due_date is not None:
            _body["due_date"] = due_date
        if due_date_time is not None:
            _body["due_date_time"] = due_date_time
        if parent is not None:
            _body["parent"] = parent
        if time_estimate is not None:
            _body["time_estimate"] = time_estimate
        if start_date is not None:
            _body["start_date"] = start_date
        if start_date_time is not None:
            _body["start_date_time"] = start_date_time
        if assignees is not None:
            _body["assignees"] = assignees
        if archived is not None:
            _body["archived"] = archived
        args.body = _body
        if custom_task_ids is not None:
            _query_params["custom_task_ids"] = custom_task_ids
        if team_id is not None:
            _query_params["team_id"] = team_id
        if task_id is not None:
            _path_params["task_id"] = task_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aupdate_task_fields_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
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
        Update Task
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_task_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_custom_task_ids,
            request_query_team_id,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
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
            path_template='/task/{task_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_update_taskrequest.serialize(body, content_type)
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
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _update_task_fields_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
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
        Update Task
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_task_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_custom_task_ids,
            request_query_team_id,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
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
            path_template='/task/{task_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_update_taskrequest.serialize(body, content_type)
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
            prefix_separator_iterator=prefix_separator_iterator,
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


class UpdateTaskFieldsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_task_fields(
        self,
        task_id: str,
        description: typing.Optional[str] = None,
        custom_item_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        priority: typing.Optional[int] = None,
        due_date: typing.Optional[int] = None,
        due_date_time: typing.Optional[bool] = None,
        parent: typing.Optional[str] = None,
        time_estimate: typing.Optional[int] = None,
        start_date: typing.Optional[int] = None,
        start_date_time: typing.Optional[bool] = None,
        assignees: typing.Optional[Assignees] = None,
        archived: typing.Optional[bool] = None,
        custom_task_ids: typing.Optional[bool] = None,
        team_id: typing.Optional[typing.Union[int, float]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_task_fields_mapped_args(
            task_id=task_id,
            description=description,
            custom_item_id=custom_item_id,
            name=name,
            status=status,
            priority=priority,
            due_date=due_date,
            due_date_time=due_date_time,
            parent=parent,
            time_estimate=time_estimate,
            start_date=start_date,
            start_date_time=start_date_time,
            assignees=assignees,
            archived=archived,
            custom_task_ids=custom_task_ids,
            team_id=team_id,
        )
        return await self._aupdate_task_fields_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def update_task_fields(
        self,
        task_id: str,
        description: typing.Optional[str] = None,
        custom_item_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        priority: typing.Optional[int] = None,
        due_date: typing.Optional[int] = None,
        due_date_time: typing.Optional[bool] = None,
        parent: typing.Optional[str] = None,
        time_estimate: typing.Optional[int] = None,
        start_date: typing.Optional[int] = None,
        start_date_time: typing.Optional[bool] = None,
        assignees: typing.Optional[Assignees] = None,
        archived: typing.Optional[bool] = None,
        custom_task_ids: typing.Optional[bool] = None,
        team_id: typing.Optional[typing.Union[int, float]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_task_fields_mapped_args(
            task_id=task_id,
            description=description,
            custom_item_id=custom_item_id,
            name=name,
            status=status,
            priority=priority,
            due_date=due_date,
            due_date_time=due_date_time,
            parent=parent,
            time_estimate=time_estimate,
            start_date=start_date,
            start_date_time=start_date_time,
            assignees=assignees,
            archived=archived,
            custom_task_ids=custom_task_ids,
            team_id=team_id,
        )
        return self._update_task_fields_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class UpdateTaskFields(BaseApi):

    async def aupdate_task_fields(
        self,
        task_id: str,
        description: typing.Optional[str] = None,
        custom_item_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        priority: typing.Optional[int] = None,
        due_date: typing.Optional[int] = None,
        due_date_time: typing.Optional[bool] = None,
        parent: typing.Optional[str] = None,
        time_estimate: typing.Optional[int] = None,
        start_date: typing.Optional[int] = None,
        start_date_time: typing.Optional[bool] = None,
        assignees: typing.Optional[Assignees] = None,
        archived: typing.Optional[bool] = None,
        custom_task_ids: typing.Optional[bool] = None,
        team_id: typing.Optional[typing.Union[int, float]] = None,
        validate: bool = False,
        **kwargs,
    ) -> UpdateTaskresponsePydantic:
        raw_response = await self.raw.aupdate_task_fields(
            task_id=task_id,
            description=description,
            custom_item_id=custom_item_id,
            name=name,
            status=status,
            priority=priority,
            due_date=due_date,
            due_date_time=due_date_time,
            parent=parent,
            time_estimate=time_estimate,
            start_date=start_date,
            start_date_time=start_date_time,
            assignees=assignees,
            archived=archived,
            custom_task_ids=custom_task_ids,
            team_id=team_id,
            **kwargs,
        )
        if validate:
            return UpdateTaskresponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(UpdateTaskresponsePydantic, raw_response.body)
    
    
    def update_task_fields(
        self,
        task_id: str,
        description: typing.Optional[str] = None,
        custom_item_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        priority: typing.Optional[int] = None,
        due_date: typing.Optional[int] = None,
        due_date_time: typing.Optional[bool] = None,
        parent: typing.Optional[str] = None,
        time_estimate: typing.Optional[int] = None,
        start_date: typing.Optional[int] = None,
        start_date_time: typing.Optional[bool] = None,
        assignees: typing.Optional[Assignees] = None,
        archived: typing.Optional[bool] = None,
        custom_task_ids: typing.Optional[bool] = None,
        team_id: typing.Optional[typing.Union[int, float]] = None,
        validate: bool = False,
    ) -> UpdateTaskresponsePydantic:
        raw_response = self.raw.update_task_fields(
            task_id=task_id,
            description=description,
            custom_item_id=custom_item_id,
            name=name,
            status=status,
            priority=priority,
            due_date=due_date,
            due_date_time=due_date_time,
            parent=parent,
            time_estimate=time_estimate,
            start_date=start_date,
            start_date_time=start_date_time,
            assignees=assignees,
            archived=archived,
            custom_task_ids=custom_task_ids,
            team_id=team_id,
        )
        if validate:
            return UpdateTaskresponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(UpdateTaskresponsePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        task_id: str,
        description: typing.Optional[str] = None,
        custom_item_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        priority: typing.Optional[int] = None,
        due_date: typing.Optional[int] = None,
        due_date_time: typing.Optional[bool] = None,
        parent: typing.Optional[str] = None,
        time_estimate: typing.Optional[int] = None,
        start_date: typing.Optional[int] = None,
        start_date_time: typing.Optional[bool] = None,
        assignees: typing.Optional[Assignees] = None,
        archived: typing.Optional[bool] = None,
        custom_task_ids: typing.Optional[bool] = None,
        team_id: typing.Optional[typing.Union[int, float]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_task_fields_mapped_args(
            task_id=task_id,
            description=description,
            custom_item_id=custom_item_id,
            name=name,
            status=status,
            priority=priority,
            due_date=due_date,
            due_date_time=due_date_time,
            parent=parent,
            time_estimate=time_estimate,
            start_date=start_date,
            start_date_time=start_date_time,
            assignees=assignees,
            archived=archived,
            custom_task_ids=custom_task_ids,
            team_id=team_id,
        )
        return await self._aupdate_task_fields_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        task_id: str,
        description: typing.Optional[str] = None,
        custom_item_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        priority: typing.Optional[int] = None,
        due_date: typing.Optional[int] = None,
        due_date_time: typing.Optional[bool] = None,
        parent: typing.Optional[str] = None,
        time_estimate: typing.Optional[int] = None,
        start_date: typing.Optional[int] = None,
        start_date_time: typing.Optional[bool] = None,
        assignees: typing.Optional[Assignees] = None,
        archived: typing.Optional[bool] = None,
        custom_task_ids: typing.Optional[bool] = None,
        team_id: typing.Optional[typing.Union[int, float]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_task_fields_mapped_args(
            task_id=task_id,
            description=description,
            custom_item_id=custom_item_id,
            name=name,
            status=status,
            priority=priority,
            due_date=due_date,
            due_date_time=due_date_time,
            parent=parent,
            time_estimate=time_estimate,
            start_date=start_date,
            start_date_time=start_date_time,
            assignees=assignees,
            archived=archived,
            custom_task_ids=custom_task_ids,
            team_id=team_id,
        )
        return self._update_task_fields_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

