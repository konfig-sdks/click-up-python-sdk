import typing_extensions

from click_up_python_sdk.apis.tags import TagValues
from click_up_python_sdk.apis.tags.time_tracking_api import TimeTrackingApi
from click_up_python_sdk.apis.tags.views_api import ViewsApi
from click_up_python_sdk.apis.tags.guests_api import GuestsApi
from click_up_python_sdk.apis.tags.lists_api import ListsApi
from click_up_python_sdk.apis.tags.comments_api import CommentsApi
from click_up_python_sdk.apis.tags.goals_api import GoalsApi
from click_up_python_sdk.apis.tags.tasks_api import TasksApi
from click_up_python_sdk.apis.tags.tags_api import TagsApi
from click_up_python_sdk.apis.tags.task_checklists_api import TaskChecklistsApi
from click_up_python_sdk.apis.tags.folders_api import FoldersApi
from click_up_python_sdk.apis.tags.spaces_api import SpacesApi
from click_up_python_sdk.apis.tags.task_relationships_api import TaskRelationshipsApi
from click_up_python_sdk.apis.tags.teams_user_groups_api import TeamsUserGroupsApi
from click_up_python_sdk.apis.tags.time_tracking_legacy_api import TimeTrackingLegacyApi
from click_up_python_sdk.apis.tags.users_api import UsersApi
from click_up_python_sdk.apis.tags.webhooks_api import WebhooksApi
from click_up_python_sdk.apis.tags.authorization_api import AuthorizationApi
from click_up_python_sdk.apis.tags.custom_fields_api import CustomFieldsApi
from click_up_python_sdk.apis.tags.teams_workspaces_api import TeamsWorkspacesApi
from click_up_python_sdk.apis.tags.members_api import MembersApi
from click_up_python_sdk.apis.tags.task_templates_api import TaskTemplatesApi
from click_up_python_sdk.apis.tags.attachments_api import AttachmentsApi
from click_up_python_sdk.apis.tags.custom_task_types_api import CustomTaskTypesApi
from click_up_python_sdk.apis.tags.roles_api import RolesApi
from click_up_python_sdk.apis.tags.shared_hierarchy_api import SharedHierarchyApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.TIME_TRACKING: TimeTrackingApi,
        TagValues.VIEWS: ViewsApi,
        TagValues.GUESTS: GuestsApi,
        TagValues.LISTS: ListsApi,
        TagValues.COMMENTS: CommentsApi,
        TagValues.GOALS: GoalsApi,
        TagValues.TASKS: TasksApi,
        TagValues.TAGS: TagsApi,
        TagValues.TASK_CHECKLISTS: TaskChecklistsApi,
        TagValues.FOLDERS: FoldersApi,
        TagValues.SPACES: SpacesApi,
        TagValues.TASK_RELATIONSHIPS: TaskRelationshipsApi,
        TagValues.TEAMS__USER_GROUPS: TeamsUserGroupsApi,
        TagValues.TIME_TRACKING_LEGACY: TimeTrackingLegacyApi,
        TagValues.USERS: UsersApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.AUTHORIZATION: AuthorizationApi,
        TagValues.CUSTOM_FIELDS: CustomFieldsApi,
        TagValues.TEAMS__WORKSPACES: TeamsWorkspacesApi,
        TagValues.MEMBERS: MembersApi,
        TagValues.TASK_TEMPLATES: TaskTemplatesApi,
        TagValues.ATTACHMENTS: AttachmentsApi,
        TagValues.CUSTOM_TASK_TYPES: CustomTaskTypesApi,
        TagValues.ROLES: RolesApi,
        TagValues.SHARED_HIERARCHY: SharedHierarchyApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.TIME_TRACKING: TimeTrackingApi,
        TagValues.VIEWS: ViewsApi,
        TagValues.GUESTS: GuestsApi,
        TagValues.LISTS: ListsApi,
        TagValues.COMMENTS: CommentsApi,
        TagValues.GOALS: GoalsApi,
        TagValues.TASKS: TasksApi,
        TagValues.TAGS: TagsApi,
        TagValues.TASK_CHECKLISTS: TaskChecklistsApi,
        TagValues.FOLDERS: FoldersApi,
        TagValues.SPACES: SpacesApi,
        TagValues.TASK_RELATIONSHIPS: TaskRelationshipsApi,
        TagValues.TEAMS__USER_GROUPS: TeamsUserGroupsApi,
        TagValues.TIME_TRACKING_LEGACY: TimeTrackingLegacyApi,
        TagValues.USERS: UsersApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.AUTHORIZATION: AuthorizationApi,
        TagValues.CUSTOM_FIELDS: CustomFieldsApi,
        TagValues.TEAMS__WORKSPACES: TeamsWorkspacesApi,
        TagValues.MEMBERS: MembersApi,
        TagValues.TASK_TEMPLATES: TaskTemplatesApi,
        TagValues.ATTACHMENTS: AttachmentsApi,
        TagValues.CUSTOM_TASK_TYPES: CustomTaskTypesApi,
        TagValues.ROLES: RolesApi,
        TagValues.SHARED_HIERARCHY: SharedHierarchyApi,
    }
)
