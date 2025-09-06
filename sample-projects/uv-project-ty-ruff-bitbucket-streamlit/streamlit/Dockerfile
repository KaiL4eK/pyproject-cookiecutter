# Stage 1 - collect wheel files for dependencies
FROM python:3.11-slim-bullseye AS builder

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project dependencies list to setup first and cache
COPY pyproject.toml uv.lock requirements.project.txt ./

# Install package manager, export to requirements and collect/build wheels
RUN pip install --upgrade pip \
    && pip install --no-cache-dir wheel~=0.45.1 \
    && pip install --no-cache-dir -r requirements.project.txt \
    # Export main packages without dev - only core dependencies
    && uv export --no-hashes --no-cache --no-dev --no-emit-workspace --no-build --format requirements.txt > requirements.txt \
    # Collect wheel files to install them in second stage
    && pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

# Stage 2 - install dependencies (wheels) and main package
FROM python:3.11-slim-bullseye

# Setup directory to work inside image
WORKDIR /app

# Prepare system environment
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# This one requires BuildKit - https://docs.docker.com/go/buildkit/
# To run without BuiltKit just copy wheels before install from build stage and remove after install
RUN --mount=type=bind,from=builder,source=/wheels,target=/wheels pip install --no-cache-dir --no-index --find-links=/wheels /wheels/*

COPY migrations ./migrations/
COPY alembic.ini ./

COPY README.md Makefile pyproject.toml ./
# Install sources package
COPY uv_project_ty_ruff_bitbucket_streamlit ./uv_project_ty_ruff_bitbucket_streamlit/
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -e .

# App
COPY streamlit/app.py ./
COPY streamlit/pages ./pages/

# Expose Streamlit port
EXPOSE 8501

ENV STREAMLIT_SERVER_ADDRESS 0.0.0.0
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS false

# Run the application
CMD ["streamlit", "run", "app.py"]
