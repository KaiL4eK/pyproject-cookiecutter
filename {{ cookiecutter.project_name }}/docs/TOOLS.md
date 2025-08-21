# Additional instructions

## Table of contents

- [Make](#make)
- [Python](#python)
{% if cookiecutter.package_manager == 'poetry' -%}
- [Poetry](#poetry)
{% elif cookiecutter.package_manager == 'uv' -%}
- [uv](#uv)
{% endif %}

## Make

- Windows:

    Install [chocolatey](https://chocolatey.org/install) and install `make` with command:

```powershell
choco install make
```

- Linux:

```bash
sudo apt-get install build-essential
```

[Table of contents](#table-of-contents)

## Python

- Windows

    Install with [official executable](https://www.python.org/downloads/)

- Linux

```bash
sudo apt install python{{ cookiecutter.minimal_python_version }}-dev
```

Sometimes you need to install `distutils`

```bash
sudo apt install python{{ cookiecutter.minimal_python_version }}-distutils
```

[Table of contents](#table-of-contents)

{% if cookiecutter.package_manager == 'poetry' -%}

## Poetry

Use [official instructions](https://python-poetry.org/docs/#installing-with-the-official-installer):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Or use [pipx](https://github.com/pypa/pipx) or [uvx](https://docs.astral.sh/uv/guides/tools/) for installing

```bash
pipx install poetry
```

{% endif %}

{% if cookiecutter.package_manager == 'uv' -%}

## uv

Use [official instructions](https://docs.astral.sh/uv/getting-started/installation/):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or use [pipx](https://github.com/pypa/pipx) or [uvx](https://docs.astral.sh/uv/guides/tools/) for installing

```bash
pipx install uv
```

{% endif -%}

[Table of contents](#table-of-contents)
