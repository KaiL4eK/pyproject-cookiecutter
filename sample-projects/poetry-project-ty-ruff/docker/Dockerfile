# Stage 1 - collect wheel files for dependencies
FROM python:3.12-slim-bullseye AS builder

# Prepare system packages
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  curl make \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# Copy project dependencies list to setup first and cache
COPY pyproject.toml poetry.lock requirements.project.txt ./

# Install Poetry, export to requirements and collect/build wheels
RUN pip install --upgrade pip \
    && pip install --no-cache-dir wheel~=0.45.1 \
    && pip install --no-cache-dir -r requirements.project.txt \
    # Export main packages without dev - only core dependencies
    && poetry export --without-hashes --only main -f requirements.txt > requirements.txt \
    && ls \
    # Collect wheel files to install them in second stage
    && pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

# Stage 2 - install dependencies (wheels) and main package
FROM python:3.12-slim-bullseye

# Prepare system packages
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  make \
  && rm -rf /var/lib/apt/lists/*

# Setup directory to work inside image
WORKDIR /workspace

# Prepare system environment
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# This one requires BuildKit - https://docs.docker.com/go/buildkit/
# To run without BuiltKit just copy wheels before install from build stage and remove after install
RUN --mount=type=bind,from=builder,source=/wheels,target=/wheels pip install --no-cache-dir --no-index --find-links=/wheels /wheels/*

COPY README.md Makefile pyproject.toml ./
# Copy project sources into image
COPY poetry_project_ty_ruff ./poetry_project_ty_ruff/

RUN pip install .
