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
    """
        PullRequestReview - A review object for a given pull request.

        author - The actor who authored the comment.

        authorAssociation - Author's association with the subject of the comment.

        authorCanPushToRepository - Indicates whether the author of this review has push access to the repository.

        body - Identifies the pull request review body.

        bodyHTML - The body rendered to HTML.

        bodyText - The body of this review rendered as plain text.

        comments - A list of review comments for the current pull request review.

        commit - Identifies the commit associated with this pull request review.

        createdAt - Identifies the date and time when the object was created.

        createdViaEmail - Check if this comment was created via an email reply.

        editor - The actor who edited the comment.

        fullDatabaseId - Identifies the primary key from the database as a BigInt.

        id - The Node ID of the PullRequestReview object

        includesCreatedEdit - Check if this comment was edited and includes an edit with the creation data

        isMinimized - Returns whether or not a comment has been minimized.

        lastEditedAt - The moment the editor made the last edit

        minimizedReason - Returns why the comment was minimized. One of `abuse`, `off-topic`,
    `outdated`, `resolved`, `duplicate` and `spam`. Note that the case and
    formatting of these values differs from the inputs to the `MinimizeComment` mutation.

        onBehalfOf - A list of teams that this review was made on behalf of.

        publishedAt - Identifies when the comment was published at.

        pullRequest - Identifies the pull request associated with this pull request review.

        reactionGroups - A list of reactions grouped by content left on the subject.

        reactions - A list of Reactions left on the Issue.

        repository - The repository associated with this node.

        resourcePath - The HTTP path permalink for this PullRequestReview.

        state - Identifies the current state of the pull request review.

        submittedAt - Identifies when the Pull Request Review was submitted

        updatedAt - Identifies the date and time when the object was last updated.

        url - The HTTP URL permalink for this PullRequestReview.

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
