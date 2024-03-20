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

from click_up_python_sdk.model.get_tasksresponse import GetTasksresponse as GetTasksresponseSchema

from click_up_python_sdk.type.get_tasksresponse import GetTasksresponse

from ...api_client import Dictionary
from click_up_python_sdk.pydantic.get_tasksresponse import GetTasksresponse as GetTasksresponsePydantic

# Query params
ArchivedSchema = schemas.BoolSchema
IncludeMarkdownDescriptionSchema = schemas.BoolSchema
PageSchema = schemas.IntSchema
OrderBySchema = schemas.StrSchema
ReverseSchema = schemas.BoolSchema
SubtasksSchema = schemas.BoolSchema


class StatusesSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'StatusesSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
IncludeClosedSchema = schemas.BoolSchema


class AssigneesSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AssigneesSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class TagsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TagsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
DueDateGtSchema = schemas.IntSchema
DueDateLtSchema = schemas.IntSchema
DateCreatedGtSchema = schemas.IntSchema
DateCreatedLtSchema = schemas.IntSchema
DateUpdatedGtSchema = schemas.IntSchema
DateUpdatedLtSchema = schemas.IntSchema
DateDoneGtSchema = schemas.IntSchema
DateDoneLtSchema = schemas.IntSchema


class CustomFieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CustomFieldsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class CustomItemsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.NumberSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CustomItemsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'archived': typing.Union[ArchivedSchema, bool, ],
        'include_markdown_description': typing.Union[IncludeMarkdownDescriptionSchema, bool, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'order_by': typing.Union[OrderBySchema, str, ],
        'reverse': typing.Union[ReverseSchema, bool, ],
        'subtasks': typing.Union[SubtasksSchema, bool, ],
        'statuses': typing.Union[StatusesSchema, list, tuple, ],
        'include_closed': typing.Union[IncludeClosedSchema, bool, ],
        'assignees': typing.Union[AssigneesSchema, list, tuple, ],
        'tags': typing.Union[TagsSchema, list, tuple, ],
        'due_date_gt': typing.Union[DueDateGtSchema, decimal.Decimal, int, ],
        'due_date_lt': typing.Union[DueDateLtSchema, decimal.Decimal, int, ],
        'date_created_gt': typing.Union[DateCreatedGtSchema, decimal.Decimal, int, ],
        'date_created_lt': typing.Union[DateCreatedLtSchema, decimal.Decimal, int, ],
        'date_updated_gt': typing.Union[DateUpdatedGtSchema, decimal.Decimal, int, ],
        'date_updated_lt': typing.Union[DateUpdatedLtSchema, decimal.Decimal, int, ],
        'date_done_gt': typing.Union[DateDoneGtSchema, decimal.Decimal, int, ],
        'date_done_lt': typing.Union[DateDoneLtSchema, decimal.Decimal, int, ],
        'custom_fields': typing.Union[CustomFieldsSchema, list, tuple, ],
        'custom_items': typing.Union[CustomItemsSchema, list, tuple, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_archived = api_client.QueryParameter(
    name="archived",
    style=api_client.ParameterStyle.FORM,
    schema=ArchivedSchema,
    explode=True,
)
request_query_include_markdown_description = api_client.QueryParameter(
    name="include_markdown_description",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeMarkdownDescriptionSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_order_by = api_client.QueryParameter(
    name="order_by",
    style=api_client.ParameterStyle.FORM,
    schema=OrderBySchema,
    explode=True,
)
request_query_reverse = api_client.QueryParameter(
    name="reverse",
    style=api_client.ParameterStyle.FORM,
    schema=ReverseSchema,
    explode=True,
)
request_query_subtasks = api_client.QueryParameter(
    name="subtasks",
    style=api_client.ParameterStyle.FORM,
    schema=SubtasksSchema,
    explode=True,
)
request_query_statuses = api_client.QueryParameter(
    name="statuses",
    style=api_client.ParameterStyle.FORM,
    schema=StatusesSchema,
    explode=True,
)
request_query_include_closed = api_client.QueryParameter(
    name="include_closed",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeClosedSchema,
    explode=True,
)
request_query_assignees = api_client.QueryParameter(
    name="assignees",
    style=api_client.ParameterStyle.FORM,
    schema=AssigneesSchema,
    explode=True,
)
request_query_tags = api_client.QueryParameter(
    name="tags",
    style=api_client.ParameterStyle.FORM,
    schema=TagsSchema,
    explode=True,
)
request_query_due_date_gt = api_client.QueryParameter(
    name="due_date_gt",
    style=api_client.ParameterStyle.FORM,
    schema=DueDateGtSchema,
    explode=True,
)
request_query_due_date_lt = api_client.QueryParameter(
    name="due_date_lt",
    style=api_client.ParameterStyle.FORM,
    schema=DueDateLtSchema,
    explode=True,
)
request_query_date_created_gt = api_client.QueryParameter(
    name="date_created_gt",
    style=api_client.ParameterStyle.FORM,
    schema=DateCreatedGtSchema,
    explode=True,
)
request_query_date_created_lt = api_client.QueryParameter(
    name="date_created_lt",
    style=api_client.ParameterStyle.FORM,
    schema=DateCreatedLtSchema,
    explode=True,
)
request_query_date_updated_gt = api_client.QueryParameter(
    name="date_updated_gt",
    style=api_client.ParameterStyle.FORM,
    schema=DateUpdatedGtSchema,
    explode=True,
)
request_query_date_updated_lt = api_client.QueryParameter(
    name="date_updated_lt",
    style=api_client.ParameterStyle.FORM,
    schema=DateUpdatedLtSchema,
    explode=True,
)
request_query_date_done_gt = api_client.QueryParameter(
    name="date_done_gt",
    style=api_client.ParameterStyle.FORM,
    schema=DateDoneGtSchema,
    explode=True,
)
request_query_date_done_lt = api_client.QueryParameter(
    name="date_done_lt",
    style=api_client.ParameterStyle.FORM,
    schema=DateDoneLtSchema,
    explode=True,
)
request_query_custom_fields = api_client.QueryParameter(
    name="custom_fields",
    style=api_client.ParameterStyle.FORM,
    schema=CustomFieldsSchema,
    explode=True,
)
request_query_custom_items = api_client.QueryParameter(
    name="custom_items",
    style=api_client.ParameterStyle.FORM,
    schema=CustomItemsSchema,
    explode=True,
)
# Path params
ListIdSchema = schemas.NumberSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'list_id': typing.Union[ListIdSchema, decimal.Decimal, int, float, ],
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


request_path_list_id = api_client.PathParameter(
    name="list_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ListIdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = GetTasksresponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: GetTasksresponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: GetTasksresponse


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

    def _get_list_tasks_mapped_args(
        self,
        list_id: typing.Union[int, float],
        archived: typing.Optional[bool] = None,
        include_markdown_description: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        reverse: typing.Optional[bool] = None,
        subtasks: typing.Optional[bool] = None,
        statuses: typing.Optional[typing.List[str]] = None,
        include_closed: typing.Optional[bool] = None,
        assignees: typing.Optional[typing.List[str]] = None,
        tags: typing.Optional[typing.List[str]] = None,
        due_date_gt: typing.Optional[int] = None,
        due_date_lt: typing.Optional[int] = None,
        date_created_gt: typing.Optional[int] = None,
        date_created_lt: typing.Optional[int] = None,
        date_updated_gt: typing.Optional[int] = None,
        date_updated_lt: typing.Optional[int] = None,
        date_done_gt: typing.Optional[int] = None,
        date_done_lt: typing.Optional[int] = None,
        custom_fields: typing.Optional[typing.List[str]] = None,
        custom_items: typing.Optional[typing.List[typing.Union[int, float]]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if archived is not None:
            _query_params["archived"] = archived
        if include_markdown_description is not None:
            _query_params["include_markdown_description"] = include_markdown_description
        if page is not None:
            _query_params["page"] = page
        if order_by is not None:
            _query_params["order_by"] = order_by
        if reverse is not None:
            _query_params["reverse"] = reverse
        if subtasks is not None:
            _query_params["subtasks"] = subtasks
        if statuses is not None:
            _query_params["statuses"] = statuses
        if include_closed is not None:
            _query_params["include_closed"] = include_closed
        if assignees is not None:
            _query_params["assignees"] = assignees
        if tags is not None:
            _query_params["tags"] = tags
        if due_date_gt is not None:
            _query_params["due_date_gt"] = due_date_gt
        if due_date_lt is not None:
            _query_params["due_date_lt"] = due_date_lt
        if date_created_gt is not None:
            _query_params["date_created_gt"] = date_created_gt
        if date_created_lt is not None:
            _query_params["date_created_lt"] = date_created_lt
        if date_updated_gt is not None:
            _query_params["date_updated_gt"] = date_updated_gt
        if date_updated_lt is not None:
            _query_params["date_updated_lt"] = date_updated_lt
        if date_done_gt is not None:
            _query_params["date_done_gt"] = date_done_gt
        if date_done_lt is not None:
            _query_params["date_done_lt"] = date_done_lt
        if custom_fields is not None:
            _query_params["custom_fields"] = custom_fields
        if custom_items is not None:
            _query_params["custom_items"] = custom_items
        if list_id is not None:
            _path_params["list_id"] = list_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_list_tasks_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get Tasks
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_list_id,
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
            request_query_archived,
            request_query_include_markdown_description,
            request_query_page,
            request_query_order_by,
            request_query_reverse,
            request_query_subtasks,
            request_query_statuses,
            request_query_include_closed,
            request_query_assignees,
            request_query_tags,
            request_query_due_date_gt,
            request_query_due_date_lt,
            request_query_date_created_gt,
            request_query_date_created_lt,
            request_query_date_updated_gt,
            request_query_date_updated_lt,
            request_query_date_done_gt,
            request_query_date_done_lt,
            request_query_custom_fields,
            request_query_custom_items,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/list/{list_id}/task',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _get_list_tasks_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get Tasks
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_list_id,
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
            request_query_archived,
            request_query_include_markdown_description,
            request_query_page,
            request_query_order_by,
            request_query_reverse,
            request_query_subtasks,
            request_query_statuses,
            request_query_include_closed,
            request_query_assignees,
            request_query_tags,
            request_query_due_date_gt,
            request_query_due_date_lt,
            request_query_date_created_gt,
            request_query_date_created_lt,
            request_query_date_updated_gt,
            request_query_date_updated_lt,
            request_query_date_done_gt,
            request_query_date_done_lt,
            request_query_custom_fields,
            request_query_custom_items,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/list/{list_id}/task',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class GetListTasksRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_list_tasks(
        self,
        list_id: typing.Union[int, float],
        archived: typing.Optional[bool] = None,
        include_markdown_description: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        reverse: typing.Optional[bool] = None,
        subtasks: typing.Optional[bool] = None,
        statuses: typing.Optional[typing.List[str]] = None,
        include_closed: typing.Optional[bool] = None,
        assignees: typing.Optional[typing.List[str]] = None,
        tags: typing.Optional[typing.List[str]] = None,
        due_date_gt: typing.Optional[int] = None,
        due_date_lt: typing.Optional[int] = None,
        date_created_gt: typing.Optional[int] = None,
        date_created_lt: typing.Optional[int] = None,
        date_updated_gt: typing.Optional[int] = None,
        date_updated_lt: typing.Optional[int] = None,
        date_done_gt: typing.Optional[int] = None,
        date_done_lt: typing.Optional[int] = None,
        custom_fields: typing.Optional[typing.List[str]] = None,
        custom_items: typing.Optional[typing.List[typing.Union[int, float]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_list_tasks_mapped_args(
            list_id=list_id,
            archived=archived,
            include_markdown_description=include_markdown_description,
            page=page,
            order_by=order_by,
            reverse=reverse,
            subtasks=subtasks,
            statuses=statuses,
            include_closed=include_closed,
            assignees=assignees,
            tags=tags,
            due_date_gt=due_date_gt,
            due_date_lt=due_date_lt,
            date_created_gt=date_created_gt,
            date_created_lt=date_created_lt,
            date_updated_gt=date_updated_gt,
            date_updated_lt=date_updated_lt,
            date_done_gt=date_done_gt,
            date_done_lt=date_done_lt,
            custom_fields=custom_fields,
            custom_items=custom_items,
        )
        return await self._aget_list_tasks_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_list_tasks(
        self,
        list_id: typing.Union[int, float],
        archived: typing.Optional[bool] = None,
        include_markdown_description: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        reverse: typing.Optional[bool] = None,
        subtasks: typing.Optional[bool] = None,
        statuses: typing.Optional[typing.List[str]] = None,
        include_closed: typing.Optional[bool] = None,
        assignees: typing.Optional[typing.List[str]] = None,
        tags: typing.Optional[typing.List[str]] = None,
        due_date_gt: typing.Optional[int] = None,
        due_date_lt: typing.Optional[int] = None,
        date_created_gt: typing.Optional[int] = None,
        date_created_lt: typing.Optional[int] = None,
        date_updated_gt: typing.Optional[int] = None,
        date_updated_lt: typing.Optional[int] = None,
        date_done_gt: typing.Optional[int] = None,
        date_done_lt: typing.Optional[int] = None,
        custom_fields: typing.Optional[typing.List[str]] = None,
        custom_items: typing.Optional[typing.List[typing.Union[int, float]]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_list_tasks_mapped_args(
            list_id=list_id,
            archived=archived,
            include_markdown_description=include_markdown_description,
            page=page,
            order_by=order_by,
            reverse=reverse,
            subtasks=subtasks,
            statuses=statuses,
            include_closed=include_closed,
            assignees=assignees,
            tags=tags,
            due_date_gt=due_date_gt,
            due_date_lt=due_date_lt,
            date_created_gt=date_created_gt,
            date_created_lt=date_created_lt,
            date_updated_gt=date_updated_gt,
            date_updated_lt=date_updated_lt,
            date_done_gt=date_done_gt,
            date_done_lt=date_done_lt,
            custom_fields=custom_fields,
            custom_items=custom_items,
        )
        return self._get_list_tasks_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetListTasks(BaseApi):

    async def aget_list_tasks(
        self,
        list_id: typing.Union[int, float],
        archived: typing.Optional[bool] = None,
        include_markdown_description: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        reverse: typing.Optional[bool] = None,
        subtasks: typing.Optional[bool] = None,
        statuses: typing.Optional[typing.List[str]] = None,
        include_closed: typing.Optional[bool] = None,
        assignees: typing.Optional[typing.List[str]] = None,
        tags: typing.Optional[typing.List[str]] = None,
        due_date_gt: typing.Optional[int] = None,
        due_date_lt: typing.Optional[int] = None,
        date_created_gt: typing.Optional[int] = None,
        date_created_lt: typing.Optional[int] = None,
        date_updated_gt: typing.Optional[int] = None,
        date_updated_lt: typing.Optional[int] = None,
        date_done_gt: typing.Optional[int] = None,
        date_done_lt: typing.Optional[int] = None,
        custom_fields: typing.Optional[typing.List[str]] = None,
        custom_items: typing.Optional[typing.List[typing.Union[int, float]]] = None,
        validate: bool = False,
        **kwargs,
    ) -> GetTasksresponsePydantic:
        raw_response = await self.raw.aget_list_tasks(
            list_id=list_id,
            archived=archived,
            include_markdown_description=include_markdown_description,
            page=page,
            order_by=order_by,
            reverse=reverse,
            subtasks=subtasks,
            statuses=statuses,
            include_closed=include_closed,
            assignees=assignees,
            tags=tags,
            due_date_gt=due_date_gt,
            due_date_lt=due_date_lt,
            date_created_gt=date_created_gt,
            date_created_lt=date_created_lt,
            date_updated_gt=date_updated_gt,
            date_updated_lt=date_updated_lt,
            date_done_gt=date_done_gt,
            date_done_lt=date_done_lt,
            custom_fields=custom_fields,
            custom_items=custom_items,
            **kwargs,
        )
        if validate:
            return GetTasksresponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(GetTasksresponsePydantic, raw_response.body)
    
    
    def get_list_tasks(
        self,
        list_id: typing.Union[int, float],
        archived: typing.Optional[bool] = None,
        include_markdown_description: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        reverse: typing.Optional[bool] = None,
        subtasks: typing.Optional[bool] = None,
        statuses: typing.Optional[typing.List[str]] = None,
        include_closed: typing.Optional[bool] = None,
        assignees: typing.Optional[typing.List[str]] = None,
        tags: typing.Optional[typing.List[str]] = None,
        due_date_gt: typing.Optional[int] = None,
        due_date_lt: typing.Optional[int] = None,
        date_created_gt: typing.Optional[int] = None,
        date_created_lt: typing.Optional[int] = None,
        date_updated_gt: typing.Optional[int] = None,
        date_updated_lt: typing.Optional[int] = None,
        date_done_gt: typing.Optional[int] = None,
        date_done_lt: typing.Optional[int] = None,
        custom_fields: typing.Optional[typing.List[str]] = None,
        custom_items: typing.Optional[typing.List[typing.Union[int, float]]] = None,
        validate: bool = False,
    ) -> GetTasksresponsePydantic:
        raw_response = self.raw.get_list_tasks(
            list_id=list_id,
            archived=archived,
            include_markdown_description=include_markdown_description,
            page=page,
            order_by=order_by,
            reverse=reverse,
            subtasks=subtasks,
            statuses=statuses,
            include_closed=include_closed,
            assignees=assignees,
            tags=tags,
            due_date_gt=due_date_gt,
            due_date_lt=due_date_lt,
            date_created_gt=date_created_gt,
            date_created_lt=date_created_lt,
            date_updated_gt=date_updated_gt,
            date_updated_lt=date_updated_lt,
            date_done_gt=date_done_gt,
            date_done_lt=date_done_lt,
            custom_fields=custom_fields,
            custom_items=custom_items,
        )
        if validate:
            return GetTasksresponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(GetTasksresponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        list_id: typing.Union[int, float],
        archived: typing.Optional[bool] = None,
        include_markdown_description: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        reverse: typing.Optional[bool] = None,
        subtasks: typing.Optional[bool] = None,
        statuses: typing.Optional[typing.List[str]] = None,
        include_closed: typing.Optional[bool] = None,
        assignees: typing.Optional[typing.List[str]] = None,
        tags: typing.Optional[typing.List[str]] = None,
        due_date_gt: typing.Optional[int] = None,
        due_date_lt: typing.Optional[int] = None,
        date_created_gt: typing.Optional[int] = None,
        date_created_lt: typing.Optional[int] = None,
        date_updated_gt: typing.Optional[int] = None,
        date_updated_lt: typing.Optional[int] = None,
        date_done_gt: typing.Optional[int] = None,
        date_done_lt: typing.Optional[int] = None,
        custom_fields: typing.Optional[typing.List[str]] = None,
        custom_items: typing.Optional[typing.List[typing.Union[int, float]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_list_tasks_mapped_args(
            list_id=list_id,
            archived=archived,
            include_markdown_description=include_markdown_description,
            page=page,
            order_by=order_by,
            reverse=reverse,
            subtasks=subtasks,
            statuses=statuses,
            include_closed=include_closed,
            assignees=assignees,
            tags=tags,
            due_date_gt=due_date_gt,
            due_date_lt=due_date_lt,
            date_created_gt=date_created_gt,
            date_created_lt=date_created_lt,
            date_updated_gt=date_updated_gt,
            date_updated_lt=date_updated_lt,
            date_done_gt=date_done_gt,
            date_done_lt=date_done_lt,
            custom_fields=custom_fields,
            custom_items=custom_items,
        )
        return await self._aget_list_tasks_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        list_id: typing.Union[int, float],
        archived: typing.Optional[bool] = None,
        include_markdown_description: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        reverse: typing.Optional[bool] = None,
        subtasks: typing.Optional[bool] = None,
        statuses: typing.Optional[typing.List[str]] = None,
        include_closed: typing.Optional[bool] = None,
        assignees: typing.Optional[typing.List[str]] = None,
        tags: typing.Optional[typing.List[str]] = None,
        due_date_gt: typing.Optional[int] = None,
        due_date_lt: typing.Optional[int] = None,
        date_created_gt: typing.Optional[int] = None,
        date_created_lt: typing.Optional[int] = None,
        date_updated_gt: typing.Optional[int] = None,
        date_updated_lt: typing.Optional[int] = None,
        date_done_gt: typing.Optional[int] = None,
        date_done_lt: typing.Optional[int] = None,
        custom_fields: typing.Optional[typing.List[str]] = None,
        custom_items: typing.Optional[typing.List[typing.Union[int, float]]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_list_tasks_mapped_args(
            list_id=list_id,
            archived=archived,
            include_markdown_description=include_markdown_description,
            page=page,
            order_by=order_by,
            reverse=reverse,
            subtasks=subtasks,
            statuses=statuses,
            include_closed=include_closed,
            assignees=assignees,
            tags=tags,
            due_date_gt=due_date_gt,
            due_date_lt=due_date_lt,
            date_created_gt=date_created_gt,
            date_created_lt=date_created_lt,
            date_updated_gt=date_updated_gt,
            date_updated_lt=date_updated_lt,
            date_done_gt=date_done_gt,
            date_done_lt=date_done_lt,
            custom_fields=custom_fields,
            custom_items=custom_items,
        )
        return self._get_list_tasks_oapg(
            query_params=args.query,
            path_params=args.path,
        )

