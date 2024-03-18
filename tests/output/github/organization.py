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
    """
        Organization - An account on GitHub, with one or more owners, that has repositories, members and teams.

        announcement - The text of the announcement

        announcementExpiresAt - The expiration date of the announcement, if any

        announcementUserDismissible - Whether the announcement can be dismissed by the user

        anyPinnableItems - Determine if this repository owner has any items that can be pinned to their profile.

        archivedAt - Identifies the date and time when the organization was archived.

        auditLog - Audit log entries of the organization

        avatarUrl - A URL pointing to the organization's public avatar.

        createdAt - Identifies the date and time when the object was created.

        databaseId - Identifies the primary key from the database.

        description - The organization's public profile description.

        descriptionHTML - The organization's public profile description rendered to HTML.

        domains - A list of domains owned by the organization.

        email - The organization's public email.

        enterpriseOwners - A list of owners of the organization's enterprise account.

        estimatedNextSponsorsPayoutInCents - The estimated next GitHub Sponsors payout for this user/organization in cents (USD).

        hasSponsorsListing - True if this user/organization has a GitHub Sponsors listing.

        id - The Node ID of the Organization object

        interactionAbility - The interaction ability settings for this organization.

        ipAllowListEnabledSetting - The setting value for whether the organization has an IP allow list enabled.

        ipAllowListEntries - The IP addresses that are allowed to access resources owned by the organization.

        ipAllowListForInstalledAppsEnabledSetting - The setting value for whether the organization has IP allow list configuration for installed GitHub Apps enabled.

        isSponsoredBy - Whether the given account is sponsoring this user/organization.

        isSponsoringViewer - True if the viewer is sponsored by this user/organization.

        isVerified - Whether the organization has verified its profile email and website.

        itemShowcase - Showcases a selection of repositories and gists that the profile owner has
    either curated or that have been selected automatically based on popularity.

        lifetimeReceivedSponsorshipValues - Calculate how much each sponsor has ever paid total to this maintainer via
    GitHub Sponsors. Does not include sponsorships paid via Patreon.

        location - The organization's public profile location.

        login - The organization's login name.

        mannequins - A list of all mannequins for this organization.

        memberStatuses - Get the status messages members of this entity have set that are either public or visible only to the organization.

        membersCanForkPrivateRepositories - Members can fork private repositories in this organization

        membersWithRole - A list of users who are members of this organization.

        monthlyEstimatedSponsorsIncomeInCents - The estimated monthly GitHub Sponsors income for this user/organization in cents (USD).

        name - The organization's public profile name.

        newTeamResourcePath - The HTTP path creating a new team

        newTeamUrl - The HTTP URL creating a new team

        notificationDeliveryRestrictionEnabledSetting - Indicates if email notification delivery for this organization is restricted to verified or approved domains.

        organizationBillingEmail - The billing email for the organization.

        packages - A list of packages under the owner.

        pendingMembers - A list of users who have been invited to join this organization.

        pinnableItems - A list of repositories and gists this profile owner can pin to their profile.

        pinnedItems - A list of repositories and gists this profile owner has pinned to their profile

        pinnedItemsRemaining - Returns how many more items this profile owner can pin to their profile.

        project - Find project by number.

        projectV2 - Find a project by number.

        projects - A list of projects under the owner.

        projectsResourcePath - The HTTP path listing organization's projects

        projectsUrl - The HTTP URL listing organization's projects

        projectsV2 - A list of projects under the owner.

        recentProjects - Recent projects that this user has modified in the context of the owner.

        repositories - A list of repositories that the user owns.

        repository - Find Repository.

        repositoryDiscussionComments - Discussion comments this user has authored.

        repositoryDiscussions - Discussions this user has started.

        repositoryMigrations - A list of all repository migrations for this organization.

        requiresTwoFactorAuthentication - When true the organization requires all members, billing managers, and outside
    collaborators to enable two-factor authentication.

        resourcePath - The HTTP path for this organization.

        ruleset - Returns a single ruleset from the current organization by ID.

        rulesets - A list of rulesets for this organization.

        samlIdentityProvider - The Organization's SAML identity provider. Visible to (1) organization owners,
    (2) organization owners' personal access tokens (classic) with read:org or
    admin:org scope, (3) GitHub App with an installation token with read or write
    access to members.

        sponsoring - List of users and organizations this entity is sponsoring.

        sponsors - List of sponsors for this user or organization.

        sponsorsActivities - Events involving this sponsorable, such as new sponsorships.

        sponsorsListing - The GitHub Sponsors listing for this user or organization.

        sponsorshipForViewerAsSponsor - The sponsorship from the viewer to this user/organization; that is, the sponsorship where you're the sponsor.

        sponsorshipForViewerAsSponsorable - The sponsorship from this user/organization to the viewer; that is, the sponsorship you're receiving.

        sponsorshipNewsletters - List of sponsorship updates sent from this sponsorable to sponsors.

        sponsorshipsAsMaintainer - The sponsorships where this user or organization is the maintainer receiving the funds.

        sponsorshipsAsSponsor - The sponsorships where this user or organization is the funder.

        team - Find an organization's team by its slug.

        teams - A list of teams in this organization.

        teamsResourcePath - The HTTP path listing organization's teams

        teamsUrl - The HTTP URL listing organization's teams

        totalSponsorshipAmountAsSponsorInCents - The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has
    spent on GitHub to fund sponsorships. Only returns a value when viewed by the
    user themselves or by a user who can manage sponsorships for the requested organization.

        twitterUsername - The organization's Twitter username.

        updatedAt - Identifies the date and time when the object was last updated.

        url - The HTTP URL for this organization.

        viewerCanAdminister - Organization is adminable by the viewer.

        viewerCanChangePinnedItems - Can the viewer pin repositories and gists to the profile?

        viewerCanCreateProjects - Can the current viewer create new projects on this owner.

        viewerCanCreateRepositories - Viewer can create repositories on this organization

        viewerCanCreateTeams - Viewer can create teams on this organization.

        viewerCanSponsor - Whether or not the viewer is able to sponsor this user/organization.

        viewerIsAMember - Viewer is an active member of this organization.

        viewerIsFollowing - Whether or not this Organization is followed by the viewer.

        viewerIsSponsoring - True if the viewer is sponsoring this user/organization.

        webCommitSignoffRequired - Whether contributors are required to sign off on web-based commits for repositories in this organization.

        websiteUrl - The organization's public profile URL.

    """

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
