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
    """
        PopulatedPlace - A place with some population of inhabitants

        id - The place native id

        wikiDataId - The place WikiData id

        name - The place name

        placeType - The place type

        elevationMeters - The place elevation (meters) above sea level

        latitude - The place latittude (-90.0 to 90.0)

        longitude - The place longitude (-180.0 to 180.0)

        population - The place population

        timezone - The place timezone id

        country - The place's country

        region - The place's region

        distance - The distance result from some location-based query
    This field has two forms:
    - As a property (e.g., place.distance), returns the distance as part of a query returning places sorted by distance.
    - As a function (e.g., place.distance(toPlaceId), returns the distance to the specified place.

        locatedIn - The place containing this place, if any

        nearbyPopulatedPlaces - Find nearby populated places

        deleted - If this place has been marked deleted

    """

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
