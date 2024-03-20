# coding: utf-8

"""
    ClickUp API Reference

    This is the ClickUp API Reference where you can learn about specific endpoints and parameters in detail.  Browse the available endpoints using the sidebar on the left.  **Not sure where to begin?** [Get Started with the ClickUp API](https://clickup.com/api) 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from click_up_python_sdk.paths.team.get import GetWorkspaceListRaw
from click_up_python_sdk.paths.team_team_id_plan.get import GetWorkspacePlanRaw
from click_up_python_sdk.paths.team_team_id_seats.get import GetWorkspaceSeatsRaw


class TeamsWorkspacesApiRaw(
    GetWorkspaceListRaw,
    GetWorkspacePlanRaw,
    GetWorkspaceSeatsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass