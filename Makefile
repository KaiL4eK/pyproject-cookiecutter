#* Variables
SHELL := /usr/bin/env bash
PYTHON ?= python3
COOKIECUTTER_VERSION ?= 2.2.0

#* Installation
.PHONY: project-init
project-init: poetry-install tools-install

project-init-ci:
	pip install cookiecutter~=${COOKIECUTTER_VERSION}

.PHONY: poetry-install
poetry-install:
	poetry install -n

.PHONY: poetry-main-install
poetry-main-install:
	poetry install --only main -n

.PHONY: poetry-lock-update
poetry-lock-update:
	poetry lock --no-update

.PHONY: pre-commit-update
pre-commit-update:
	poetry run pre-commit autoupdate

.PHONY: tools-install
tools-install:
	poetry run pre-commit install --hook-type prepare-commit-msg --hook-type pre-commit
	poetry run nbdime config-git --enable

#* Linting
.PHONY: lint
lint:
	poetry run pre-commit run -a

#* Create test project and test data
COOKIECUTTER_TEST_DIR = /tmp/cookiecutter
TEST_PROJECT_NAME = test-project
TEST_PROJECT_CONFIG_POETRY = py312-poetry-docker-github.yaml
TEST_PROJECT_CONFIG_UV = py312-uv-github.yaml

.PHONY: test-project-creation-poetry
test-project-creation-poetry:
	poetry run cookiecutter . -f --config-file test-configs/${TEST_PROJECT_CONFIG_POETRY} --no-input -o ${COOKIECUTTER_TEST_DIR}
	ln -sf ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME} .

.PHONY: test-project-poetry
test-project-poetry: test-project-creation-poetry
	bash scripts/test_project_poetry.sh ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME}

.PHONY: test-project-creation-uv
test-project-creation-uv:
	poetry run cookiecutter . -f --config-file test-configs/${TEST_PROJECT_CONFIG_UV} --no-input -o ${COOKIECUTTER_TEST_DIR}
	ln -sf ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME} .

.PHONY: test-project-uv
test-project-uv: test-project-creation-uv
	bash scripts/test_project_uv.sh ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME}

.PHONY: test-project-clean
test-project-clean:
	rm -rf ${TEST_PROJECT_NAME}
	rm -rf ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME}

#* Tools
.PHONY: generate-samples
generate-samples:
	poetry run bash scripts/generate_sample_projects.sh
