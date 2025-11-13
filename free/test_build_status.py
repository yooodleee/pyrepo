from unittest import mock 
from constants import STATUS_ENDPOINT
from build_status import BuildStatus
import pytest


@pytest.fixture
def build_status():
    bstatus = BuildStatus(mock.Mock())
    bstatus.build_date = mock.Mock(return_value="2025-08-25T00:00:01")
    return bstatus

def test_build_notification_sent(build_status):
    build_status.notify(1234, "OK")

    expected_payload = {
        "id": 1234,
        "status": "OK",
        "build_at": build_status.build_date(),
    }
    build_status.transport.post.assert_called_with(
        build_status.endpoint, json=expected_payload
    )