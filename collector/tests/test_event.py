"""Tests for the collector event contract."""

import json
import unittest
from datetime import datetime, timedelta, timezone

from collector.models.event import Event


class EventTests(unittest.TestCase):
    def test_defaults_are_independent_and_utc(self) -> None:
        first = Event(source="ssh", event_type="login", message="Accepted")
        second = Event(source="ssh", event_type="login", message="Denied")

        self.assertEqual(first.severity, "info")
        self.assertIsNot(first.metadata, second.metadata)
        self.assertEqual(first.timestamp.utcoffset(), timedelta(0))
        first.metadata["user"] = "alice"
        self.assertEqual(second.metadata, {})

    def test_serialization_normalizes_timestamp_and_preserves_fields(self) -> None:
        event = Event(
            source="ssh",
            event_type="login",
            message="Failed password",
            timestamp=datetime(2026, 1, 2, 3, 4, 5, tzinfo=timezone(timedelta(hours=2))),
            severity="warning",
            metadata={"user": "alice", "attempt": 2},
        )
        expected = {
            "timestamp": "2026-01-02T01:04:05Z",
            "source": "ssh",
            "event_type": "login",
            "message": "Failed password",
            "severity": "warning",
            "metadata": {"user": "alice", "attempt": 2},
        }

        self.assertEqual(event.to_dict(), expected)
        self.assertEqual(json.loads(event.to_json()), expected)

    def test_naive_timestamp_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            Event(
                source="ssh",
                event_type="login",
                message="Denied",
                timestamp=datetime(2026, 1, 2),
            )


if __name__ == "__main__":
    unittest.main()
