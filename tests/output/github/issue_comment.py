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
    """
        IssueComment - Represents a comment on an Issue.

        author - The actor who authored the comment.

        authorAssociation - Author's association with the subject of the comment.

        body - The body as Markdown.

        bodyHTML - The body rendered to HTML.

        bodyText - The body rendered to text.

        createdAt - Identifies the date and time when the object was created.

        createdViaEmail - Check if this comment was created via an email reply.

        databaseId - Identifies the primary key from the database.

        editor - The actor who edited the comment.

        fullDatabaseId - Identifies the primary key from the database as a BigInt.

        id - The Node ID of the IssueComment object

        includesCreatedEdit - Check if this comment was edited and includes an edit with the creation data

        isMinimized - Returns whether or not a comment has been minimized.

        issue - Identifies the issue associated with the comment.

        lastEditedAt - The moment the editor made the last edit

        minimizedReason - Returns why the comment was minimized. One of `abuse`, `off-topic`,
    `outdated`, `resolved`, `duplicate` and `spam`. Note that the case and
    formatting of these values differs from the inputs to the `MinimizeComment` mutation.

        publishedAt - Identifies when the comment was published at.

        pullRequest - Returns the pull request associated with the comment, if this comment was made on a
    pull request.

        reactionGroups - A list of reactions grouped by content left on the subject.

        reactions - A list of Reactions left on the Issue.

        repository - The repository associated with this node.

        resourcePath - The HTTP path for this issue comment

        updatedAt - Identifies the date and time when the object was last updated.

        url - The HTTP URL for this issue comment

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
