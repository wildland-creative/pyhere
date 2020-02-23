# pyhere

[![Build Status](https://travis-ci.com/joshpsawyer/pyhere.svg?branch=master)](https://travis-ci.com/joshpsawyer/pyhere)

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
In: from pyhere import here

In: here("your", "relative", "directory", "file.txt")
Out: 'C:\\proj\\code\\pyhere\\your\\relative\\directory\\file.txt'
```

`pyhere` uses simple heuristics to find a project's root directory. From `os.cwd()`, it traverses upwards, looking for a possible `root_indicator`:

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

When found, it attaches to that root path all arguments passed to `here()`. If it reaches the system root, it returns the system root and throws a warning. Returned values are strings.

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

from `script.py`, you'll get a string representing `\project\data\data1.csv` with your system specific path formatting.


[1]: https://github.com/r-lib/here
[2]: https://github.com/chendaniely
[3]: https://github.com/chendaniely/pyprojroot
