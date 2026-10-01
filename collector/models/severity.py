""" Defines standardized severity levels used throughout SentinelSIEM.

Severity levels are declared in ascending order of urgency: info, low, medium, high, and critical.

These severity levels provide a consistent way to classify security
events across different log sources and processing components.
"""

from enum import StrEnum


class Severity(StrEnum):
    """Represents the severity level of a normalized security event."""

    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
    