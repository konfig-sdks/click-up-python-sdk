from click_up_python_sdk.paths.view_view_id.get import ApiForget
from click_up_python_sdk.paths.view_view_id.put import ApiForput
from click_up_python_sdk.paths.view_view_id.delete import ApiFordelete


class ViewViewId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
