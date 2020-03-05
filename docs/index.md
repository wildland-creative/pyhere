# pyhere: stopping path madness today

Release v1.0.0.

[![Build Status](https://travis-ci.com/dorkwood/pyhere.svg?branch=master)](https://travis-ci.com/joshpsawyer/pyhere)
[![Latest pypi version](https://img.shields.io/pypi/v/pyhere)](https://pypi.org/project/pyhere/)

# The User Guide

## Introduction

`pyhere` is a Python 2.x / 3.x equivalent of R's [`here`][1] package, drawing inspiration from [chendaniely][2]'s [`pyprojroot`][3] package, but more closely mirroring the functionality within R's `here`. It allows you to reference files relative to the root of a project, determined by some simple heuristics, and eliminate a lot of path nonsense.

For a more concrete example: imagine you've got a project you need to share with a colleague. You developed it on Windows, but they're on Linux. Your paths all look like this:

```python
telemetry = r"c:\\project\\Data\\Src\\Telemetry.dat"
telem_config = r"\\project\\telem.cfg"
...
```

As soon as your colleague runs your script, it will throw errors - both because those files don't exist in that location _and_ because that's not the convention for Linux paths. You've created work for your colleague just by sending them the project.

`pyhere` allows you to specify paths relative to the _root_ of your project as follows:

```python
telemetry = here("Data", "Src", "Telemetry.dat")
telem_config = here("telem.cfg")
```

Even better - these aren't strings, they're platform safe `Path` objects. Your colleague will thank you for not wasting their time and you'll feel good about creating reproducible work.

## Installation

### pip

You can install the latest stable version with pip via:

```bash
pip install pyhere
```

### conda

Not in conda, yet - just install it from pip in your environment.

## Quickstart

```python
from pyhere import here

relative_dirA = here("your", "relative", "directory", "file.txt")
relative_dirB = here("your/relative/directory/file.txt")
```

`pyhere` uses simple heuristics to find a project's root directory. From `Path.cwd()`, it traverses upwards, looking for a possible `root_indicator`:

```python
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
```

When found, it joins the arguments passed to `here()` to the rootpath and returns as a `Path` object. If it reaches the system root, it returns the system root and throws a warning.

For a concrete example, imagine the following directory structure:

```
\project\src\script.py
\project\data\data1.csv
\project\.here
```

If you call

```python
data = here("data", "data1.csv")
```

from `script.py`, you'll get a `Path` object representing `\project\data\data1.csv`.

## Advanced Usage

There are three exposed functions in this package and one exposed list and that's it. They are as follows:

- `here()`: This function can take any number of string or path arguments and it will build a pathlib `Path` object relative to your project's root directory and return it. You can pass strings in the form of `here("a/relative/scheme")` or as individual items: `here("a", "relative", "scheme")`. The intention behind multiple arguments is to reduce mental friction for people working in both R and Python.
- `set_here()`: This function takes a `Path` object and creates a `.here` file at that location, creating directories as necessary. Strictly speaking, this doesn't need to exist but because it exists in the R equivalent it's maintained here.
- `find_root()`: This is used by `here()` whenever it's called. It uses the above described heuristics to find exactly where the project root is. It takes no parameters and returns a `Path` object.
- `root_indicators[]`: This is simply a list of the root indicators in the event the user wants to review them.

## A note on strings vs. Path objects

String-based paths are very common and many modules - I'm looking at you, `arcpy` - use them as normal. They're not going away anytime soon. I won't get too into the weeds on why string paths suck - [Trey Hunner already did that quite eloquently](https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/) - so just know that if you're working with something that requires a string path, you can always do the following:

```python
a_string_path = str(here("what", "a", "path.txt"))
```

and get a platform specific string for that path. (I originally thought about adding string support to `pyhere`, but it's really unnecessary based on how simple it is to convert to string.)

## Release History

### 1.0.0 (2020-03-05)

First production release. Public API is now stable and version numbering will follow Semantic Versioning going forward. Improvements, bugfixes, dependencies and deprecations will be noted relative to previous version going forward.

But realistically, this repo will be quiet unless somebody finds an issue or Python 4 rolls out.

### 0.2.0 (2020-02-23)

Pre-release not ready for production.

### 0.1.0 (2020-02-23)

Pre-release not ready for production.

[1]: https://github.com/r-lib/here
[2]: https://github.com/chendaniely
[3]: https://github.com/chendaniely/pyprojroot
