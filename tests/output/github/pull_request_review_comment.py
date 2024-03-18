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
    """
        PullRequestReviewComment - A review comment associated with a given repository pull request.

        author - The actor who authored the comment.

        authorAssociation - Author's association with the subject of the comment.

        body - The comment body of this review comment.

        bodyHTML - The body rendered to HTML.

        bodyText - The comment body of this review comment rendered as plain text.

        commit - Identifies the commit associated with the comment.

        createdAt - Identifies when the comment was created.

        createdViaEmail - Check if this comment was created via an email reply.

        diffHunk - The diff hunk to which the comment applies.

        draftedAt - Identifies when the comment was created in a draft state.

        editor - The actor who edited the comment.

        fullDatabaseId - Identifies the primary key from the database as a BigInt.

        id - The Node ID of the PullRequestReviewComment object

        includesCreatedEdit - Check if this comment was edited and includes an edit with the creation data

        isMinimized - Returns whether or not a comment has been minimized.

        lastEditedAt - The moment the editor made the last edit

        line - The end line number on the file to which the comment applies

        minimizedReason - Returns why the comment was minimized. One of `abuse`, `off-topic`,
    `outdated`, `resolved`, `duplicate` and `spam`. Note that the case and
    formatting of these values differs from the inputs to the `MinimizeComment` mutation.

        originalCommit - Identifies the original commit associated with the comment.

        originalLine - The end line number on the file to which the comment applied when it was first created

        originalStartLine - The start line number on the file to which the comment applied when it was first created

        outdated - Identifies when the comment body is outdated

        path - The path to which the comment applies.

        publishedAt - Identifies when the comment was published at.

        pullRequest - The pull request associated with this review comment.

        pullRequestReview - The pull request review associated with this review comment.

        reactionGroups - A list of reactions grouped by content left on the subject.

        reactions - A list of Reactions left on the Issue.

        replyTo - The comment this is a reply to.

        repository - The repository associated with this node.

        resourcePath - The HTTP path permalink for this review comment.

        startLine - The start line number on the file to which the comment applies

        state - Identifies the state of the comment.

        subjectType - The level at which the comments in the corresponding thread are targeted, can be a diff line or a file

        updatedAt - Identifies when the comment was last updated.

        url - The HTTP URL permalink for this review comment.

        userContentEdits - A list of edits to this content.

        viewerCanDelete - Check if the current viewer can delete this object.

        viewerCanMinimize - Check if the current viewer can minimize this object.

        viewerCanReact - Can user react to this subject

        viewerCanUpdate - Check if the current viewer can update this object.

        viewerCannotUpdateReasons - Reasons why the current viewer can not update this comment.

        viewerDidAuthor - Did the viewer author this comment.

    """

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
