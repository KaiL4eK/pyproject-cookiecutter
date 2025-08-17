# Docker for poetry-project-ty-ruff

## Installation

To create Docker you need to run:

```bash
make docker-build
```

which is equivalent to:

```bash
make docker-build VERSION=latest
```

You may provide name and version for the image.
Default name is `IMAGE := poetry_project_ty_ruff`.
Default version is `VERSION := latest`.

```bash
make docker-build IMAGE=some_name VERSION=0.1.0
```

## Usage

```bash
docker run -it --rm \
   -v $(pwd):/workspace \
   poetry_project_ty_ruff bash
```

## How to clean up

To uninstall docker image run `make docker-remove` with `VERSION`:

```bash
make docker-remove VERSION=0.1.0
```

you may also choose the image name

```bash
make docker-remove IMAGE=some_name VERSION=latest
```

If you want to clean all, including `build` and `pycache` run `make clean-all`

## Dive analyzer

You can analyze you image using tool [dive](https://github.com/wagoodman/dive).

```sh
make docker-dive-analyze
```
