# -*- coding: utf-8 -*-

import sys

if sys.version_info[0] == 2:
    from pathlib2 import Path
else:
    from pathlib import Path

import os
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
    heredir = find_root()
    
    for arg in args:
        heredir = heredir / arg
      
    return heredir

def set_here(wd = None):
    if wd is None:
        wd = Path.cwd()
    elif type(wd) is str:
        wd = Path(wd)

    wd.parent.mkdir(parents=True, exist_ok=True)
    wd.joinpath(".here").touch()
        
def find_root(path = None):
    if path is None:
        return find_root(Path.cwd())
    else:
        for root_indicator in root_indicators:
            if path.joinpath(root_indicator).exists():
                return path
        
        next_path = path / ".."
        
        if (next_path.resolve() != path.resolve()):
            return find_root(next_path)
        else:
            warnings.warn("No project indicator found - returning root system directory")
            return path
