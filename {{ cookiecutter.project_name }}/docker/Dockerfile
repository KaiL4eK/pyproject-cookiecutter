FROM python:{{ cookiecutter.minimal_python_version }}-slim-buster

ENV LANG=C.UTF-8 \
  LC_ALL=C.UTF-8

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  curl make \
  && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock Makefile ./

# Install Poetry
ENV POETRY_HOME=/opt/poetry
RUN make poetry-download && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    # Install all packages into system env
    poetry config virtualenvs.create false

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

CMD mkdir -p /workspace
WORKDIR /workspace
