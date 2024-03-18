from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .scalars import HTML, ID, URI, Date, DateTime

if TYPE_CHECKING:
    from .organization import Organization
    from .sponsorable import Sponsorable
    from .gql_types import SponsorsGoal
    from .gql_types import StripeConnectAccount
    from .gql_types import SponsorsListingFeaturedItem
    from .gql_types import SponsorsTierConnection


@dataclass(kw_only=True)
class SponsorsListing:
    active_goal: Optional[SponsorsGoal] = None
    active_stripe_connect_account: Optional[StripeConnectAccount] = None
    billing_country_or_region: Optional[str] = None
    contact_email_address: Optional[str] = None
    created_at: DateTime
    dashboard_resource_path: URI
    dashboard_url: URI
    featured_items: list[SponsorsListingFeaturedItem]
    fiscal_host: Optional[Organization] = None
    full_description: str
    full_description_h_t_m_l: HTML
    id: ID
    is_public: bool
    name: str
    next_payout_date: Optional[Date] = None
    residence_country_or_region: Optional[str] = None
    resource_path: URI
    short_description: str
    slug: str
    sponsorable: Sponsorable
    tiers: Optional[SponsorsTierConnection] = None
    url: URI
