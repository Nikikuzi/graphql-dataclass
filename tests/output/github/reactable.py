from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .scalars import ID

if TYPE_CHECKING:
    from .reaction_group import ReactionGroup
    from .gql_types import ReactionConnection


@dataclass(kw_only=True)
class Reactable:
    """
    Reactable - Represents a subject that can be reacted on.

    databaseId - Identifies the primary key from the database.

    id - The Node ID of the Reactable object

    reactionGroups - A list of reactions grouped by content left on the subject.

    reactions - A list of Reactions left on the Issue.

    viewerCanReact - Can user react to this subject

    """

    database_id: Optional[int] = None
    id: ID
    reaction_groups: Optional[list[ReactionGroup]] = None
    reactions: ReactionConnection
    viewer_can_react: bool
