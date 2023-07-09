#* Variables
SHELL := /usr/bin/env bash
PYTHON ?= python3

#* Installation
.PHONY: project-init
project-init: poetry-install tools-install

.PHONY: poetry-install
poetry-install:
	poetry install -n

.PHONY: poetry-main-install
poetry-main-install:
	poetry install --only main -n

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
	poetry run cookiecutter . -f --config-file test-configs/py39-poetry-docker-github.yaml --no-input -o ${COOKIECUTTER_TEST_DIR}
	ln -sf ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME} .
	bash scripts/test_project_poetry.sh ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME}

.PHONY: test-project-clean
test-project-clean:
	rm -rf ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME}
