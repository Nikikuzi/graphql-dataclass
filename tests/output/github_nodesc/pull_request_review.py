from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import (
    CommentAuthorAssociation,
    CommentCannotUpdateReason,
    PullRequestReviewState,
)
from .gql_simple_types import Actor
from .scalars import HTML, ID, URI, BigInt, DateTime

if TYPE_CHECKING:
    from .pull_request import PullRequest
    from .repository import Repository
    from .reaction_group import ReactionGroup
    from .commit import Commit
    from .gql_types import TeamConnection
    from .gql_types import ReactionConnection
    from .gql_types import UserContentEditConnection
    from .gql_types import PullRequestReviewCommentConnection


@dataclass(kw_only=True)
class PullRequestReview:
    author: Optional[Actor] = None
    author_association: CommentAuthorAssociation
    author_can_push_to_repository: bool
    body: str
    body_h_t_m_l: HTML
    body_text: str
    comments: PullRequestReviewCommentConnection
    commit: Optional[Commit] = None
    created_at: DateTime
    created_via_email: bool
    editor: Optional[Actor] = None
    full_database_id: Optional[BigInt] = None
    id: ID
    includes_created_edit: bool
    is_minimized: bool
    last_edited_at: Optional[DateTime] = None
    minimized_reason: Optional[str] = None
    on_behalf_of: TeamConnection
    published_at: Optional[DateTime] = None
    pull_request: PullRequest
    reaction_groups: Optional[list[ReactionGroup]] = None
    reactions: ReactionConnection
    repository: Repository
    resource_path: URI
    state: PullRequestReviewState
    submitted_at: Optional[DateTime] = None
    updated_at: DateTime
    url: URI
    user_content_edits: Optional[UserContentEditConnection] = None
    viewer_can_delete: bool
    viewer_can_minimize: bool
    viewer_can_react: bool
    viewer_can_update: bool
    viewer_cannot_update_reasons: list[CommentCannotUpdateReason]
    viewer_did_author: bool
