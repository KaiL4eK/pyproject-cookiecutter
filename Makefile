#* Variables
SHELL := /usr/bin/env bash
PYTHON ?= python3
POETRY_VERSION ?= 1.2.0

#* Poetry
.PHONY: poetry-download
poetry-download:
	curl -sSL https://install.python-poetry.org | $(PYTHON) - --version ${POETRY_VERSION}

.PHONY: poetry-remove
poetry-remove:
	curl -sSL https://install.python-poetry.org | $(PYTHON) - --uninstall

#* Installation
.PHONY: project-init
project-init: poetry-install tools-install

.PHONY: poetry-install
poetry-install:
	poetry install -n

.PHONY: poetry-lock-update
poetry-lock-update:
	poetry lock --no-update

.PHONY: tools-install
tools-install:
	poetry run pre-commit install
	poetry run nbdime config-git --enable

COOKIECUTTER_TEST_DIR = /tmp/cookiecutter
TEST_PROJECT_NAME = test-project

#* Linting
.PHONY: lint
lint:
	poetry run pre-commit run -a

#* Create test project and test data
.PHONY: test-project-creation
test-project-creation:
	poetry run cookiecutter . -f --config-file test-configs/poetry-docker-github.yaml --no-input -o ${COOKIECUTTER_TEST_DIR}
	ln -sf ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME} .
	bash scripts/test_project_poetry.sh ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME}

.PHONY: test-project-clean
test-project-clean:
	rm -rf ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME}
