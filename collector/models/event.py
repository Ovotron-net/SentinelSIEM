"""
It is the main event defining module which will be used to map events in SentinelSIEM.

These fields are used to collect an event and serialize it as JSON for the processor framework.
"""


from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, Any
import uuid
from .log_source import LogSource
from .severity import Severity



def generate_uuid_str() -> str:
    return str(uuid.uuid4())
def generate_utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()
@dataclass(slots=True)
class Event:
    sources: LogSource
    event_type: str
    severity: Severity
    hostname: str | None
    username: str | None
    source_ip: str | None
    destination_ip: str | None
    port: int | None
    event_id: str = field(default_factory=generate_uuid_str)
    timestamp: str = field(default_factory=generate_utc_timestamp)
    details: dict = field(default_factory=dict)
