from click_up_python_sdk.paths.folder_folder_id.get import ApiForget
from click_up_python_sdk.paths.folder_folder_id.put import ApiForput
from click_up_python_sdk.paths.folder_folder_id.delete import ApiFordelete


class FolderFolderId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
