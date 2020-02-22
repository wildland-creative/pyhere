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
pip install --editable=git+https://github.com/joshpsawyer/extarc.git#egg=extarc
```

### conda

Not in conda, yet - just install it from pip in your environment.

## Usage

```python
from pyhere import here
```

[1]: https://github.com/r-lib/here
[2]: https://github.com/chendaniely
[3]: https://github.com/chendaniely/pyprojroot
