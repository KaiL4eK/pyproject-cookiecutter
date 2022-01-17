import os
import shutil

REMOVE_PATHS = [
    '{% if cookiecutter.include_docker_sample == "n" %} docker {% endif %}',
    '{% if cookiecutter.include_docker_sample == "n" %} .dockerignore {% endif %}',
    '{% if cookiecutter.include_tests_sample == "n" %} tests {% endif %}',
    '{% if cookiecutter.include_notebooks_sample == "n" %} notebooks {% endif %}',
    '{% if cookiecutter.include_cli_example == "n" %} {{ cookiecutter.project_slug }}/__main__.py {% endif %}',
    '{% if cookiecutter.base_package_manager != "poetry" %} poetry.toml {% endif %}',
    '{% if cookiecutter.base_package_manager != "poetry" %} pyproject.toml {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if not path:
        continue

    print("Removing {}".format(path))

    if not os.path.exists(path):
        print(f"Not found: {path}")
        continue

    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)
