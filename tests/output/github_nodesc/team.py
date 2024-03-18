from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import (
    SubscriptionState,
    TeamNotificationSetting,
    TeamPrivacy,
    TeamReviewAssignmentAlgorithm,
)
from .scalars import ID, URI, DateTime

if TYPE_CHECKING:
    from .organization import Organization
    from .team_discussion import TeamDiscussion
    from .project_v2 import ProjectV2
    from .gql_types import TeamConnection
    from .gql_types import TeamDiscussionConnection
    from .gql_types import OrganizationInvitationConnection
    from .gql_types import UserStatusConnection
    from .gql_types import TeamMemberConnection
    from .gql_types import ProjectV2Connection
    from .gql_types import TeamRepositoryConnection


@dataclass(kw_only=True)
class Team:
    ancestors: TeamConnection
    avatar_url: Optional[URI] = None
    child_teams: TeamConnection
    combined_slug: str
    created_at: DateTime
    database_id: Optional[int] = None
    description: Optional[str] = None
    discussion: Optional[TeamDiscussion] = None
    discussions: TeamDiscussionConnection
    discussions_resource_path: URI
    discussions_url: URI
    edit_team_resource_path: URI
    edit_team_url: URI
    id: ID
    invitations: Optional[OrganizationInvitationConnection] = None
    member_statuses: UserStatusConnection
    members: TeamMemberConnection
    members_resource_path: URI
    members_url: URI
    name: str
    new_team_resource_path: URI
    new_team_url: URI
    notification_setting: TeamNotificationSetting
    organization: Organization
    parent_team: Optional["Team"] = None
    privacy: TeamPrivacy
    project_v2: Optional[ProjectV2] = None
    projects_v2: ProjectV2Connection
    repositories: TeamRepositoryConnection
    repositories_resource_path: URI
    repositories_url: URI
    resource_path: URI
    review_request_delegation_algorithm: Optional[TeamReviewAssignmentAlgorithm] = None
    review_request_delegation_enabled: bool
    review_request_delegation_member_count: Optional[int] = None
    review_request_delegation_notify_team: bool
    slug: str
    teams_resource_path: URI
    teams_url: URI
    updated_at: DateTime
    url: URI
    viewer_can_administer: bool
    viewer_can_subscribe: bool
    viewer_subscription: Optional[SubscriptionState] = None
