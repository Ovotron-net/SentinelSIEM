""" Defines standardized severity levels used throughout SentinelSIEM.

It has types declared in this files from the ascending point of view of it's urgency e.g., info,low medium,high,critical, etc. 

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
    