# Development guide

This is guide how to prepare development environment and use main tools

## Table of contents

- [Prerequisites](#prerequisites)
- [Initialize your code](#initialize-your-code)
  - [Just created project?](#just-created-project)
  - [Cloned existing project](#cloned-existing-project)
- [Linting](#linting)
  - [Type check](#type-check)
- [Optional setup steps](#optional-setup-steps)
- [Other recommendations for the project](#other-recommendations-for-the-project)
- [Some known issues](#some-known-issues)

## Prerequisites

> If you need to install tools, check links

- [Python](docs/TOOLS.md#python)
- [uv](docs/TOOLS.md#uv)
- [Make](docs/TOOLS.md#make)

## Initialize your code

### Just created project?

0. Create repository on your favourite server (Bitbucket, Github or other) and obtain "Version control system URL" like this one:

```url
https://github.com/user/my-project.git
```

1. Create folder and initialize `git` inside your repo folder:

```bash
cd uv-project-ty-ruff-bitbucket-airflow && git init
```

2. Initialize virtual environment and install `pre-commit` hooks:

```bash
make project-init
```

3. Upload initial code to GitHub:

```bash
git add .
git commit -m ":tada: Initial commit"
git branch -M develop
git remote add origin <Version control system URL>
git push -u origin develop
```

[Table of contents](#table-of-contents)

### Cloned existing project

1. Initialize virtual environment and install `pre-commit` hooks:

```bash
make project-init
```

[Table of contents](#table-of-contents)

## Linting

### Type check

Run type checker on your project sources

```bash
make type-check
```

[Table of contents](#table-of-contents)

## Optional setup steps

1. Install VSCode Extensions
   - [EditorConfig for VS Code](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
      Open control panel (Ctrl+P) and enter `ext install EditorConfig.EditorConfig`



[Table of contents](#table-of-contents)

## Other recommendations for the project

- Versioning (tags)
- Automate various venv creations with [tox](https://pypi.org/project/tox/) for tests
- Make documentation for your code based on docstrings (sphinx, mkdocs)
- Organize package build + publication
- For better data control create data split and fix lists of splitted files in CSV/Excel files
- Use Git Flow [ref1](https://danielkummer.github.io/git-flow-cheatsheet/index.ru_RU.html), [ref2](https://www.gitkraken.com/learn/git/git-flow)
- Even if you`ve prepared data manually (remove lines, update values) - spend time to automated even smallest steps to make it repetative from source data
- If you want to keep credentials away (e.g. remote server) but cache them use `git config credential.helper 'cache --timeout=3600'`
- Use [pipx](https://github.com/pypa/pipx) or [uvx](https://docs.astral.sh/uv/guides/tools/) for global tools
- If you are going to use project with pip-only environment, call `pip install -e .` to setup your sources in venv

## Some known issues

- If you have issues with python version like:

    ```bash
    The currently activated Python version 3.9.7 is not supported by the project (~3.11.0)
    ...
    NoCompatiblePythonVersionFound
    ...
    ```

    Check version of your `python3` binary and make sure you have python3.11 installed.

[Table of contents](#table-of-contents)
