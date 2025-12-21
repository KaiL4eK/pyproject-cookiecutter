#* Variables
SHELL := /usr/bin/env bash
PYTHON ?= python3
ENV_FILE := .env

#* Docker variables
IMAGE := uv_project_ty_ruff_github
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
	uv sync

lock-update:
	uv lock

requirements-export: lock-update
	uv export --no-hashes --no-cache --no-dev --no-emit-workspace --format requirements.txt > requirements.txt

requirements-export-dev: lock-update
	uv export --no-hashes --no-cache --no-emit-workspace --format requirements.txt > requirements.dev.txt

#* Tools
tools-install:
	uv run pre-commit install --hook-type prepare-commit-msg --hook-type pre-commit
#* Notebooks
	uv run nbdime config-git --enable

pre-commit-update:
	uv run pre-commit autoupdate

pre-commit-run-all:
	uv run pre-commit run --all-files

#* Notebooks
nbextention-toc-install:
	uv run jupyter contrib nbextension install --user
	uv run jupyter nbextension enable toc2/main

#* Tests
tests:
	uv run pytest tests/ -c pyproject.toml

#* Linting
type-check:
	uv run ty check

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
