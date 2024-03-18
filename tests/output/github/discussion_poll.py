from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .scalars import ID

if TYPE_CHECKING:
    from .discussion import Discussion
    from .gql_types import DiscussionPollOptionConnection


@dataclass(kw_only=True)
class DiscussionPoll:
    """
    DiscussionPoll - A poll for a discussion.

    discussion - The discussion that this poll belongs to.

    id - The Node ID of the DiscussionPoll object

    options - The options for this poll.

    question - The question that is being asked by this poll.

    totalVoteCount - The total number of votes that have been cast for this poll.

    viewerCanVote - Indicates if the viewer has permission to vote in this poll.

    viewerHasVoted - Indicates if the viewer has voted for any option in this poll.

    """

    discussion: Optional[Discussion] = None
    id: ID
    options: Optional[DiscussionPollOptionConnection] = None
    question: str
    total_vote_count: int
    viewer_can_vote: bool
    viewer_has_voted: bool
