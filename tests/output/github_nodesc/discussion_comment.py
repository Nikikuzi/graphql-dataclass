from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import CommentAuthorAssociation, CommentCannotUpdateReason
from .gql_simple_types import Actor
from .scalars import HTML, ID, URI, DateTime

if TYPE_CHECKING:
    from .reaction_group import ReactionGroup
    from .discussion import Discussion
    from .gql_types import ReactionConnection
    from .gql_types import UserContentEditConnection
    from .gql_types import DiscussionCommentConnection


@dataclass(kw_only=True)
class DiscussionComment:
    author: Optional[Actor] = None
    author_association: CommentAuthorAssociation
    body: str
    body_h_t_m_l: HTML
    body_text: str
    created_at: DateTime
    created_via_email: bool
    database_id: Optional[int] = None
    deleted_at: Optional[DateTime] = None
    discussion: Optional[Discussion] = None
    editor: Optional[Actor] = None
    id: ID
    includes_created_edit: bool
    is_answer: bool
    is_minimized: bool
    last_edited_at: Optional[DateTime] = None
    minimized_reason: Optional[str] = None
    published_at: Optional[DateTime] = None
    reaction_groups: Optional[list[ReactionGroup]] = None
    reactions: ReactionConnection
    replies: DiscussionCommentConnection
    reply_to: Optional["DiscussionComment"] = None
    resource_path: URI
    updated_at: DateTime
    upvote_count: int
    url: URI
    user_content_edits: Optional[UserContentEditConnection] = None
    viewer_can_delete: bool
    viewer_can_mark_as_answer: bool
    viewer_can_minimize: bool
    viewer_can_react: bool
    viewer_can_unmark_as_answer: bool
    viewer_can_update: bool
    viewer_can_upvote: bool
    viewer_cannot_update_reasons: list[CommentCannotUpdateReason]
    viewer_did_author: bool
    viewer_has_upvoted: bool
