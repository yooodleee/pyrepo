from metrics_client import WrappedClient

from unittest import TestCase, main
from unittest.mock import Mock


class TestWrappedClient(TestCase):
    def test_send_converts_types(self):
        wrapped_clinet = WrappedClient()
        wrapped_clinet.client = Mock()
        wrapped_clinet.send('value', 1)

        wrapped_clinet.client.assert_called_with('value', '1')