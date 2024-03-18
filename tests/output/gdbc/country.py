from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .scalars import ID

if TYPE_CHECKING:
    from .country_region import CountryRegion
    from .gql_types import CountryRegionsConnection


@dataclass(kw_only=True)
class Country:
    """
    Country - A country

    code - The ISO-3166 country code

    callingCode - The country dialing prefix

    wikiDataId - The country WikiData id

    capital - The country's capital city

    name - The country name

    currencyCodes - A list of supported ISO-4217 currency codes

    flagImageUri - The country flag image

    numRegions - The number of regions in this country

    region - Look up a region in this country

    regions - Find regions in this country

    """

    code: ID
    calling_code: str
    wiki_data_id: ID
    capital: Optional[str] = None
    name: str
    currency_codes: list[str]
    flag_image_uri: str
    num_regions: int
    region: Optional[CountryRegion] = None
    regions: Optional[CountryRegionsConnection] = None
