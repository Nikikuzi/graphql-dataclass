from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .scalars import ID, URI, DateTime

if TYPE_CHECKING:
    from .ip_allow_list_entry_connection import IpAllowListEntryConnection


@dataclass(kw_only=True)
class App:
    """
    App - A GitHub App.

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    description - The description of the app.

    id - The Node ID of the App object

    ipAllowListEntries - The IP addresses of the app.

    logoBackgroundColor - The hex color code, without the leading '#', for the logo background.

    logoUrl - A URL pointing to the app's logo.

    name - The name of the app.

    slug - A slug based on the name of the app for use in URLs.

    updatedAt - Identifies the date and time when the object was last updated.

    url - The URL to the app's homepage.

    """

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
