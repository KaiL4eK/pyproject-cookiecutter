import os
import platform
import shutil

REMOVE_PATHS = [
    '{% if cookiecutter.python_linter == "ruff" %} .flake8 {% endif %}',
    '{% if cookiecutter.include_docker_sample == "n" %} docker {% endif %}',
    '{% if cookiecutter.include_docker_sample == "n" %} .dockerignore {% endif %}',
    '{% if cookiecutter.include_tests_sample == "n" %} tests {% endif %}',
    '{% if cookiecutter.include_notebooks_sample == "n" %} notebooks {% endif %}',
    '{% if cookiecutter.include_cli_example == "n" %} {{ cookiecutter.project_slug }}/__main__.py {% endif %}',
    '{% if cookiecutter.vcs_remote_type != "github" %} .additional/github_commit_prefix.py {% endif %}',
    '{% if cookiecutter.vcs_remote_type != "bitbucket" %} .additional/bitbucket_commit_prefix.py {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if not path:
        continue

    # print("Removing {}".format(path))

    if not os.path.exists(path):
        print(f"Not found: {path}")
        continue

    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)


# Linux / Windows / Darwin (Mac)
DETECTED_OS = platform.system()
