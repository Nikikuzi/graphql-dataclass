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
    """
        Sponsorable - Entities that can sponsor or be sponsored through GitHub Sponsors.

        estimatedNextSponsorsPayoutInCents - The estimated next GitHub Sponsors payout for this user/organization in cents (USD).

        hasSponsorsListing - True if this user/organization has a GitHub Sponsors listing.

        isSponsoredBy - Whether the given account is sponsoring this user/organization.

        isSponsoringViewer - True if the viewer is sponsored by this user/organization.

        lifetimeReceivedSponsorshipValues - Calculate how much each sponsor has ever paid total to this maintainer via
    GitHub Sponsors. Does not include sponsorships paid via Patreon.

        monthlyEstimatedSponsorsIncomeInCents - The estimated monthly GitHub Sponsors income for this user/organization in cents (USD).

        sponsoring - List of users and organizations this entity is sponsoring.

        sponsors - List of sponsors for this user or organization.

        sponsorsActivities - Events involving this sponsorable, such as new sponsorships.

        sponsorsListing - The GitHub Sponsors listing for this user or organization.

        sponsorshipForViewerAsSponsor - The sponsorship from the viewer to this user/organization; that is, the sponsorship where you're the sponsor.

        sponsorshipForViewerAsSponsorable - The sponsorship from this user/organization to the viewer; that is, the sponsorship you're receiving.

        sponsorshipNewsletters - List of sponsorship updates sent from this sponsorable to sponsors.

        sponsorshipsAsMaintainer - The sponsorships where this user or organization is the maintainer receiving the funds.

        sponsorshipsAsSponsor - The sponsorships where this user or organization is the funder.

        totalSponsorshipAmountAsSponsorInCents - The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has
    spent on GitHub to fund sponsorships. Only returns a value when viewed by the
    user themselves or by a user who can manage sponsorships for the requested organization.

        viewerCanSponsor - Whether or not the viewer is able to sponsor this user/organization.

        viewerIsSponsoring - True if the viewer is sponsoring this user/organization.

    """

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
