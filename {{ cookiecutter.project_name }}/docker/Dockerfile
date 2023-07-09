FROM python:{{ cookiecutter.minimal_python_version }}-slim-buster

# Prepare system environment
ENV LANG=C.UTF-8 \
  LC_ALL=C.UTF-8

# Prepare system packages
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  curl make \
  && rm -rf /var/lib/apt/lists/*

# Setup directory to work inside image
RUN mkdir -p /workspace
WORKDIR /workspace

# Copy project dependencies list to setup first and cache
COPY pyproject.toml poetry.lock Makefile ./

# Install Poetry
ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.4.0 && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    # Install all packages into system env
    poetry config virtualenvs.create false

# Install main packages without dev - only core dependencies
RUN poetry install --only main --no-root

# Copy project sources into image
COPY README.md ./
COPY {{ cookiecutter.project_slug }} ./{{ cookiecutter.project_slug }}/

# Install root as package
RUN poetry install --only-root
