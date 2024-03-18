from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .populated_place import PopulatedPlace


@dataclass(kw_only=True)
class PopulatedPlaceEdge:
    cursor: str
    node: PopulatedPlace
