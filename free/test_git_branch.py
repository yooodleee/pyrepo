from git_branch import GitBranch, author_by_id
from unittest import mock


def test_find_commit():
    branch = GitBranch([{"id": "123", "author": "dev1"}])
    assert author_by_id("123", branch) == "dev1"

def test_find_any():
    # author = author_by_id("123", mock.Mock()) is not None
    # ...
    mbranch = mock.MagicMock()
    mbranch.__getitem__.return_value = {"author": "test"}
    assert author_by_id("123", mbranch) == "test"