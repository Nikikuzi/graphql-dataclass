from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .pull_request import PullRequest
    from .gql_types import PageInfo
    from .gql_types import PullRequestEdge


@dataclass(kw_only=True)
class PullRequestConnection:
    """
    PullRequestConnection - The connection type for PullRequest.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[PullRequestEdge]] = None
    nodes: Optional[list[PullRequest]] = None
    page_info: PageInfo
    total_count: int
