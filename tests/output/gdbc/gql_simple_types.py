from dataclasses import dataclass
from typing import Optional

from .enums import Language


@dataclass(kw_only=True)
class ConnectionPageInfo:
    """
    ConnectionPageInfo - Info about the current connection page slice

    startCursor - The opaque id of the cursor representing the index of the first element in this page

    endCursor - The opaque id of the cursor representing the index of the last element in this page

    hasNextPage - Whether there are more pages in the results

    hasPreviousPage - Whether there are previous pages in the results

    """

    start_cursor: str
    end_cursor: str
    has_next_page: bool
    has_previous_page: bool


@dataclass(kw_only=True)
class DisplayOptions:
    """
    DisplayOptions - How the results should be rendered

    asciiMode - Whether to display results using ASCII-only characters

    language - What language to display the results in

    """

    ascii_mode: Optional[bool] = None
    language: Optional[Language] = None


@dataclass(kw_only=True)
class Location:
    """
    Location - Location GPS latitude/longitude coordinates

    latitude - DD.DDDD from -90 to 90

    longitude - DD.DDDD from -180 to 180

    """

    latitude: Optional[float] = None
    longitude: Optional[float] = None
