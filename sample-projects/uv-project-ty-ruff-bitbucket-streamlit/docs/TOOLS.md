# Additional instructions

## Table of contents

- [Make](#make)
- [Python](#python)
- [uv](#uv)


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
sudo apt install python3.12-dev
```

Sometimes you need to install `distutils`

```bash
sudo apt install python3.12-distutils
```

[Table of contents](#table-of-contents)



## uv

Use [official instructions](https://docs.astral.sh/uv/getting-started/installation/):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or use [pipx](https://github.com/pypa/pipx) or [uvx](https://docs.astral.sh/uv/guides/tools/) for installing

```bash
pipx install uv
```

[Table of contents](#table-of-contents)
