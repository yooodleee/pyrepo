from merge_request import MergeRequest, MergeRequestStatus, AcceptanceThreshold, MergeRequestException
import unittest


class BaseCase(unittest.TestCase):
    """Base Test Suite."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mr_cls = MergeRequest

    def setUp(self):
        self.merge_request = self.mr_cls()
    
    def test_simple_rejected(self):
        self.merge_request.downvote("maintainer")
        self.assertEqual(
            self.merge_request.status.value, MergeRequestStatus.REJECTED.value
        )
    
    def test_just_created_is_pending(self):
        self.assertEqual(
            self.mr_cls().status.value, MergeRequestStatus.PENDING.value
        )
    
    def test_pending_awaiting_review(self):
        self.merge_request.upvote("core-dev")
        self.assertEqual(
            self.merge_request.status.value, MergeRequestStatus.PENDING.value
        )
    
    def test_approved(self):
        self.merge_request.upvote("dev1")
        self.merge_request.upvote("dev2")
        self.assertEqual(
            self.merge_request.status.value, MergeRequestStatus.APPROVED.value
        )
    
    def test_no_double_approve(self):
        self.merge_request.upvote("dev1")
        self.merge_request.upvote("dev2")
        self.assertEqual(
            self.merge_request.status.value, MergeRequestStatus.PENDING.value
        )
    
    def test_upvote_changes_to_downvote(self):
        self.merge_request.upvote("dev1")
        self.merge_request.upvote("dev2")
        self.merge_request.downvote("dev1")
        self.assertEqual(
            self.merge_request.status.value, MergeRequestStatus.REJECTED.value
        )
    
    def test_downvote_to_upvote(self):
        self.merge_request.upvote("dev1")
        self.merge_request.downvote("dev2")
        self.merge_request.upvote("dev2")
        self.assertEqual(
            self.merge_request.status.value, MergeRequestStatus.APPROVED.value
        )
    
    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            self.merge_request.upvote({"invalid-object"})


class ExtendedCases(unittest.TestCase):
    """Exnteded Edge-case Tests."""

    def __init__(self):
        self.merge_request = MergeRequest()

    def test_cannot_upvote_on_closed_merge_request(self):
        self.merge_request.close()
        with self.assertRaises(MergeRequestException):
            self.merge_request.downvote("dev1")


class TestUTFrameworks(BaseCase, ExtendedCases):
    mr_cls = MergeRequest

    def setUp(self):
        super().setUp()
        self.fixture_data = (
            (
                {"downvotes": set(), "upvotes": set()},
                MergeRequestStatus.PENDING,
            ),
            (
                {"downvotes": set(), "upvotes": {"dev1"}},
                MergeRequestStatus.PENDING,
            ),
            (
                {'downvotes': "dev1", "upvotes": set()},
                MergeRequestStatus.REJECTED,
            ),
            (
                {"downvotes": set(), "upvotes": {"dev1", "dev2"}},
                MergeRequestStatus.APPROVED,
            ),
        )
    
    def test_status_resolution(self):
        for context, expected in self.fixture_data:
            with self.subTest(context=context):
                status = AcceptanceThreshold(context).status()
                self.assertEqual(status.value, expected.value)