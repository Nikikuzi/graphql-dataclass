from typing import Union

from .app import App
from .commit import Commit
from .discussion import Discussion
from .enterprise import Enterprise
from .gist import Gist
from .gql_simple_types import (
    BranchNamePatternParameters,
    CommitterEmailPatternParameters,
    PullRequestParameters,
    UpdateParameters,
)
from .gql_types import (
    AddedToMergeQueueEvent,
    AddedToProjectEvent,
    AssignedEvent,
    AutomaticBaseChangeFailedEvent,
    AutomaticBaseChangeSucceededEvent,
    AutoMergeDisabledEvent,
    AutoMergeEnabledEvent,
    AutoRebaseEnabledEvent,
    AutoSquashEnabledEvent,
    BaseRefChangedEvent,
    BaseRefDeletedEvent,
    BaseRefForcePushedEvent,
    Bot,
    CheckRun,
    ClosedEvent,
    CommentDeletedEvent,
    CommitAuthorEmailPatternParameters,
    CommitCommentThread,
    CommitMessagePatternParameters,
    ConnectedEvent,
    ConvertedNoteToIssueEvent,
    ConvertedToDiscussionEvent,
    ConvertToDraftEvent,
    CreatedIssueContribution,
    CreatedPullRequestContribution,
    CreatedRepositoryContribution,
    CrossReferencedEvent,
    DemilestonedEvent,
    DeployedEvent,
    DeploymentEnvironmentChangedEvent,
    DisconnectedEvent,
    DraftIssue,
    EnterpriseUserAccount,
    HeadRefDeletedEvent,
    HeadRefForcePushedEvent,
    HeadRefRestoredEvent,
    LabeledEvent,
    LockedEvent,
    Mannequin,
    MarkedAsDuplicateEvent,
    MarketplaceListing,
    MembersCanDeleteReposClearAuditEntry,
    MembersCanDeleteReposDisableAuditEntry,
    MembersCanDeleteReposEnableAuditEntry,
    MentionedEvent,
    MergedEvent,
    MilestonedEvent,
    MovedColumnsInProjectEvent,
    OauthApplicationCreateAuditEntry,
    OrgAddBillingManagerAuditEntry,
    OrgAddMemberAuditEntry,
    OrgBlockUserAuditEntry,
    OrgConfigDisableCollaboratorsOnlyAuditEntry,
    OrgConfigEnableCollaboratorsOnlyAuditEntry,
    OrgCreateAuditEntry,
    OrgDisableOauthAppRestrictionsAuditEntry,
    OrgDisableSamlAuditEntry,
    OrgDisableTwoFactorRequirementAuditEntry,
    OrgEnableOauthAppRestrictionsAuditEntry,
    OrgEnableSamlAuditEntry,
    OrgEnableTwoFactorRequirementAuditEntry,
    OrgInviteMemberAuditEntry,
    OrgInviteToBusinessAuditEntry,
    OrgOauthAppAccessApprovedAuditEntry,
    OrgOauthAppAccessBlockedAuditEntry,
    OrgOauthAppAccessDeniedAuditEntry,
    OrgOauthAppAccessRequestedAuditEntry,
    OrgOauthAppAccessUnblockedAuditEntry,
    OrgRemoveBillingManagerAuditEntry,
    OrgRemoveMemberAuditEntry,
    OrgRemoveOutsideCollaboratorAuditEntry,
    OrgRestoreMemberAuditEntry,
    OrgRestoreMemberMembershipOrganizationAuditEntryData,
    OrgRestoreMemberMembershipRepositoryAuditEntryData,
    OrgRestoreMemberMembershipTeamAuditEntryData,
    OrgUnblockUserAuditEntry,
    OrgUpdateDefaultRepositoryPermissionAuditEntry,
    OrgUpdateMemberAuditEntry,
    OrgUpdateMemberRepositoryCreationPermissionAuditEntry,
    OrgUpdateMemberRepositoryInvitationPermissionAuditEntry,
    PinnedEvent,
    PrivateRepositoryForkingDisableAuditEntry,
    PrivateRepositoryForkingEnableAuditEntry,
    ProjectV2Field,
    ProjectV2ItemFieldDateValue,
    ProjectV2ItemFieldIterationValue,
    ProjectV2ItemFieldLabelValue,
    ProjectV2ItemFieldMilestoneValue,
    ProjectV2ItemFieldNumberValue,
    ProjectV2ItemFieldPullRequestValue,
    ProjectV2ItemFieldRepositoryValue,
    ProjectV2ItemFieldReviewerValue,
    ProjectV2ItemFieldSingleSelectValue,
    ProjectV2ItemFieldTextValue,
    ProjectV2ItemFieldUserValue,
    ProjectV2IterationField,
    ProjectV2SingleSelectField,
    PullRequestCommit,
    PullRequestCommitCommentThread,
    PullRequestReviewThread,
    PullRequestRevisionMarker,
    ReadyForReviewEvent,
    ReferencedEvent,
    RemovedFromMergeQueueEvent,
    RemovedFromProjectEvent,
    RenamedTitleEvent,
    ReopenedEvent,
    RepoAccessAuditEntry,
    RepoAddMemberAuditEntry,
    RepoAddTopicAuditEntry,
    RepoArchivedAuditEntry,
    RepoChangeMergeSettingAuditEntry,
    RepoConfigDisableAnonymousGitAccessAuditEntry,
    RepoConfigDisableCollaboratorsOnlyAuditEntry,
    RepoConfigDisableContributorsOnlyAuditEntry,
    RepoConfigDisableSockpuppetDisallowedAuditEntry,
    RepoConfigEnableAnonymousGitAccessAuditEntry,
    RepoConfigEnableCollaboratorsOnlyAuditEntry,
    RepoConfigEnableContributorsOnlyAuditEntry,
    RepoConfigEnableSockpuppetDisallowedAuditEntry,
    RepoConfigLockAnonymousGitAccessAuditEntry,
    RepoConfigUnlockAnonymousGitAccessAuditEntry,
    RepoCreateAuditEntry,
    RepoDestroyAuditEntry,
    RepoRemoveMemberAuditEntry,
    RepoRemoveTopicAuditEntry,
    RepositoryVisibilityChangeDisableAuditEntry,
    RepositoryVisibilityChangeEnableAuditEntry,
    RequiredDeploymentsParameters,
    RequiredStatusChecksParameters,
    RestrictedContribution,
    ReviewDismissedEvent,
    ReviewRequestedEvent,
    ReviewRequestRemovedEvent,
    StatusContext,
    SubscribedEvent,
    TagNamePatternParameters,
    TeamAddMemberAuditEntry,
    TeamAddRepositoryAuditEntry,
    TeamChangeParentTeamAuditEntry,
    TeamRemoveMemberAuditEntry,
    TeamRemoveRepositoryAuditEntry,
    TransferredEvent,
    UnassignedEvent,
    UnlabeledEvent,
    UnlockedEvent,
    UnmarkedAsDuplicateEvent,
    UnpinnedEvent,
    UnsubscribedEvent,
    UserBlockedEvent,
    WorkflowsParameters,
)
from .issue import Issue
from .issue_comment import IssueComment
from .organization import Organization
from .pull_request import PullRequest
from .pull_request_review import PullRequestReview
from .pull_request_review_comment import PullRequestReviewComment
from .repository import Repository
from .team import Team
from .user import User

"""
Types that can initiate an audit log event.
"""

AuditEntryActor = Union[User, Organization, Bot]


"""
Types that can be assigned to reactions.
"""

Reactor = Union[User, Organization, Mannequin, Bot]


"""
Configurations for project fields.
"""

ProjectV2FieldConfiguration = Union[
    ProjectV2SingleSelectField, ProjectV2IterationField, ProjectV2Field
]


"""
Types that can be inside Project Items.
"""

ProjectV2ItemContent = Union[PullRequest, Issue, DraftIssue]


"""
Types that can be requested reviewers.
"""

RequestedReviewer = Union[User, Team, Mannequin, Bot]


"""
Project field values
"""

ProjectV2ItemFieldValue = Union[
    ProjectV2ItemFieldUserValue,
    ProjectV2ItemFieldTextValue,
    ProjectV2ItemFieldSingleSelectValue,
    ProjectV2ItemFieldReviewerValue,
    ProjectV2ItemFieldRepositoryValue,
    ProjectV2ItemFieldPullRequestValue,
    ProjectV2ItemFieldNumberValue,
    ProjectV2ItemFieldMilestoneValue,
    ProjectV2ItemFieldLabelValue,
    ProjectV2ItemFieldIterationValue,
    ProjectV2ItemFieldDateValue,
]


"""
Types that can grant permissions on a repository to a user
"""

PermissionGranter = Union[Team, Repository, Organization]


"""
Users and teams.
"""

DeploymentReviewer = Union[User, Team]


"""
Used for return value of Repository.issueOrPullRequest.
"""

IssueOrPullRequest = Union[PullRequest, Issue]


"""
Types that can be inside Project Cards.
"""

ProjectCardItem = Union[PullRequest, Issue]


"""
Types that can represent a repository ruleset bypass actor.
"""

BypassActor = Union[Team, App]


"""
Types which can be parameters for `RepositoryRule` objects.
"""

RuleParameters = Union[
    WorkflowsParameters,
    UpdateParameters,
    TagNamePatternParameters,
    RequiredStatusChecksParameters,
    RequiredDeploymentsParameters,
    PullRequestParameters,
    CommitterEmailPatternParameters,
    CommitMessagePatternParameters,
    CommitAuthorEmailPatternParameters,
    BranchNamePatternParameters,
]


"""
Types which can have `RepositoryRule` objects.
"""

RuleSource = Union[Repository, Organization]


"""
Types of memberships that can be restored for an Organization member.
"""

OrgRestoreMemberAuditEntryMembership = Union[
    OrgRestoreMemberMembershipTeamAuditEntryData,
    OrgRestoreMemberMembershipRepositoryAuditEntryData,
    OrgRestoreMemberMembershipOrganizationAuditEntryData,
]


"""
An audit entry in an organization audit log.
"""

OrganizationAuditEntry = Union[
    TeamRemoveRepositoryAuditEntry,
    TeamRemoveMemberAuditEntry,
    TeamChangeParentTeamAuditEntry,
    TeamAddRepositoryAuditEntry,
    TeamAddMemberAuditEntry,
    RepositoryVisibilityChangeEnableAuditEntry,
    RepositoryVisibilityChangeDisableAuditEntry,
    RepoRemoveTopicAuditEntry,
    RepoRemoveMemberAuditEntry,
    RepoDestroyAuditEntry,
    RepoCreateAuditEntry,
    RepoConfigUnlockAnonymousGitAccessAuditEntry,
    RepoConfigLockAnonymousGitAccessAuditEntry,
    RepoConfigEnableSockpuppetDisallowedAuditEntry,
    RepoConfigEnableContributorsOnlyAuditEntry,
    RepoConfigEnableCollaboratorsOnlyAuditEntry,
    RepoConfigEnableAnonymousGitAccessAuditEntry,
    RepoConfigDisableSockpuppetDisallowedAuditEntry,
    RepoConfigDisableContributorsOnlyAuditEntry,
    RepoConfigDisableCollaboratorsOnlyAuditEntry,
    RepoConfigDisableAnonymousGitAccessAuditEntry,
    RepoChangeMergeSettingAuditEntry,
    RepoArchivedAuditEntry,
    RepoAddTopicAuditEntry,
    RepoAddMemberAuditEntry,
    RepoAccessAuditEntry,
    PrivateRepositoryForkingEnableAuditEntry,
    PrivateRepositoryForkingDisableAuditEntry,
    OrgUpdateMemberRepositoryInvitationPermissionAuditEntry,
    OrgUpdateMemberRepositoryCreationPermissionAuditEntry,
    OrgUpdateMemberAuditEntry,
    OrgUpdateDefaultRepositoryPermissionAuditEntry,
    OrgUnblockUserAuditEntry,
    OrgRestoreMemberAuditEntry,
    OrgRemoveOutsideCollaboratorAuditEntry,
    OrgRemoveMemberAuditEntry,
    OrgRemoveBillingManagerAuditEntry,
    OrgOauthAppAccessUnblockedAuditEntry,
    OrgOauthAppAccessRequestedAuditEntry,
    OrgOauthAppAccessDeniedAuditEntry,
    OrgOauthAppAccessBlockedAuditEntry,
    OrgOauthAppAccessApprovedAuditEntry,
    OrgInviteToBusinessAuditEntry,
    OrgInviteMemberAuditEntry,
    OrgEnableTwoFactorRequirementAuditEntry,
    OrgEnableSamlAuditEntry,
    OrgEnableOauthAppRestrictionsAuditEntry,
    OrgDisableTwoFactorRequirementAuditEntry,
    OrgDisableSamlAuditEntry,
    OrgDisableOauthAppRestrictionsAuditEntry,
    OrgCreateAuditEntry,
    OrgConfigEnableCollaboratorsOnlyAuditEntry,
    OrgConfigDisableCollaboratorsOnlyAuditEntry,
    OrgBlockUserAuditEntry,
    OrgAddMemberAuditEntry,
    OrgAddBillingManagerAuditEntry,
    OauthApplicationCreateAuditEntry,
    MembersCanDeleteReposEnableAuditEntry,
    MembersCanDeleteReposDisableAuditEntry,
    MembersCanDeleteReposClearAuditEntry,
]


"""
Types that can own a verifiable domain.
"""

VerifiableDomainOwner = Union[Organization, Enterprise]


"""
Types that can be pinned to a profile page.
"""

PinnableItem = Union[Repository, Gist]


"""
Entities that can sponsor others via GitHub Sponsors
"""

Sponsor = Union[User, Organization]


"""
A record that can be featured on a GitHub Sponsors profile.
"""

SponsorsListingFeatureableItem = Union[User, Repository]


"""
An object that is a member of an enterprise.
"""

EnterpriseMember = Union[User, EnterpriseUserAccount]


"""
Types that can own an IP allow list.
"""

IpAllowListOwner = Union[Organization, Enterprise, App]


"""
Types which can be actors for `BranchActorAllowance` objects.
"""

BranchActorAllowanceActor = Union[User, Team, App]


"""
Types that can be an actor.
"""

PushAllowanceActor = Union[User, Team, App]


"""
Types that can be an actor.
"""

ReviewDismissalAllowanceActor = Union[User, Team, App]


"""
Types that can be assigned to issues.
"""

Assignee = Union[User, Organization, Mannequin, Bot]


"""
The object which triggered a `ClosedEvent`.
"""

Closer = Union[PullRequest, Commit]


"""
Any referencable object
"""

ReferencedSubject = Union[PullRequest, Issue]


"""
Types that can be inside a Milestone.
"""

MilestoneItem = Union[PullRequest, Issue]


"""
An object which has a renamable title
"""

RenamedTitleSubject = Union[PullRequest, Issue]


"""
An item in a pull request timeline
"""

PullRequestTimelineItem = Union[
    UserBlockedEvent,
    UnsubscribedEvent,
    UnlockedEvent,
    UnlabeledEvent,
    UnassignedEvent,
    SubscribedEvent,
    ReviewRequestedEvent,
    ReviewRequestRemovedEvent,
    ReviewDismissedEvent,
    ReopenedEvent,
    RenamedTitleEvent,
    ReferencedEvent,
    PullRequestReviewThread,
    PullRequestReviewComment,
    PullRequestReview,
    MilestonedEvent,
    MergedEvent,
    LockedEvent,
    LabeledEvent,
    IssueComment,
    HeadRefRestoredEvent,
    HeadRefForcePushedEvent,
    HeadRefDeletedEvent,
    DeploymentEnvironmentChangedEvent,
    DeployedEvent,
    DemilestonedEvent,
    CrossReferencedEvent,
    CommitCommentThread,
    Commit,
    ClosedEvent,
    BaseRefForcePushedEvent,
    BaseRefDeletedEvent,
    AssignedEvent,
]


"""
An item in a pull request timeline
"""

PullRequestTimelineItems = Union[
    UserBlockedEvent,
    UnsubscribedEvent,
    UnpinnedEvent,
    UnmarkedAsDuplicateEvent,
    UnlockedEvent,
    UnlabeledEvent,
    UnassignedEvent,
    TransferredEvent,
    SubscribedEvent,
    ReviewRequestedEvent,
    ReviewRequestRemovedEvent,
    ReviewDismissedEvent,
    ReopenedEvent,
    RenamedTitleEvent,
    RemovedFromProjectEvent,
    RemovedFromMergeQueueEvent,
    ReferencedEvent,
    ReadyForReviewEvent,
    PullRequestRevisionMarker,
    PullRequestReviewThread,
    PullRequestReview,
    PullRequestCommitCommentThread,
    PullRequestCommit,
    PinnedEvent,
    MovedColumnsInProjectEvent,
    MilestonedEvent,
    MergedEvent,
    MentionedEvent,
    MarkedAsDuplicateEvent,
    LockedEvent,
    LabeledEvent,
    IssueComment,
    HeadRefRestoredEvent,
    HeadRefForcePushedEvent,
    HeadRefDeletedEvent,
    DisconnectedEvent,
    DeploymentEnvironmentChangedEvent,
    DeployedEvent,
    DemilestonedEvent,
    CrossReferencedEvent,
    ConvertedToDiscussionEvent,
    ConvertedNoteToIssueEvent,
    ConvertToDraftEvent,
    ConnectedEvent,
    CommentDeletedEvent,
    ClosedEvent,
    BaseRefForcePushedEvent,
    BaseRefDeletedEvent,
    BaseRefChangedEvent,
    AutomaticBaseChangeSucceededEvent,
    AutomaticBaseChangeFailedEvent,
    AutoSquashEnabledEvent,
    AutoRebaseEnabledEvent,
    AutoMergeEnabledEvent,
    AutoMergeDisabledEvent,
    AssignedEvent,
    AddedToProjectEvent,
    AddedToMergeQueueEvent,
]


"""
Types that can be inside a StatusCheckRollup context.
"""

StatusCheckRollupContext = Union[StatusContext, CheckRun]


"""
Represents either a issue the viewer can access or a restricted contribution.
"""

CreatedIssueOrRestrictedContribution = Union[
    RestrictedContribution, CreatedIssueContribution
]


"""
Represents either a pull request the viewer can access or a restricted contribution.
"""

CreatedPullRequestOrRestrictedContribution = Union[
    RestrictedContribution, CreatedPullRequestContribution
]


"""
Represents either a repository the viewer can access or a restricted contribution.
"""

CreatedRepositoryOrRestrictedContribution = Union[
    RestrictedContribution, CreatedRepositoryContribution
]


"""
Types that can be added to a user list.
"""

UserListItems = Repository


"""
An item in an issue timeline
"""

IssueTimelineItem = Union[
    UserBlockedEvent,
    UnsubscribedEvent,
    UnlockedEvent,
    UnlabeledEvent,
    UnassignedEvent,
    TransferredEvent,
    SubscribedEvent,
    ReopenedEvent,
    RenamedTitleEvent,
    ReferencedEvent,
    MilestonedEvent,
    LockedEvent,
    LabeledEvent,
    IssueComment,
    DemilestonedEvent,
    CrossReferencedEvent,
    Commit,
    ClosedEvent,
    AssignedEvent,
]


"""
An item in an issue timeline
"""

IssueTimelineItems = Union[
    UserBlockedEvent,
    UnsubscribedEvent,
    UnpinnedEvent,
    UnmarkedAsDuplicateEvent,
    UnlockedEvent,
    UnlabeledEvent,
    UnassignedEvent,
    TransferredEvent,
    SubscribedEvent,
    ReopenedEvent,
    RenamedTitleEvent,
    RemovedFromProjectEvent,
    ReferencedEvent,
    PinnedEvent,
    MovedColumnsInProjectEvent,
    MilestonedEvent,
    MentionedEvent,
    MarkedAsDuplicateEvent,
    LockedEvent,
    LabeledEvent,
    IssueComment,
    DisconnectedEvent,
    DemilestonedEvent,
    CrossReferencedEvent,
    ConvertedToDiscussionEvent,
    ConvertedNoteToIssueEvent,
    ConnectedEvent,
    CommentDeletedEvent,
    ClosedEvent,
    AssignedEvent,
    AddedToProjectEvent,
]


"""
An object which can have its data claimed or claim data from another.
"""

Claimable = Union[User, Mannequin]


"""
Used for argument of CreateProjectV2 mutation.
"""

OrganizationOrUser = Union[User, Organization]


"""
Possible collaborators for a project.
"""

ProjectV2Actor = Union[User, Team]


"""
The results of a search.
"""

SearchResultItem = Union[
    User,
    Repository,
    PullRequest,
    Organization,
    MarketplaceListing,
    Issue,
    Discussion,
    App,
]


"""
Entities that can be sponsored via GitHub Sponsors
"""

SponsorableItem = Union[User, Organization]
