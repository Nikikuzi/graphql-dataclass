from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .gql_types import PageInfo
    from .gql_types import SponsorAndLifetimeValue
    from .gql_types import SponsorAndLifetimeValueEdge


@dataclass(kw_only=True)
class SponsorAndLifetimeValueConnection:
    edges: Optional[list[SponsorAndLifetimeValueEdge]] = None
    nodes: Optional[list[SponsorAndLifetimeValue]] = None
    page_info: PageInfo
    total_count: int
