from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import (
    CommentAuthorAssociation,
    CommentCannotUpdateReason,
    PullRequestReviewCommentState,
    PullRequestReviewThreadSubjectType,
)
from .gql_simple_types import Actor
from .scalars import HTML, ID, URI, BigInt, DateTime

if TYPE_CHECKING:
    from .pull_request import PullRequest
    from .repository import Repository
    from .reaction_group import ReactionGroup
    from .commit import Commit
    from .pull_request_review import PullRequestReview
    from .gql_types import ReactionConnection
    from .gql_types import UserContentEditConnection


@dataclass(kw_only=True)
class PullRequestReviewComment:
    author: Optional[Actor] = None
    author_association: CommentAuthorAssociation
    body: str
    body_h_t_m_l: HTML
    body_text: str
    commit: Optional[Commit] = None
    created_at: DateTime
    created_via_email: bool
    diff_hunk: str
    drafted_at: DateTime
    editor: Optional[Actor] = None
    full_database_id: Optional[BigInt] = None
    id: ID
    includes_created_edit: bool
    is_minimized: bool
    last_edited_at: Optional[DateTime] = None
    line: Optional[int] = None
    minimized_reason: Optional[str] = None
    original_commit: Optional[Commit] = None
    original_line: Optional[int] = None
    original_start_line: Optional[int] = None
    outdated: bool
    path: str
    published_at: Optional[DateTime] = None
    pull_request: PullRequest
    pull_request_review: Optional[PullRequestReview] = None
    reaction_groups: Optional[list[ReactionGroup]] = None
    reactions: ReactionConnection
    reply_to: Optional["PullRequestReviewComment"] = None
    repository: Repository
    resource_path: URI
    start_line: Optional[int] = None
    state: PullRequestReviewCommentState
    subject_type: PullRequestReviewThreadSubjectType
    updated_at: DateTime
    url: URI
    user_content_edits: Optional[UserContentEditConnection] = None
    viewer_can_delete: bool
    viewer_can_minimize: bool
    viewer_can_react: bool
    viewer_can_update: bool
    viewer_cannot_update_reasons: list[CommentCannotUpdateReason]
    viewer_did_author: bool
