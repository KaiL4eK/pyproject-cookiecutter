# Development guide

This is guide how to prepare development environment and use main tools

## Table of contents

- [Table of contents](#table-of-contents)
- [Prerequisites](#prerequisites)
- [Initialize your code](#initialize-your-code)
  - [Just created project?](#just-created-project)
  - [Cloned existing project](#cloned-existing-project)
- [Optional setup steps](#optional-setup-steps)
- [Other recommendations for the project](#other-recommendations-for-the-project)
- [Some known issues](#some-known-issues)

## Prerequisites

> If you need to install tools, check links

- [Python](docs/TOOLS.md#python)
- [Poetry](docs/TOOLS.md#poetry)
- [Make](docs/TOOLS.md#make)

## Initialize your code

### Just created project?

0. Create repository on your favourite server (Bitbucket, Github or other) and obtain "Version control system URL" like this one:

```url
https://github.com/user/my-project.git
```

1. Create folder and initialize `git` inside your repo folder:

```bash
cd {{ cookiecutter.project_name }} && git init
```

2. Initialize poetry and install `pre-commit` hooks:

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

1. Initialize poetry and install `pre-commit` hooks:

```bash
make project-init
```

[Table of contents](#table-of-contents)

## Optional setup steps

1. Install VSCode Extensions
   - [EditorConfig for VS Code](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
      Open control panel (Ctrl+P) and enter `ext install EditorConfig.EditorConfig`

{% if cookiecutter.include_notebooks_sample == 'y' -%}

1. To initialize generation of Table of Contents from notebook headers we use `nbextension`:

    - `nbextention-toc-install`

    > It is required version nbconvert~=5.6.1 (checked for date 2021-12-29)

    - To export notebook with ToC use next command:

      ```bash
      poetry run jupyter nbconvert --template toc2 --to html_toc --output-dir ./exports <путь до файла>
      ```

      > For example, `poetry run jupyter nbconvert --template toc2 --to html_toc --output-dir ./exports notebooks/example.ipynb`

      To use embedded images into HTML use option `html_embed`:

      ```bash
      poetry run jupyter nbconvert --template toc2 --to html_embed --output-dir ./exports <путь до файла>
      ```
{%- endif %}

[Table of contents](#table-of-contents)

## Other recommendations for the project

- Versioning (tags) + changelog
- Automate various venv creations with [tox](https://pypi.org/project/tox/)
- Make documentation for your code based on docstrings (sphinx, mkdocs)
- Organize package build + publication
- For better data control create data split and fix lists of splitted files in CSV/Excel files
- Use Git Flow [ref1](https://danielkummer.github.io/git-flow-cheatsheet/index.ru_RU.html), [ref2](https://www.gitkraken.com/learn/git/git-flow)
- Even if you`ve prepared data manually (remove lines, update values) - spend time to automated even smallest steps to make it repetative from source data
- If you want to keep credentials away (e.g. remote server) but cache them use `git config credential.helper 'cache --timeout=3600'`
- Use [pipx](https://github.com/pypa/pipx) for global tools

## Some known issues

- If you have issues with python version like:

    ```bash
    The currently activated Python version 3.9.7 is not supported by the project (~{{ cookiecutter.minimal_python_version }}.0)
    ...
    NoCompatiblePythonVersionFound
    ...
    ```

    Check version of your `python3` binary and make sure you have python{{ cookiecutter.minimal_python_version }} installed.

[Table of contents](#table-of-contents)
