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
