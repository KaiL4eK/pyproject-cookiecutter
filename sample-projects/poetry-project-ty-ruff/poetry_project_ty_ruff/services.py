"""Module for tasks definition. Here you define main logic (code)."""

from __future__ import annotations

import logging
from datetime import datetime, timezone

logger = logging.getLogger(__name__)


def simple_logic() -> None:
    """Sample service."""
    logger.info("Hello! It`s simple python task.")


def show_logic_time(logical_ts: datetime | None = None) -> None:
    """Service to debug logical time."""
    logical_ts = logical_ts or datetime.now(tz=timezone.utc)
    logger.info(f"Logical time: {logical_ts}")
