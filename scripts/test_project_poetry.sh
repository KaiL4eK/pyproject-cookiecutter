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

poetry run jupyter nbconvert --inplace --to notebook --execute notebooks/example.ipynb \
    && make nbextention-toc-install \
    && poetry run jupyter nbconvert --template toc2 --to html_toc --output-dir ./exports notebooks/example.ipynb \
    && poetry run pytest \
    && poetry run python scripts/config_sample.py --config configs/config_sample.yml

if [ $? -ne 0 ]; then
    echo "Failed to check project"
    exit 1
fi

poetry run pre-commit run --files notebooks/* nbstripout || true

poetry run pre-commit run -a --show-diff-on-failure \
    && poetry build \
    && make docker-build-cached \
    && make docker-remove

if [ $? -ne 0 ]; then
    echo "Failed to check project"
    exit 1
fi
