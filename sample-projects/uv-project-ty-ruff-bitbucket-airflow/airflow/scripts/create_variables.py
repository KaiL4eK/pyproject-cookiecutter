"""Script for creating non-existent Airflow Variables."""

import logging

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from airflow.sdk import Variable


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)-8s] %(name)s:%(lineno)d | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


class AirflowEnv(BaseSettings):
    """AirflowEnv config class with Airflow Variables."""
    model_config = SettingsConfigDict(
        case_sensitive=True,
        extra="ignore",
    )

    AIRFLOW_SAMPLE_VARIABLE: str = Field(default="RU")


def add_variable(key: str, val: str, overwrite: bool = False) -> None:
    """
    Add or update an Airflow variable.

    If overwrite is False and the variable with the given key already exists,
    the function logs a message and skips creation. If the variable does not exist,
    it is created and assigned the provided value. If overwrite is True, the variable
    is set regardless of whether it exists. Logs any failures during the process.
    """
    try:
        if not overwrite:
            value = Variable.get(key, default=None)
            if value is None:
                logger.info(f"Variable {key} already exists, skipping...")
                return
        Variable.set(key, val)
        logger.info(f"Variable {key} set successfully to {val}")
    except Exception:
        logger.exception("Failed to set variable")
        SystemExit(1)


def main() -> None:
    """Add Airflow variables."""
    env = AirflowEnv()
    for key, val in env.model_dump().items():
        if val is not None:
            add_variable(key, val)


if __name__ == "__main__":
    main()
