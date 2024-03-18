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
