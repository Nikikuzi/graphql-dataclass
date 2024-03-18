from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .project_v2_item import ProjectV2Item
    from .gql_types import PageInfo
    from .gql_types import ProjectV2ItemEdge


@dataclass(kw_only=True)
class ProjectV2ItemConnection:
    edges: Optional[list[ProjectV2ItemEdge]] = None
    nodes: Optional[list[ProjectV2Item]] = None
    page_info: PageInfo
    total_count: int
