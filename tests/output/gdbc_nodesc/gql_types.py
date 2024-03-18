from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from .gql_simple_types import ConnectionPageInfo
from .scalars import ID

if TYPE_CHECKING:
    from .country import Country
    from .country_region import CountryRegion
    from .populated_place_edge import PopulatedPlaceEdge


@dataclass(kw_only=True)
class Currency:
    country_codes: list[ID]
    code: ID
    symbol: str


@dataclass(kw_only=True)
class Locale:
    code: ID
    name: str


@dataclass(kw_only=True)
class TimeZone:
    id: ID
    name: str
    raw_utc_offset_hours: int
    date_time: str
    time: str


@dataclass(kw_only=True)
class NearbyPopulatedPlacesConnection:
    total_count: int
    edges: list[PopulatedPlaceEdge]
    page_info: ConnectionPageInfo


@dataclass(kw_only=True)
class RegionPopulatedPlacesConnection:
    total_count: int
    edges: list[PopulatedPlaceEdge]
    page_info: ConnectionPageInfo


@dataclass(kw_only=True)
class CountryRegionEdge:
    cursor: str
    node: CountryRegion


@dataclass(kw_only=True)
class CountryRegionsConnection:
    total_count: int
    edges: list[CountryRegionEdge]
    page_info: ConnectionPageInfo


@dataclass(kw_only=True)
class CountryEdge:
    cursor: str
    node: Country


@dataclass(kw_only=True)
class CountriesConnection:
    total_count: int
    edges: list[CountryEdge]
    page_info: ConnectionPageInfo


@dataclass(kw_only=True)
class CurrencyEdge:
    cursor: str
    node: Currency


@dataclass(kw_only=True)
class CurrenciesConnection:
    total_count: int
    edges: list[CurrencyEdge]
    page_info: ConnectionPageInfo


@dataclass(kw_only=True)
class LocaleEdge:
    cursor: str
    node: Locale


@dataclass(kw_only=True)
class LocalesConnection:
    total_count: int
    edges: list[LocaleEdge]
    page_info: ConnectionPageInfo


@dataclass(kw_only=True)
class PopulatedPlacesConnection:
    total_count: int
    edges: list[PopulatedPlaceEdge]
    page_info: ConnectionPageInfo


@dataclass(kw_only=True)
class TimeZoneEdge:
    cursor: str
    node: TimeZone


@dataclass(kw_only=True)
class TimeZonesConnection:
    total_count: int
    edges: list[TimeZoneEdge]
    page_info: ConnectionPageInfo
