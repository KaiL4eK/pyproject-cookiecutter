#!/usr/bin/env bash

TEST_PROJECT_DPATH=$1

cd ${TEST_PROJECT_DPATH}
unset VIRTUAL_ENV

git init && git add -A \
    && make project-init

if [ $? -ne 0 ]; then
    echo "Failed to init project"
    exit 1
fi

uv run jupyter nbconvert --inplace --to notebook --execute notebooks/example.ipynb \
    && make nbextention-toc-install \
    && uv run jupyter nbconvert --template toc2 --to html_toc --output-dir ./exports notebooks/example.ipynb \
    && make tests \
    && uv run python scripts/config_sample.py --config configs/config_sample.yml

if [ $? -ne 0 ]; then
    echo "Failed to check project"
    exit 1
fi

uv run ruff check .
if [ $? -ne 0 ]; then
    echo "Failed to check project"
    exit 1
fi

uv run pre-commit run --show-diff-on-failure -a lint
uv run pre-commit run --show-diff-on-failure -a type-check

uv build \
    && make docker-build-cached \
    && make docker-remove

if [ $? -ne 0 ]; then
    echo "Failed to check project"
    exit 1
fi
