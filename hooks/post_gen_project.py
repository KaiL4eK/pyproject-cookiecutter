import os
import shutil

REMOVE_PATHS = [
    '{% if cookiecutter.include_docker_sample == "no" %} docker {% endif %}',
    '{% if cookiecutter.include_tests_sample == "no" %} tests {% endif %}',
    '{% if cookiecutter.include_notebooks_sample == "no" %} notebooks {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if not path:
        continue

    print(f"Removing {path}")

    if not os.path.exists(path):
        print(f"Not found: {path}")
        continue

    shutil.rmtree(path)
