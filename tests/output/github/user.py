from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .scalars import HTML, ID, URI, DateTime

if TYPE_CHECKING:
    from .pull_request_connection import PullRequestConnection
    from .organization import Organization
    from .repository import Repository
    from .project_v2 import ProjectV2
    from .commit_comment_connection import CommitCommentConnection
    from .project import Project
    from .gist import Gist
    from .sponsor_and_lifetime_value_connection import SponsorAndLifetimeValueConnection
    from .sponsors_listing import SponsorsListing
    from .contributions_collection import ContributionsCollection
    from .gql_types import RepositoryInteractionAbility
    from .gql_types import UserListSuggestion
    from .gql_types import UserStatus
    from .gql_types import ProjectV2Connection
    from .gql_types import IssueConnection
    from .gql_types import RepositoryConnection
    from .gql_types import DiscussionCommentConnection
    from .gql_types import DiscussionConnection
    from .gql_types import PackageConnection
    from .gql_types import ProjectConnection
    from .gql_types import GistCommentConnection
    from .gql_types import GistConnection
    from .gql_types import PinnableItemConnection
    from .gql_types import ProfileItemShowcase
    from .gql_types import SponsorConnection
    from .gql_types import Sponsorship
    from .gql_types import SponsorshipConnection
    from .gql_types import SponsorsActivityConnection
    from .gql_types import SponsorshipNewsletterConnection
    from .gql_types import OrganizationConnection
    from .gql_types import IssueCommentConnection
    from .gql_types import Hovercard
    from .gql_types import EnterpriseConnection
    from .gql_types import FollowerConnection
    from .gql_types import FollowingConnection
    from .gql_types import UserListConnection
    from .gql_types import PublicKeyConnection
    from .gql_types import SavedReplyConnection
    from .gql_types import SocialAccountConnection
    from .gql_types import StarredRepositoryConnection


@dataclass(kw_only=True)
class User:
    """
        User - A user is an individual's account on GitHub that owns repositories and can make new content.

        anyPinnableItems - Determine if this repository owner has any items that can be pinned to their profile.

        avatarUrl - A URL pointing to the user's public avatar.

        bio - The user's public profile bio.

        bioHTML - The user's public profile bio as HTML.

        canReceiveOrganizationEmailsWhenNotificationsRestricted - Could this user receive email notifications, if the organization had notification restrictions enabled?

        commitComments - A list of commit comments made by this user.

        company - The user's public profile company.

        companyHTML - The user's public profile company as HTML.

        contributionsCollection - The collection of contributions this user has made to different repositories.

        createdAt - Identifies the date and time when the object was created.

        databaseId - Identifies the primary key from the database.

        email - The user's publicly visible profile email.

        enterprises - A list of enterprises that the user belongs to.

        estimatedNextSponsorsPayoutInCents - The estimated next GitHub Sponsors payout for this user/organization in cents (USD).

        followers - A list of users the given user is followed by.

        following - A list of users the given user is following.

        gist - Find gist by repo name.

        gistComments - A list of gist comments made by this user.

        gists - A list of the Gists the user has created.

        hasSponsorsListing - True if this user/organization has a GitHub Sponsors listing.

        hovercard - The hovercard information for this user in a given context

        id - The Node ID of the User object

        interactionAbility - The interaction ability settings for this user.

        isBountyHunter - Whether or not this user is a participant in the GitHub Security Bug Bounty.

        isCampusExpert - Whether or not this user is a participant in the GitHub Campus Experts Program.

        isDeveloperProgramMember - Whether or not this user is a GitHub Developer Program member.

        isEmployee - Whether or not this user is a GitHub employee.

        isFollowingViewer - Whether or not this user is following the viewer. Inverse of viewerIsFollowing

        isGitHubStar - Whether or not this user is a member of the GitHub Stars Program.

        isHireable - Whether or not the user has marked themselves as for hire.

        isSiteAdmin - Whether or not this user is a site administrator.

        isSponsoredBy - Whether the given account is sponsoring this user/organization.

        isSponsoringViewer - True if the viewer is sponsored by this user/organization.

        isViewer - Whether or not this user is the viewing user.

        issueComments - A list of issue comments made by this user.

        issues - A list of issues associated with this user.

        itemShowcase - Showcases a selection of repositories and gists that the profile owner has
    either curated or that have been selected automatically based on popularity.

        lifetimeReceivedSponsorshipValues - Calculate how much each sponsor has ever paid total to this maintainer via
    GitHub Sponsors. Does not include sponsorships paid via Patreon.

        lists - A user-curated list of repositories

        location - The user's public profile location.

        login - The username used to login.

        monthlyEstimatedSponsorsIncomeInCents - The estimated monthly GitHub Sponsors income for this user/organization in cents (USD).

        name - The user's public profile name.

        organization - Find an organization by its login that the user belongs to.

        organizationVerifiedDomainEmails - Verified email addresses that match verified domains for a specified organization the user is a member of.

        organizations - A list of organizations the user belongs to.

        packages - A list of packages under the owner.

        pinnableItems - A list of repositories and gists this profile owner can pin to their profile.

        pinnedItems - A list of repositories and gists this profile owner has pinned to their profile

        pinnedItemsRemaining - Returns how many more items this profile owner can pin to their profile.

        project - Find project by number.

        projectV2 - Find a project by number.

        projects - A list of projects under the owner.

        projectsResourcePath - The HTTP path listing user's projects

        projectsUrl - The HTTP URL listing user's projects

        projectsV2 - A list of projects under the owner.

        pronouns - The user's profile pronouns

        publicKeys - A list of public keys associated with this user.

        pullRequests - A list of pull requests associated with this user.

        recentProjects - Recent projects that this user has modified in the context of the owner.

        repositories - A list of repositories that the user owns.

        repositoriesContributedTo - A list of repositories that the user recently contributed to.

        repository - Find Repository.

        repositoryDiscussionComments - Discussion comments this user has authored.

        repositoryDiscussions - Discussions this user has started.

        resourcePath - The HTTP path for this user

        savedReplies - Replies this user has saved

        socialAccounts - The user's social media accounts, ordered as they appear on the user's profile.

        sponsoring - List of users and organizations this entity is sponsoring.

        sponsors - List of sponsors for this user or organization.

        sponsorsActivities - Events involving this sponsorable, such as new sponsorships.

        sponsorsListing - The GitHub Sponsors listing for this user or organization.

        sponsorshipForViewerAsSponsor - The sponsorship from the viewer to this user/organization; that is, the sponsorship where you're the sponsor.

        sponsorshipForViewerAsSponsorable - The sponsorship from this user/organization to the viewer; that is, the sponsorship you're receiving.

        sponsorshipNewsletters - List of sponsorship updates sent from this sponsorable to sponsors.

        sponsorshipsAsMaintainer - The sponsorships where this user or organization is the maintainer receiving the funds.

        sponsorshipsAsSponsor - The sponsorships where this user or organization is the funder.

        starredRepositories - Repositories the user has starred.

        status - The user's description of what they're currently doing.

        suggestedListNames - Suggested names for user lists

        topRepositories - Repositories the user has contributed to, ordered by contribution rank, plus repositories the user has created

        totalSponsorshipAmountAsSponsorInCents - The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has
    spent on GitHub to fund sponsorships. Only returns a value when viewed by the
    user themselves or by a user who can manage sponsorships for the requested organization.

        twitterUsername - The user's Twitter username.

        updatedAt - Identifies the date and time when the object was last updated.

        url - The HTTP URL for this user

        viewerCanChangePinnedItems - Can the viewer pin repositories and gists to the profile?

        viewerCanCreateProjects - Can the current viewer create new projects on this owner.

        viewerCanFollow - Whether or not the viewer is able to follow the user.

        viewerCanSponsor - Whether or not the viewer is able to sponsor this user/organization.

        viewerIsFollowing - Whether or not this user is followed by the viewer. Inverse of isFollowingViewer.

        viewerIsSponsoring - True if the viewer is sponsoring this user/organization.

        watching - A list of repositories the given user is watching.

        websiteUrl - A URL pointing to the user's public website/blog.

    """

    any_pinnable_items: bool
    avatar_url: URI
    bio: Optional[str] = None
    bio_h_t_m_l: HTML
    can_receive_organization_emails_when_notifications_restricted: bool
    commit_comments: CommitCommentConnection
    company: Optional[str] = None
    company_h_t_m_l: HTML
    contributions_collection: ContributionsCollection
    created_at: DateTime
    database_id: Optional[int] = None
    email: str
    enterprises: Optional[EnterpriseConnection] = None
    estimated_next_sponsors_payout_in_cents: int
    followers: FollowerConnection
    following: FollowingConnection
    gist: Optional[Gist] = None
    gist_comments: GistCommentConnection
    gists: GistConnection
    has_sponsors_listing: bool
    hovercard: Hovercard
    id: ID
    interaction_ability: Optional[RepositoryInteractionAbility] = None
    is_bounty_hunter: bool
    is_campus_expert: bool
    is_developer_program_member: bool
    is_employee: bool
    is_following_viewer: bool
    is_git_hub_star: bool
    is_hireable: bool
    is_site_admin: bool
    is_sponsored_by: bool
    is_sponsoring_viewer: bool
    is_viewer: bool
    issue_comments: IssueCommentConnection
    issues: IssueConnection
    item_showcase: ProfileItemShowcase
    lifetime_received_sponsorship_values: SponsorAndLifetimeValueConnection
    lists: UserListConnection
    location: Optional[str] = None
    login: str
    monthly_estimated_sponsors_income_in_cents: int
    name: Optional[str] = None
    organization: Optional[Organization] = None
    organization_verified_domain_emails: list[str]
    organizations: OrganizationConnection
    packages: PackageConnection
    pinnable_items: PinnableItemConnection
    pinned_items: PinnableItemConnection
    pinned_items_remaining: int
    project: Optional[Project] = None
    project_v2: Optional[ProjectV2] = None
    projects: ProjectConnection
    projects_resource_path: URI
    projects_url: URI
    projects_v2: ProjectV2Connection
    pronouns: Optional[str] = None
    public_keys: PublicKeyConnection
    pull_requests: PullRequestConnection
    recent_projects: ProjectV2Connection
    repositories: RepositoryConnection
    repositories_contributed_to: RepositoryConnection
    repository: Optional[Repository] = None
    repository_discussion_comments: DiscussionCommentConnection
    repository_discussions: DiscussionConnection
    resource_path: URI
    saved_replies: Optional[SavedReplyConnection] = None
    social_accounts: SocialAccountConnection
    sponsoring: SponsorConnection
    sponsors: SponsorConnection
    sponsors_activities: SponsorsActivityConnection
    sponsors_listing: Optional[SponsorsListing] = None
    sponsorship_for_viewer_as_sponsor: Optional[Sponsorship] = None
    sponsorship_for_viewer_as_sponsorable: Optional[Sponsorship] = None
    sponsorship_newsletters: SponsorshipNewsletterConnection
    sponsorships_as_maintainer: SponsorshipConnection
    sponsorships_as_sponsor: SponsorshipConnection
    starred_repositories: StarredRepositoryConnection
    status: Optional[UserStatus] = None
    suggested_list_names: list[UserListSuggestion]
    top_repositories: RepositoryConnection
    total_sponsorship_amount_as_sponsor_in_cents: Optional[int] = None
    twitter_username: Optional[str] = None
    updated_at: DateTime
    url: URI
    viewer_can_change_pinned_items: bool
    viewer_can_create_projects: bool
    viewer_can_follow: bool
    viewer_can_sponsor: bool
    viewer_is_following: bool
    viewer_is_sponsoring: bool
    watching: RepositoryConnection
    website_url: Optional[URI] = None
