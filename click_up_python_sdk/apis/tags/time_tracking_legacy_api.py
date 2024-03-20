# coding: utf-8

"""
    ClickUp API Reference

    This is the ClickUp API Reference where you can learn about specific endpoints and parameters in detail.  Browse the available endpoints using the sidebar on the left.  **Not sure where to begin?** [Get Started with the ClickUp API](https://clickup.com/api) 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from click_up_python_sdk.paths.task_task_id_time_interval_id.put import EditTimeTracked
from click_up_python_sdk.paths.task_task_id_time.get import GetTrackedTime
from click_up_python_sdk.paths.task_task_id_time.post import RecordTimeForTask
from click_up_python_sdk.paths.task_task_id_time_interval_id.delete import RemoveTrackedTime
from click_up_python_sdk.apis.tags.time_tracking_legacy_api_raw import TimeTrackingLegacyApiRaw


class TimeTrackingLegacyApi(
    EditTimeTracked,
    GetTrackedTime,
    RecordTimeForTask,
    RemoveTrackedTime,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TimeTrackingLegacyApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TimeTrackingLegacyApiRaw(api_client)