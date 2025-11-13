from unittest import mock 
from constants import STATUS_ENDPOINT
from build_status import BuildStatus


@mock.patch("build_stats.requests")
def test_build_notification_sent(mock_requests):
    build_date = "2025-08-24T00:00:01"
    with mock.patch("build_status.BuildStatus.build_date", return_value=build_date):
        BuildStatus.notify(123, "OK")

    expected_payload = {"id": 123, "status": "OK", "build_at": build_date}
    mock_requests.post.assert_called_with(
        STATUS_ENDPOINT, json=expected_payload
    )