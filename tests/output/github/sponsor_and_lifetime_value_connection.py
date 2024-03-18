from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .gql_types import PageInfo
    from .gql_types import SponsorAndLifetimeValue
    from .gql_types import SponsorAndLifetimeValueEdge


@dataclass(kw_only=True)
class SponsorAndLifetimeValueConnection:
    """
    SponsorAndLifetimeValueConnection - The connection type for SponsorAndLifetimeValue.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[SponsorAndLifetimeValueEdge]] = None
    nodes: Optional[list[SponsorAndLifetimeValue]] = None
    page_info: PageInfo
    total_count: int
