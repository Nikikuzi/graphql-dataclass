from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .user import User
    from .user_edge import UserEdge
    from .gql_types import PageInfo


@dataclass(kw_only=True)
class UserConnection:
    edges: Optional[list[UserEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int
