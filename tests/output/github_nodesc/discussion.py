from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import (
    CommentAuthorAssociation,
    DiscussionStateReason,
    LockReason,
    SubscriptionState,
)
from .gql_simple_types import Actor
from .scalars import HTML, ID, URI, DateTime

if TYPE_CHECKING:
    from .repository import Repository
    from .reaction_group import ReactionGroup
    from .discussion_comment import DiscussionComment
    from .discussion_poll import DiscussionPoll
    from .gql_types import ReactionConnection
    from .gql_types import UserContentEditConnection
    from .gql_types import LabelConnection
    from .gql_types import DiscussionCommentConnection
    from .gql_types import DiscussionCategory


@dataclass(kw_only=True)
class Discussion:
    active_lock_reason: Optional[LockReason] = None
    answer: Optional[DiscussionComment] = None
    answer_chosen_at: Optional[DateTime] = None
    answer_chosen_by: Optional[Actor] = None
    author: Optional[Actor] = None
    author_association: CommentAuthorAssociation
    body: str
    body_h_t_m_l: HTML
    body_text: str
    category: DiscussionCategory
    closed: bool
    closed_at: Optional[DateTime] = None
    comments: DiscussionCommentConnection
    created_at: DateTime
    created_via_email: bool
    database_id: Optional[int] = None
    editor: Optional[Actor] = None
    id: ID
    includes_created_edit: bool
    is_answered: Optional[bool] = None
    labels: Optional[LabelConnection] = None
    last_edited_at: Optional[DateTime] = None
    locked: bool
    number: int
    poll: Optional[DiscussionPoll] = None
    published_at: Optional[DateTime] = None
    reaction_groups: Optional[list[ReactionGroup]] = None
    reactions: ReactionConnection
    repository: Repository
    resource_path: URI
    state_reason: Optional[DiscussionStateReason] = None
    title: str
    updated_at: DateTime
    upvote_count: int
    url: URI
    user_content_edits: Optional[UserContentEditConnection] = None
    viewer_can_close: bool
    viewer_can_delete: bool
    viewer_can_react: bool
    viewer_can_reopen: bool
    viewer_can_subscribe: bool
    viewer_can_update: bool
    viewer_can_upvote: bool
    viewer_did_author: bool
    viewer_has_upvoted: bool
    viewer_subscription: Optional[SubscriptionState] = None
