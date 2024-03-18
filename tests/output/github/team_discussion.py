from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import CommentCannotUpdateReason, SubscriptionState
from .gql_simple_types import Actor
from .scalars import HTML, ID, DateTime

if TYPE_CHECKING:
    from .reaction_group import ReactionGroup
    from .gql_types import ReactionConnection
    from .gql_types import UserContentEditConnection


@dataclass(kw_only=True)
class TeamDiscussion:
    """
    TeamDiscussion - A team discussion.

    author - The actor who authored the comment.

    body - The body as Markdown.

    bodyHTML - The body rendered to HTML.

    bodyText - The body rendered to text.

    createdAt - Identifies the date and time when the object was created.

    createdViaEmail - Check if this comment was created via an email reply.

    databaseId - Identifies the primary key from the database.

    editor - The actor who edited the comment.

    id - The Node ID of the TeamDiscussion object

    includesCreatedEdit - Check if this comment was edited and includes an edit with the creation data

    lastEditedAt - The moment the editor made the last edit

    publishedAt - Identifies when the comment was published at.

    reactionGroups - A list of reactions grouped by content left on the subject.

    reactions - A list of Reactions left on the Issue.

    updatedAt - Identifies the date and time when the object was last updated.

    userContentEdits - A list of edits to this content.

    viewerCanDelete - Check if the current viewer can delete this object.

    viewerCanReact - Can user react to this subject

    viewerCanSubscribe - Check if the viewer is able to change their subscription status for the repository.

    viewerCanUpdate - Check if the current viewer can update this object.

    viewerCannotUpdateReasons - Reasons why the current viewer can not update this comment.

    viewerDidAuthor - Did the viewer author this comment.

    viewerSubscription - Identifies if the viewer is watching, not watching, or ignoring the subscribable entity.

    """

    author: Optional[Actor] = None
    body: str
    body_h_t_m_l: HTML
    body_text: str
    created_at: DateTime
    created_via_email: bool
    database_id: Optional[int] = None
    editor: Optional[Actor] = None
    id: ID
    includes_created_edit: bool
    last_edited_at: Optional[DateTime] = None
    published_at: Optional[DateTime] = None
    reaction_groups: Optional[list[ReactionGroup]] = None
    reactions: ReactionConnection
    updated_at: DateTime
    user_content_edits: Optional[UserContentEditConnection] = None
    viewer_can_delete: bool
    viewer_can_react: bool
    viewer_can_subscribe: bool
    viewer_can_update: bool
    viewer_cannot_update_reasons: list[CommentCannotUpdateReason]
    viewer_did_author: bool
    viewer_subscription: Optional[SubscriptionState] = None
