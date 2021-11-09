# Python project template for cookiecutter #

> Based on https://github.com/TezRomacH/python-package-template and https://awesomeopensource.com/project/TezRomacH/python-package-template

<div align="center">

[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/KaiL4eK/pyproject-cookiecutter/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/KaiL4eK/pyproject-cookiecutter/blob/main/.pre-commit-config.yaml)

</div>

## Table of Content <a id="toc"></a>

* [How to start](#howto)
* [Template testing](#template)


## How to start <a id="howto"></a>

- Install [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)
- Create project from template
```bash
cookiecutter https://github.com/KaiL4eK/pyproject-cookiecutter.git
```
- Answer some questions and get ready to code!

[Table of Content](#toc)

## Template testing <a id="template"></a>

To test execution, build and other checks use command:

```bash
make test-project-creation
```

> This command creates directory `/tmp/cookiecutter` and builds project from template there with local soft link in this directory

[Table of Content](#toc)