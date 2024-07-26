# -*- coding: utf-8 -*-

import sys

if sys.version_info[0] == 2:
    from pathlib2 import Path
else:
    from pathlib import Path

import warnings

root_indicators = [
    ".here",
    "requirements.txt",
    "setup.py",
    ".vscode", # vscode project
    ".idea", # pycharm project
    ".git",
    ".spyderproject", # spyder
    ".spyproject", # spyder
    ".ropeproject" # rope
]

def here(*args):
    """
    Finds a project's root directory and then iteratively appends all passed
    arguments to it, construction a path relative to the root directory.

    Parameters
    ----------
    *args : Path or str
        The path additions to be attached to the root directory.

    Returns
    -------
    Path
        A path directory pointing to the passed arguments relative to the
        project's root directory.

    """
    heredir = find_root()
    
    for arg in args:
        heredir = heredir / arg
      
    return heredir.resolve()

def set_here(wd = None):
    """
    Creates a .here file at the passed directory.

    Parameters
    ----------
    wd : Path object or string
        The directory that a .here file will be created in. If none is set,
        uses Path.cwd()
    
    """
    if wd is None:
        wd = Path.cwd()
    elif type(wd) is str:
        wd = Path(wd)

    wd.parent.mkdir(parents=True, exist_ok=True)
    wd.joinpath(".here").touch()
        
    
def find_root(path = None):
    """
    Find's the root of a python project.
    
    Traverses directories upwards, iteratively searching for root_indicators.
    If no match is found, the system root is returned and a warning is thrown.

    Parameters
    ----------
    path : Path, str or None
        The starting directory to begin the search. If none is set, uses
        Path.cwd()

    Returns
    -------
    Path
        Either the path where a root_indicator was found or the system root.

    """
    if path is None:
        return find_root(Path.cwd())
    else:
        for root_indicator in root_indicators:
            if path.joinpath(root_indicator).exists():
                return path.resolve()
        
        next_path = path / ".."
        
        # if we've hit the system root
        if (next_path.resolve() != path.resolve()):
            return find_root(next_path)
        else:
            warnings.warn(
                "No project indicator found - returning root system directory"
            )
            return path.resolve()
