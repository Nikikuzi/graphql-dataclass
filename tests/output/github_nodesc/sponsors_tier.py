from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .scalars import HTML, ID, DateTime

if TYPE_CHECKING:
    from .sponsors_listing import SponsorsListing
    from .gql_types import SponsorsTierAdminInfo


@dataclass(kw_only=True)
class SponsorsTier:
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
