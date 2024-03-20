from click_up_python_sdk.paths.list_list_id.get import ApiForget
from click_up_python_sdk.paths.list_list_id.put import ApiForput
from click_up_python_sdk.paths.list_list_id.delete import ApiFordelete


class ListListId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
