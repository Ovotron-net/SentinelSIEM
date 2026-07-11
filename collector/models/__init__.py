"""All the public models that are used by collector package."""

from .log_source import LogSource
from .severity import Severity

__all__ = [
    "LogSource",
    "Severity",
]