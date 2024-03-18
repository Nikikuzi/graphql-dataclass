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
    """
        PullRequest - A repository pull request.

        activeLockReason - Reason that the conversation was locked.

        additions - The number of additions in this pull request.

        assignees - A list of Users assigned to this object.

        author - The actor who authored the comment.

        authorAssociation - Author's association with the subject of the comment.

        autoMergeRequest - Returns the auto-merge request object if one exists for this pull request.

        baseRef - Identifies the base Ref associated with the pull request.

        baseRefName - Identifies the name of the base Ref associated with the pull request, even if the ref has been deleted.

        baseRefOid - Identifies the oid of the base ref associated with the pull request, even if the ref has been deleted.

        baseRepository - The repository associated with this pull request's base Ref.

        body - The body as Markdown.

        bodyHTML - The body rendered to HTML.

        bodyText - The body rendered to text.

        canBeRebased - Whether or not the pull request is rebaseable.

        changedFiles - The number of changed files in this pull request.

        checksResourcePath - The HTTP path for the checks of this pull request.

        checksUrl - The HTTP URL for the checks of this pull request.

        closed - `true` if the pull request is closed

        closedAt - Identifies the date and time when the object was closed.

        closingIssuesReferences - List of issues that were may be closed by this pull request

        comments - A list of comments associated with the pull request.

        commits - A list of commits present in this pull request's head branch not present in the base branch.

        createdAt - Identifies the date and time when the object was created.

        createdViaEmail - Check if this comment was created via an email reply.

        deletions - The number of deletions in this pull request.

        editor - The actor who edited this pull request's body.

        files - Lists the files changed within this pull request.

        fullDatabaseId - Identifies the primary key from the database as a BigInt.

        headRef - Identifies the head Ref associated with the pull request.

        headRefName - Identifies the name of the head Ref associated with the pull request, even if the ref has been deleted.

        headRefOid - Identifies the oid of the head ref associated with the pull request, even if the ref has been deleted.

        headRepository - The repository associated with this pull request's head Ref.

        headRepositoryOwner - The owner of the repository associated with this pull request's head Ref.

        hovercard - The hovercard information for this issue

        id - The Node ID of the PullRequest object

        includesCreatedEdit - Check if this comment was edited and includes an edit with the creation data

        isCrossRepository - The head and base repositories are different.

        isDraft - Identifies if the pull request is a draft.

        isInMergeQueue - Indicates whether the pull request is in a merge queue

        isMergeQueueEnabled - Indicates whether the pull request's base ref has a merge queue enabled.

        isReadByViewer - Is this pull request read by the viewer

        labels - A list of labels associated with the object.

        lastEditedAt - The moment the editor made the last edit

        latestOpinionatedReviews - A list of latest reviews per user associated with the pull request.

        latestReviews - A list of latest reviews per user associated with the pull request that are not also pending review.

        locked - `true` if the pull request is locked

        maintainerCanModify - Indicates whether maintainers can modify the pull request.

        mergeCommit - The commit that was created when this pull request was merged.

        mergeQueue - The merge queue for the pull request's base branch

        mergeQueueEntry - The merge queue entry of the pull request in the base branch's merge queue

        mergeStateStatus - Detailed information about the current pull request merge state status.

        mergeable - Whether or not the pull request can be merged based on the existence of merge conflicts.

        merged - Whether or not the pull request was merged.

        mergedAt - The date and time that the pull request was merged.

        mergedBy - The actor who merged the pull request.

        milestone - Identifies the milestone associated with the pull request.

        number - Identifies the pull request number.

        participants - A list of Users that are participating in the Pull Request conversation.

        permalink - The permalink to the pull request.

        potentialMergeCommit - The commit that GitHub automatically generated to test if this pull request
    could be merged. This field will not return a value if the pull request is
    merged, or if the test merge commit is still being generated. See the
    `mergeable` field for more details on the mergeability of the pull request.

        projectCards - List of project cards associated with this pull request.

        projectItems - List of project items associated with this pull request.

        projectV2 - Find a project by number.

        projectsV2 - A list of projects under the owner.

        publishedAt - Identifies when the comment was published at.

        reactionGroups - A list of reactions grouped by content left on the subject.

        reactions - A list of Reactions left on the Issue.

        repository - The repository associated with this node.

        resourcePath - The HTTP path for this pull request.

        revertResourcePath - The HTTP path for reverting this pull request.

        revertUrl - The HTTP URL for reverting this pull request.

        reviewDecision - The current status of this pull request with respect to code review.

        reviewRequests - A list of review requests associated with the pull request.

        reviewThreads - The list of all review threads for this pull request.

        reviews - A list of reviews associated with the pull request.

        state - Identifies the state of the pull request.

        suggestedReviewers - A list of reviewer suggestions based on commit history and past review comments.

        timelineItems - A list of events, comments, commits, etc. associated with the pull request.

        title - Identifies the pull request title.

        titleHTML - Identifies the pull request title rendered to HTML.

        totalCommentsCount - Returns a count of how many comments this pull request has received.

        updatedAt - Identifies the date and time when the object was last updated.

        url - The HTTP URL for this pull request.

        userContentEdits - A list of edits to this content.

        viewerCanApplySuggestion - Whether or not the viewer can apply suggestion.

        viewerCanClose - Indicates if the object can be closed by the viewer.

        viewerCanDeleteHeadRef - Check if the viewer can restore the deleted head ref.

        viewerCanDisableAutoMerge - Whether or not the viewer can disable auto-merge

        viewerCanEditFiles - Can the viewer edit files within this pull request.

        viewerCanEnableAutoMerge - Whether or not the viewer can enable auto-merge

        viewerCanMergeAsAdmin - Indicates whether the viewer can bypass branch protections and merge the pull request immediately

        viewerCanReact - Can user react to this subject

        viewerCanReopen - Indicates if the object can be reopened by the viewer.

        viewerCanSubscribe - Check if the viewer is able to change their subscription status for the repository.

        viewerCanUpdate - Check if the current viewer can update this object.

        viewerCanUpdateBranch - Whether or not the viewer can update the head ref of this PR, by merging or rebasing the base ref.
    If the head ref is up to date or unable to be updated by this user, this will return false.

        viewerCannotUpdateReasons - Reasons why the current viewer can not update this comment.

        viewerDidAuthor - Did the viewer author this comment.

        viewerLatestReview - The latest review given from the viewer.

        viewerLatestReviewRequest - The person who has requested the viewer for review on this pull request.

        viewerMergeBodyText - The merge body text for the viewer and method.

        viewerMergeHeadlineText - The merge headline text for the viewer and method.

        viewerSubscription - Identifies if the viewer is watching, not watching, or ignoring the subscribable entity.

    """

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
