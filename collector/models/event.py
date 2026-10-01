"""
It is the main event defining module which will be used to map events in SentinelSIEM.

There fields will be used to collect a event and make a JSON file to use it in processor framework.
"""


from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, Any
import uuid
from models import LogSource
from models import Severity



def generate_uuid_str() -> str:
    return str(uuid.uuid4())
def generate_utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()
@dataclass(slots=True)
class Event:
    event_id: str = field(default_factory=generate_uuid_str)
    timestamp: str = field(default_factory=generate_utc_timestamp)
    sources: LogSource
    event_type: str
    severity: Severity
    hostname: str | None
    username: str | None
    source_ip: str | None
    destination_ip: str | None
    port: int | None
    details: dict = field(default_factory=dict)
