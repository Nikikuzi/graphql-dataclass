from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .issue_comment import IssueComment


@dataclass(kw_only=True)
class IssueCommentEdge:
    """
    IssueCommentEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[IssueComment] = None
