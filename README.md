# Python project template for cookiecutter #

<div align="center">

[![PythonSupported](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-brightgreen.svg)](https://python3statement.org/#sections50-why)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/KaiL4eK/pyproject-cookiecutter/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/KaiL4eK/pyproject-cookiecutter/blob/main/.pre-commit-config.yaml)
[![pydantic-settings](https://img.shields.io/badge/settings-pydantic-settings)](https://github.com/pydantic/pydantic-settings)
[![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://github.com/streamlit)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-306998?logo=python&logoColor=white)](https://github.com/sqlalchemy/sqlalchemy)
[![Postgres](https://img.shields.io/badge/Postgres-%23316192.svg?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Bandit](https://img.shields.io/badge/security-bandit-informational.svg)](https://github.com/KaiL4eK/pyproject-cookiecutter/blob/main/.pre-commit-config.yaml)
[![mypy](https://img.shields.io/badge/type%20checked-mypy-039dfc)](https://mypy-lang.org/)
[![ty](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)


</div>

## Features ##

* Python 3.9, 3.10, 3.11, 3.12 supported
* [Poetry](https://python-poetry.org/) for package/dependency management
  * Version `>= 1.8.0` supported
* Tests are based on [`pytest`](https://docs.pytest.org/en/stable/)
* Pre-commit hooks with [pre-commit](https://pre-commit.com/)
  * Linting using (one of)
    * [ruff linter](https://docs.astral.sh/ruff/linter/)
    * [wemake](https://wemake-python-styleguide.readthedocs.io/en/latest/pages/usage/configuration.html)
    * [flake8](https://flake8.pycqa.org/en/latest/)
  * Code style via (one of)
    * [ruff formatter](https://docs.astral.sh/ruff/formatter/)
    * [black](https://github.com/psf/black)
  * Type checking via (one of)
    * [mypy](https://mypy.readthedocs.io/en/stable/)
    * [ty](https://docs.astral.sh/ty/)
  * Notebooks cleaning via [nbstripout](https://github.com/kynan/nbstripout)
  * Security checks via [bandit](https://github.com/PyCQA/bandit)
  * Local hooks for issues number substitution into commit comment for
    * [GitHub](https://github.com/)
    * [Bitbucket (JIRA)](https://bitbucket.org/)
* [VSCode](https://code.visualstudio.com/) editor config with [EditorConfig](https://editorconfig.org/)
* [Numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) format for docstring
* Ready-to-go [Dockerfile](https://docs.docker.com/engine/reference/builder/) to build image with package
  * With multistage build
* Docker image analyzer - [dive](https://github.com/wagoodman/dive)
* Project samples generated in [sample-projects](sample-projects) directory

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
