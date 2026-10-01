"""Tests for the collector generator interface."""

import unittest

from collector.generators.base_generator import BaseGenerator


class BaseGeneratorTests(unittest.TestCase):
    def test_base_generator_is_abstract(self) -> None:
        with self.assertRaises(TypeError):
            BaseGenerator()

    def test_subclass_implements_generate(self) -> None:
        class ExampleGenerator(BaseGenerator):
            def generate(self) -> str:
                return "sample log record"

        self.assertEqual(ExampleGenerator().generate(), "sample log record")


if __name__ == "__main__":
    unittest.main()
