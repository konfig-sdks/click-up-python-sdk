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

from click_up_python_sdk.model.get_access_tokenresponse import GetAccessTokenresponse as GetAccessTokenresponseSchema

from click_up_python_sdk.type.get_access_tokenresponse import GetAccessTokenresponse

from ...api_client import Dictionary
from click_up_python_sdk.pydantic.get_access_tokenresponse import GetAccessTokenresponse as GetAccessTokenresponsePydantic

# Query params
ClientIdSchema = schemas.StrSchema
ClientSecretSchema = schemas.StrSchema
CodeSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'client_id': typing.Union[ClientIdSchema, str, ],
        'client_secret': typing.Union[ClientSecretSchema, str, ],
        'code': typing.Union[CodeSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_client_id = api_client.QueryParameter(
    name="client_id",
    style=api_client.ParameterStyle.FORM,
    schema=ClientIdSchema,
    required=True,
    explode=True,
)
request_query_client_secret = api_client.QueryParameter(
    name="client_secret",
    style=api_client.ParameterStyle.FORM,
    schema=ClientSecretSchema,
    required=True,
    explode=True,
)
request_query_code = api_client.QueryParameter(
    name="code",
    style=api_client.ParameterStyle.FORM,
    schema=CodeSchema,
    required=True,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = GetAccessTokenresponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: GetAccessTokenresponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: GetAccessTokenresponse


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

    def _get_access_token_mapped_args(
        self,
        client_id: str,
        client_secret: str,
        code: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if client_id is not None:
            _query_params["client_id"] = client_id
        if client_secret is not None:
            _query_params["client_secret"] = client_secret
        if code is not None:
            _query_params["code"] = code
        args.query = _query_params
        return args

    async def _aget_access_token_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        Get Access Token
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_client_id,
            request_query_client_secret,
            request_query_code,
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
        method = 'post'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/oauth/token',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _get_access_token_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get Access Token
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_client_id,
            request_query_client_secret,
            request_query_code,
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
        method = 'post'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/oauth/token',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class GetAccessTokenRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_access_token(
        self,
        client_id: str,
        client_secret: str,
        code: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_access_token_mapped_args(
            client_id=client_id,
            client_secret=client_secret,
            code=code,
        )
        return await self._aget_access_token_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_access_token(
        self,
        client_id: str,
        client_secret: str,
        code: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_access_token_mapped_args(
            client_id=client_id,
            client_secret=client_secret,
            code=code,
        )
        return self._get_access_token_oapg(
            query_params=args.query,
        )

class GetAccessToken(BaseApi):

    async def aget_access_token(
        self,
        client_id: str,
        client_secret: str,
        code: str,
        validate: bool = False,
        **kwargs,
    ) -> GetAccessTokenresponsePydantic:
        raw_response = await self.raw.aget_access_token(
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            **kwargs,
        )
        if validate:
            return GetAccessTokenresponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(GetAccessTokenresponsePydantic, raw_response.body)
    
    
    def get_access_token(
        self,
        client_id: str,
        client_secret: str,
        code: str,
        validate: bool = False,
    ) -> GetAccessTokenresponsePydantic:
        raw_response = self.raw.get_access_token(
            client_id=client_id,
            client_secret=client_secret,
            code=code,
        )
        if validate:
            return GetAccessTokenresponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(GetAccessTokenresponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        client_id: str,
        client_secret: str,
        code: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_access_token_mapped_args(
            client_id=client_id,
            client_secret=client_secret,
            code=code,
        )
        return await self._aget_access_token_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        client_id: str,
        client_secret: str,
        code: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_access_token_mapped_args(
            client_id=client_id,
            client_secret=client_secret,
            code=code,
        )
        return self._get_access_token_oapg(
            query_params=args.query,
        )
