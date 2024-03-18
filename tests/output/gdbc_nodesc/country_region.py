from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .scalars import ID

if TYPE_CHECKING:
    from .country import Country
    from .gql_types import RegionPopulatedPlacesConnection


@dataclass(kw_only=True)
class CountryRegion:
    fips_code: Optional[ID] = None
    iso_code: ID
    wiki_data_id: Optional[ID] = None
    name: str
    capital: Optional[str] = None
    country: Country
    num_populated_places: int
    populated_places: Optional[RegionPopulatedPlacesConnection] = None
