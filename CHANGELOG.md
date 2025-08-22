# Change Log

## [Unreleased]

### Added

- CHANGELOG.md to template and base project
- New package manager - `uv`! [#54]
- New python version - `3.12` [#48]
- Added `ty` type checker [#51]
- Samples of packages to see results of generation

### Changed

- `pytest` is now always presented in template, no choice
- Increased default line length `88` -> `100`

### Removed

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
