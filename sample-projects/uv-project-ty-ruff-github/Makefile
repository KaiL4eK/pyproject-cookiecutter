#* Variables
SHELL := /usr/bin/env bash
PYTHON ?= python3

#* Docker variables
IMAGE := uv_project_ty_ruff_github
VERSION := latest

#* Docker
# Example: make docker-build VERSION=latest
# Example: make docker-build IMAGE=some_name VERSION=0.1.0
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
# Example: make docker-remove IMAGE=some_name VERSION=0.1.0
.PHONY: docker-remove
docker-remove:
	@echo Removing docker $(IMAGE):$(VERSION) ...
	docker rmi -f $(IMAGE):$(VERSION)

#* Initialization
.PHONY: project-init
project-init: install-packages tools-install

.PHONY: install-packages
install-packages:
	uv sync

.PHONY: lock-update
lock-update:
	uv lock

.PHONY: requirements-export
requirements-export: lock-update
	uv export --no-hashes --no-cache --no-dev --no-emit-workspace --format requirements.txt > requirements.txt

.PHONY: requirements-export-dev
requirements-export-dev: lock-update
	uv export --no-hashes --no-cache --no-emit-workspace --format requirements.txt > requirements.dev.txt

#* Tools
.PHONY: tools-install
tools-install:
	uv run pre-commit install --hook-type prepare-commit-msg --hook-type pre-commit
#* Notebooks
	uv run nbdime config-git --enable

.PHONY: pre-commit-update
pre-commit-update:
	uv run pre-commit autoupdate

.PHONY: pre-commit-run-all
pre-commit-run-all:
	uv run pre-commit run --all-files

#* Notebooks
.PHONY: nbextention-toc-install
nbextention-toc-install:
	uv run jupyter contrib nbextension install --user
	uv run jupyter nbextension enable toc2/main

#* Tests
.PHONY: tests
tests:
	uv run pytest -c pyproject.toml

#* Linting
.PHONY: type-check
type-check:
	uv run ty check

#* Cleaning
.PHONY: pycache-remove
pycache-remove:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf
	find . | grep -E "(.ipynb_checkpoints$$)" | xargs rm -rf

.PHONY: build-remove
build-remove:
	rm -rf build/

.PHONY: clean-all
clean-all: pycache-remove build-remove docker-remove

#* Service targets
.PHONY: grep-todos
grep-todos:
	git grep -EIn "TODO|FIXME|XXX"
