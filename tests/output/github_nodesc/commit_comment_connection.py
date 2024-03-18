from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .gql_types import PageInfo
    from .gql_types import CommitComment
    from .gql_types import CommitCommentEdge


@dataclass(kw_only=True)
class CommitCommentConnection:
    edges: Optional[list[CommitCommentEdge]] = None
    nodes: Optional[list[CommitComment]] = None
    page_info: PageInfo
    total_count: int
