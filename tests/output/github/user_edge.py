from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .user import User


@dataclass(kw_only=True)
class UserEdge:
    """
    UserEdge - Represents a user.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[User] = None
