from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import (
    CommentAuthorAssociation,
    CommentCannotUpdateReason,
    IssueState,
    IssueStateReason,
    LockReason,
    SubscriptionState,
    ThreadSubscriptionFormAction,
    ThreadSubscriptionState,
)
from .gql_simple_types import Actor
from .scalars import HTML, ID, URI, BigInt, DateTime

if TYPE_CHECKING:
    from .user_connection import UserConnection
    from .repository import Repository
    from .reaction_group import ReactionGroup
    from .project_v2 import ProjectV2
    from .project_v2_item_connection import ProjectV2ItemConnection
    from .gql_types import ReactionConnection
    from .gql_types import UserContentEditConnection
    from .gql_types import ProjectV2Connection
    from .gql_types import IssueConnection
    from .gql_types import LabelConnection
    from .gql_types import Milestone
    from .gql_types import ProjectCardConnection
    from .gql_types import IssueCommentConnection
    from .gql_types import Hovercard
    from .gql_types import LinkedBranchConnection
    from .gql_types import IssueTimelineItemsConnection


@dataclass(kw_only=True)
class Issue:
    active_lock_reason: Optional[LockReason] = None
    assignees: UserConnection
    author: Optional[Actor] = None
    author_association: CommentAuthorAssociation
    body: str
    body_h_t_m_l: HTML
    body_resource_path: URI
    body_text: str
    body_url: URI
    closed: bool
    closed_at: Optional[DateTime] = None
    comments: IssueCommentConnection
    created_at: DateTime
    created_via_email: bool
    database_id: Optional[int] = None
    editor: Optional[Actor] = None
    full_database_id: Optional[BigInt] = None
    hovercard: Hovercard
    id: ID
    includes_created_edit: bool
    is_pinned: Optional[bool] = None
    is_read_by_viewer: Optional[bool] = None
    labels: Optional[LabelConnection] = None
    last_edited_at: Optional[DateTime] = None
    linked_branches: LinkedBranchConnection
    locked: bool
    milestone: Optional[Milestone] = None
    number: int
    participants: UserConnection
    project_cards: ProjectCardConnection
    project_items: ProjectV2ItemConnection
    project_v2: Optional[ProjectV2] = None
    projects_v2: ProjectV2Connection
    published_at: Optional[DateTime] = None
    reaction_groups: Optional[list[ReactionGroup]] = None
    reactions: ReactionConnection
    repository: Repository
    resource_path: URI
    state: IssueState
    state_reason: Optional[IssueStateReason] = None
    timeline_items: IssueTimelineItemsConnection
    title: str
    title_h_t_m_l: str
    tracked_in_issues: IssueConnection
    tracked_issues: IssueConnection
    tracked_issues_count: int
    updated_at: DateTime
    url: URI
    user_content_edits: Optional[UserContentEditConnection] = None
    viewer_can_close: bool
    viewer_can_delete: bool
    viewer_can_react: bool
    viewer_can_reopen: bool
    viewer_can_subscribe: bool
    viewer_can_update: bool
    viewer_cannot_update_reasons: list[CommentCannotUpdateReason]
    viewer_did_author: bool
    viewer_subscription: Optional[SubscriptionState] = None
    viewer_thread_subscription_form_action: Optional[
        ThreadSubscriptionFormAction
    ] = None
    viewer_thread_subscription_status: Optional[ThreadSubscriptionState] = None
