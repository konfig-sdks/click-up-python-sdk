# coding: utf-8

"""
    ClickUp API Reference

    This is the ClickUp API Reference where you can learn about specific endpoints and parameters in detail.  Browse the available endpoints using the sidebar on the left.  **Not sure where to begin?** [Get Started with the ClickUp API](https://clickup.com/api) 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from click_up_python_sdk.paths.list_list_id_task_task_id.post import AddTaskToList
from click_up_python_sdk.paths.folder_folder_id_list.post import AddToFolder
from click_up_python_sdk.paths.space_space_id_list.post import CreateFolderlessList
from click_up_python_sdk.paths.folder_folder_id_list.get import GetFolderLists
from click_up_python_sdk.paths.space_space_id_list.get import GetFolderless
from click_up_python_sdk.paths.list_list_id.get import GetListDetails
from click_up_python_sdk.paths.list_list_id.delete import RemoveList
from click_up_python_sdk.paths.list_list_id_task_task_id.delete import RemoveTaskFromList
from click_up_python_sdk.paths.list_list_id.put import UpdateListInfoDueDatePriorityAssigneeColor
from click_up_python_sdk.apis.tags.lists_api_raw import ListsApiRaw


class ListsApi(
    AddTaskToList,
    AddToFolder,
    CreateFolderlessList,
    GetFolderLists,
    GetFolderless,
    GetListDetails,
    RemoveList,
    RemoveTaskFromList,
    UpdateListInfoDueDatePriorityAssigneeColor,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ListsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ListsApiRaw(api_client)