operation_parameter_map = {
    '/task/{task_id}/attachment-POST': {
        'parameters': [
            {
                'name': 'task_id'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'attachment'
            },
        ]
    },
    '/oauth/token-POST': {
        'parameters': [
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/team-GET': {
        'parameters': [
        ]
    },
    '/user-GET': {
        'parameters': [
        ]
    },
    '/list/{list_id}/comment-POST': {
        'parameters': [
            {
                'name': 'comment_text'
            },
            {
                'name': 'assignee'
            },
            {
                'name': 'notify_all'
            },
            {
                'name': 'list_id'
            },
        ]
    },
    '/view/{view_id}/comment-POST': {
        'parameters': [
            {
                'name': 'comment_text'
            },
            {
                'name': 'notify_all'
            },
            {
                'name': 'view_id'
            },
        ]
    },
    '/task/{task_id}/comment-POST': {
        'parameters': [
            {
                'name': 'comment_text'
            },
            {
                'name': 'assignee'
            },
            {
                'name': 'notify_all'
            },
            {
                'name': 'task_id'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/comment/{comment_id}-DELETE': {
        'parameters': [
            {
                'name': 'comment_id'
            },
        ]
    },
    '/list/{list_id}/comment-GET': {
        'parameters': [
            {
                'name': 'list_id'
            },
            {
                'name': 'start'
            },
            {
                'name': 'start_id'
            },
        ]
    },
    '/task/{task_id}/comment-GET': {
        'parameters': [
            {
                'name': 'task_id'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'start'
            },
            {
                'name': 'start_id'
            },
        ]
    },
    '/view/{view_id}/comment-GET': {
        'parameters': [
            {
                'name': 'view_id'
            },
            {
                'name': 'start'
            },
            {
                'name': 'start_id'
            },
        ]
    },
    '/comment/{comment_id}-PUT': {
        'parameters': [
            {
                'name': 'comment_text'
            },
            {
                'name': 'assignee'
            },
            {
                'name': 'resolved'
            },
            {
                'name': 'comment_id'
            },
        ]
    },
    '/list/{list_id}/field-GET': {
        'parameters': [
            {
                'name': 'list_id'
            },
        ]
    },
    '/task/{task_id}/field/{field_id}-DELETE': {
        'parameters': [
            {
                'name': 'task_id'
            },
            {
                'name': 'field_id'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/task/{task_id}/field/{field_id}-POST': {
        'parameters': [
            {
                'name': 'task_id'
            },
            {
                'name': 'field_id'
            },
            {
                'name': 'value'
            },
            {
                'name': 'value_options'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/team/{team_id}/custom_item-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
        ]
    },
    '/space/{space_id}/folder-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'space_id'
            },
        ]
    },
    '/space/{space_id}/folder-GET': {
        'parameters': [
            {
                'name': 'space_id'
            },
            {
                'name': 'archived'
            },
        ]
    },
    '/folder/{folder_id}-GET': {
        'parameters': [
            {
                'name': 'folder_id'
            },
        ]
    },
    '/folder/{folder_id}-DELETE': {
        'parameters': [
            {
                'name': 'folder_id'
            },
        ]
    },
    '/folder/{folder_id}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'folder_id'
            },
        ]
    },
    '/goal/{goal_id}/key_result-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'owners'
            },
            {
                'name': 'type'
            },
            {
                'name': 'steps_start'
            },
            {
                'name': 'steps_end'
            },
            {
                'name': 'unit'
            },
            {
                'name': 'task_ids'
            },
            {
                'name': 'list_ids'
            },
            {
                'name': 'goal_id'
            },
        ]
    },
    '/team/{team_id}/goal-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'due_date'
            },
            {
                'name': 'multiple_owners'
            },
            {
                'name': 'owners'
            },
            {
                'name': 'color'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/goal/{goal_id}-GET': {
        'parameters': [
            {
                'name': 'goal_id'
            },
        ]
    },
    '/team/{team_id}/goal-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
            {
                'name': 'include_completed'
            },
        ]
    },
    '/goal/{goal_id}-DELETE': {
        'parameters': [
            {
                'name': 'goal_id'
            },
        ]
    },
    '/key_result/{key_result_id}-DELETE': {
        'parameters': [
            {
                'name': 'key_result_id'
            },
        ]
    },
    '/goal/{goal_id}-PUT': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'due_date'
            },
            {
                'name': 'rem_owners'
            },
            {
                'name': 'add_owners'
            },
            {
                'name': 'color'
            },
            {
                'name': 'goal_id'
            },
        ]
    },
    '/key_result/{key_result_id}-PUT': {
        'parameters': [
            {
                'name': 'steps_current'
            },
            {
                'name': 'note'
            },
            {
                'name': 'key_result_id'
            },
        ]
    },
    '/folder/{folder_id}/guest/{guest_id}-POST': {
        'parameters': [
            {
                'name': 'permission_level'
            },
            {
                'name': 'folder_id'
            },
            {
                'name': 'guest_id'
            },
            {
                'name': 'include_shared'
            },
        ]
    },
    '/task/{task_id}/guest/{guest_id}-POST': {
        'parameters': [
            {
                'name': 'permission_level'
            },
            {
                'name': 'task_id'
            },
            {
                'name': 'guest_id'
            },
            {
                'name': 'include_shared'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/team/{team_id}/guest/{guest_id}-PUT': {
        'parameters': [
            {
                'name': 'username'
            },
            {
                'name': 'can_edit_tags'
            },
            {
                'name': 'can_see_time_spent'
            },
            {
                'name': 'can_see_time_estimated'
            },
            {
                'name': 'can_create_views'
            },
            {
                'name': 'custom_role_id'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'guest_id'
            },
        ]
    },
    '/team/{team_id}/guest/{guest_id}-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
            {
                'name': 'guest_id'
            },
        ]
    },
    '/team/{team_id}/guest-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'can_edit_tags'
            },
            {
                'name': 'can_see_time_spent'
            },
            {
                'name': 'can_see_time_estimated'
            },
            {
                'name': 'can_create_views'
            },
            {
                'name': 'custom_role_id'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/list/{list_id}/guest/{guest_id}-DELETE': {
        'parameters': [
            {
                'name': 'list_id'
            },
            {
                'name': 'guest_id'
            },
            {
                'name': 'include_shared'
            },
        ]
    },
    '/folder/{folder_id}/guest/{guest_id}-DELETE': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'guest_id'
            },
            {
                'name': 'include_shared'
            },
        ]
    },
    '/task/{task_id}/guest/{guest_id}-DELETE': {
        'parameters': [
            {
                'name': 'task_id'
            },
            {
                'name': 'guest_id'
            },
            {
                'name': 'include_shared'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/team/{team_id}/guest/{guest_id}-DELETE': {
        'parameters': [
            {
                'name': 'team_id'
            },
            {
                'name': 'guest_id'
            },
        ]
    },
    '/list/{list_id}/guest/{guest_id}-POST': {
        'parameters': [
            {
                'name': 'permission_level'
            },
            {
                'name': 'list_id'
            },
            {
                'name': 'guest_id'
            },
            {
                'name': 'include_shared'
            },
        ]
    },
    '/list/{list_id}/task/{task_id}-POST': {
        'parameters': [
            {
                'name': 'list_id'
            },
            {
                'name': 'task_id'
            },
        ]
    },
    '/folder/{folder_id}/list-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'folder_id'
            },
            {
                'name': 'content'
            },
            {
                'name': 'due_date'
            },
            {
                'name': 'due_date_time'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'assignee'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/space/{space_id}/list-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'space_id'
            },
            {
                'name': 'content'
            },
            {
                'name': 'due_date'
            },
            {
                'name': 'due_date_time'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'assignee'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/folder/{folder_id}/list-GET': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'archived'
            },
        ]
    },
    '/space/{space_id}/list-GET': {
        'parameters': [
            {
                'name': 'space_id'
            },
            {
                'name': 'archived'
            },
        ]
    },
    '/list/{list_id}-GET': {
        'parameters': [
            {
                'name': 'list_id'
            },
        ]
    },
    '/list/{list_id}-DELETE': {
        'parameters': [
            {
                'name': 'list_id'
            },
        ]
    },
    '/list/{list_id}/task/{task_id}-DELETE': {
        'parameters': [
            {
                'name': 'list_id'
            },
            {
                'name': 'task_id'
            },
        ]
    },
    '/list/{list_id}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'content'
            },
            {
                'name': 'due_date'
            },
            {
                'name': 'due_date_time'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'assignee'
            },
            {
                'name': 'status'
            },
            {
                'name': 'unset_status'
            },
            {
                'name': 'list_id'
            },
        ]
    },
    '/list/{list_id}/member-GET': {
        'parameters': [
            {
                'name': 'list_id'
            },
        ]
    },
    '/task/{task_id}/member-GET': {
        'parameters': [
            {
                'name': 'task_id'
            },
        ]
    },
    '/team/{team_id}/customroles-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
            {
                'name': 'include_members'
            },
        ]
    },
    '/team/{team_id}/shared-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
        ]
    },
    '/team/{team_id}/space-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'multiple_assignees'
            },
            {
                'name': 'features'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/space/{space_id}-GET': {
        'parameters': [
            {
                'name': 'space_id'
            },
        ]
    },
    '/team/{team_id}/space-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
            {
                'name': 'archived'
            },
        ]
    },
    '/space/{space_id}-DELETE': {
        'parameters': [
            {
                'name': 'space_id'
            },
        ]
    },
    '/space/{space_id}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'color'
            },
            {
                'name': 'private'
            },
            {
                'name': 'admin_can_manage'
            },
            {
                'name': 'multiple_assignees'
            },
            {
                'name': 'features'
            },
            {
                'name': 'space_id'
            },
        ]
    },
    '/task/{task_id}/tag/{tag_name}-POST': {
        'parameters': [
            {
                'name': 'task_id'
            },
            {
                'name': 'tag_name'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/space/{space_id}/tag-POST': {
        'parameters': [
            {
                'name': 'tag'
            },
            {
                'name': 'space_id'
            },
        ]
    },
    '/space/{space_id}/tag-GET': {
        'parameters': [
            {
                'name': 'space_id'
            },
        ]
    },
    '/task/{task_id}/tag/{tag_name}-DELETE': {
        'parameters': [
            {
                'name': 'task_id'
            },
            {
                'name': 'tag_name'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/space/{space_id}/tag/{tag_name}-DELETE': {
        'parameters': [
            {
                'name': 'tag'
            },
            {
                'name': 'space_id'
            },
            {
                'name': 'tag_name'
            },
        ]
    },
    '/space/{space_id}/tag/{tag_name}-PUT': {
        'parameters': [
            {
                'name': 'tag'
            },
            {
                'name': 'space_id'
            },
            {
                'name': 'tag_name'
            },
        ]
    },
    '/checklist/{checklist_id}/checklist_item-POST': {
        'parameters': [
            {
                'name': 'checklist_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'assignee'
            },
        ]
    },
    '/task/{task_id}/checklist-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'task_id'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/checklist/{checklist_id}-DELETE': {
        'parameters': [
            {
                'name': 'checklist_id'
            },
        ]
    },
    '/checklist/{checklist_id}/checklist_item/{checklist_item_id}-DELETE': {
        'parameters': [
            {
                'name': 'checklist_id'
            },
            {
                'name': 'checklist_item_id'
            },
        ]
    },
    '/checklist/{checklist_id}-PUT': {
        'parameters': [
            {
                'name': 'checklist_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'position'
            },
        ]
    },
    '/checklist/{checklist_id}/checklist_item/{checklist_item_id}-PUT': {
        'parameters': [
            {
                'name': 'checklist_id'
            },
            {
                'name': 'checklist_item_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'assignee'
            },
            {
                'name': 'resolved'
            },
            {
                'name': 'parent'
            },
        ]
    },
    '/task/{task_id}/dependency-POST': {
        'parameters': [
            {
                'name': 'task_id'
            },
            {
                'name': 'depends_on'
            },
            {
                'name': 'depedency_of'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/task/{task_id}/link/{links_to}-POST': {
        'parameters': [
            {
                'name': 'task_id'
            },
            {
                'name': 'links_to'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/task/{task_id}/dependency-DELETE': {
        'parameters': [
            {
                'name': 'task_id'
            },
            {
                'name': 'depends_on'
            },
            {
                'name': 'dependency_of'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/task/{task_id}/link/{links_to}-DELETE': {
        'parameters': [
            {
                'name': 'task_id'
            },
            {
                'name': 'links_to'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/list/{list_id}/taskTemplate/{template_id}-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'list_id'
            },
            {
                'name': 'template_id'
            },
        ]
    },
    '/team/{team_id}/taskTemplate-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/list/{list_id}/task-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'list_id'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'description'
            },
            {
                'name': 'assignees'
            },
            {
                'name': 'status'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'due_date'
            },
            {
                'name': 'due_date_time'
            },
            {
                'name': 'time_estimate'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'start_date_time'
            },
            {
                'name': 'notify_all'
            },
            {
                'name': 'parent'
            },
            {
                'name': 'links_to'
            },
            {
                'name': 'check_required_custom_fields'
            },
            {
                'name': 'custom_fields'
            },
            {
                'name': 'custom_item_id'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/team/{team_Id}/task-GET': {
        'parameters': [
            {
                'name': 'team_Id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'reverse'
            },
            {
                'name': 'subtasks'
            },
            {
                'name': 'space_ids'
            },
            {
                'name': 'project_ids'
            },
            {
                'name': 'list_ids'
            },
            {
                'name': 'statuses'
            },
            {
                'name': 'include_closed'
            },
            {
                'name': 'assignees'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'due_date_gt'
            },
            {
                'name': 'due_date_lt'
            },
            {
                'name': 'date_created_gt'
            },
            {
                'name': 'date_created_lt'
            },
            {
                'name': 'date_updated_gt'
            },
            {
                'name': 'date_updated_lt'
            },
            {
                'name': 'date_done_gt'
            },
            {
                'name': 'date_done_lt'
            },
            {
                'name': 'custom_fields'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'parent'
            },
            {
                'name': 'include_markdown_description'
            },
            {
                'name': 'custom_items'
            },
        ]
    },
    '/list/{list_id}/task-GET': {
        'parameters': [
            {
                'name': 'list_id'
            },
            {
                'name': 'archived'
            },
            {
                'name': 'include_markdown_description'
            },
            {
                'name': 'page'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'reverse'
            },
            {
                'name': 'subtasks'
            },
            {
                'name': 'statuses'
            },
            {
                'name': 'include_closed'
            },
            {
                'name': 'assignees'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'due_date_gt'
            },
            {
                'name': 'due_date_lt'
            },
            {
                'name': 'date_created_gt'
            },
            {
                'name': 'date_created_lt'
            },
            {
                'name': 'date_updated_gt'
            },
            {
                'name': 'date_updated_lt'
            },
            {
                'name': 'date_done_gt'
            },
            {
                'name': 'date_done_lt'
            },
            {
                'name': 'custom_fields'
            },
            {
                'name': 'custom_items'
            },
        ]
    },
    '/task/{task_id}-GET': {
        'parameters': [
            {
                'name': 'task_id'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'include_subtasks'
            },
            {
                'name': 'include_markdown_description'
            },
        ]
    },
    '/task/{task_id}/time_in_status-GET': {
        'parameters': [
            {
                'name': 'task_id'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/task/bulk_time_in_status/task_ids-GET': {
        'parameters': [
            {
                'name': 'task_ids'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/task/{task_id}-DELETE': {
        'parameters': [
            {
                'name': 'task_id'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/task/{task_id}-PUT': {
        'parameters': [
            {
                'name': 'task_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'custom_item_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'status'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'due_date'
            },
            {
                'name': 'due_date_time'
            },
            {
                'name': 'parent'
            },
            {
                'name': 'time_estimate'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'start_date_time'
            },
            {
                'name': 'assignees'
            },
            {
                'name': 'archived'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/team/{team_id}/group-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'members'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/group-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
            {
                'name': 'group_ids'
            },
        ]
    },
    '/group/{group_id}-DELETE': {
        'parameters': [
            {
                'name': 'group_id'
            },
        ]
    },
    '/group/{group_id}-PUT': {
        'parameters': [
            {
                'name': 'group_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'handle'
            },
            {
                'name': 'members'
            },
        ]
    },
    '/team-GET': {
        'parameters': [
        ]
    },
    '/team/{team_id}/plan-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
        ]
    },
    '/team/{team_id}/seats-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
        ]
    },
    '/team/{team_id}/time_entries/tags-POST': {
        'parameters': [
            {
                'name': 'tags'
            },
            {
                'name': 'time_entry_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/team/{team_id}/time_entries/tags-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'new_name'
            },
            {
                'name': 'tag_bg'
            },
            {
                'name': 'tag_fg'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/team/{team_Id}/time_entries-POST': {
        'parameters': [
            {
                'name': 'start'
            },
            {
                'name': 'duration'
            },
            {
                'name': 'team_Id'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'description'
            },
            {
                'name': 'stop'
            },
            {
                'name': 'end'
            },
            {
                'name': 'billable'
            },
            {
                'name': 'assignee'
            },
            {
                'name': 'tid'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/team/{team_id}/time_entries/tags-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
        ]
    },
    '/team/{team_id}/time_entries/current-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
            {
                'name': 'assignee'
            },
        ]
    },
    '/team/{team_id}/time_entries/{timer_id}-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
            {
                'name': 'timer_id'
            },
            {
                'name': 'include_task_'
            },
            {
                'name': 'include_location_names'
            },
        ]
    },
    '/team/{team_Id}/time_entries-GET': {
        'parameters': [
            {
                'name': 'team_Id'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'assignee'
            },
            {
                'name': 'include_task_tags'
            },
            {
                'name': 'include_location_names'
            },
            {
                'name': 'space_id'
            },
            {
                'name': 'folder_id'
            },
            {
                'name': 'list_id'
            },
            {
                'name': 'task_id'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/team/{team_id}/time_entries/{timer_id}/history-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
            {
                'name': 'timer_id'
            },
        ]
    },
    '/team/{team_id}/time_entries/{timer_id}-DELETE': {
        'parameters': [
            {
                'name': 'team_id'
            },
            {
                'name': 'timer_id'
            },
        ]
    },
    '/team/{team_id}/time_entries/tags-DELETE': {
        'parameters': [
            {
                'name': 'tags'
            },
            {
                'name': 'time_entry_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/team/{team_Id}/time_entries/start-POST': {
        'parameters': [
            {
                'name': 'team_Id'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'description'
            },
            {
                'name': 'tid'
            },
            {
                'name': 'billable'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/team/{team_id}/time_entries/stop-POST': {
        'parameters': [
            {
                'name': 'team_id'
            },
        ]
    },
    '/team/{team_id}/time_entries/{timer_id}-PUT': {
        'parameters': [
            {
                'name': 'tags'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'timer_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'tag_action'
            },
            {
                'name': 'start'
            },
            {
                'name': 'end'
            },
            {
                'name': 'tid'
            },
            {
                'name': 'billable'
            },
            {
                'name': 'duration'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/task/{task_id}/time/{interval_id}-PUT': {
        'parameters': [
            {
                'name': 'start'
            },
            {
                'name': 'end'
            },
            {
                'name': 'time'
            },
            {
                'name': 'task_id'
            },
            {
                'name': 'interval_id'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/task/{task_id}/time-GET': {
        'parameters': [
            {
                'name': 'task_id'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/task/{task_id}/time-POST': {
        'parameters': [
            {
                'name': 'start'
            },
            {
                'name': 'end'
            },
            {
                'name': 'time'
            },
            {
                'name': 'task_id'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/task/{task_id}/time/{interval_id}-DELETE': {
        'parameters': [
            {
                'name': 'task_id'
            },
            {
                'name': 'interval_id'
            },
            {
                'name': 'custom_task_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/team/{team_id}/user/{user_id}-DELETE': {
        'parameters': [
            {
                'name': 'team_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/team/{team_id}/user/{user_id}-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/team/{team_id}/user-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'admin'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'custom_role_id'
            },
        ]
    },
    '/team/{team_id}/user/{user_id}-PUT': {
        'parameters': [
            {
                'name': 'username'
            },
            {
                'name': 'admin'
            },
            {
                'name': 'custom_role_id'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/folder/{folder_id}/view-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'type'
            },
            {
                'name': 'grouping'
            },
            {
                'name': 'divide'
            },
            {
                'name': 'sorting'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'columns'
            },
            {
                'name': 'team_sidebar'
            },
            {
                'name': 'settings'
            },
            {
                'name': 'folder_id'
            },
        ]
    },
    '/list/{list_id}/view-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'type'
            },
            {
                'name': 'grouping'
            },
            {
                'name': 'divide'
            },
            {
                'name': 'sorting'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'columns'
            },
            {
                'name': 'team_sidebar'
            },
            {
                'name': 'settings'
            },
            {
                'name': 'list_id'
            },
        ]
    },
    '/space/{space_id}/view-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'type'
            },
            {
                'name': 'grouping'
            },
            {
                'name': 'divide'
            },
            {
                'name': 'sorting'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'columns'
            },
            {
                'name': 'team_sidebar'
            },
            {
                'name': 'settings'
            },
            {
                'name': 'space_id'
            },
        ]
    },
    '/team/{team_id}/view-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'type'
            },
            {
                'name': 'grouping'
            },
            {
                'name': 'divide'
            },
            {
                'name': 'sorting'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'columns'
            },
            {
                'name': 'team_sidebar'
            },
            {
                'name': 'settings'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/view/{view_id}-DELETE': {
        'parameters': [
            {
                'name': 'view_id'
            },
        ]
    },
    '/folder/{folder_id}/view-GET': {
        'parameters': [
            {
                'name': 'folder_id'
            },
        ]
    },
    '/team/{team_id}/view-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
        ]
    },
    '/list/{list_id}/view-GET': {
        'parameters': [
            {
                'name': 'list_id'
            },
        ]
    },
    '/view/{view_id}/task-GET': {
        'parameters': [
            {
                'name': 'view_id'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/view/{view_id}-GET': {
        'parameters': [
            {
                'name': 'view_id'
            },
        ]
    },
    '/space/{space_id}/view-GET': {
        'parameters': [
            {
                'name': 'space_id'
            },
        ]
    },
    '/view/{view_id}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'type'
            },
            {
                'name': 'parent'
            },
            {
                'name': 'grouping'
            },
            {
                'name': 'divide'
            },
            {
                'name': 'sorting'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'columns'
            },
            {
                'name': 'team_sidebar'
            },
            {
                'name': 'settings'
            },
            {
                'name': 'view_id'
            },
        ]
    },
    '/team/{team_id}/webhook-POST': {
        'parameters': [
            {
                'name': 'endpoint'
            },
            {
                'name': 'events'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'space_id'
            },
            {
                'name': 'folder_id'
            },
            {
                'name': 'list_id'
            },
            {
                'name': 'task_id'
            },
        ]
    },
    '/webhook/{webhook_id}-DELETE': {
        'parameters': [
            {
                'name': 'webhook_id'
            },
        ]
    },
    '/webhook/{webhook_id}-PUT': {
        'parameters': [
            {
                'name': 'endpoint'
            },
            {
                'name': 'events'
            },
            {
                'name': 'status'
            },
            {
                'name': 'webhook_id'
            },
        ]
    },
    '/team/{team_id}/webhook-GET': {
        'parameters': [
            {
                'name': 'team_id'
            },
        ]
    },
};