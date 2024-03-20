# coding: utf-8

"""
    ClickUp API Reference

    This is the ClickUp API Reference where you can learn about specific endpoints and parameters in detail.  Browse the available endpoints using the sidebar on the left.  **Not sure where to begin?** [Get Started with the ClickUp API](https://clickup.com/api) 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from click_up_python_sdk.paths.list_list_id_comment.post import AddToListComment
from click_up_python_sdk.paths.view_view_id_comment.post import CreateChatViewComment
from click_up_python_sdk.paths.task_task_id_comment.post import CreateNewTaskComment
from click_up_python_sdk.paths.comment_comment_id.delete import DeleteTaskComment
from click_up_python_sdk.paths.list_list_id_comment.get import GetListComments
from click_up_python_sdk.paths.task_task_id_comment.get import GetTaskComments
from click_up_python_sdk.paths.view_view_id_comment.get import GetViewComments
from click_up_python_sdk.paths.comment_comment_id.put import UpdateTaskComment
from click_up_python_sdk.apis.tags.comments_api_raw import CommentsApiRaw


class CommentsApi(
    AddToListComment,
    CreateChatViewComment,
    CreateNewTaskComment,
    DeleteTaskComment,
    GetListComments,
    GetTaskComments,
    GetViewComments,
    UpdateTaskComment,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CommentsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CommentsApiRaw(api_client)
