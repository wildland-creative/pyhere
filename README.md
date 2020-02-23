# pyhere

[![Build Status](https://travis-ci.com/joshpsawyer/pyhere.svg?branch=master)](https://travis-ci.com/joshpsawyer/pyhere)
[![Latest pypi version](https://img.shields.io/pypi/v/pyhere)](https://pypi.org/project/pyhere/)

A Python 2.x / 3.x equivalent of R's [`here`][1] package, drawing inspiration from [chendaniely][2]'s [`pyprojroot`][3] package, but more closely mirroring the functionality within R's `here`. Relative file referencing has never been easier!

## Installation

### pip

You can install the latest stable version with pip via:

```bash
pip install pyhere
```

And if you want to be on the bleeding edge of development, get the latest version from github:

```bash
pip install --editable=git+https://github.com/joshpsawyer/pyhere.git#egg=pyhere
```

### conda

Not in conda, yet - just install it from pip in your environment.

## Usage

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

### In consideration of arcpy

`arcpy` wants a string for in / out feature classes. Wrap `here()` in `str()` as follows:

```python
polyline = str(here("data.gdb", "f_dataset", "roads"))
```

[1]: https://github.com/r-lib/here
[2]: https://github.com/chendaniely
[3]: https://github.com/chendaniely/pyprojroot
