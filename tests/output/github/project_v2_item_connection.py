from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .project_v2_item import ProjectV2Item
    from .gql_types import PageInfo
    from .gql_types import ProjectV2ItemEdge


@dataclass(kw_only=True)
class ProjectV2ItemConnection:
    """
    ProjectV2ItemConnection - The connection type for ProjectV2Item.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[ProjectV2ItemEdge]] = None
    nodes: Optional[list[ProjectV2Item]] = None
    page_info: PageInfo
    total_count: int
