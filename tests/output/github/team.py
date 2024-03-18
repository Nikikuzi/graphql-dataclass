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
    """
    Team - A team of users in an organization.

    ancestors - A list of teams that are ancestors of this team.

    avatarUrl - A URL pointing to the team's avatar.

    childTeams - List of child teams belonging to this team

    combinedSlug - The slug corresponding to the organization and team.

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    description - The description of the team.

    discussion - Find a team discussion by its number.

    discussions - A list of team discussions.

    discussionsResourcePath - The HTTP path for team discussions

    discussionsUrl - The HTTP URL for team discussions

    editTeamResourcePath - The HTTP path for editing this team

    editTeamUrl - The HTTP URL for editing this team

    id - The Node ID of the Team object

    invitations - A list of pending invitations for users to this team

    memberStatuses - Get the status messages members of this entity have set that are either public or visible only to the organization.

    members - A list of users who are members of this team.

    membersResourcePath - The HTTP path for the team' members

    membersUrl - The HTTP URL for the team' members

    name - The name of the team.

    newTeamResourcePath - The HTTP path creating a new team

    newTeamUrl - The HTTP URL creating a new team

    notificationSetting - The notification setting that the team has set.

    organization - The organization that owns this team.

    parentTeam - The parent team of the team.

    privacy - The level of privacy the team has.

    projectV2 - Finds and returns the project according to the provided project number.

    projectsV2 - List of projects this team has collaborator access to.

    repositories - A list of repositories this team has access to.

    repositoriesResourcePath - The HTTP path for this team's repositories

    repositoriesUrl - The HTTP URL for this team's repositories

    resourcePath - The HTTP path for this team

    reviewRequestDelegationAlgorithm - What algorithm is used for review assignment for this team

    reviewRequestDelegationEnabled - True if review assignment is enabled for this team

    reviewRequestDelegationMemberCount - How many team members are required for review assignment for this team

    reviewRequestDelegationNotifyTeam - When assigning team members via delegation, whether the entire team should be notified as well.

    slug - The slug corresponding to the team.

    teamsResourcePath - The HTTP path for this team's teams

    teamsUrl - The HTTP URL for this team's teams

    updatedAt - Identifies the date and time when the object was last updated.

    url - The HTTP URL for this team

    viewerCanAdminister - Team is adminable by the viewer.

    viewerCanSubscribe - Check if the viewer is able to change their subscription status for the repository.

    viewerSubscription - Identifies if the viewer is watching, not watching, or ignoring the subscribable entity.

    """

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
