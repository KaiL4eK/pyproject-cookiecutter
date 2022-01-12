# Python project template for cookiecutter #

<div align="center">

[![PythonSupported](https://img.shields.io/badge/python-3.8%20%7C%203.9-brightgreen.svg)](https://python3statement.org/#sections50-why)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/KaiL4eK/pyproject-cookiecutter/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/KaiL4eK/pyproject-cookiecutter/blob/main/.pre-commit-config.yaml)
[![Bandit](https://img.shields.io/badge/security-bandit-informational.svg)](https://github.com/KaiL4eK/pyproject-cookiecutter/blob/main/.pre-commit-config.yaml)

</div>

## Features

* Python 3.8 or 3.9 supported
* [Poetry](https://python-poetry.org/) for package/dependency management
* Tests are based on [`pytest`](https://docs.pytest.org/en/stable/)
* Pre-commit hooks with [pre-commit](https://pre-commit.com/)
  * Linting using [flake8](https://flake8.pycqa.org/en/latest/)
  * Code style via [black](https://github.com/psf/black)
  * Notebooks cleaning via [nbstripout](https://github.com/kynan/nbstripout)
  * Security checks via [bandit](https://github.com/PyCQA/bandit) and [safety](https://github.com/pyupio/safety)
* [VSCode](https://code.visualstudio.com/) editor config with [EditorConfig](https://editorconfig.org/)

## How to start <a id="howto"></a>

* Install [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)
* Create project from template

```bash
cookiecutter gh:KaiL4eK/pyproject-cookiecutter
```

* Answer some questions and get ready to code!

[Table of Content](#toc)

## Thanks to <a id="thanks"></a>

* https://awesomeopensource.com/project/TezRomacH/python-package-template
