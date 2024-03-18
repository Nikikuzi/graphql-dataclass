from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .gql_simple_types import EnterpriseBillingInfo
from .scalars import HTML, ID, URI, DateTime

if TYPE_CHECKING:
    from .gql_types import EnterpriseMemberConnection
    from .gql_types import OrganizationConnection
    from .gql_types import EnterpriseOwnerInfo


@dataclass(kw_only=True)
class Enterprise:
    """
        Enterprise - An account to manage multiple organizations with consolidated policy and billing.

        announcement - The text of the announcement

        announcementExpiresAt - The expiration date of the announcement, if any

        announcementUserDismissible - Whether the announcement can be dismissed by the user

        avatarUrl - A URL pointing to the enterprise's public avatar.

        billingEmail - The enterprise's billing email.

        billingInfo - Enterprise billing information visible to enterprise billing managers.

        createdAt - Identifies the date and time when the object was created.

        databaseId - Identifies the primary key from the database.

        description - The description of the enterprise.

        descriptionHTML - The description of the enterprise as HTML.

        id - The Node ID of the Enterprise object

        location - The location of the enterprise.

        members - A list of users who are members of this enterprise.

        name - The name of the enterprise.

        organizations - A list of organizations that belong to this enterprise.

        ownerInfo - Enterprise information visible to enterprise owners or enterprise owners'
    personal access tokens (classic) with read:enterprise or admin:enterprise scope.

        resourcePath - The HTTP path for this enterprise.

        slug - The URL-friendly identifier for the enterprise.

        url - The HTTP URL for this enterprise.

        viewerIsAdmin - Is the current viewer an admin of this enterprise?

        websiteUrl - The URL of the enterprise website.

    """

    announcement: Optional[str] = None
    announcement_expires_at: Optional[DateTime] = None
    announcement_user_dismissible: Optional[bool] = None
    avatar_url: URI
    billing_email: Optional[str] = None
    billing_info: Optional[EnterpriseBillingInfo] = None
    created_at: DateTime
    database_id: Optional[int] = None
    description: Optional[str] = None
    description_h_t_m_l: HTML
    id: ID
    location: Optional[str] = None
    members: EnterpriseMemberConnection
    name: str
    organizations: OrganizationConnection
    owner_info: Optional[EnterpriseOwnerInfo] = None
    resource_path: URI
    slug: str
    url: URI
    viewer_is_admin: bool
    website_url: Optional[URI] = None
