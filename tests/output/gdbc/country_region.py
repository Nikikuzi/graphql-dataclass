from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .scalars import ID

if TYPE_CHECKING:
    from .country import Country
    from .gql_types import RegionPopulatedPlacesConnection


@dataclass(kw_only=True)
class CountryRegion:
    """
    CountryRegion - A region in a country. This could be a state, province, district, or otherwise major political division.

    fipsCode - The region FIPS 10-4 code

    isoCode - The region ISO-3166 code

    wikiDataId - The region WikiData id

    name - The region name

    capital - The region's capital city

    country - The region's country

    numPopulatedPlaces - The number of populated places in this region

    populatedPlaces - Find populated places in this region

    """

    fips_code: Optional[ID] = None
    iso_code: ID
    wiki_data_id: Optional[ID] = None
    name: str
    capital: Optional[str] = None
    country: Country
    num_populated_places: int
    populated_places: Optional[RegionPopulatedPlacesConnection] = None
