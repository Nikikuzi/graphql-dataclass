from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .scalars import ID

if TYPE_CHECKING:
    from .discussion import Discussion
    from .gql_types import DiscussionPollOptionConnection


@dataclass(kw_only=True)
class DiscussionPoll:
    discussion: Optional[Discussion] = None
    id: ID
    options: Optional[DiscussionPollOptionConnection] = None
    question: str
    total_vote_count: int
    viewer_can_vote: bool
    viewer_has_voted: bool
