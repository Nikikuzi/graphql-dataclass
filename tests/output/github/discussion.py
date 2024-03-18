from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import (
    CommentAuthorAssociation,
    DiscussionStateReason,
    LockReason,
    SubscriptionState,
)
from .gql_simple_types import Actor
from .scalars import HTML, ID, URI, DateTime

if TYPE_CHECKING:
    from .repository import Repository
    from .reaction_group import ReactionGroup
    from .discussion_comment import DiscussionComment
    from .discussion_poll import DiscussionPoll
    from .gql_types import ReactionConnection
    from .gql_types import UserContentEditConnection
    from .gql_types import LabelConnection
    from .gql_types import DiscussionCommentConnection
    from .gql_types import DiscussionCategory


@dataclass(kw_only=True)
class Discussion:
    """
    Discussion - A discussion in a repository.

    activeLockReason - Reason that the conversation was locked.

    answer - The comment chosen as this discussion's answer, if any.

    answerChosenAt - The time when a user chose this discussion's answer, if answered.

    answerChosenBy - The user who chose this discussion's answer, if answered.

    author - The actor who authored the comment.

    authorAssociation - Author's association with the subject of the comment.

    body - The main text of the discussion post.

    bodyHTML - The body rendered to HTML.

    bodyText - The body rendered to text.

    category - The category for this discussion.

    closed - Indicates if the object is closed (definition of closed may depend on type)

    closedAt - Identifies the date and time when the object was closed.

    comments - The replies to the discussion.

    createdAt - Identifies the date and time when the object was created.

    createdViaEmail - Check if this comment was created via an email reply.

    databaseId - Identifies the primary key from the database.

    editor - The actor who edited the comment.

    id - The Node ID of the Discussion object

    includesCreatedEdit - Check if this comment was edited and includes an edit with the creation data

    isAnswered - Only return answered/unanswered discussions

    labels - A list of labels associated with the object.

    lastEditedAt - The moment the editor made the last edit

    locked - `true` if the object is locked

    number - The number identifying this discussion within the repository.

    poll - The poll associated with this discussion, if one exists.

    publishedAt - Identifies when the comment was published at.

    reactionGroups - A list of reactions grouped by content left on the subject.

    reactions - A list of Reactions left on the Issue.

    repository - The repository associated with this node.

    resourcePath - The path for this discussion.

    stateReason - Identifies the reason for the discussion's state.

    title - The title of this discussion.

    updatedAt - Identifies the date and time when the object was last updated.

    upvoteCount - Number of upvotes that this subject has received.

    url - The URL for this discussion.

    userContentEdits - A list of edits to this content.

    viewerCanClose - Indicates if the object can be closed by the viewer.

    viewerCanDelete - Check if the current viewer can delete this object.

    viewerCanReact - Can user react to this subject

    viewerCanReopen - Indicates if the object can be reopened by the viewer.

    viewerCanSubscribe - Check if the viewer is able to change their subscription status for the repository.

    viewerCanUpdate - Check if the current viewer can update this object.

    viewerCanUpvote - Whether or not the current user can add or remove an upvote on this subject.

    viewerDidAuthor - Did the viewer author this comment.

    viewerHasUpvoted - Whether or not the current user has already upvoted this subject.

    viewerSubscription - Identifies if the viewer is watching, not watching, or ignoring the subscribable entity.

    """

    active_lock_reason: Optional[LockReason] = None
    answer: Optional[DiscussionComment] = None
    answer_chosen_at: Optional[DateTime] = None
    answer_chosen_by: Optional[Actor] = None
    author: Optional[Actor] = None
    author_association: CommentAuthorAssociation
    body: str
    body_h_t_m_l: HTML
    body_text: str
    category: DiscussionCategory
    closed: bool
    closed_at: Optional[DateTime] = None
    comments: DiscussionCommentConnection
    created_at: DateTime
    created_via_email: bool
    database_id: Optional[int] = None
    editor: Optional[Actor] = None
    id: ID
    includes_created_edit: bool
    is_answered: Optional[bool] = None
    labels: Optional[LabelConnection] = None
    last_edited_at: Optional[DateTime] = None
    locked: bool
    number: int
    poll: Optional[DiscussionPoll] = None
    published_at: Optional[DateTime] = None
    reaction_groups: Optional[list[ReactionGroup]] = None
    reactions: ReactionConnection
    repository: Repository
    resource_path: URI
    state_reason: Optional[DiscussionStateReason] = None
    title: str
    updated_at: DateTime
    upvote_count: int
    url: URI
    user_content_edits: Optional[UserContentEditConnection] = None
    viewer_can_close: bool
    viewer_can_delete: bool
    viewer_can_react: bool
    viewer_can_reopen: bool
    viewer_can_subscribe: bool
    viewer_can_update: bool
    viewer_can_upvote: bool
    viewer_did_author: bool
    viewer_has_upvoted: bool
    viewer_subscription: Optional[SubscriptionState] = None
