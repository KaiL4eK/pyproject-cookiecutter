"""Module for project paths.

Don`t use it if you build package and use it externally!
"""

from pathlib import Path

PROJECT_DPATH = Path(__file__).resolve().parents[1]
