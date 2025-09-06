# Development guide

Notes for template development

## Template testing

To test execution, build and other checks use command:

```bash
make test-project-creation
```

> This command creates directory `/tmp/cookiecutter` and builds project from template there with local soft link in this directory

## Badges

Adding new functionality to the template requires adding badges to [README.md](README.md) and `{{ cookiecutter.project_slug }}/README.md` files.

You can find some [here](https://github.com/inttter/md-badges).

## CHANGELOG.md

Adding new functionality to the template requires adding info to [CHANGELOG.md](CHANGELOG.md).
