# coding: utf-8

"""
    ClickUp API Reference

    This is the ClickUp API Reference where you can learn about specific endpoints and parameters in detail.  Browse the available endpoints using the sidebar on the left.  **Not sure where to begin?** [Get Started with the ClickUp API](https://clickup.com/api) 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from click_up_python_sdk.paths.space_space_id_folder.post import CreateNewFolder
from click_up_python_sdk.paths.space_space_id_folder.get import GetContentsOf
from click_up_python_sdk.paths.folder_folder_id.get import GetFolderContent
from click_up_python_sdk.paths.folder_folder_id.delete import RemoveFolder
from click_up_python_sdk.paths.folder_folder_id.put import RenameFolder
from click_up_python_sdk.apis.tags.folders_api_raw import FoldersApiRaw


class FoldersApi(
    CreateNewFolder,
    GetContentsOf,
    GetFolderContent,
    RemoveFolder,
    RenameFolder,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: FoldersApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = FoldersApiRaw(api_client)
