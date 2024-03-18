from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .scalars import HTML, ID, DateTime

if TYPE_CHECKING:
    from .sponsors_listing import SponsorsListing
    from .gql_types import SponsorsTierAdminInfo


@dataclass(kw_only=True)
class SponsorsTier:
    """
        SponsorsTier - A GitHub Sponsors tier associated with a GitHub Sponsors listing.

        adminInfo - SponsorsTier information only visible to users that can administer the associated Sponsors listing.

        closestLesserValueTier - Get a different tier for this tier's maintainer that is at the same frequency
    as this tier but with an equal or lesser cost. Returns the published tier with
    the monthly price closest to this tier's without going over.

        createdAt - Identifies the date and time when the object was created.

        description - The description of the tier.

        descriptionHTML - The tier description rendered to HTML

        id - The Node ID of the SponsorsTier object

        isCustomAmount - Whether this tier was chosen at checkout time by the sponsor rather than
    defined ahead of time by the maintainer who manages the Sponsors listing.

        isOneTime - Whether this tier is only for use with one-time sponsorships.

        monthlyPriceInCents - How much this tier costs per month in cents.

        monthlyPriceInDollars - How much this tier costs per month in USD.

        name - The name of the tier.

        sponsorsListing - The sponsors listing that this tier belongs to.

        updatedAt - Identifies the date and time when the object was last updated.

    """

    admin_info: Optional[SponsorsTierAdminInfo] = None
    closest_lesser_value_tier: Optional["SponsorsTier"] = None
    created_at: DateTime
    description: str
    description_h_t_m_l: HTML
    id: ID
    is_custom_amount: bool
    is_one_time: bool
    monthly_price_in_cents: int
    monthly_price_in_dollars: int
    name: str
    sponsors_listing: SponsorsListing
    updated_at: DateTime
