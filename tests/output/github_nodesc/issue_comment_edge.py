from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .issue_comment import IssueComment


@dataclass(kw_only=True)
class IssueCommentEdge:
    cursor: str
    node: Optional[IssueComment] = None
