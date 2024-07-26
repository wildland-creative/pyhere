# pyhere

[![Build Status](https://app.travis-ci.com/wildland-creative/pyhere.svg?token=GxyKmrsgdFZwzkt4xB3m&branch=master)](https://travis-ci.com/wildland-creative/pyhere)
[![Latest pypi version](https://img.shields.io/pypi/v/pyhere)](https://pypi.org/project/pyhere/)

A Python 2.x / 3.x equivalent of R's [`here`][1] package, drawing inspiration from [chendaniely][2]'s [`pyprojroot`][3] package, but more closely mirroring the functionality within R's `here`. Relative file referencing has never been easier!

For complete information, check out the [docs](docs).

## Installation

### pip

You can install the latest stable version with pip via:

```bash
pip install pyhere
```

And if you want to be on the bleeding edge of development, get the latest version from github:

```bash
pip install --editable=git+https://github.com/wildland-creative/pyhere.git#egg=pyhere
```

### conda

Not in conda - just install it from pip in your environment.

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

## Changelog

[Changelog is over here.](CHANGELOG.md)

[1]: https://github.com/r-lib/here
[2]: https://github.com/chendaniely
[3]: https://github.com/chendaniely/pyprojroot
