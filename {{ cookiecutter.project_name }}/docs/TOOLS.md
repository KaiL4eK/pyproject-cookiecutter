# Additional instructions

- [Additional instructions](#additional-instructions)
  - [Make](#make)
  - [Python](#python)
  - [Poetry](#poetry)

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

## Python

- Windows

    Install with [official executable](https://www.python.org/downloads/)

- Linux

```bash
sudo apt install python{{ cookiecutter.minimal_python_version }}-dev
```

## Poetry

- Windows

    Use [official instructions](https://python-poetry.org/docs/#windows-powershell-install-instructions) or use `powershell` command:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

- Linux

    Use [official instructions](https://python-poetry.org/docs/#installing-with-the-official-installer) or bash command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

[Table of contents](#table-of-contents)

