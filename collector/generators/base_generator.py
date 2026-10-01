"""Common interface for log generators."""

from __future__ import annotations

from abc import ABC, abstractmethod


class BaseGenerator(ABC):
    """Abstract base class for generators that produce raw log records."""

    @abstractmethod
    def generate(self) -> str:
        """Generate and return one raw log record."""
        raise NotImplementedError
