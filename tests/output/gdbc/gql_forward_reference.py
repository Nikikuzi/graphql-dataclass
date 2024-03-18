from .country import Country
from .country_region import CountryRegion
from .gql_types import (
    CountriesConnection,
    CountryEdge,
    CountryRegionEdge,
    CountryRegionsConnection,
    CurrenciesConnection,
    Currency,
    CurrencyEdge,
    Locale,
    LocaleEdge,
    LocalesConnection,
    NearbyPopulatedPlacesConnection,
    PopulatedPlacesConnection,
    RegionPopulatedPlacesConnection,
    TimeZone,
    TimeZoneEdge,
    TimeZonesConnection,
)
from .populated_place import PopulatedPlace
from .populated_place_edge import PopulatedPlaceEdge

forward_reference = {
    "Currency": Currency,
    "Locale": Locale,
    "TimeZone": TimeZone,
    "NearbyPopulatedPlacesConnection": NearbyPopulatedPlacesConnection,
    "PopulatedPlace": PopulatedPlace,
    "PopulatedPlaceEdge": PopulatedPlaceEdge,
    "RegionPopulatedPlacesConnection": RegionPopulatedPlacesConnection,
    "CountryRegion": CountryRegion,
    "CountryRegionEdge": CountryRegionEdge,
    "CountryRegionsConnection": CountryRegionsConnection,
    "Country": Country,
    "CountryEdge": CountryEdge,
    "CountriesConnection": CountriesConnection,
    "CurrencyEdge": CurrencyEdge,
    "CurrenciesConnection": CurrenciesConnection,
    "LocaleEdge": LocaleEdge,
    "LocalesConnection": LocalesConnection,
    "PopulatedPlacesConnection": PopulatedPlacesConnection,
    "TimeZoneEdge": TimeZoneEdge,
    "TimeZonesConnection": TimeZonesConnection,
}
