{%- if cookiecutter.package_manager == "poetry" -%}
  {%- set pm_cmd = "poetry" -%}
{%- elif cookiecutter.package_manager == "uv" -%}
  {%- set pm_cmd = "uv" -%}
{%- endif -%}

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
project-init: install-packages tools-install

.PHONY: install-packages
install-packages:
{%- if cookiecutter.package_manager == "poetry" %}
	poetry install -n
{%- elif cookiecutter.package_manager == "uv" %}
	uv sync
{%- endif %}

.PHONY: lock-update
lock-update:
{%- if cookiecutter.package_manager == "poetry" %}
	poetry lock --no-update
{%- elif cookiecutter.package_manager == "uv" %}
	uv lock
{%- endif %}

.PHONY: requirements-export
requirements-export: lock-update
{%- if cookiecutter.package_manager == "poetry" %}
	poetry export --without-hashes > requirements.txt
{%- elif cookiecutter.package_manager == "uv" %}
	uv export --no-hashes --no-cache --no-dev --no-emit-workspace --format requirements.txt > requirements.txt
{%- endif %}

.PHONY: requirements-export-dev
requirements-export-dev: lock-update
{%- if cookiecutter.package_manager == "poetry" %}
	poetry export --with dev --without-hashes > requirements.dev.txt
{%- elif cookiecutter.package_manager == "uv" %}
	uv export --no-hashes --no-cache --no-emit-workspace --format requirements.txt > requirements.dev.txt
{%- endif %}

#* Tools
.PHONY: tools-install
tools-install:
	{{ pm_cmd }} run pre-commit install --hook-type prepare-commit-msg --hook-type pre-commit
{% if cookiecutter.include_notebooks_sample == 'y' -%}#* Notebooks
	{{ pm_cmd }} run nbdime config-git --enable{%- endif %}

.PHONY: pre-commit-update
pre-commit-update:
	{{ pm_cmd }} run pre-commit autoupdate

.PHONY: pre-commit-run-all
pre-commit-run-all:
	{{ pm_cmd }} run pre-commit run --all-files

{% if cookiecutter.include_notebooks_sample == 'y' -%}#* Notebooks
.PHONY: nbextention-toc-install
nbextention-toc-install:
	{{ pm_cmd }} run jupyter contrib nbextension install --user
	{{ pm_cmd }} run jupyter nbextension enable toc2/main{%- endif %}

#* Tests
.PHONY: tests
tests:
	{{ pm_cmd }} run pytest -c pyproject.toml

#* Linting
.PHONY: type-check
type-check:
{%- if cookiecutter.python_type_checker == 'mypy' %}
	{{ pm_cmd }} run mypy
{%- elif cookiecutter.python_type_checker == 'ty' %}
	{{ pm_cmd }} run ty check
{%- endif %}

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
