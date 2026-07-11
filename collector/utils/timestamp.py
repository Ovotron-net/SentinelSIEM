"""
Utility functions for generating and formatting UTC timestamps.

This module provides reusable helpers for working with timezone-aware
timestamps throughout SentinelSIEM. Timestamp generation and formatting
are intentionally kept separate to promote flexibility and maintainability.
"""

from __future__ import annotations

import random
from datetime import datetime, timedelta, timezone


def get_current_utc_timestamp() -> datetime:
    """Return the current UTC timestamp.

    Returns:
        datetime: The current timezone-aware UTC datetime.
    """
    return datetime.now(timezone.utc)


def format_iso8601(timestamp: datetime) -> str:
    """Convert a datetime object to an ISO 8601 formatted string.

    UTC timestamps are represented using the 'Z' suffix.

    Args:
        timestamp: A timezone-aware datetime object.

    Returns:
        str: The timestamp formatted as an ISO 8601 string.

    Raises:
        ValueError: If the provided datetime is not timezone-aware.
    """
    if timestamp.tzinfo is None:
        raise ValueError("Timestamp must be timezone-aware.")

    return timestamp.isoformat().replace("+00:00", "Z")


def generate_random_timestamp(
    start_time: datetime,
    end_time: datetime,
) -> datetime:
    """Generate a random timestamp between two UTC datetimes.

    Args:
        start_time: The earliest possible timestamp.
        end_time: The latest possible timestamp.

    Returns:
        datetime: A randomly generated timezone-aware datetime.

    Raises:
        ValueError: If the timestamps are invalid or not timezone-aware.
    """
    if start_time.tzinfo is None or end_time.tzinfo is None:
        raise ValueError("Both timestamps must be timezone-aware.")

    if start_time >= end_time:
        raise ValueError("start_time must be before end_time.")

    total_seconds = int((end_time - start_time).total_seconds())
    random_seconds = random.randint(0, total_seconds)

    return start_time + timedelta(seconds=random_seconds)


def generate_random_timestamps(
    start_time: datetime,
    end_time: datetime,
    count: int,
) -> list[datetime]:
    """Generate multiple random timestamps.

    Args:
        start_time: The earliest possible timestamp.
        end_time: The latest possible timestamp.
        count: Number of timestamps to generate.

    Returns:
        list[datetime]: A list of randomly generated timezone-aware
        datetime objects.

    Raises:
        ValueError: If count is less than zero.
    """
    if count < 0:
        raise ValueError("count must be greater than or equal to 0.")

    return [
        generate_random_timestamp(start_time, end_time)
        for _ in range(count)
    ]
