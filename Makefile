#* Variables
SHELL := /usr/bin/env bash
PYTHON := python

#* Poetry
.PHONY: poetry-download
poetry-download:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | $(PYTHON) -

.PHONY: poetry-remove
poetry-remove:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | $(PYTHON) - --uninstall

#* Installation
.PHONY: install
install: poetry-install tools-install

.PHONY: poetry-install
poetry-install:
	poetry install -n

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
	poetry run cookiecutter . -f --config-file test-config.yaml --no-input -o ${COOKIECUTTER_TEST_DIR}
	ln -sf ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME} .
	cd ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME}; git init && git add -A
	make -C ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME} install
	cd ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME}; poetry run jupyter nbconvert --inplace --to notebook --execute notebooks/example.ipynb
	cd ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME}; poetry run pytest
	cd ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME}; poetry run python scripts/config_sample.py --config configs/config_sample.yml
	cd ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME}; poetry run pre-commit run --files notebooks/* nbstripout || true
	cd ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME}; poetry run pre-commit run -a --show-diff-on-failure
	cd ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME}; poetry build
	cd ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME}; make docker-build
	cd ${COOKIECUTTER_TEST_DIR}/${TEST_PROJECT_NAME}; make docker-remove
