from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import (
    IpAllowListEnabledSettingValue,
    IpAllowListForInstalledAppsEnabledSettingValue,
    NotificationRestrictionSettingValue,
)
from .scalars import ID, URI, DateTime

if TYPE_CHECKING:
    from .user_connection import UserConnection
    from .repository import Repository
    from .team import Team
    from .project_v2 import ProjectV2
    from .project import Project
    from .repository_ruleset import RepositoryRuleset
    from .ip_allow_list_entry_connection import IpAllowListEntryConnection
    from .sponsor_and_lifetime_value_connection import SponsorAndLifetimeValueConnection
    from .sponsors_listing import SponsorsListing
    from .gql_types import RepositoryInteractionAbility
    from .gql_types import TeamConnection
    from .gql_types import UserStatusConnection
    from .gql_types import ProjectV2Connection
    from .gql_types import RepositoryConnection
    from .gql_types import DiscussionCommentConnection
    from .gql_types import DiscussionConnection
    from .gql_types import PackageConnection
    from .gql_types import ProjectConnection
    from .gql_types import RepositoryRulesetConnection
    from .gql_types import OrganizationAuditEntryConnection
    from .gql_types import VerifiableDomainConnection
    from .gql_types import OrganizationEnterpriseOwnerConnection
    from .gql_types import PinnableItemConnection
    from .gql_types import ProfileItemShowcase
    from .gql_types import SponsorConnection
    from .gql_types import Sponsorship
    from .gql_types import SponsorshipConnection
    from .gql_types import SponsorsActivityConnection
    from .gql_types import SponsorshipNewsletterConnection
    from .gql_types import MannequinConnection
    from .gql_types import OrganizationMemberConnection
    from .gql_types import RepositoryMigrationConnection
    from .gql_types import OrganizationIdentityProvider


@dataclass(kw_only=True)
class Organization:
    announcement: Optional[str] = None
    announcement_expires_at: Optional[DateTime] = None
    announcement_user_dismissible: Optional[bool] = None
    any_pinnable_items: bool
    archived_at: Optional[DateTime] = None
    audit_log: OrganizationAuditEntryConnection
    avatar_url: URI
    created_at: DateTime
    database_id: Optional[int] = None
    description: Optional[str] = None
    description_h_t_m_l: Optional[str] = None
    domains: Optional[VerifiableDomainConnection] = None
    email: Optional[str] = None
    enterprise_owners: OrganizationEnterpriseOwnerConnection
    estimated_next_sponsors_payout_in_cents: int
    has_sponsors_listing: bool
    id: ID
    interaction_ability: Optional[RepositoryInteractionAbility] = None
    ip_allow_list_enabled_setting: IpAllowListEnabledSettingValue
    ip_allow_list_entries: IpAllowListEntryConnection
    ip_allow_list_for_installed_apps_enabled_setting: IpAllowListForInstalledAppsEnabledSettingValue
    is_sponsored_by: bool
    is_sponsoring_viewer: bool
    is_verified: bool
    item_showcase: ProfileItemShowcase
    lifetime_received_sponsorship_values: SponsorAndLifetimeValueConnection
    location: Optional[str] = None
    login: str
    mannequins: MannequinConnection
    member_statuses: UserStatusConnection
    members_can_fork_private_repositories: bool
    members_with_role: OrganizationMemberConnection
    monthly_estimated_sponsors_income_in_cents: int
    name: Optional[str] = None
    new_team_resource_path: URI
    new_team_url: URI
    notification_delivery_restriction_enabled_setting: NotificationRestrictionSettingValue
    organization_billing_email: Optional[str] = None
    packages: PackageConnection
    pending_members: UserConnection
    pinnable_items: PinnableItemConnection
    pinned_items: PinnableItemConnection
    pinned_items_remaining: int
    project: Optional[Project] = None
    project_v2: Optional[ProjectV2] = None
    projects: ProjectConnection
    projects_resource_path: URI
    projects_url: URI
    projects_v2: ProjectV2Connection
    recent_projects: ProjectV2Connection
    repositories: RepositoryConnection
    repository: Optional[Repository] = None
    repository_discussion_comments: DiscussionCommentConnection
    repository_discussions: DiscussionConnection
    repository_migrations: RepositoryMigrationConnection
    requires_two_factor_authentication: Optional[bool] = None
    resource_path: URI
    ruleset: Optional[RepositoryRuleset] = None
    rulesets: Optional[RepositoryRulesetConnection] = None
    saml_identity_provider: Optional[OrganizationIdentityProvider] = None
    sponsoring: SponsorConnection
    sponsors: SponsorConnection
    sponsors_activities: SponsorsActivityConnection
    sponsors_listing: Optional[SponsorsListing] = None
    sponsorship_for_viewer_as_sponsor: Optional[Sponsorship] = None
    sponsorship_for_viewer_as_sponsorable: Optional[Sponsorship] = None
    sponsorship_newsletters: SponsorshipNewsletterConnection
    sponsorships_as_maintainer: SponsorshipConnection
    sponsorships_as_sponsor: SponsorshipConnection
    team: Optional[Team] = None
    teams: TeamConnection
    teams_resource_path: URI
    teams_url: URI
    total_sponsorship_amount_as_sponsor_in_cents: Optional[int] = None
    twitter_username: Optional[str] = None
    updated_at: DateTime
    url: URI
    viewer_can_administer: bool
    viewer_can_change_pinned_items: bool
    viewer_can_create_projects: bool
    viewer_can_create_repositories: bool
    viewer_can_create_teams: bool
    viewer_can_sponsor: bool
    viewer_is_a_member: bool
    viewer_is_following: bool
    viewer_is_sponsoring: bool
    web_commit_signoff_required: bool
    website_url: Optional[URI] = None
