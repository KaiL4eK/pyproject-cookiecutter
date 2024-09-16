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
	poetry run pre-commit install
	poetry run nbdime config-git --enable

#* Linting
.PHONY: lint
lint:
	poetry run pre-commit run -a

#* Create test project and test data
COOKIECUTTER_TEST_DIR = /tmp/cookiecutter
TEST_PROJECT_NAME = test-project
TEST_PROJECT_CONFIG = py310-poetry-docker-github-ruff.yaml
# TEST_PROJECT_CONFIG = py310-poetry-docker-github.yaml
# TEST_PROJECT_CONFIG = py310-poetry-mypy-docker-github.yaml
.PHONY: test-project-creation
test-project-creation:
	poetry run cookiecutter . -f --config-file test-configs/${TEST_PROJECT_CONFIG} --no-input -o ${COOKIECUTTER_TEST_DIR}
	ln -sf ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME} .

.PHONY: test-project
test-project: test-project-creation
	bash scripts/test_project_poetry.sh ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME}

.PHONY: test-project-clean
test-project-clean:
	rm -rf ${TEST_PROJECT_NAME}
	rm -rf ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME}
