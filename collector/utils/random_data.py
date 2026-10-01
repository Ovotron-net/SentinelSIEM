"""Helpers for generating synthetic data for collector events."""

from __future__ import annotations

import ipaddress
import random
import string


_USERNAMES = (
    "admin",
    "analyst",
    "jdoe",
    "jsmith",
    "svc-account",
    "system",
)
_HOSTNAME_PREFIXES = ("app", "db", "host", "node", "server", "workstation")
_HOSTNAME_SUFFIXES = ("alpha", "bravo", "delta", "east", "west")


def generate_random_ip(version: int = 4) -> str:
    """Generate a random IPv4 or IPv6 address.

    Args:
        version: IP version to generate; must be 4 or 6.

    Raises:
        ValueError: If version is not 4 or 6.
    """
    if version not in (4, 6):
        raise ValueError("version must be 4 or 6.")

    bit_count = 32 if version == 4 else 128
    return str(ipaddress.ip_address(random.getrandbits(bit_count)))


def select_random_username() -> str:
    """Select a username from a small set of common synthetic identities."""
    return random.choice(_USERNAMES)


def generate_random_hostname() -> str:
    """Generate a lowercase hostname-like value."""
    prefix = random.choice(_HOSTNAME_PREFIXES)
    suffix = random.choice(_HOSTNAME_SUFFIXES)
    number = random.randint(1, 999)
    return f"{prefix}-{suffix}-{number}"


def generate_random_port() -> int:
    """Generate a valid non-zero TCP/UDP port number."""
    return random.randint(1, 65535)


def generate_random_process_id() -> int:
    """Generate a positive process ID in the commonly supported range."""
    return random.randint(1, 65535)


def generate_random_string(length: int = 12) -> str:
    """Generate a random alphanumeric string of the requested length.

    Args:
        length: Number of characters to generate; must be non-negative.

    Raises:
        ValueError: If length is negative.
    """
    if length < 0:
        raise ValueError("length must be non-negative.")

    return "".join(
        random.choices(string.ascii_letters + string.digits, k=length)
    )
