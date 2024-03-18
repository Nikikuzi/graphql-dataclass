from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .scalars import ID, URI, DateTime

if TYPE_CHECKING:
    from .ip_allow_list_entry_connection import IpAllowListEntryConnection


@dataclass(kw_only=True)
class App:
    created_at: DateTime
    database_id: Optional[int] = None
    description: Optional[str] = None
    id: ID
    ip_allow_list_entries: IpAllowListEntryConnection
    logo_background_color: str
    logo_url: URI
    name: str
    slug: str
    updated_at: DateTime
    url: URI
