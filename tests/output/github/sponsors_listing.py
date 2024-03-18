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
    """
        SponsorsListing - A GitHub Sponsors listing.

        activeGoal - The current goal the maintainer is trying to reach with GitHub Sponsors, if any.

        activeStripeConnectAccount - The Stripe Connect account currently in use for payouts for this Sponsors
    listing, if any. Will only return a value when queried by the maintainer
    themselves, or by an admin of the sponsorable organization.

        billingCountryOrRegion - The name of the country or region with the maintainer's bank account or fiscal
    host. Will only return a value when queried by the maintainer themselves, or
    by an admin of the sponsorable organization.

        contactEmailAddress - The email address used by GitHub to contact the sponsorable about their GitHub
    Sponsors profile. Will only return a value when queried by the maintainer
    themselves, or by an admin of the sponsorable organization.

        createdAt - Identifies the date and time when the object was created.

        dashboardResourcePath - The HTTP path for the Sponsors dashboard for this Sponsors listing.

        dashboardUrl - The HTTP URL for the Sponsors dashboard for this Sponsors listing.

        featuredItems - The records featured on the GitHub Sponsors profile.

        fiscalHost - The fiscal host used for payments, if any. Will only return a value when
    queried by the maintainer themselves, or by an admin of the sponsorable organization.

        fullDescription - The full description of the listing.

        fullDescriptionHTML - The full description of the listing rendered to HTML.

        id - The Node ID of the SponsorsListing object

        isPublic - Whether this listing is publicly visible.

        name - The listing's full name.

        nextPayoutDate - A future date on which this listing is eligible to receive a payout.

        residenceCountryOrRegion - The name of the country or region where the maintainer resides. Will only
    return a value when queried by the maintainer themselves, or by an admin of
    the sponsorable organization.

        resourcePath - The HTTP path for this Sponsors listing.

        shortDescription - The short description of the listing.

        slug - The short name of the listing.

        sponsorable - The entity this listing represents who can be sponsored on GitHub Sponsors.

        tiers - The tiers for this GitHub Sponsors profile.

        url - The HTTP URL for this Sponsors listing.

    """

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
