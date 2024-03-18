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
