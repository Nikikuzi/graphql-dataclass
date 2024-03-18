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
    """
    Issue - An Issue is a place to discuss ideas, enhancements, tasks, and bugs for a project.

    activeLockReason - Reason that the conversation was locked.

    assignees - A list of Users assigned to this object.

    author - The actor who authored the comment.

    authorAssociation - Author's association with the subject of the comment.

    body - Identifies the body of the issue.

    bodyHTML - The body rendered to HTML.

    bodyResourcePath - The http path for this issue body

    bodyText - Identifies the body of the issue rendered to text.

    bodyUrl - The http URL for this issue body

    closed - Indicates if the object is closed (definition of closed may depend on type)

    closedAt - Identifies the date and time when the object was closed.

    comments - A list of comments associated with the Issue.

    createdAt - Identifies the date and time when the object was created.

    createdViaEmail - Check if this comment was created via an email reply.

    databaseId - Identifies the primary key from the database.

    editor - The actor who edited the comment.

    fullDatabaseId - Identifies the primary key from the database as a BigInt.

    hovercard - The hovercard information for this issue

    id - The Node ID of the Issue object

    includesCreatedEdit - Check if this comment was edited and includes an edit with the creation data

    isPinned - Indicates whether or not this issue is currently pinned to the repository issues list

    isReadByViewer - Is this issue read by the viewer

    labels - A list of labels associated with the object.

    lastEditedAt - The moment the editor made the last edit

    linkedBranches - Branches linked to this issue.

    locked - `true` if the object is locked

    milestone - Identifies the milestone associated with the issue.

    number - Identifies the issue number.

    participants - A list of Users that are participating in the Issue conversation.

    projectCards - List of project cards associated with this issue.

    projectItems - List of project items associated with this issue.

    projectV2 - Find a project by number.

    projectsV2 - A list of projects under the owner.

    publishedAt - Identifies when the comment was published at.

    reactionGroups - A list of reactions grouped by content left on the subject.

    reactions - A list of Reactions left on the Issue.

    repository - The repository associated with this node.

    resourcePath - The HTTP path for this issue

    state - Identifies the state of the issue.

    stateReason - Identifies the reason for the issue state.

    timelineItems - A list of events, comments, commits, etc. associated with the issue.

    title - Identifies the issue title.

    titleHTML - Identifies the issue title rendered to HTML.

    trackedInIssues - A list of issues that track this issue

    trackedIssues - A list of issues tracked inside the current issue

    trackedIssuesCount - The number of tracked issues for this issue

    updatedAt - Identifies the date and time when the object was last updated.

    url - The HTTP URL for this issue

    userContentEdits - A list of edits to this content.

    viewerCanClose - Indicates if the object can be closed by the viewer.

    viewerCanDelete - Check if the current viewer can delete this object.

    viewerCanReact - Can user react to this subject

    viewerCanReopen - Indicates if the object can be reopened by the viewer.

    viewerCanSubscribe - Check if the viewer is able to change their subscription status for the repository.

    viewerCanUpdate - Check if the current viewer can update this object.

    viewerCannotUpdateReasons - Reasons why the current viewer can not update this comment.

    viewerDidAuthor - Did the viewer author this comment.

    viewerSubscription - Identifies if the viewer is watching, not watching, or ignoring the subscribable entity.

    viewerThreadSubscriptionFormAction - Identifies the viewer's thread subscription form action.

    viewerThreadSubscriptionStatus - Identifies the viewer's thread subscription status.

    """

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
