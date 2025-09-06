# Project README! Here we go!

<div align="center">

[![PythonSupported](https://img.shields.io/badge/python-3.12-brightgreen.svg)](https://python3statement.org/#sections50-why)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![pydantic-settings](https://img.shields.io/badge/settings-pydantic-settings)](https://github.com/pydantic/pydantic-settings)
[![poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![mypy](https://img.shields.io/badge/type%20checked-mypy-039dfc)](https://mypy-lang.org/)

Awesome `poetry-project-mypy-wemake-black` project!
</div>

- [Repository contents](#repository-contents)
- [Additional directories to be considered](#additional-directories-to-be-considered)
- [System requirements](#system-requirements)
- [Other interesting info](#other-interesting-info)

## Repository contents

- [README.md](README.md) - the one you read =)
- [DEVELOPMENT.md](DEVELOPMENT.md) - guide for development team
- [CHANGELOG.md](CHANGELOG.md) - simple changelog, don't forget to keep it updated! Base format is [here](https://keepachangelog.com/en/1.0.0/)
- [docs](docs) - documentation of the project
- [reports](reports) - reports generated (as generated from notebooks)
  > Check if you need to ignore large reports or keep them in Git LFS
- [configs](configs) - configuration files directory
- [Docker](Docker) - definition of "How to build image for Docker"
- [.dockerignore](.dockerignore) - the files/folders `docker` should ignore
- [notebooks](notebooks) - directory for `jupyter` notebooks
- [tests](tests) - project tasts based on [pytest](https://docs.pytest.org/en/stable/)
- [scripts](scripts) - repository service scripts
  > These ones are not included into the pakckage if you build one - these scripts are only for usage with repository
- [poetry_project_mypy_wemake_black](poetry_project_mypy_wemake_black) - source files of the project
- [.editorconfig](.editorconfig) - configuration for [editorconfig](https://editorconfig.org/)
- [.gitignore](.gitignore) - the files/folders `git` should ignore
- [.pre-commit-config.yaml](.pre-commit-config.yaml) - [pre-commit](https://pre-commit.com/) configuration file
- [Makefile](Makefile) - targets for `make` command
- [cookiecutter-config-file.yml](cookiecutter-config-file.yml) - cookiecutter project config log
- [poetry.toml](poetry.toml) - poetry local config
- [pyproject.toml](pyproject.toml) - Python project configuration
- [requirements.project.txt](requirements.project.txt) - Python project requirements (e.g. poetry/uv and may be other packages to be installed before installing core packages)
  > Mainly used in docker and for documentation
## Additional directories to be considered

- [data](data) - various data representations (raw/source, preprocessed)
  - for small files (less than e.g. 5 Mb for all files) you can put them directly to repo
  - for medium files (less than e.g. 1 Gb for all files) you can use [Git LFS](https://git-lfs.com/)
  - for large files better use FTP, Samba, NFS or other cloud/hosted persistent storage and describe here all required access and structure
  - for data versioning better use [DVC](https://dvc.org/), [ClearML Data](https://clear.ml/docs/latest/docs/clearml_data/) or other data versioning tool
- [models](models) - serialized models
  - same rules as for `data` directory

## System requirements

- Python version: 3.12
- Operating system: Ubuntu or WSL

> We tested on this setup - you can try other versions or operation systems by yourself!

## Other interesting info

Here you can write anything about your project!
