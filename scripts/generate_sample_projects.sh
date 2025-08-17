#!/usr/bin/env bash

mkdir -p sample-projects

PROJECT_NAME=poetry-project

poetry run cookiecutter . -f \
    --config-file test-configs/py312-poetry-docker-github.yaml \
    --no-input \
    -o sample-projects \
    project_name=$PROJECT_NAME
