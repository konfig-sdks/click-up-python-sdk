import typing_extensions

from click_up_python_sdk.paths import PathValues
from click_up_python_sdk.apis.paths.task_task_id_attachment import TaskTaskIdAttachment
from click_up_python_sdk.apis.paths.oauth_token import OauthToken
from click_up_python_sdk.apis.paths.user import User
from click_up_python_sdk.apis.paths.team import Team
from click_up_python_sdk.apis.paths.task_task_id_checklist import TaskTaskIdChecklist
from click_up_python_sdk.apis.paths.checklist_checklist_id import ChecklistChecklistId
from click_up_python_sdk.apis.paths.checklist_checklist_id_checklist_item import ChecklistChecklistIdChecklistItem
from click_up_python_sdk.apis.paths.checklist_checklist_id_checklist_item_checklist_item_id import ChecklistChecklistIdChecklistItemChecklistItemId
from click_up_python_sdk.apis.paths.task_task_id_comment import TaskTaskIdComment
from click_up_python_sdk.apis.paths.view_view_id_comment import ViewViewIdComment
from click_up_python_sdk.apis.paths.list_list_id_comment import ListListIdComment
from click_up_python_sdk.apis.paths.comment_comment_id import CommentCommentId
from click_up_python_sdk.apis.paths.list_list_id_field import ListListIdField
from click_up_python_sdk.apis.paths.task_task_id_field_field_id import TaskTaskIdFieldFieldId
from click_up_python_sdk.apis.paths.task_task_id_dependency import TaskTaskIdDependency
from click_up_python_sdk.apis.paths.task_task_id_link_links_to import TaskTaskIdLinkLinksTo
from click_up_python_sdk.apis.paths.space_space_id_folder import SpaceSpaceIdFolder
from click_up_python_sdk.apis.paths.folder_folder_id import FolderFolderId
from click_up_python_sdk.apis.paths.team_team_id_goal import TeamTeamIdGoal
from click_up_python_sdk.apis.paths.goal_goal_id import GoalGoalId
from click_up_python_sdk.apis.paths.goal_goal_id_key_result import GoalGoalIdKeyResult
from click_up_python_sdk.apis.paths.key_result_key_result_id import KeyResultKeyResultId
from click_up_python_sdk.apis.paths.team_team_id_guest import TeamTeamIdGuest
from click_up_python_sdk.apis.paths.team_team_id_guest_guest_id import TeamTeamIdGuestGuestId
from click_up_python_sdk.apis.paths.task_task_id_guest_guest_id import TaskTaskIdGuestGuestId
from click_up_python_sdk.apis.paths.list_list_id_guest_guest_id import ListListIdGuestGuestId
from click_up_python_sdk.apis.paths.folder_folder_id_guest_guest_id import FolderFolderIdGuestGuestId
from click_up_python_sdk.apis.paths.folder_folder_id_list import FolderFolderIdList
from click_up_python_sdk.apis.paths.space_space_id_list import SpaceSpaceIdList
from click_up_python_sdk.apis.paths.list_list_id import ListListId
from click_up_python_sdk.apis.paths.list_list_id_task_task_id import ListListIdTaskTaskId
from click_up_python_sdk.apis.paths.task_task_id_member import TaskTaskIdMember
from click_up_python_sdk.apis.paths.list_list_id_member import ListListIdMember
from click_up_python_sdk.apis.paths.team_team_id_customroles import TeamTeamIdCustomroles
from click_up_python_sdk.apis.paths.team_team_id_shared import TeamTeamIdShared
from click_up_python_sdk.apis.paths.team_team_id_space import TeamTeamIdSpace
from click_up_python_sdk.apis.paths.space_space_id import SpaceSpaceId
from click_up_python_sdk.apis.paths.space_space_id_tag import SpaceSpaceIdTag
from click_up_python_sdk.apis.paths.space_space_id_tag_tag_name import SpaceSpaceIdTagTagName
from click_up_python_sdk.apis.paths.task_task_id_tag_tag_name import TaskTaskIdTagTagName
from click_up_python_sdk.apis.paths.list_list_id_task import ListListIdTask
from click_up_python_sdk.apis.paths.task_task_id import TaskTaskId
from click_up_python_sdk.apis.paths.team_team_id_task import TeamTeamIdTask
from click_up_python_sdk.apis.paths.task_task_id_time_in_status import TaskTaskIdTimeInStatus
from click_up_python_sdk.apis.paths.task_bulk_time_in_status_task_ids import TaskBulkTimeInStatusTaskIds
from click_up_python_sdk.apis.paths.team_team_id_task_template import TeamTeamIdTaskTemplate
from click_up_python_sdk.apis.paths.list_list_id_task_template_template_id import ListListIdTaskTemplateTemplateId
from click_up_python_sdk.apis.paths.team_team_id_seats import TeamTeamIdSeats
from click_up_python_sdk.apis.paths.team_team_id_plan import TeamTeamIdPlan
from click_up_python_sdk.apis.paths.team_team_id_group import TeamTeamIdGroup
from click_up_python_sdk.apis.paths.team_team_id_custom_item import TeamTeamIdCustomItem
from click_up_python_sdk.apis.paths.group_group_id import GroupGroupId
from click_up_python_sdk.apis.paths.group import Group
from click_up_python_sdk.apis.paths.task_task_id_time import TaskTaskIdTime
from click_up_python_sdk.apis.paths.task_task_id_time_interval_id import TaskTaskIdTimeIntervalId
from click_up_python_sdk.apis.paths.team_team_id_time_entries import TeamTeamIdTimeEntries
from click_up_python_sdk.apis.paths.team_team_id_time_entries_timer_id import TeamTeamIdTimeEntriesTimerId
from click_up_python_sdk.apis.paths.team_team_id_time_entries_timer_id_history import TeamTeamIdTimeEntriesTimerIdHistory
from click_up_python_sdk.apis.paths.team_team_id_time_entries_current import TeamTeamIdTimeEntriesCurrent
from click_up_python_sdk.apis.paths.team_team_id_time_entries_tags import TeamTeamIdTimeEntriesTags
from click_up_python_sdk.apis.paths.team_team_id_time_entries_start import TeamTeamIdTimeEntriesStart
from click_up_python_sdk.apis.paths.team_team_id_time_entries_stop import TeamTeamIdTimeEntriesStop
from click_up_python_sdk.apis.paths.team_team_id_user import TeamTeamIdUser
from click_up_python_sdk.apis.paths.team_team_id_user_user_id import TeamTeamIdUserUserId
from click_up_python_sdk.apis.paths.team_team_id_view import TeamTeamIdView
from click_up_python_sdk.apis.paths.space_space_id_view import SpaceSpaceIdView
from click_up_python_sdk.apis.paths.folder_folder_id_view import FolderFolderIdView
from click_up_python_sdk.apis.paths.list_list_id_view import ListListIdView
from click_up_python_sdk.apis.paths.view_view_id import ViewViewId
from click_up_python_sdk.apis.paths.view_view_id_task import ViewViewIdTask
from click_up_python_sdk.apis.paths.team_team_id_webhook import TeamTeamIdWebhook
from click_up_python_sdk.apis.paths.webhook_webhook_id import WebhookWebhookId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.TASK_TASK_ID_ATTACHMENT: TaskTaskIdAttachment,
        PathValues.OAUTH_TOKEN: OauthToken,
        PathValues.USER: User,
        PathValues.TEAM: Team,
        PathValues.TASK_TASK_ID_CHECKLIST: TaskTaskIdChecklist,
        PathValues.CHECKLIST_CHECKLIST_ID: ChecklistChecklistId,
        PathValues.CHECKLIST_CHECKLIST_ID_CHECKLIST_ITEM: ChecklistChecklistIdChecklistItem,
        PathValues.CHECKLIST_CHECKLIST_ID_CHECKLIST_ITEM_CHECKLIST_ITEM_ID: ChecklistChecklistIdChecklistItemChecklistItemId,
        PathValues.TASK_TASK_ID_COMMENT: TaskTaskIdComment,
        PathValues.VIEW_VIEW_ID_COMMENT: ViewViewIdComment,
        PathValues.LIST_LIST_ID_COMMENT: ListListIdComment,
        PathValues.COMMENT_COMMENT_ID: CommentCommentId,
        PathValues.LIST_LIST_ID_FIELD: ListListIdField,
        PathValues.TASK_TASK_ID_FIELD_FIELD_ID: TaskTaskIdFieldFieldId,
        PathValues.TASK_TASK_ID_DEPENDENCY: TaskTaskIdDependency,
        PathValues.TASK_TASK_ID_LINK_LINKS_TO: TaskTaskIdLinkLinksTo,
        PathValues.SPACE_SPACE_ID_FOLDER: SpaceSpaceIdFolder,
        PathValues.FOLDER_FOLDER_ID: FolderFolderId,
        PathValues.TEAM_TEAM_ID_GOAL: TeamTeamIdGoal,
        PathValues.GOAL_GOAL_ID: GoalGoalId,
        PathValues.GOAL_GOAL_ID_KEY_RESULT: GoalGoalIdKeyResult,
        PathValues.KEY_RESULT_KEY_RESULT_ID: KeyResultKeyResultId,
        PathValues.TEAM_TEAM_ID_GUEST: TeamTeamIdGuest,
        PathValues.TEAM_TEAM_ID_GUEST_GUEST_ID: TeamTeamIdGuestGuestId,
        PathValues.TASK_TASK_ID_GUEST_GUEST_ID: TaskTaskIdGuestGuestId,
        PathValues.LIST_LIST_ID_GUEST_GUEST_ID: ListListIdGuestGuestId,
        PathValues.FOLDER_FOLDER_ID_GUEST_GUEST_ID: FolderFolderIdGuestGuestId,
        PathValues.FOLDER_FOLDER_ID_LIST: FolderFolderIdList,
        PathValues.SPACE_SPACE_ID_LIST: SpaceSpaceIdList,
        PathValues.LIST_LIST_ID: ListListId,
        PathValues.LIST_LIST_ID_TASK_TASK_ID: ListListIdTaskTaskId,
        PathValues.TASK_TASK_ID_MEMBER: TaskTaskIdMember,
        PathValues.LIST_LIST_ID_MEMBER: ListListIdMember,
        PathValues.TEAM_TEAM_ID_CUSTOMROLES: TeamTeamIdCustomroles,
        PathValues.TEAM_TEAM_ID_SHARED: TeamTeamIdShared,
        PathValues.TEAM_TEAM_ID_SPACE: TeamTeamIdSpace,
        PathValues.SPACE_SPACE_ID: SpaceSpaceId,
        PathValues.SPACE_SPACE_ID_TAG: SpaceSpaceIdTag,
        PathValues.SPACE_SPACE_ID_TAG_TAG_NAME: SpaceSpaceIdTagTagName,
        PathValues.TASK_TASK_ID_TAG_TAG_NAME: TaskTaskIdTagTagName,
        PathValues.LIST_LIST_ID_TASK: ListListIdTask,
        PathValues.TASK_TASK_ID: TaskTaskId,
        PathValues.TEAM_TEAM_ID_TASK: TeamTeamIdTask,
        PathValues.TASK_TASK_ID_TIME_IN_STATUS: TaskTaskIdTimeInStatus,
        PathValues.TASK_BULK_TIME_IN_STATUS_TASK_IDS: TaskBulkTimeInStatusTaskIds,
        PathValues.TEAM_TEAM_ID_TASK_TEMPLATE: TeamTeamIdTaskTemplate,
        PathValues.LIST_LIST_ID_TASK_TEMPLATE_TEMPLATE_ID: ListListIdTaskTemplateTemplateId,
        PathValues.TEAM_TEAM_ID_SEATS: TeamTeamIdSeats,
        PathValues.TEAM_TEAM_ID_PLAN: TeamTeamIdPlan,
        PathValues.TEAM_TEAM_ID_GROUP: TeamTeamIdGroup,
        PathValues.TEAM_TEAM_ID_CUSTOM_ITEM: TeamTeamIdCustomItem,
        PathValues.GROUP_GROUP_ID: GroupGroupId,
        PathValues.GROUP: Group,
        PathValues.TASK_TASK_ID_TIME: TaskTaskIdTime,
        PathValues.TASK_TASK_ID_TIME_INTERVAL_ID: TaskTaskIdTimeIntervalId,
        PathValues.TEAM_TEAM_ID_TIME_ENTRIES: TeamTeamIdTimeEntries,
        PathValues.TEAM_TEAM_ID_TIME_ENTRIES_TIMER_ID: TeamTeamIdTimeEntriesTimerId,
        PathValues.TEAM_TEAM_ID_TIME_ENTRIES_TIMER_ID_HISTORY: TeamTeamIdTimeEntriesTimerIdHistory,
        PathValues.TEAM_TEAM_ID_TIME_ENTRIES_CURRENT: TeamTeamIdTimeEntriesCurrent,
        PathValues.TEAM_TEAM_ID_TIME_ENTRIES_TAGS: TeamTeamIdTimeEntriesTags,
        PathValues.TEAM_TEAM_ID_TIME_ENTRIES_START: TeamTeamIdTimeEntriesStart,
        PathValues.TEAM_TEAM_ID_TIME_ENTRIES_STOP: TeamTeamIdTimeEntriesStop,
        PathValues.TEAM_TEAM_ID_USER: TeamTeamIdUser,
        PathValues.TEAM_TEAM_ID_USER_USER_ID: TeamTeamIdUserUserId,
        PathValues.TEAM_TEAM_ID_VIEW: TeamTeamIdView,
        PathValues.SPACE_SPACE_ID_VIEW: SpaceSpaceIdView,
        PathValues.FOLDER_FOLDER_ID_VIEW: FolderFolderIdView,
        PathValues.LIST_LIST_ID_VIEW: ListListIdView,
        PathValues.VIEW_VIEW_ID: ViewViewId,
        PathValues.VIEW_VIEW_ID_TASK: ViewViewIdTask,
        PathValues.TEAM_TEAM_ID_WEBHOOK: TeamTeamIdWebhook,
        PathValues.WEBHOOK_WEBHOOK_ID: WebhookWebhookId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.TASK_TASK_ID_ATTACHMENT: TaskTaskIdAttachment,
        PathValues.OAUTH_TOKEN: OauthToken,
        PathValues.USER: User,
        PathValues.TEAM: Team,
        PathValues.TASK_TASK_ID_CHECKLIST: TaskTaskIdChecklist,
        PathValues.CHECKLIST_CHECKLIST_ID: ChecklistChecklistId,
        PathValues.CHECKLIST_CHECKLIST_ID_CHECKLIST_ITEM: ChecklistChecklistIdChecklistItem,
        PathValues.CHECKLIST_CHECKLIST_ID_CHECKLIST_ITEM_CHECKLIST_ITEM_ID: ChecklistChecklistIdChecklistItemChecklistItemId,
        PathValues.TASK_TASK_ID_COMMENT: TaskTaskIdComment,
        PathValues.VIEW_VIEW_ID_COMMENT: ViewViewIdComment,
        PathValues.LIST_LIST_ID_COMMENT: ListListIdComment,
        PathValues.COMMENT_COMMENT_ID: CommentCommentId,
        PathValues.LIST_LIST_ID_FIELD: ListListIdField,
        PathValues.TASK_TASK_ID_FIELD_FIELD_ID: TaskTaskIdFieldFieldId,
        PathValues.TASK_TASK_ID_DEPENDENCY: TaskTaskIdDependency,
        PathValues.TASK_TASK_ID_LINK_LINKS_TO: TaskTaskIdLinkLinksTo,
        PathValues.SPACE_SPACE_ID_FOLDER: SpaceSpaceIdFolder,
        PathValues.FOLDER_FOLDER_ID: FolderFolderId,
        PathValues.TEAM_TEAM_ID_GOAL: TeamTeamIdGoal,
        PathValues.GOAL_GOAL_ID: GoalGoalId,
        PathValues.GOAL_GOAL_ID_KEY_RESULT: GoalGoalIdKeyResult,
        PathValues.KEY_RESULT_KEY_RESULT_ID: KeyResultKeyResultId,
        PathValues.TEAM_TEAM_ID_GUEST: TeamTeamIdGuest,
        PathValues.TEAM_TEAM_ID_GUEST_GUEST_ID: TeamTeamIdGuestGuestId,
        PathValues.TASK_TASK_ID_GUEST_GUEST_ID: TaskTaskIdGuestGuestId,
        PathValues.LIST_LIST_ID_GUEST_GUEST_ID: ListListIdGuestGuestId,
        PathValues.FOLDER_FOLDER_ID_GUEST_GUEST_ID: FolderFolderIdGuestGuestId,
        PathValues.FOLDER_FOLDER_ID_LIST: FolderFolderIdList,
        PathValues.SPACE_SPACE_ID_LIST: SpaceSpaceIdList,
        PathValues.LIST_LIST_ID: ListListId,
        PathValues.LIST_LIST_ID_TASK_TASK_ID: ListListIdTaskTaskId,
        PathValues.TASK_TASK_ID_MEMBER: TaskTaskIdMember,
        PathValues.LIST_LIST_ID_MEMBER: ListListIdMember,
        PathValues.TEAM_TEAM_ID_CUSTOMROLES: TeamTeamIdCustomroles,
        PathValues.TEAM_TEAM_ID_SHARED: TeamTeamIdShared,
        PathValues.TEAM_TEAM_ID_SPACE: TeamTeamIdSpace,
        PathValues.SPACE_SPACE_ID: SpaceSpaceId,
        PathValues.SPACE_SPACE_ID_TAG: SpaceSpaceIdTag,
        PathValues.SPACE_SPACE_ID_TAG_TAG_NAME: SpaceSpaceIdTagTagName,
        PathValues.TASK_TASK_ID_TAG_TAG_NAME: TaskTaskIdTagTagName,
        PathValues.LIST_LIST_ID_TASK: ListListIdTask,
        PathValues.TASK_TASK_ID: TaskTaskId,
        PathValues.TEAM_TEAM_ID_TASK: TeamTeamIdTask,
        PathValues.TASK_TASK_ID_TIME_IN_STATUS: TaskTaskIdTimeInStatus,
        PathValues.TASK_BULK_TIME_IN_STATUS_TASK_IDS: TaskBulkTimeInStatusTaskIds,
        PathValues.TEAM_TEAM_ID_TASK_TEMPLATE: TeamTeamIdTaskTemplate,
        PathValues.LIST_LIST_ID_TASK_TEMPLATE_TEMPLATE_ID: ListListIdTaskTemplateTemplateId,
        PathValues.TEAM_TEAM_ID_SEATS: TeamTeamIdSeats,
        PathValues.TEAM_TEAM_ID_PLAN: TeamTeamIdPlan,
        PathValues.TEAM_TEAM_ID_GROUP: TeamTeamIdGroup,
        PathValues.TEAM_TEAM_ID_CUSTOM_ITEM: TeamTeamIdCustomItem,
        PathValues.GROUP_GROUP_ID: GroupGroupId,
        PathValues.GROUP: Group,
        PathValues.TASK_TASK_ID_TIME: TaskTaskIdTime,
        PathValues.TASK_TASK_ID_TIME_INTERVAL_ID: TaskTaskIdTimeIntervalId,
        PathValues.TEAM_TEAM_ID_TIME_ENTRIES: TeamTeamIdTimeEntries,
        PathValues.TEAM_TEAM_ID_TIME_ENTRIES_TIMER_ID: TeamTeamIdTimeEntriesTimerId,
        PathValues.TEAM_TEAM_ID_TIME_ENTRIES_TIMER_ID_HISTORY: TeamTeamIdTimeEntriesTimerIdHistory,
        PathValues.TEAM_TEAM_ID_TIME_ENTRIES_CURRENT: TeamTeamIdTimeEntriesCurrent,
        PathValues.TEAM_TEAM_ID_TIME_ENTRIES_TAGS: TeamTeamIdTimeEntriesTags,
        PathValues.TEAM_TEAM_ID_TIME_ENTRIES_START: TeamTeamIdTimeEntriesStart,
        PathValues.TEAM_TEAM_ID_TIME_ENTRIES_STOP: TeamTeamIdTimeEntriesStop,
        PathValues.TEAM_TEAM_ID_USER: TeamTeamIdUser,
        PathValues.TEAM_TEAM_ID_USER_USER_ID: TeamTeamIdUserUserId,
        PathValues.TEAM_TEAM_ID_VIEW: TeamTeamIdView,
        PathValues.SPACE_SPACE_ID_VIEW: SpaceSpaceIdView,
        PathValues.FOLDER_FOLDER_ID_VIEW: FolderFolderIdView,
        PathValues.LIST_LIST_ID_VIEW: ListListIdView,
        PathValues.VIEW_VIEW_ID: ViewViewId,
        PathValues.VIEW_VIEW_ID_TASK: ViewViewIdTask,
        PathValues.TEAM_TEAM_ID_WEBHOOK: TeamTeamIdWebhook,
        PathValues.WEBHOOK_WEBHOOK_ID: WebhookWebhookId,
    }
)
