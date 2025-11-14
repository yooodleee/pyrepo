from enum import Enum


class MergeRequestException(Exception):
    pass

class MergeRequestStatus(Enum):
    APPROVED = "approved"       # approved Merge Request
    REJECTED = "rejected"       # rejected Merge Request
    PENDING = "pending"         # pending Merge Request
    OPEN = "open"               # opend Merge Request
    CLOSED = "closed"           # closed Merge Request


class AcceptanceThreshold:
    def __init__(self, merge_request_context: dict) -> None:
        self._context = merge_request_context
    
    def status(self):
        if self._context["downvotes"]:
            return MergeRequestStatus.REJECTED
        elif len(self._context["upvotes"]) >= 2:
            return MergeRequestStatus.APPROVED
        return MergeRequestStatus.PENDING
    

class MergeRequest:
    """An entity abstracting a merge request."""

    def __init__(self):
        self._context = {"upvotes": set(), "downvotes": set()}
        self._status = MergeRequestStatus.OPEN
    
    def close(self):
        self._status = MergeRequestStatus.CLOSED
    
    @property
    def status(self):
        if self._status == MergeRequestStatus.CLOSED:
            return self._status

        if self._context["downvotes"]:
            return MergeRequestStatus.REJECTED
        elif len(self._context["upvotes"]) > 2:
            return MergeRequestStatus.APPROVED
        
        return AcceptanceThreshold(self._context).status()
    
    def _cannot_vote_if_closed(self):
        if self._status == MergeRequestStatus.CLOSED:
            raise MergeRequestException("can't vote on a closed merge request")
    
    def upvote(self, by_user):
        self._context["downvotes"].discard(by_user)
        self._context["upvotes"].add(by_user)
    
    def downvote(self, by_user):
        self._context["upvotes"].discard(by_user)
        self._context["downvotes"].add(by_user)
    
    def evaluate_merge_request(upvote_count, downvote_count):
        if downvote_count > 0:
            return MergeRequestStatus.REJECTED
        if upvote_count >= 2:
            return MergeRequestStatus.APPROVED
        return MergeRequestStatus.PENDING