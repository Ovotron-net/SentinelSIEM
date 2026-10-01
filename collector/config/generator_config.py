"""Configuration loading and validation for log generators."""

from __future__ import annotations

import math
import os
from dataclasses import dataclass
from typing import Mapping


DEFAULT_LOG_LEVEL = "INFO"
DEFAULT_BATCH_SIZE = 100
DEFAULT_FLUSH_INTERVAL_SECONDS = 5.0
_LOG_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}


@dataclass(frozen=True)
class GeneratorConfig:
    """Validated settings used by a log generator."""

    log_level: str = DEFAULT_LOG_LEVEL
    batch_size: int = DEFAULT_BATCH_SIZE
    flush_interval_seconds: float = DEFAULT_FLUSH_INTERVAL_SECONDS

    def __post_init__(self) -> None:
        if not isinstance(self.log_level, str):
            raise ValueError("log_level must be a supported logging level")
        normalized_log_level = self.log_level.strip().upper()
        if normalized_log_level not in _LOG_LEVELS:
            allowed_levels = ", ".join(sorted(_LOG_LEVELS))
            raise ValueError(f"log_level must be one of: {allowed_levels}")
        object.__setattr__(self, "log_level", normalized_log_level)

        if isinstance(self.batch_size, bool) or not isinstance(self.batch_size, int):
            raise ValueError("batch_size must be a positive integer")
        if self.batch_size <= 0:
            raise ValueError("batch_size must be a positive integer")

        if isinstance(self.flush_interval_seconds, bool):
            raise ValueError("flush_interval_seconds must be a positive number")
        try:
            interval = float(self.flush_interval_seconds)
        except (TypeError, ValueError) as error:
            raise ValueError(
                "flush_interval_seconds must be a positive number"
            ) from error
        if not math.isfinite(interval) or interval <= 0:
            raise ValueError("flush_interval_seconds must be a positive number")
        object.__setattr__(self, "flush_interval_seconds", interval)


def load_config(environ: Mapping[str, str] | None = None) -> GeneratorConfig:
    """Load generator settings from environment variables, using defaults.

    The supported variables are ``GENERATOR_LOG_LEVEL``,
    ``GENERATOR_BATCH_SIZE``, and ``GENERATOR_FLUSH_INTERVAL_SECONDS``.
    """
    values = os.environ if environ is None else environ

    log_level = values.get("GENERATOR_LOG_LEVEL", DEFAULT_LOG_LEVEL)
    batch_size_value = values.get("GENERATOR_BATCH_SIZE", str(DEFAULT_BATCH_SIZE))
    interval_value = values.get(
        "GENERATOR_FLUSH_INTERVAL_SECONDS",
        str(DEFAULT_FLUSH_INTERVAL_SECONDS),
    )

    try:
        batch_size = int(batch_size_value)
    except (TypeError, ValueError) as error:
        raise ValueError("GENERATOR_BATCH_SIZE must be a positive integer") from error

    try:
        flush_interval_seconds = float(interval_value)
    except (TypeError, ValueError) as error:
        raise ValueError(
            "GENERATOR_FLUSH_INTERVAL_SECONDS must be a positive number"
        ) from error

    return GeneratorConfig(
        log_level=log_level,
        batch_size=batch_size,
        flush_interval_seconds=flush_interval_seconds,
    )
