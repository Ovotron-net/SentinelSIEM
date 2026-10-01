import ipaddress
import re
import unittest

from collector.utils.random_data import (
    generate_random_hostname,
    generate_random_ip,
    generate_random_port,
    generate_random_process_id,
    generate_random_string,
    select_random_username,
)


class RandomDataTests(unittest.TestCase):
    def test_generates_valid_ipv4_and_ipv6_addresses(self) -> None:
        self.assertEqual(ipaddress.ip_address(generate_random_ip()).version, 4)
        self.assertEqual(
            ipaddress.ip_address(generate_random_ip(version=6)).version, 6
        )

    def test_rejects_unsupported_ip_version(self) -> None:
        with self.assertRaises(ValueError):
            generate_random_ip(version=5)

    def test_selects_a_username(self) -> None:
        self.assertTrue(select_random_username())

    def test_generates_hostname_like_value(self) -> None:
        self.assertRegex(
            generate_random_hostname(),
            re.compile(r"^[a-z]+-[a-z]+-[1-9]\d{0,2}$"),
        )

    def test_generates_valid_port_and_process_id(self) -> None:
        self.assertIn(generate_random_port(), range(1, 65536))
        self.assertIn(generate_random_process_id(), range(1, 65536))

    def test_generates_string_of_requested_length(self) -> None:
        value = generate_random_string(24)
        self.assertEqual(len(value), 24)
        self.assertTrue(value.isalnum())
        self.assertEqual(generate_random_string(0), "")

    def test_rejects_negative_string_length(self) -> None:
        with self.assertRaises(ValueError):
            generate_random_string(-1)


if __name__ == "__main__":
    unittest.main()
