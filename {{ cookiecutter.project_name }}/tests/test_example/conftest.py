"""General fixtures for tests."""

from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def project_dpath() -> Path:
    return Path(__file__).resolve().parents[1]
