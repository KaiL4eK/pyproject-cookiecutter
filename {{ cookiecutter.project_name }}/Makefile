#* Variables
SHELL := /usr/bin/env bash
PYTHON := python

{% if cookiecutter.include_docker_sample == 'y' -%}#* Docker variables
IMAGE := {{ cookiecutter.project_slug }}
VERSION := latest{%- endif %}

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
	poetry install -n{% if cookiecutter.include_mypy_linter == 'y' -%}
	poetry run mypy --install-types --non-interactive ./{% endif %}

.PHONY: poetry-export
poetry-export:
	poetry lock -n && poetry export --without-hashes > requirements.txt

.PHONY: poetry-export-dev
poetry-export-dev:
	poetry lock -n && poetry export --dev --without-hashes > requirements.dev.txt

.PHONY: tools-install
tools-install:
	poetry run pre-commit install
	poetry run nbdime config-git --enable

{% if cookiecutter.include_tests_sample == 'y' -%}#* Tests
.PHONY: tests
tests:
	poetry run pytest -c pyproject.toml{%- endif %}

{% if cookiecutter.include_mypy_linter == 'y' -%}#* Linting
.PHONY: mypy
mypy:
	poetry run mypy --config-file pyproject.toml ./{%- endif %}

{% if cookiecutter.include_docker_sample == 'y' %}
#* Docker
# Example: make docker VERSION=latest
# Example: make docker IMAGE=some_name VERSION={{ cookiecutter.version }}
.PHONY: docker-build
docker-build:
	@echo Building docker $(IMAGE):$(VERSION) ...
	docker build \
		-t $(IMAGE):$(VERSION) . \
		-f ./docker/Dockerfile --no-cache

# Example: make clean_docker VERSION=latest
# Example: make clean_docker IMAGE=some_name VERSION={{ cookiecutter.version }}
.PHONY: docker-remove
docker-remove:
	@echo Removing docker $(IMAGE):$(VERSION) ...
	docker rmi -f $(IMAGE):$(VERSION)
{% endif %}

#* Cleaning
.PHONY: pycache-remove
pycache-remove:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf
	find . | grep -E "(.ipynb_checkpoints$$)" | xargs rm -rf

.PHONY: build-remove
build-remove:
	rm -rf build/

.PHONY: clean-all
clean-all: pycache-remove build-remove {% if cookiecutter.include_docker_sample == 'y' -%}docker-remove{% endif %}
