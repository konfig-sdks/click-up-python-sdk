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

from click_up_python_sdk.model.remove_guest_from_listresponse import RemoveGuestFromListresponse as RemoveGuestFromListresponseSchema

from click_up_python_sdk.type.remove_guest_from_listresponse import RemoveGuestFromListresponse

from ...api_client import Dictionary
from click_up_python_sdk.pydantic.remove_guest_from_listresponse import RemoveGuestFromListresponse as RemoveGuestFromListresponsePydantic

from . import path

# Query params
IncludeSharedSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'include_shared': typing.Union[IncludeSharedSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_include_shared = api_client.QueryParameter(
    name="include_shared",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeSharedSchema,
    explode=True,
)
# Path params
ListIdSchema = schemas.NumberSchema
GuestIdSchema = schemas.NumberSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'list_id': typing.Union[ListIdSchema, decimal.Decimal, int, float, ],
        'guest_id': typing.Union[GuestIdSchema, decimal.Decimal, int, float, ],
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
request_path_guest_id = api_client.PathParameter(
    name="guest_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=GuestIdSchema,
    required=True,
)
_auth = [
    'Authorization Token',
]
SchemaFor200ResponseBodyApplicationJson = RemoveGuestFromListresponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: RemoveGuestFromListresponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: RemoveGuestFromListresponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _remove_from_list_mapped_args(
        self,
        list_id: typing.Union[int, float],
        guest_id: typing.Union[int, float],
        include_shared: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if include_shared is not None:
            _query_params["include_shared"] = include_shared
        if list_id is not None:
            _path_params["list_id"] = list_id
        if guest_id is not None:
            _path_params["guest_id"] = guest_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aremove_from_list_oapg(
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
        Remove Guest From List
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
            request_path_guest_id,
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
            request_query_include_shared,
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
        method = 'delete'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/list/{list_id}/guest/{guest_id}',
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


    def _remove_from_list_oapg(
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
        Remove Guest From List
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
            request_path_guest_id,
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
            request_query_include_shared,
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
        method = 'delete'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/list/{list_id}/guest/{guest_id}',
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


class RemoveFromListRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aremove_from_list(
        self,
        list_id: typing.Union[int, float],
        guest_id: typing.Union[int, float],
        include_shared: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._remove_from_list_mapped_args(
            list_id=list_id,
            guest_id=guest_id,
            include_shared=include_shared,
        )
        return await self._aremove_from_list_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def remove_from_list(
        self,
        list_id: typing.Union[int, float],
        guest_id: typing.Union[int, float],
        include_shared: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._remove_from_list_mapped_args(
            list_id=list_id,
            guest_id=guest_id,
            include_shared=include_shared,
        )
        return self._remove_from_list_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class RemoveFromList(BaseApi):

    async def aremove_from_list(
        self,
        list_id: typing.Union[int, float],
        guest_id: typing.Union[int, float],
        include_shared: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> RemoveGuestFromListresponsePydantic:
        raw_response = await self.raw.aremove_from_list(
            list_id=list_id,
            guest_id=guest_id,
            include_shared=include_shared,
            **kwargs,
        )
        if validate:
            return RemoveGuestFromListresponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(RemoveGuestFromListresponsePydantic, raw_response.body)
    
    
    def remove_from_list(
        self,
        list_id: typing.Union[int, float],
        guest_id: typing.Union[int, float],
        include_shared: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> RemoveGuestFromListresponsePydantic:
        raw_response = self.raw.remove_from_list(
            list_id=list_id,
            guest_id=guest_id,
            include_shared=include_shared,
        )
        if validate:
            return RemoveGuestFromListresponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(RemoveGuestFromListresponsePydantic, raw_response.body)


class ApiFordelete(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def adelete(
        self,
        list_id: typing.Union[int, float],
        guest_id: typing.Union[int, float],
        include_shared: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._remove_from_list_mapped_args(
            list_id=list_id,
            guest_id=guest_id,
            include_shared=include_shared,
        )
        return await self._aremove_from_list_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def delete(
        self,
        list_id: typing.Union[int, float],
        guest_id: typing.Union[int, float],
        include_shared: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._remove_from_list_mapped_args(
            list_id=list_id,
            guest_id=guest_id,
            include_shared=include_shared,
        )
        return self._remove_from_list_oapg(
            query_params=args.query,
            path_params=args.path,
        )

