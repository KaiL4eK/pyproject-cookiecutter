# Project README! Here we go!
{% if cookiecutter.vcs_remote_type != 'bitbucket' %}
<div align="center">
{%- endif %}

[![PythonSupported](https://img.shields.io/badge/python-{{ cookiecutter.minimal_python_version }}-brightgreen.svg)](https://python3statement.org/#sections50-why)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
{% if cookiecutter.python_formatter == 'ruff' or cookiecutter.python_linter == 'ruff' -%}
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
{% endif -%}
{% if cookiecutter.python_linter == 'wemake' -%}
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
{% endif -%}
{% if cookiecutter.python_formatter == 'black' -%}
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
{% endif -%}
{% if cookiecutter.python_type_checker == 'ty' -%}
[![ty](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
{% endif -%}
{% if cookiecutter.python_type_checker == 'mypy' -%}
[![mypy](https://img.shields.io/badge/type%20checked-mypy-039dfc)](https://mypy-lang.org/)
{% endif %}
{{ cookiecutter.project_description }}

{%- if cookiecutter.vcs_remote_type != 'bitbucket' %}
</div>
{%- endif %}

- [Repository contents](#repository-contents)
- [Additional directories to be considered](#additional-directories-to-be-considered)
- [System requirements](#system-requirements)
- [Other interesting info](#other-interesting-info)

## Repository contents

- [docs](docs) - documentation of the project
- [reports](reports) - reports generated (as generated from notebooks)
  > Check if you need to ignore large reports or keep them in Git LFS
- [configs](configs) - configuration files directory
{% if cookiecutter.include_docker_sample == 'y' -%}- [Docker](Docker) - definition of "How to build image for Docker"
- [.dockerignore](.dockerignore) - the files/folders `docker` should ignore{%- endif %}
{% if cookiecutter.include_notebooks_sample == 'y' -%}- [notebooks](notebooks) - directory for `jupyter` notebooks{%- endif %}
{% if cookiecutter.include_tests_sample == 'y' -%}- [tests](tests) - project tasts based on [pytest](https://docs.pytest.org/en/stable/){%- endif %}
- [scripts](scripts) - repository service scripts
  > These ones are not included into the pakckage if you build one - these scripts are only for usage with repository
- [{{ cookiecutter.project_slug }}]({{ cookiecutter.project_slug }}) - source files of the project
- [.editorconfig](.editorconfig) - configuration for [editorconfig](https://editorconfig.org/)
{% if cookiecutter.python_formatter != 'ruff' %}- [.flake8](.flake8) - [flake8](https://github.com/pycqa/flake8) linter configuration{% endif %}
- [.gitignore](.gitignore) - the files/folders `git` should ignore
- [.pre-commit-config.yaml](.pre-commit-config.yaml) - [pre-commit](https://pre-commit.com/) configuration file
- [README.md](README.md) - the one you read =)
- [DEVELOPMENT.md](DEVELOPMENT.md) - guide for development team
- [Makefile](Makefile) - targets for `make` command
- [cookiecutter-config-file.yml](cookiecutter-config-file.yml) - cookiecutter project config log
- [poetry.toml](poetry.toml) - poetry local config
- [pyproject.toml](pyproject.toml) - Python project configuration
- [requirements.project.txt](requirements.project.txt) - Python project requirements (e.g. poetry and may be other packages to be installed before installing core packages)

## Additional directories to be considered

- [data](data) - various data representations (raw/source, preprocessed)
  - for small files (less than e.g. 5 Mb for all files) you can put them directly to repo
  - for medium files (less than e.g. 1 Gb for all files) you can use [Git LFS](https://git-lfs.com/)
  - for large files better use FTP, Samba, NFS or other cloud/hosted persistent storage and describe here all required access and structure
  - for data versioning better use [DVC](https://dvc.org/), [ClearML Data](https://clear.ml/docs/latest/docs/clearml_data/) or other data versioning tool
- [models](models) - serialized models
  - same rules as for `data` directory

## System requirements

- Python version: {{ cookiecutter.minimal_python_version }}
- Operating system: Ubuntu or WSL
- Poetry version >= 1.8.0

> We tested on this setup - you can try other versions or operation systems by yourself!

## Other interesting info

Here you can write anything about your project!
