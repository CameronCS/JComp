from typing import Literal
from os     import getcwd, walk

__package__ = "JPack"
__version__ = "1.1.0.0"
__name__    = "file_sys.py"
__all__     = [
    "get_file",
    "get_folder",
    "get_package",
    "get_embeded_files",
    "get_embeded_dirs"
]

# METHODS #
def extract_files(path: str) -> tuple[Literal[""], str] | tuple[str, str]:
    found = False    
    index = len(path) - 1
    while index > 0 and found is False:
        c = path[index]
        if c == "\\" or c == "/":
            found = True
            folder = path[:index]
            file   = path[index + 1:]
        
        index -= 1

    if index == 0 and found is False:
        return "", path

    return folder, file

def get_file(path: str) -> str:
    _, file = extract_files(path)
    return file

def get_folder(path: str) -> str:
    folder, _ = extract_files(path)
    return folder

def get_package(folders: str) -> str:
    _folders = get_folder(folders)
    if _folders.__contains__("/"):
        repChar = "/"
    else:
        repChar = "\\"

    return _folders.replace(repChar, ".")

def get_embeded_files(path: str) -> list[str]:
    file_ls = []
    contents = walk(path)

    for root, _, files in contents:
        for file in files:
            file_ls.append(f"{root}\\{file}")

    return file_ls

def get_embeded_dirs(path: str) -> list[str]:
    dir_ls = []
    content = walk(path)

    for root, _dirs, _ in content:
        for _dir in _dirs:
            dir_ls.append(f"{root}\\{_dir}")

    return dir_ls