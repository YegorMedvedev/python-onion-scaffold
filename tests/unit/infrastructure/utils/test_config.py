import unittest

from os import getenv
from src.infrastructure.utils.config import read_env_config


class TestConfig(unittest.TestCase):
    def test_read_env_config(self):
        read_env_config()
        self.assertEqual(getenv("NAME"), "python-onion-scaffold")
        self.assertEqual(getenv("ENV"), "test")
        self.assertEqual(getenv("PORT"), "5000")
        self.assertIs(type(getenv("POSTGRESQL_URL")), str)


if __name__ == '__main__':
    unittest.main()
