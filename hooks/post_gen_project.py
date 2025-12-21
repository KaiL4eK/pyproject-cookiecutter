import os
import platform
import shutil

REMOVE_PATHS = [
    '{% if cookiecutter.python_linter != "wemake" and cookiecutter.python_linter != "flake8" %} .flake8 {% endif %}',
    '{% if cookiecutter.include_docker_sample == "n" %} docker {% endif %}',
    '{% if cookiecutter.include_docker_sample == "n" %} .dockerignore {% endif %}',
    '{% if cookiecutter.include_notebooks_sample == "n" %} notebooks {% endif %}',
    '{% if cookiecutter.include_cli_example == "n" %} {{ cookiecutter.project_slug }}/__main__.py {% endif %}',
    '{% if cookiecutter.vcs_remote_type != "github" %} .additional/github_commit_prefix.py {% endif %}',
    '{% if cookiecutter.vcs_remote_type != "bitbucket" %} .additional/bitbucket_commit_prefix.py {% endif %}',
    '{% if cookiecutter.package_manager != "poetry" %} poetry.toml {% endif %}',
    '{% if cookiecutter.include_streamlit == "n" %} streamlit {% endif %}',
    '{% if cookiecutter.include_streamlit == "n" %} migrations {% endif %}',
    '{% if cookiecutter.include_streamlit == "n" %} alembic.ini {% endif %}',
    '{% if cookiecutter.include_streamlit == "n" %} {{ cookiecutter.project_slug }}/schemas {% endif %}',
    '{% if cookiecutter.include_streamlit == "n" %} {{ cookiecutter.project_slug }}/settings/db.py {% endif %}',
    '{% if cookiecutter.include_streamlit == "n" %} {{ cookiecutter.project_slug }}/db {% endif %}',
    '{% if cookiecutter.include_airflow == "n" %} airflow {% endif %}',
    '{% if cookiecutter.include_airflow == "n" %} {{ cookiecutter.project_slug }}/airflow {% endif %}',
]

def remove_path(path: str):
    path = path.strip()
    if not path:
        return

    # print("Removing {}".format(path))

    if not os.path.exists(path):
        print(f"Not found: {path}")
        return

    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)


for path in REMOVE_PATHS:
    remove_path(path)

# Linux / Windows / Darwin (Mac)
DETECTED_OS = platform.system()

# Unify pyproject files
general_fname = "pyproject.general.toml"
pyproject_all_files = [
    "pyproject.uv.toml",
    "pyproject.poetry.toml",
    general_fname,
]

base_pyproject_fname = "pyproject.{{ cookiecutter.package_manager }}.toml"

def read_files_content(fpath: str):
    merged_content = []
    with open(fpath, 'r') as f:
        merged_content.append(f.read())

    return merged_content

package_manager_content = read_files_content(base_pyproject_fname)
general_content = read_files_content(general_fname)

with open('pyproject.toml', 'w') as f:
    f.write('\n'.join(package_manager_content + general_content))

for fpath in pyproject_all_files:
    remove_path(fpath)
