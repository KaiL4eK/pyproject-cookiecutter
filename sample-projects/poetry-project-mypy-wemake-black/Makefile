#* Variables
SHELL := /usr/bin/env bash
PYTHON ?= python3

#* Docker variables
IMAGE := poetry_project_mypy_wemake_black
VERSION := latest

#* Docker
# Example: make docker-build VERSION=latest
# Example: make docker-build IMAGE=some_name VERSION=0.1.0
docker-build:
	@echo Building docker $(IMAGE):$(VERSION) ...
	docker build \
		-t $(IMAGE):$(VERSION) . \
		-f ./docker/Dockerfile --no-cache

docker-build-cached:
	@echo Building docker $(IMAGE):$(VERSION) ...
	docker build \
		-t $(IMAGE):$(VERSION) . \
		-f ./docker/Dockerfile

docker-dive-analyze:
	@echo Analyze docker image with dive $(IMAGE):$(VERSION) ...
	docker run -ti --rm  \
		-v /var/run/docker.sock:/var/run/docker.sock \
		-e CI=true \
		wagoodman/dive:0.13.0 \
		$(IMAGE):$(VERSION)

# Example: make docker-remove VERSION=latest
# Example: make docker-remove IMAGE=some_name VERSION=0.1.0
docker-remove:
	@echo Removing docker $(IMAGE):$(VERSION) ...
	docker rmi -f $(IMAGE):$(VERSION)

#* Initialization
project-init: install-packages tools-install

install-packages:
	poetry install -n

lock-update:
	poetry lock --no-update

requirements-export: lock-update
	poetry export --without-hashes > requirements.txt

requirements-export-dev: lock-update
	poetry export --with dev --without-hashes > requirements.dev.txt

#* Tools
tools-install:
	poetry run pre-commit install --hook-type prepare-commit-msg --hook-type pre-commit
#* Notebooks
	poetry run nbdime config-git --enable

pre-commit-update:
	poetry run pre-commit autoupdate

pre-commit-run-all:
	poetry run pre-commit run --all-files

#* Notebooks
nbextention-toc-install:
	poetry run jupyter contrib nbextension install --user
	poetry run jupyter nbextension enable toc2/main

#* Tests
tests:
	poetry run pytest -c pyproject.toml

#* Linting
type-check:
	poetry run mypy

#* Cleaning
pycache-remove:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf
	find . | grep -E "(.ipynb_checkpoints$$)" | xargs rm -rf

build-remove:
	rm -rf build/

clean-all: pycache-remove build-remove docker-remove

#* Service targets
grep-todos:
	git grep -EIn "TODO|FIXME|XXX"
