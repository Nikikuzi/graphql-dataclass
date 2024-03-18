from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import CommentAuthorAssociation, CommentCannotUpdateReason
from .gql_simple_types import Actor
from .scalars import HTML, ID, URI, DateTime

if TYPE_CHECKING:
    from .reaction_group import ReactionGroup
    from .discussion import Discussion
    from .gql_types import ReactionConnection
    from .gql_types import UserContentEditConnection
    from .gql_types import DiscussionCommentConnection


@dataclass(kw_only=True)
class DiscussionComment:
    """
        DiscussionComment - A comment on a discussion.

        author - The actor who authored the comment.

        authorAssociation - Author's association with the subject of the comment.

        body - The body as Markdown.

        bodyHTML - The body rendered to HTML.

        bodyText - The body rendered to text.

        createdAt - Identifies the date and time when the object was created.

        createdViaEmail - Check if this comment was created via an email reply.

        databaseId - Identifies the primary key from the database.

        deletedAt - The time when this replied-to comment was deleted

        discussion - The discussion this comment was created in

        editor - The actor who edited the comment.

        id - The Node ID of the DiscussionComment object

        includesCreatedEdit - Check if this comment was edited and includes an edit with the creation data

        isAnswer - Has this comment been chosen as the answer of its discussion?

        isMinimized - Returns whether or not a comment has been minimized.

        lastEditedAt - The moment the editor made the last edit

        minimizedReason - Returns why the comment was minimized. One of `abuse`, `off-topic`,
    `outdated`, `resolved`, `duplicate` and `spam`. Note that the case and
    formatting of these values differs from the inputs to the `MinimizeComment` mutation.

        publishedAt - Identifies when the comment was published at.

        reactionGroups - A list of reactions grouped by content left on the subject.

        reactions - A list of Reactions left on the Issue.

        replies - The threaded replies to this comment.

        replyTo - The discussion comment this comment is a reply to

        resourcePath - The path for this discussion comment.

        updatedAt - Identifies the date and time when the object was last updated.

        upvoteCount - Number of upvotes that this subject has received.

        url - The URL for this discussion comment.

        userContentEdits - A list of edits to this content.

        viewerCanDelete - Check if the current viewer can delete this object.

        viewerCanMarkAsAnswer - Can the current user mark this comment as an answer?

        viewerCanMinimize - Check if the current viewer can minimize this object.

        viewerCanReact - Can user react to this subject

        viewerCanUnmarkAsAnswer - Can the current user unmark this comment as an answer?

        viewerCanUpdate - Check if the current viewer can update this object.

        viewerCanUpvote - Whether or not the current user can add or remove an upvote on this subject.

        viewerCannotUpdateReasons - Reasons why the current viewer can not update this comment.

        viewerDidAuthor - Did the viewer author this comment.

        viewerHasUpvoted - Whether or not the current user has already upvoted this subject.

    """

    author: Optional[Actor] = None
    author_association: CommentAuthorAssociation
    body: str
    body_h_t_m_l: HTML
    body_text: str
    created_at: DateTime
    created_via_email: bool
    database_id: Optional[int] = None
    deleted_at: Optional[DateTime] = None
    discussion: Optional[Discussion] = None
    editor: Optional[Actor] = None
    id: ID
    includes_created_edit: bool
    is_answer: bool
    is_minimized: bool
    last_edited_at: Optional[DateTime] = None
    minimized_reason: Optional[str] = None
    published_at: Optional[DateTime] = None
    reaction_groups: Optional[list[ReactionGroup]] = None
    reactions: ReactionConnection
    replies: DiscussionCommentConnection
    reply_to: Optional["DiscussionComment"] = None
    resource_path: URI
    updated_at: DateTime
    upvote_count: int
    url: URI
    user_content_edits: Optional[UserContentEditConnection] = None
    viewer_can_delete: bool
    viewer_can_mark_as_answer: bool
    viewer_can_minimize: bool
    viewer_can_react: bool
    viewer_can_unmark_as_answer: bool
    viewer_can_update: bool
    viewer_can_upvote: bool
    viewer_cannot_update_reasons: list[CommentCannotUpdateReason]
    viewer_did_author: bool
    viewer_has_upvoted: bool
