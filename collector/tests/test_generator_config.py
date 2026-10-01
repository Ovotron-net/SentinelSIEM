import unittest

from collector.config.generator_config import GeneratorConfig, load_config


class GeneratorConfigTests(unittest.TestCase):
    def test_load_config_uses_defaults(self):
        config = load_config({})

        self.assertEqual(
            config,
            GeneratorConfig(
                log_level="INFO",
                batch_size=100,
                flush_interval_seconds=5.0,
            ),
        )

    def test_load_config_reads_and_normalizes_environment_values(self):
        config = load_config(
            {
                "GENERATOR_LOG_LEVEL": " debug ",
                "GENERATOR_BATCH_SIZE": "25",
                "GENERATOR_FLUSH_INTERVAL_SECONDS": "0.5",
            }
        )

        self.assertEqual(config.log_level, "DEBUG")
        self.assertEqual(config.batch_size, 25)
        self.assertEqual(config.flush_interval_seconds, 0.5)

    def test_load_config_rejects_invalid_values(self):
        invalid_values = (
            ({"GENERATOR_LOG_LEVEL": "TRACE"}, "log_level"),
            ({"GENERATOR_BATCH_SIZE": "zero"}, "GENERATOR_BATCH_SIZE"),
            ({"GENERATOR_BATCH_SIZE": "0"}, "batch_size"),
            ({"GENERATOR_FLUSH_INTERVAL_SECONDS": "nan"}, "flush_interval_seconds"),
            ({"GENERATOR_FLUSH_INTERVAL_SECONDS": "0"}, "flush_interval_seconds"),
        )

        for environ, message in invalid_values:
            with self.subTest(environ=environ):
                with self.assertRaisesRegex(ValueError, message):
                    load_config(environ)

    def test_direct_configuration_is_validated(self):
        with self.assertRaisesRegex(ValueError, "log_level"):
            GeneratorConfig(log_level=None)
        with self.assertRaisesRegex(ValueError, "batch_size"):
            GeneratorConfig(batch_size=True)
        with self.assertRaisesRegex(ValueError, "flush_interval_seconds"):
            GeneratorConfig(flush_interval_seconds=float("inf"))


if __name__ == "__main__":
    unittest.main()
