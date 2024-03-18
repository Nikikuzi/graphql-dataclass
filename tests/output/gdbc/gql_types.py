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
    """
    Currency - A country currency

    """

    country_codes: list[ID]
    code: ID
    symbol: str


@dataclass(kw_only=True)
class Locale:
    """
    Locale - A regional locale representing some country/language combination

    """

    code: ID
    name: str


@dataclass(kw_only=True)
class TimeZone:
    """
    TimeZone - A time-zone

    """

    id: ID
    name: str
    raw_utc_offset_hours: int
    date_time: str
    time: str


@dataclass(kw_only=True)
class NearbyPopulatedPlacesConnection:
    """
    NearbyPopulatedPlacesConnection - A pageable view into nearby populated-place results

    totalCount - The total number of results

    edges - The edges in the current page of results

    pageInfo - Info about the current page of results

    """

    total_count: int
    edges: list[PopulatedPlaceEdge]
    page_info: ConnectionPageInfo


@dataclass(kw_only=True)
class RegionPopulatedPlacesConnection:
    """
    RegionPopulatedPlacesConnection - A pageable view into regional populated-place results

    totalCount - The total number of results

    edges - The edges in the current page of results

    pageInfo - Info about the current page of results

    """

    total_count: int
    edges: list[PopulatedPlaceEdge]
    page_info: ConnectionPageInfo


@dataclass(kw_only=True)
class CountryRegionEdge:
    """
    CountryRegionEdge - When paging regions, wraps a region node together with the cursor referencing its position in the results

    cursor - The cursor id referencing the position of this node in the results

    node - The node value

    """

    cursor: str
    node: CountryRegion


@dataclass(kw_only=True)
class CountryRegionsConnection:
    """
    CountryRegionsConnection - A pageable view into region results

    totalCount - The total number of results

    edges - The edges in the current page of results

    pageInfo - Info about the current page of results

    """

    total_count: int
    edges: list[CountryRegionEdge]
    page_info: ConnectionPageInfo


@dataclass(kw_only=True)
class CountryEdge:
    """
    CountryEdge - When paging countries, wraps a country node together with the cursor referencing its position in the results

    cursor - The cursor id referencing the position of this node in the results

    node - The node value

    """

    cursor: str
    node: Country


@dataclass(kw_only=True)
class CountriesConnection:
    """
    CountriesConnection - A pageable view into country results

    totalCount - The total number of results

    edges - The edges in the current page of results

    pageInfo - Info about the current page of results

    """

    total_count: int
    edges: list[CountryEdge]
    page_info: ConnectionPageInfo


@dataclass(kw_only=True)
class CurrencyEdge:
    """
    CurrencyEdge - When paging currencies, wraps a currency node together with the cursor referencing its position in the results

    cursor - The cursor id referencing the position of this node in the results

    node - The node value

    """

    cursor: str
    node: Currency


@dataclass(kw_only=True)
class CurrenciesConnection:
    """
    CurrenciesConnection - A pageable view into currency results

    totalCount - The total number of results

    edges - The edges in the current page of results

    pageInfo - Info about the current page of results

    """

    total_count: int
    edges: list[CurrencyEdge]
    page_info: ConnectionPageInfo


@dataclass(kw_only=True)
class LocaleEdge:
    """
    LocaleEdge - When paging locales, wraps a locale node together with the cursor referencing its position in the results

    cursor - The cursor id referencing the position of this node in the results

    node - The node value

    """

    cursor: str
    node: Locale


@dataclass(kw_only=True)
class LocalesConnection:
    """
    LocalesConnection - A pageable view into locale results

    totalCount - The total number of results

    edges - The edges in the current page of results

    pageInfo - Info about the current page of results

    """

    total_count: int
    edges: list[LocaleEdge]
    page_info: ConnectionPageInfo


@dataclass(kw_only=True)
class PopulatedPlacesConnection:
    """
    PopulatedPlacesConnection - A pageable view into populated-place results

    totalCount - The total number of results

    edges - The edges in the current page of results

    pageInfo - Info about the current page of results

    """

    total_count: int
    edges: list[PopulatedPlaceEdge]
    page_info: ConnectionPageInfo


@dataclass(kw_only=True)
class TimeZoneEdge:
    """
    TimeZoneEdge - When paging time-zones, wraps a time-zone node together with the cursor referencing its position in the results

    cursor - The cursor id referencing the position of this node in the results

    node - The node value

    """

    cursor: str
    node: TimeZone


@dataclass(kw_only=True)
class TimeZonesConnection:
    """
    TimeZonesConnection - A pageable view into time-zone results

    totalCount - The total number of results

    edges - The edges in the current page of results

    pageInfo - Info about the current page of results

    """

    total_count: int
    edges: list[TimeZoneEdge]
    page_info: ConnectionPageInfo
