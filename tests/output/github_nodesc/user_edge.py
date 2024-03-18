from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .user import User


@dataclass(kw_only=True)
class UserEdge:
    cursor: str
    node: Optional[User] = None
