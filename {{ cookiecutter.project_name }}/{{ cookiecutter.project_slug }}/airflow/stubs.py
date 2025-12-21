"""
Module to replace main airflow features to work locally.

What must be done to work:
- Create .env with required connections
- Import this module before all main modules
"""

from __future__ import annotations

import logging
from typing import Any

from airflow import decorators

logger = logging.getLogger(__name__)
logger.warning("Airflow Stubs are imported! Don`t use it in real Airflow env!")


def dummy_task_decorator_factory(  # noqa: D103
    func=None,
    **dec_kwargs,  # noqa: ARG001
):
    def decorator(func):
        def wrapped_f(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapped_f

    if func is not None:
        return decorator(func)

    return decorator


class TaskDecoratorCollectionStub:
    """Implementation to provide the ``@task`` syntax."""

    python = staticmethod(dummy_task_decorator_factory)
    branch = staticmethod(dummy_task_decorator_factory)

    __call__: Any = python  # Alias '@task' to '@task.python'.


# =========================================================
# It`s time to replace Airflow code!
decorators.task = TaskDecoratorCollectionStub()  # type: ignore [assignment]
