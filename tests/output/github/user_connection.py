from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .user import User
    from .user_edge import UserEdge
    from .gql_types import PageInfo


@dataclass(kw_only=True)
class UserConnection:
    """
    UserConnection - A list of users.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[UserEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int
