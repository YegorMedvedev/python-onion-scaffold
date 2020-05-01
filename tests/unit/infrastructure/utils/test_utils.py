import mock
import unittest

from src.infrastructure.utils.utils import get_port


class TestGetPort(unittest.TestCase):
    @mock.patch('src.infrastructure.utils.utils.os')
    def test_get_port_testing_env(self, mock_os):
        mock_os.getenv = mock.Mock()
        mock_os.getenv.side_effect = ["5000", "5000", "test"]
        result = get_port()

        self.assertEqual(result, 6000)

    @mock.patch('src.infrastructure.utils.utils.os')
    def test_get_port_any_env(self, mock_os):
        mock_os.getenv.side_effect = ["5000", "5000", "development"]
        result = get_port()

        self.assertEqual(result, 5000)
