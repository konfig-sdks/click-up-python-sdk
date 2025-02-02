# coding: utf-8

"""
    ClickUp API Reference

    This is the ClickUp API Reference where you can learn about specific endpoints and parameters in detail.  Browse the available endpoints using the sidebar on the left.  **Not sure where to begin?** [Get Started with the ClickUp API](https://clickup.com/api) 

    The version of the OpenAPI document: 2.0
    Generated by: https://konfigthis.com
"""

from click_up_python_sdk.paths.goal_goal_id_key_result.post import AddKeyResultRaw
from click_up_python_sdk.paths.team_team_id_goal.post import AddNewGoalToWorkspaceRaw
from click_up_python_sdk.paths.goal_goal_id.get import GetDetailsRaw
from click_up_python_sdk.paths.team_team_id_goal.get import GetWorkspaceGoalsRaw
from click_up_python_sdk.paths.goal_goal_id.delete import RemoveGoalRaw
from click_up_python_sdk.paths.key_result_key_result_id.delete import RemoveTargetRaw
from click_up_python_sdk.paths.goal_goal_id.put import UpdateGoalDetailsRaw
from click_up_python_sdk.paths.key_result_key_result_id.put import UpdateKeyResultRaw


class GoalsApiRaw(
    AddKeyResultRaw,
    AddNewGoalToWorkspaceRaw,
    GetDetailsRaw,
    GetWorkspaceGoalsRaw,
    RemoveGoalRaw,
    RemoveTargetRaw,
    UpdateGoalDetailsRaw,
    UpdateKeyResultRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
