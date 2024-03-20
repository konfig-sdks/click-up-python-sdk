# coding: utf-8

"""
    ClickUp API Reference

    This is the ClickUp API Reference where you can learn about specific endpoints and parameters in detail.  Browse the available endpoints using the sidebar on the left.  **Not sure where to begin?** [Get Started with the ClickUp API](https://clickup.com/api) 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from click_up_python_sdk.paths.team_team_id_time_entries_tags.post import AddTagsFromTimeEntriesRaw
from click_up_python_sdk.paths.team_team_id_time_entries_tags.put import ChangeTagNamesRaw
from click_up_python_sdk.paths.team_team_id_time_entries.post import CreateTimeEntryRaw
from click_up_python_sdk.paths.team_team_id_time_entries_tags.get import GetAllTagsFromTimeEntriesRaw
from click_up_python_sdk.paths.team_team_id_time_entries_current.get import GetCurrentTimeEntryRaw
from click_up_python_sdk.paths.team_team_id_time_entries_timer_id.get import GetSingleTimeEntryRaw
from click_up_python_sdk.paths.team_team_id_time_entries.get import GetTimeEntriesWithinDateRangeRaw
from click_up_python_sdk.paths.team_team_id_time_entries_timer_id_history.get import GetTimeEntryHistoryRaw
from click_up_python_sdk.paths.team_team_id_time_entries_timer_id.delete import RemoveEntryRaw
from click_up_python_sdk.paths.team_team_id_time_entries_tags.delete import RemoveTagsFromTimeEntriesRaw
from click_up_python_sdk.paths.team_team_id_time_entries_start.post import StartTimerRaw
from click_up_python_sdk.paths.team_team_id_time_entries_stop.post import StopTimeEntryRaw
from click_up_python_sdk.paths.team_team_id_time_entries_timer_id.put import UpdateTimeEntryDetailsRaw


class TimeTrackingApiRaw(
    AddTagsFromTimeEntriesRaw,
    ChangeTagNamesRaw,
    CreateTimeEntryRaw,
    GetAllTagsFromTimeEntriesRaw,
    GetCurrentTimeEntryRaw,
    GetSingleTimeEntryRaw,
    GetTimeEntriesWithinDateRangeRaw,
    GetTimeEntryHistoryRaw,
    RemoveEntryRaw,
    RemoveTagsFromTimeEntriesRaw,
    StartTimerRaw,
    StopTimeEntryRaw,
    UpdateTimeEntryDetailsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass