from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import CommentAuthorAssociation, CommentCannotUpdateReason
from .gql_simple_types import Actor
from .scalars import HTML, ID, URI, BigInt, DateTime

if TYPE_CHECKING:
    from .pull_request import PullRequest
    from .repository import Repository
    from .reaction_group import ReactionGroup
    from .issue import Issue
    from .gql_types import ReactionConnection
    from .gql_types import UserContentEditConnection


@dataclass(kw_only=True)
class IssueComment:
    author: Optional[Actor] = None
    author_association: CommentAuthorAssociation
    body: str
    body_h_t_m_l: HTML
    body_text: str
    created_at: DateTime
    created_via_email: bool
    database_id: Optional[int] = None
    editor: Optional[Actor] = None
    full_database_id: Optional[BigInt] = None
    id: ID
    includes_created_edit: bool
    is_minimized: bool
    issue: Issue
    last_edited_at: Optional[DateTime] = None
    minimized_reason: Optional[str] = None
    published_at: Optional[DateTime] = None
    pull_request: Optional[PullRequest] = None
    reaction_groups: Optional[list[ReactionGroup]] = None
    reactions: ReactionConnection
    repository: Repository
    resource_path: URI
    updated_at: DateTime
    url: URI
    user_content_edits: Optional[UserContentEditConnection] = None
    viewer_can_delete: bool
    viewer_can_minimize: bool
    viewer_can_react: bool
    viewer_can_update: bool
    viewer_cannot_update_reasons: list[CommentCannotUpdateReason]
    viewer_did_author: bool
