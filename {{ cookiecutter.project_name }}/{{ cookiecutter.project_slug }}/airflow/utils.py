"""Airflow utils."""

import pickle
from pathlib import Path
from typing import Any

from {{cookiecutter.project_slug}}.paths import PROJECT_DPATH


def serialize(
    data: Any,
    name: str,
    root_path: Path = (PROJECT_DPATH / "dumps"),
) -> Path:
    """Simple serialization function to call during local notebooks code debug."""
    root_path.mkdir(exist_ok=True, parents=True)
    fpath = root_path / f"{name}.pkl"
    with fpath.open("wb") as f:
        pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

    return fpath


def deserialize(name: str, root_path: Path = (PROJECT_DPATH / "dumps")) -> Any:
    """Simple deserialization function to call during local notebooks code debug."""
    fpath = root_path / f"{name}.pkl"
    with fpath.open("rb") as f:
        data = pickle.load(f)  # noqa: S301

    return data
