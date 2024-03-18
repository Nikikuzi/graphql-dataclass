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
    content: ReactionContent
    created_at: Optional[DateTime] = None
    reactors: ReactorConnection
    subject: Reactable
    viewer_has_reacted: bool
