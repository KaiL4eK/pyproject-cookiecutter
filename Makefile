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

#* Create test project and test data
.PHONY: test-project-creation
test-project-creation:
	poetry run cookiecutter . -f --config-file test-config.yaml --no-input
	make -C test-project install
	cd test-project; poetry run jupyter nbconvert --inplace --to notebook --execute notebooks/example.ipynb
	cd test-project; poetry run pytest
	cd test-project; poetry run pre-commit run --all-files
