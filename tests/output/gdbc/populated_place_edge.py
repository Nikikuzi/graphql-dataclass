from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .populated_place import PopulatedPlace


@dataclass(kw_only=True)
class PopulatedPlaceEdge:
    """
    PopulatedPlaceEdge - When paging populated places, wraps a place node together with the cursor referencing its position in the results

    cursor - The cursor id referencing the position of this node in the results

    node - The node value

    """

    cursor: str
    node: PopulatedPlace
