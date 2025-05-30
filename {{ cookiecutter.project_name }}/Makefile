#* Variables
SHELL := /usr/bin/env bash
PYTHON ?= python3

{% if cookiecutter.include_docker_sample == 'y' -%}#* Docker variables
IMAGE := {{ cookiecutter.project_slug }}
VERSION := latest

#* Docker
# Example: make docker-build VERSION=latest
# Example: make docker-build IMAGE=some_name VERSION={{ cookiecutter.version }}
.PHONY: docker-build
docker-build:
	@echo Building docker $(IMAGE):$(VERSION) ...
	docker build \
		-t $(IMAGE):$(VERSION) . \
		-f ./docker/Dockerfile --no-cache

.PHONY: docker-build-cached
docker-build-cached:
	@echo Building docker $(IMAGE):$(VERSION) ...
	docker build \
		-t $(IMAGE):$(VERSION) . \
		-f ./docker/Dockerfile

.PHONY: docker-dive-analyze
docker-dive-analyze:
	@echo Analyze docker image with dive $(IMAGE):$(VERSION) ...
	docker run -ti --rm  \
		-v /var/run/docker.sock:/var/run/docker.sock \
		-e CI=true \
		wagoodman/dive:0.13.0 \
		$(IMAGE):$(VERSION)

# Example: make docker-remove VERSION=latest
# Example: make docker-remove IMAGE=some_name VERSION={{ cookiecutter.version }}
.PHONY: docker-remove
docker-remove:
	@echo Removing docker $(IMAGE):$(VERSION) ...
	docker rmi -f $(IMAGE):$(VERSION)
{%- endif %}

#* Initialization
.PHONY: project-init
project-init: poetry-install tools-install{% if cookiecutter.include_mypy_type_checker == 'y' %} mypy-install{%- endif %}

.PHONY: poetry-install
poetry-install:
	poetry install -n

.PHONY: poetry-lock-update
poetry-lock-update:
	poetry lock --no-update

.PHONY: poetry-export
poetry-export:
	poetry lock -n && poetry export --without-hashes > requirements.txt

.PHONY: poetry-export-dev
poetry-export-dev:
	poetry lock -n && poetry export --with dev --without-hashes > requirements.dev.txt

#* Tools
.PHONY: tools-install
tools-install:
	poetry run pre-commit install --hook-type prepare-commit-msg --hook-type pre-commit
{% if cookiecutter.include_notebooks_sample == 'y' -%}#* Notebooks
	poetry run nbdime config-git --enable{%- endif %}

.PHONY: pre-commit-update
pre-commit-update:
	poetry run pre-commit autoupdate

.PHONY: pre-commit-run-all
pre-commit-run-all:
	poetry run pre-commit run --all-files

{% if cookiecutter.include_notebooks_sample == 'y' -%}#* Notebooks
.PHONY: nbextention-toc-install
nbextention-toc-install:
	poetry run jupyter contrib nbextension install --user
	poetry run jupyter nbextension enable toc2/main{%- endif %}

{% if cookiecutter.include_tests_sample == 'y' -%}#* Tests
.PHONY: tests
tests:
	poetry run pytest -c pyproject.toml{%- endif %}

{% if cookiecutter.include_mypy_type_checker == 'y' -%}#* Linting
.PHONY: mypy-install
mypy-install:
	poetry run mypy --install-types --non-interactive ./

.PHONY: mypy
mypy:
	poetry run mypy --config-file pyproject.toml ./{%- endif %}

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

#* Service targets
.PHONY: grep-todos
grep-todos:
	git grep -EIn "TODO|FIXME|XXX"
