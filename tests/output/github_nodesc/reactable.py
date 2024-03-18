from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .scalars import ID

if TYPE_CHECKING:
    from .reaction_group import ReactionGroup
    from .gql_types import ReactionConnection


@dataclass(kw_only=True)
class Reactable:
    database_id: Optional[int] = None
    id: ID
    reaction_groups: Optional[list[ReactionGroup]] = None
    reactions: ReactionConnection
    viewer_can_react: bool
