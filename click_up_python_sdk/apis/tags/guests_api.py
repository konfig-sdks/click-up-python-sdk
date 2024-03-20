# coding: utf-8

"""
    ClickUp API Reference

    This is the ClickUp API Reference where you can learn about specific endpoints and parameters in detail.  Browse the available endpoints using the sidebar on the left.  **Not sure where to begin?** [Get Started with the ClickUp API](https://clickup.com/api) 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from click_up_python_sdk.paths.folder_folder_id_guest_guest_id.post import AddGuestToFolder
from click_up_python_sdk.paths.task_task_id_guest_guest_id.post import AddToTask
from click_up_python_sdk.paths.team_team_id_guest_guest_id.put import EditGuestOnWorkspace
from click_up_python_sdk.paths.team_team_id_guest_guest_id.get import GetGuestInformation
from click_up_python_sdk.paths.team_team_id_guest.post import InviteToWorkspace
from click_up_python_sdk.paths.list_list_id_guest_guest_id.delete import RemoveFromList
from click_up_python_sdk.paths.folder_folder_id_guest_guest_id.delete import RevokeAccessFromFolder
from click_up_python_sdk.paths.task_task_id_guest_guest_id.delete import RevokeAccessToTask
from click_up_python_sdk.paths.team_team_id_guest_guest_id.delete import RevokeGuestAccessToWorkspace
from click_up_python_sdk.paths.list_list_id_guest_guest_id.post import ShareListWith
from click_up_python_sdk.apis.tags.guests_api_raw import GuestsApiRaw


class GuestsApi(
    AddGuestToFolder,
    AddToTask,
    EditGuestOnWorkspace,
    GetGuestInformation,
    InviteToWorkspace,
    RemoveFromList,
    RevokeAccessFromFolder,
    RevokeAccessToTask,
    RevokeGuestAccessToWorkspace,
    ShareListWith,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: GuestsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = GuestsApiRaw(api_client)