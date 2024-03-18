from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .scalars import ID

if TYPE_CHECKING:
    from .country_region import CountryRegion
    from .gql_types import CountryRegionsConnection


@dataclass(kw_only=True)
class Country:
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
