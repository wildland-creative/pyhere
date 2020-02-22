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

# credit to ThiefMaster on stack overflow for a simple touch function
# https://stackoverflow.com/questions/12654772/create-empty-file-using-python
def touch(path):
    basedir = os.path.dirname(path)
    
    if not os.path.exists(basedir):
        os.makedirs(basedir)

    with open(path, 'a'):
        os.utime(path, None)

def here(*args):
    heredir = find_root()
    
    for arg in args:
        heredir = os.path.join(heredir, arg)
      
    return heredir

def set_here(wd = None):
    if wd is None:
        wd = os.getcwd()

    touch(os.path.join(wd, ".here"))
        
def find_root(path = None):
    if path is None:
        return find_root(os.getcwd())
    else:
        for root_indicator in root_indicators:
            if os.path.isfile(os.path.join(path, root_indicator)):
                return os.path.abspath(path)
            elif os.path.isdir(os.path.join(path, root_indicator)):
                return os.path.abspath(path)
        
        next_path = os.path.join(path, "..")
        
        if (os.path.realpath(next_path) != os.path.realpath(path)):
            return find_root(os.path.join(path, ".."))
        else:
            warnings.warn("No project indicator found - returning root system directory")
            return os.path.abspath(path)
