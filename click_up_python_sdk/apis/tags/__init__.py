# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from click_up_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    TIME_TRACKING = "Time Tracking"
    VIEWS = "Views"
    GUESTS = "Guests"
    LISTS = "Lists"
    COMMENTS = "Comments"
    GOALS = "Goals"
    TASKS = "Tasks"
    TAGS = "Tags"
    TASK_CHECKLISTS = "Task Checklists"
    FOLDERS = "Folders"
    SPACES = "Spaces"
    TASK_RELATIONSHIPS = "Task Relationships"
    TEAMS__USER_GROUPS = "Teams - User Groups"
    TIME_TRACKING_LEGACY = "Time Tracking (Legacy)"
    USERS = "Users"
    WEBHOOKS = "Webhooks"
    AUTHORIZATION = "Authorization"
    CUSTOM_FIELDS = "Custom Fields"
    TEAMS__WORKSPACES = "Teams - Workspaces"
    MEMBERS = "Members"
    TASK_TEMPLATES = "Task Templates"
    ATTACHMENTS = "Attachments"
    CUSTOM_TASK_TYPES = "Custom Task Types"
    ROLES = "Roles"
    SHARED_HIERARCHY = "Shared Hierarchy"
