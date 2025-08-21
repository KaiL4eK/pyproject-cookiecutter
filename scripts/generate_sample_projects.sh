#!/usr/bin/env bash

set -e

mkdir -p sample-projects

poetry run cookiecutter . -f \
    --config-file test-configs/py312-poetry-docker-github.yaml \
    --no-input \
    -o sample-projects \
    project_name=poetry-project-mypy-wemake-black \
    python_type_checker=mypy \
    python_linter=wemake \
    python_formatter=black

poetry run cookiecutter . -f \
    --config-file test-configs/py312-poetry-docker-github.yaml \
    --no-input \
    -o sample-projects \
    project_name=poetry-project-ty-ruff \
    python_type_checker=ty \
    python_linter=ruff \
    python_formatter=ruff

poetry run cookiecutter . -f \
    --config-file test-configs/py312-uv-github.yaml \
    --no-input \
    -o sample-projects \
    project_name=uv-project-ty-ruff-github \
    package_manager=uv \
    python_type_checker=ty \
    python_linter=ruff \
    python_formatter=ruff
