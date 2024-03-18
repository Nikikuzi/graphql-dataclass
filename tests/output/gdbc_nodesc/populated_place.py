from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import PopulatedPlaceType
from .scalars import ID

if TYPE_CHECKING:
    from .country import Country
    from .country_region import CountryRegion
    from .gql_types import NearbyPopulatedPlacesConnection


@dataclass(kw_only=True)
class PopulatedPlace:
    id: ID
    wiki_data_id: Optional[ID] = None
    name: str
    place_type: PopulatedPlaceType
    elevation_meters: Optional[int] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    population: int
    timezone: str
    country: Country
    region: Optional[CountryRegion] = None
    distance: Optional[float] = None
    located_in: Optional["PopulatedPlace"] = None
    nearby_populated_places: Optional[NearbyPopulatedPlacesConnection] = None
    deleted: bool
