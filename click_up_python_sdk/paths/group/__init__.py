# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from click_up_python_sdk.paths.group import Api

from click_up_python_sdk.paths import PathValues

path = PathValues.GROUP