# Python project template for cookiecutter #

<div align="center">

[![PythonSupported](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-brightgreen.svg)](https://python3statement.org/#sections50-why)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/KaiL4eK/pyproject-cookiecutter/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/KaiL4eK/pyproject-cookiecutter/blob/main/.pre-commit-config.yaml)
[![Bandit](https://img.shields.io/badge/security-bandit-informational.svg)](https://github.com/KaiL4eK/pyproject-cookiecutter/blob/main/.pre-commit-config.yaml)

</div>

## Features ##

* Python 3.9, 3.10, 3.11, 3.12 supported
* [Poetry](https://python-poetry.org/) for package/dependency management
  * Version `>= 1.8.0` supported
* Tests are based on [`pytest`](https://docs.pytest.org/en/stable/)
* Pre-commit hooks with [pre-commit](https://pre-commit.com/)
  * Linting using [flake8](https://flake8.pycqa.org/en/latest/)
  * Code style via [black](https://github.com/psf/black)
  * Notebooks cleaning via [nbstripout](https://github.com/kynan/nbstripout)
  * Security checks via [bandit](https://github.com/PyCQA/bandit)
  * Local hooks for issues number substitution into commit comment for [GitHub](https://github.com/) and [Bitbucket (JIRA)](https://bitbucket.org/)
* [VSCode](https://code.visualstudio.com/) editor config with [EditorConfig](https://editorconfig.org/)
* [Numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) format for docstring
* Ready-to-go [Dockerfile](https://docs.docker.com/engine/reference/builder/) to build image with package
  * With multistage build
* Docker image analyzer - [dive](https://github.com/wagoodman/dive)

## How to start ##

* Install [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)
* Create project from template

```bash
cookiecutter gh:KaiL4eK/pyproject-cookiecutter
```

* Answer some questions and get ready to code!

## Notes ##

### Cookiecutter is not working properly (errors during project creation) ###

Check that you've installed version for `python3`. You can call `python3 -m cookiecutter gh:KaiL4eK/pyproject-cookiecutter` to ensure that it is called with required python version.

### [Windows] warning: LF will be replaced by CRLF in ...

Check [this answer](https://stackoverflow.com/a/5834094). In short, setup `git config core.autocrlf false` to disable line-ending check. Or you can setup as you wish.

## How to improve project MORE ##

### [Linux] Use [safety](https://github.com/pyupio/safety) as pre-commit hook to check for security

```yaml
  - repo: https://github.com/Lucas-C/pre-commit-hooks-safety
    rev: v1.3.0
    hooks:
      - id: python-safety-dependencies-check
```

> This hook sometimes breaks on Windows, be careful!

### Use [bandit](https://bandit.readthedocs.io/en/latest/) as pre-commit hook to check for security

```yaml
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.0
    hooks:
      - id: bandit
        exclude: ^tests/
        args:
          - -s
          - B311
```

### Use [black](https://github.com/psf/black) or other formatter as pre-commit hook or just setup in your IDE/Development Environment

```yaml
  - repo: local
      # Requires to be installed in venv
      - id: black
        name: black
        entry: poetry run black --config pyproject.toml
        types: [python]
        language: system
```

```toml
# For pyptoject.toml

[tool.black]
# https://github.com/psf/black
target-version = ["py39"]
line-length = 100
color = true

exclude = '''
/(
    \.git
    | \.hg
    | \.mypy_cache
    | \.tox
    | \.venv
    | _build
    | buck-out
    | build
    | dist
    | env
    | venv
)/
'''
```

### Use other ways to update code via formatters just if you know what they do

```yaml
  - repo: https://github.com/asottile/pyupgrade
    rev: v2.31.0
    hooks:
      - id: pyupgrade
        args:
          - --py3-plus

  - repo: https://github.com/humitos/mirrors-autoflake
    rev: v1.3
    hooks:
      - id: autoflake
        args:
          [
            "--in-place",
            "--remove-all-unused-imports",
            "--remove-unused-variable",
            "--remove-duplicate-keys",
          ]
```

## Thanks to ##

* <https://awesomeopensource.com/project/TezRomacH/python-package-template>
