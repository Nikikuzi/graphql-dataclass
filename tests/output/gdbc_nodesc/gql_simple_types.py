from dataclasses import dataclass
from typing import Optional

from .enums import Language


@dataclass(kw_only=True)
class ConnectionPageInfo:
    start_cursor: str
    end_cursor: str
    has_next_page: bool
    has_previous_page: bool


@dataclass(kw_only=True)
class DisplayOptions:
    ascii_mode: Optional[bool] = None
    language: Optional[Language] = None


@dataclass(kw_only=True)
class Location:
    latitude: Optional[float] = None
    longitude: Optional[float] = None
