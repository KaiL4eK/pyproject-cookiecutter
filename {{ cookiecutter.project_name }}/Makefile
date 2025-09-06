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
# Example: make docker-remove IMAGE=some_name VERSION={{ cookiecutter.version }}
docker-remove:
	@echo Removing docker $(IMAGE):$(VERSION) ...
	docker rmi -f $(IMAGE):$(VERSION)
{%- endif %}

#* Initialization
project-init: install-packages tools-install

install-packages:
{%- if cookiecutter.package_manager == "poetry" %}
	poetry install -n
{%- elif cookiecutter.package_manager == "uv" %}
	uv sync
{%- endif %}

lock-update:
{%- if cookiecutter.package_manager == "poetry" %}
	poetry lock --no-update
{%- elif cookiecutter.package_manager == "uv" %}
	uv lock
{%- endif %}

requirements-export: lock-update
{%- if cookiecutter.package_manager == "poetry" %}
	poetry export --without-hashes > requirements.txt
{%- elif cookiecutter.package_manager == "uv" %}
	uv export --no-hashes --no-cache --no-dev --no-emit-workspace --format requirements.txt > requirements.txt
{%- endif %}

requirements-export-dev: lock-update
{%- if cookiecutter.package_manager == "poetry" %}
	poetry export --with dev --without-hashes > requirements.dev.txt
{%- elif cookiecutter.package_manager == "uv" %}
	uv export --no-hashes --no-cache --no-emit-workspace --format requirements.txt > requirements.dev.txt
{%- endif %}

#* Tools
tools-install:
	{{ pm_cmd }} run pre-commit install --hook-type prepare-commit-msg --hook-type pre-commit
{% if cookiecutter.include_notebooks_sample == 'y' -%}#* Notebooks
	{{ pm_cmd }} run nbdime config-git --enable{%- endif %}

pre-commit-update:
	{{ pm_cmd }} run pre-commit autoupdate

pre-commit-run-all:
	{{ pm_cmd }} run pre-commit run --all-files

{% if cookiecutter.include_notebooks_sample == 'y' -%}#* Notebooks
nbextention-toc-install:
	{{ pm_cmd }} run jupyter contrib nbextension install --user
	{{ pm_cmd }} run jupyter nbextension enable toc2/main{%- endif %}

#* Tests
tests:
	{{ pm_cmd }} run pytest -c pyproject.toml

#* Linting
type-check:
{%- if cookiecutter.python_type_checker == 'mypy' %}
	{{ pm_cmd }} run mypy
{%- elif cookiecutter.python_type_checker == 'ty' %}
	{{ pm_cmd }} run ty check
{%- endif %}

#* Cleaning
pycache-remove:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf
	find . | grep -E "(.ipynb_checkpoints$$)" | xargs rm -rf

build-remove:
	rm -rf build/

clean-all: pycache-remove build-remove {% if cookiecutter.include_docker_sample == 'y' -%}docker-remove{% endif %}

#* Service targets
grep-todos:
	git grep -EIn "TODO|FIXME|XXX"

{% if cookiecutter.include_streamlit == 'y' -%}
#* Streamlit Docker
streamlit-docker-build:
	docker compose -f streamlit/docker-compose.yml build

streamlit-docker-start:
	docker compose -f streamlit/docker-compose.yml up --build

streamlit-docker-start-daemon:
	docker compose -f streamlit/docker-compose.yml up --build -d

streamlit-docker-start-debug:
	docker compose -f streamlit/docker-compose.yml -f streamlit/docker-compose.debug.yml up --build --watch app

streamlit-docker-down:
	docker compose -f streamlit/docker-compose.yml down

streamlit-docker-clean:
	docker compose -f streamlit/docker-compose.yml down -v

streamlit-docker-clean-debug:
	docker compose -f streamlit/docker-compose.yml -f streamlit/docker-compose.debug.yml down -v

streamlit-docker-push: streamlit-docker-build
	docker compose -f streamlit/docker-compose.yml push

#* Streamlit
streamlit-start:
	{{ pm_cmd }} run {% if cookiecutter.package_manager == "uv" %}--env-file=.env{% endif %} \
		streamlit run streamlit/app.py \
			--server.runOnSave true \
			--server.address 0.0.0.0 \
			--server.port 8503

#* Migrations
MIGRATION_COMMENT?=""
migrations-check-env:
	@if [ -z "$(MIGRATION_COMMENT)" ]; then \
	    echo "MIGRATION_COMMENT is not set." && exit 1; \
	elif echo "$(MIGRATION_COMMENT)" | grep -q ' '; then \
	    echo "MIGRATION_COMMENT must not contain spaces." && exit 1; \
	fi

migrations-new-revision: migrations-check-env
	DATABASE_HOST=localhost \
		{{ pm_cmd }} run {% if cookiecutter.package_manager == "uv" %}--env-file=.env{% endif %} \
		alembic revision --autogenerate -m ${MIGRATION_COMMENT}
{%- endif %}
