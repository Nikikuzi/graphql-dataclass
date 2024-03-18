from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import ReactionContent
from .scalars import DateTime

if TYPE_CHECKING:
    from .reactable import Reactable
    from .gql_types import ReactorConnection


@dataclass(kw_only=True)
class ReactionGroup:
    """
    ReactionGroup - A group of emoji reactions to a particular piece of content.

    content - Identifies the emoji reaction.

    createdAt - Identifies when the reaction was created.

    reactors - Reactors to the reaction subject with the emotion represented by this reaction group.

    subject - The subject that was reacted to.

    viewerHasReacted - Whether or not the authenticated user has left a reaction on the subject.

    """

    content: ReactionContent
    created_at: Optional[DateTime] = None
    reactors: ReactorConnection
    subject: Reactable
    viewer_has_reacted: bool
