from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import (
    CommentAuthorAssociation,
    CommentCannotUpdateReason,
    LockReason,
    MergeableState,
    MergeStateStatus,
    PullRequestReviewDecision,
    PullRequestState,
    SubscriptionState,
)
from .gql_simple_types import Actor
from .scalars import HTML, ID, URI, BigInt, DateTime, GitObjectID

if TYPE_CHECKING:
    from .user_connection import UserConnection
    from .ref import Ref
    from .repository import Repository
    from .reaction_group import ReactionGroup
    from .project_v2 import ProjectV2
    from .project_v2_item_connection import ProjectV2ItemConnection
    from .commit import Commit
    from .merge_queue import MergeQueue
    from .pull_request_review import PullRequestReview
    from .gql_types import AutoMergeRequest
    from .gql_types import ReactionConnection
    from .gql_types import UserContentEditConnection
    from .gql_types import ProjectV2Connection
    from .gql_types import IssueConnection
    from .gql_types import LabelConnection
    from .gql_types import Milestone
    from .gql_types import MergeQueueEntry
    from .gql_types import RepositoryOwner
    from .gql_types import ProjectCardConnection
    from .gql_types import IssueCommentConnection
    from .gql_types import PullRequestCommitConnection
    from .gql_types import PullRequestChangedFileConnection
    from .gql_types import Hovercard
    from .gql_types import PullRequestReviewConnection
    from .gql_types import ReviewRequest
    from .gql_types import ReviewRequestConnection
    from .gql_types import PullRequestReviewThreadConnection
    from .gql_types import SuggestedReviewer
    from .gql_types import PullRequestTimelineItemsConnection


@dataclass(kw_only=True)
class PullRequest:
    active_lock_reason: Optional[LockReason] = None
    additions: int
    assignees: UserConnection
    author: Optional[Actor] = None
    author_association: CommentAuthorAssociation
    auto_merge_request: Optional[AutoMergeRequest] = None
    base_ref: Optional[Ref] = None
    base_ref_name: str
    base_ref_oid: GitObjectID
    base_repository: Optional[Repository] = None
    body: str
    body_h_t_m_l: HTML
    body_text: str
    can_be_rebased: bool
    changed_files: int
    checks_resource_path: URI
    checks_url: URI
    closed: bool
    closed_at: Optional[DateTime] = None
    closing_issues_references: Optional[IssueConnection] = None
    comments: IssueCommentConnection
    commits: PullRequestCommitConnection
    created_at: DateTime
    created_via_email: bool
    deletions: int
    editor: Optional[Actor] = None
    files: Optional[PullRequestChangedFileConnection] = None
    full_database_id: Optional[BigInt] = None
    head_ref: Optional[Ref] = None
    head_ref_name: str
    head_ref_oid: GitObjectID
    head_repository: Optional[Repository] = None
    head_repository_owner: Optional[RepositoryOwner] = None
    hovercard: Hovercard
    id: ID
    includes_created_edit: bool
    is_cross_repository: bool
    is_draft: bool
    is_in_merge_queue: bool
    is_merge_queue_enabled: bool
    is_read_by_viewer: Optional[bool] = None
    labels: Optional[LabelConnection] = None
    last_edited_at: Optional[DateTime] = None
    latest_opinionated_reviews: Optional[PullRequestReviewConnection] = None
    latest_reviews: Optional[PullRequestReviewConnection] = None
    locked: bool
    maintainer_can_modify: bool
    merge_commit: Optional[Commit] = None
    merge_queue: Optional[MergeQueue] = None
    merge_queue_entry: Optional[MergeQueueEntry] = None
    merge_state_status: MergeStateStatus
    mergeable: MergeableState
    merged: bool
    merged_at: Optional[DateTime] = None
    merged_by: Optional[Actor] = None
    milestone: Optional[Milestone] = None
    number: int
    participants: UserConnection
    permalink: URI
    potential_merge_commit: Optional[Commit] = None
    project_cards: ProjectCardConnection
    project_items: ProjectV2ItemConnection
    project_v2: Optional[ProjectV2] = None
    projects_v2: ProjectV2Connection
    published_at: Optional[DateTime] = None
    reaction_groups: Optional[list[ReactionGroup]] = None
    reactions: ReactionConnection
    repository: Repository
    resource_path: URI
    revert_resource_path: URI
    revert_url: URI
    review_decision: Optional[PullRequestReviewDecision] = None
    review_requests: Optional[ReviewRequestConnection] = None
    review_threads: PullRequestReviewThreadConnection
    reviews: Optional[PullRequestReviewConnection] = None
    state: PullRequestState
    suggested_reviewers: list[SuggestedReviewer]
    timeline_items: PullRequestTimelineItemsConnection
    title: str
    title_h_t_m_l: HTML
    total_comments_count: Optional[int] = None
    updated_at: DateTime
    url: URI
    user_content_edits: Optional[UserContentEditConnection] = None
    viewer_can_apply_suggestion: bool
    viewer_can_close: bool
    viewer_can_delete_head_ref: bool
    viewer_can_disable_auto_merge: bool
    viewer_can_edit_files: bool
    viewer_can_enable_auto_merge: bool
    viewer_can_merge_as_admin: bool
    viewer_can_react: bool
    viewer_can_reopen: bool
    viewer_can_subscribe: bool
    viewer_can_update: bool
    viewer_can_update_branch: bool
    viewer_cannot_update_reasons: list[CommentCannotUpdateReason]
    viewer_did_author: bool
    viewer_latest_review: Optional[PullRequestReview] = None
    viewer_latest_review_request: Optional[ReviewRequest] = None
    viewer_merge_body_text: str
    viewer_merge_headline_text: str
    viewer_subscription: Optional[SubscriptionState] = None
