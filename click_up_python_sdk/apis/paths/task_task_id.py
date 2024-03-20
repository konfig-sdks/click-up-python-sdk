from click_up_python_sdk.paths.task_task_id.get import ApiForget
from click_up_python_sdk.paths.task_task_id.put import ApiForput
from click_up_python_sdk.paths.task_task_id.delete import ApiFordelete


class TaskTaskId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
