# Change Log

## [Unreleased]

### Added

- Added `.env.example` as default file to keep samples of required ENVs
- Added `sqlalchemy` Data Access Object pattern
- Added `streamlit` application sample with Database migrations using `alembic`, check [this sample project](https://github.com/KaiL4eK/pyproject-cookiecutter/tree/main/sample-projects/uv-project-ty-ruff-bitbucket-streamlit)
- Added `pydantic-settings` to be used as main ENVs parser
    - `python-dotenv` better used for notebooks and other development scripts
- CHANGELOG.md to template and base project
- New package manager - `uv`! [#54](https://github.com/KaiL4eK/pyproject-cookiecutter/issues/54)
    - And [instruction how to transfer from `poetry`](https://github.com/KaiL4eK/pyproject-cookiecutter/wiki/Transfer-Poetry-2-uv)
- New python version - `3.12` [#48](https://github.com/KaiL4eK/pyproject-cookiecutter/issues/48)
- Added `ty` type checker [#51](https://github.com/KaiL4eK/pyproject-cookiecutter/issues/51)
- Samples of packages to see results of generation
- Added `airflow` to be used in your project, check [this sample project](https://github.com/KaiL4eK/pyproject-cookiecutter/tree/main/sample-projects/uv-project-ty-ruff-bitbucket-airflow)

### Changed

- Moved `python-dotenv` to development dependencies as `load_dotenv()` has to be used only for development
    - Production deployemnt has to provide ENVs to app so no usage of `.env` in production
- `pytest` is now always presented in template, no choice
- Increased default line length `88` -> `120`

### Removed

- `.PHONY` instructions from Makefile as not required for generic python project
- Python `<3.9` support
- Poetry `<1.8` support

## [1.0.0]

### Added

- Poetry package manager
- Pytest samples
    - conftest
    - fixtures
    - parametrization
- `.env` sample and `python-dotenv` framework
- Black formatter
- Ruff formatter/linter
- Wemake/flake8 linters
- Docker sample with multistage to download and build wheels (1st stage) and install them to clean images (2nd stage)
- Tests for different build configurations
- Scripts to automatically set task number from branch name
- Pre-commit configuration
- Notebook sample
- YAML config sample (with loggin setup) and processing script
