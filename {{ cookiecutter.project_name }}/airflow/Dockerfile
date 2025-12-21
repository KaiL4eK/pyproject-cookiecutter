# Custom Airflow image to install dependencies
ARG AIRFLOW_IMAGE_NAME=apache/airflow:3.1.5-python{{ cookiecutter.minimal_python_version }}
FROM ${AIRFLOW_IMAGE_NAME}

# `root` user to install everything
USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      curl \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Back to `airflow` user
USER airflow

# Install package manager, export and install dependent packages
RUN --mount=type=bind,source=requirements.project.txt,target=requirements.project.txt \
    --mount=type=bind,source={{ cookiecutter.package_manager }}.lock,target={{ cookiecutter.package_manager }}.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.project.txt \
{%- if cookiecutter.package_manager == "poetry" %}
    && poetry export --without-hashes --only main -f requirements.txt > requirements.txt \
{%- elif cookiecutter.package_manager == "uv" %}
    && uv export --no-hashes --no-cache --no-dev --no-emit-workspace --no-build --format requirements.txt > requirements.txt \
{%- endif %}
    && pip install -r requirements.txt

# Install root package
COPY {{cookiecutter.project_slug}} ./{{cookiecutter.project_slug}}/
RUN --mount=type=bind,source=README.md,target=README.md \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    pip install .

COPY airflow/scripts/ ./scripts/
