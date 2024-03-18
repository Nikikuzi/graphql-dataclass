from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .gql_types import PageInfo
    from .gql_types import IpAllowListEntry
    from .gql_types import IpAllowListEntryEdge


@dataclass(kw_only=True)
class IpAllowListEntryConnection:
    """
    IpAllowListEntryConnection - The connection type for IpAllowListEntry.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[IpAllowListEntryEdge]] = None
    nodes: Optional[list[IpAllowListEntry]] = None
    page_info: PageInfo
    total_count: int
