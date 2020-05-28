<p align="center">
    <img src="https://github.com/douglasfarinelli/decker/blob/main/decker.png" alt="decker"/>
</p>

<p align="center">
    Simple development tool that simplifies a pythonist's daily tasks.
</p>

<p align="center">
    <a href="https://pypi.org/project/decker/#history" target="_blank">
        <img src="https://img.shields.io/pypi/status/decker?style=flat" alt="PyPi Status">
    </a>
    <a href="https://travis-ci.com/douglasfarinelli/decker" target="_blank">
        <img src="https://travis-ci.com/douglasfarinelli/decker.svg" alt="Build Status">
    </a>
    <a href="https://pypi.org/project/decker/" target="_blank">
        <img src="https://badge.fury.io/py/decker.svg" alt="Package version">
    </a>
    <a href="https://pypi.org/project/decker/" target="_blank">
        <img src="https://img.shields.io/pypi/wheel/decker?style=flat" alt="PyPI - Wheel">
    </a>
</p>

---

_Decker_ is a command line, which aims to optimize some tasks, such as configuration and execution of the tools most used by the community.
In addition, it aims to reduce configuration files and centralize everything on pyproject.toml.

---

- [Features](#features)
- [Installation](#installation)
- [Global Settings](#global-settings)
- [Extra](#extra)
- [Next features](#next-features)
- [License](#license)

--- 

## Installation

The installation of decker can be via `pip`,` pipenv`, `poetry` or any other tool you prefer:

```bash
pipenv install decker
```

> Note: We recommend installing only on virtualenv.

## Features

```
Welcome to Decker!

  Simple development tool that simplifies a pythonist's daily tasks.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  format  Run code style format.
```

### Format your code

```
  Run code style format.

Options:
  --exclude TEXT                  Files and directories that should be
                                  excluded on recursive searches.

  -l, --line-length INTEGER       How many characters per line to allow.
                                  [default: 79]

  -b, --backend [autoflake|docformatter|black|unify|isort]
                                  Specify formatting backends.
  --help                          Show this message and exit.
```

Formatting uses several tools, such as: 

- [autoflake](https://github.com/myint/autoflake) to remove unusable variables and imports,
- [docformatter](https://github.com/myint/docformatter) to format docstrings,
- [black](https://github.com/psf/black) to apply your coding style, format blocks, constants, among other things,
- [unify](https://github.com/myint/unify) to normalize quotes,
- And last but not least, [isort](https://github.com/timothycrosley/isort) to reorganize your imports.

To save and avoid many configurations, decker pre defines some things like:

Tool | Option | Pré defined  | Description
---- | ------ | ------------ | -----------
autoflake | expand-star-imports | True | Expand wildcard star imports with undefined names
autoflake | in-place | True | Apply changes
autoflake | recursive | True | Recursive to defined sources
autoflake | remove-all-unused-imports | True | Remove all unused imports (not just those from the standard library)
autoflake | remove-unused-variables | True | 
docformatter | blank | False | Remove blank line after description
docformatter | in-place | True | Apply changes
docformatter | make-summary-multi-line | True | Add a newline before and after the summary of a one-line docstring
docformatter | pre-summary-newline | True | Add a newline before the summary of a multi-line docstring
docformatter | recursive | True | Recursive to defined sources
docformatter | wrap-summaries | 79 (from decker global line-length setting) | Wrap long summary lines
black | line-length | 79 (from decker global line-length setting) | How many characters per line to allow
black | skip-string-normalization | False | Skip string normalization to use unify to normalize
unify | in-place | True | Apply changes
unify | quote | "'" (Single quote) | 
unify | recursive | True | Recursive to defined sources
isort | apply | True | Apply changes
isort | atomic | True | Ensures the output doesn't save if the resulting file contains syntax errors
isort | case-sensitive | True | Tells isort to include casing when sorting module names
isort | combine-as | True | Combines as imports on the same line
isort | dont-skip | [`__init__`] | Files that sort imports should never skip over
isort | line-length | 79 (from decker global line-length setting) | How many characters per line to allow
isort | lines-after-imports | 2 | 
isort | multi-line | 3 | Multi line output (0-grid, 1-vertical, 2-hanging, 3-vert-hanging, 4-vert-grid, 5-vert-grid-grouped, 6-vert-grid-grouped-no-comma).
isort | order-by-type | True | Order imports by type in addition to alphabetically
isort | recursive | True | Recursive to defined sources
isort | remove-import | [`__future__`] | Removes the specified import from all files
isort | skip-glob | `*venv*` | Files that sort imports should skip over
isort | trailing-comma | True | Includes a trailing comma on multi line imports that include parentheses
isort | use-parentheses | True | Use parenthesis for line continuation on length limit instead of slashes


> Note: Despite pre-defining all these settings, nothing is MANDATORY. All of these and any other configuration of these tools can be adjusted in pyproject.toml or in each configuration file of these tools.

> The intention was to save time for those who already know and help those who do not already know.


## Global Settings

To ensure ease and centralization of the other configurations, decker searches almost all of them in the pyproject.toml file, if any. Example:

```
[tool.autoflake]
expand-star-imports=false

[tool.black]
line-length=120
...

[tool.docformatter]
blank=false
...

[tool.unify]
quote='"'
...

[tool.isort]
line-length=120
trailing-comma=false
...
```

### Decker settings on pyproject.toml

In addition, there are some that are global, where they are automatically passed on to all tools, such as:

```
[tool.decker]
line-length=79
exclude=same-package
verbose=1
sources=src/
```

### Default sources (src/)

And to help as well, if the sources were not defined by the command line or pyproject.toml, decker looks for `.py` files in the directory in question and also for the `src` folder.

## Extra

### pdb++ & ipython

When installing decker, [pdb++](https://github.com/pdbpp/pdbpp) and [ipython](https://github.com/ipython/ipython) are also installed to aid development.

### Better print to pyproject.toml errors 

Wraps and shows toml errors in a more "human" way, for example:

```
 + Unable to load pyproject.toml:
 |   
 |   [project]
 |   author='Douglas Farinelli'
 |   name='decker'
 |   repository='https://gitlab.com/douglasfarinelli/decker/'
 |   
 |   [tool.black]
 |   line-length=79
 |   skip-string-normalization=true
 |   target-version=
 |   
 + ^ Empty value is invalid
 |   
 |   ['py38']
 |   
 |   [tool.isort]
 |   atomic=true
 |   
 |   [tool.towncrier]
 |   package = 'crm'
 |   package_dir = 'src'
 |   filename = 'CHANGELOG.md'
 |   directory = 'changelog.d'
```

## Next features

- [0.2.0] - Command `decker check`

A command to analyze various things in your code, such as type hints, pep8 and Code quality.

- [0.3.0] - Command `decker release`

Why not automate the flow VCS + [bumpversion](https://github.com/peritus/bumpversion) + [towncrier](https://github.com/twisted/towncrier)? In other words, automate the generation of tags, changelog and auto-commit them.

Example:

```
decker release minor
```

---

## License

This project is licensed under the terms of the MIT license.
