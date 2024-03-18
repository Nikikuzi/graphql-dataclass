from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .sponsor_and_lifetime_value_connection import SponsorAndLifetimeValueConnection
    from .sponsors_listing import SponsorsListing
    from .gql_types import SponsorConnection
    from .gql_types import Sponsorship
    from .gql_types import SponsorshipConnection
    from .gql_types import SponsorsActivityConnection
    from .gql_types import SponsorshipNewsletterConnection


@dataclass(kw_only=True)
class Sponsorable:
    estimated_next_sponsors_payout_in_cents: int
    has_sponsors_listing: bool
    is_sponsored_by: bool
    is_sponsoring_viewer: bool
    lifetime_received_sponsorship_values: SponsorAndLifetimeValueConnection
    monthly_estimated_sponsors_income_in_cents: int
    sponsoring: SponsorConnection
    sponsors: SponsorConnection
    sponsors_activities: SponsorsActivityConnection
    sponsors_listing: Optional[SponsorsListing] = None
    sponsorship_for_viewer_as_sponsor: Optional[Sponsorship] = None
    sponsorship_for_viewer_as_sponsorable: Optional[Sponsorship] = None
    sponsorship_newsletters: SponsorshipNewsletterConnection
    sponsorships_as_maintainer: SponsorshipConnection
    sponsorships_as_sponsor: SponsorshipConnection
    total_sponsorship_amount_as_sponsor_in_cents: Optional[int] = None
    viewer_can_sponsor: bool
    viewer_is_sponsoring: bool
