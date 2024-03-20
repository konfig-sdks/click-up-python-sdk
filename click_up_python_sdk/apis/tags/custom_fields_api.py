# coding: utf-8

"""
    ClickUp API Reference

    This is the ClickUp API Reference where you can learn about specific endpoints and parameters in detail.  Browse the available endpoints using the sidebar on the left.  **Not sure where to begin?** [Get Started with the ClickUp API](https://clickup.com/api) 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from click_up_python_sdk.paths.list_list_id_field.get import GetListFields
from click_up_python_sdk.paths.task_task_id_field_field_id.delete import RemoveFieldValue
from click_up_python_sdk.paths.task_task_id_field_field_id.post import SetFieldValue
from click_up_python_sdk.apis.tags.custom_fields_api_raw import CustomFieldsApiRaw


class CustomFieldsApi(
    GetListFields,
    RemoveFieldValue,
    SetFieldValue,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CustomFieldsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CustomFieldsApiRaw(api_client)
