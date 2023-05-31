# {{ cookiecutter.project_name }}

<div align="center">

[![PythonSupported](https://img.shields.io/badge/python-{{ cookiecutter.minimal_python_version }}-brightgreen.svg)](https://python3statement.org/#sections50-why)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![Bandit](https://img.shields.io/badge/security-bandit-informational.svg)](https://github.com/PyCQA/bandit)

{{ cookiecutter.project_description }}

</div>

- [Repository contents](#repository-contents)
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
- [.flake8](.flake8) - [flake8](https://github.com/pycqa/flake8) linter configuration
- [.gitignore](.gitignore) - the files/folders `git` should ignore
- [.pre-commit-config.yaml](.pre-commit-config.yaml) - [pre-commit](https://pre-commit.com/) configuration file
- [README.md](README.md) - the one you read =)
- [DEVELOPMENT.md](DEVELOPMENT.md) - guide for development team
- [Makefile](Makefile) - targets for `make` command
- [cookiecutter-config-file.yml](cookiecutter-config-file.yml) - cookiecutter project config log
- [poetry.toml](poetry.toml) - poetry local config
- [pyproject.toml](pyproject.toml) - Python project configuration

## System requirements

- Python version: {{ cookiecutter.minimal_python_version }}
- Operating system: Ubuntu 20.04
- Poetry version >= 1.2.0

> We tested on this setup - you can try other versions or operation systems by yourself!

## Other interesting info

Here you can write anything about your project!
