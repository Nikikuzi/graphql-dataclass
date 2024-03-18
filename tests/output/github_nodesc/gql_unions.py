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

AuditEntryActor = Union[User, Organization, Bot]


Reactor = Union[User, Organization, Mannequin, Bot]


ProjectV2FieldConfiguration = Union[
    ProjectV2SingleSelectField, ProjectV2IterationField, ProjectV2Field
]


ProjectV2ItemContent = Union[PullRequest, Issue, DraftIssue]


RequestedReviewer = Union[User, Team, Mannequin, Bot]


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


PermissionGranter = Union[Team, Repository, Organization]


DeploymentReviewer = Union[User, Team]


IssueOrPullRequest = Union[PullRequest, Issue]


ProjectCardItem = Union[PullRequest, Issue]


BypassActor = Union[Team, App]


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


RuleSource = Union[Repository, Organization]


OrgRestoreMemberAuditEntryMembership = Union[
    OrgRestoreMemberMembershipTeamAuditEntryData,
    OrgRestoreMemberMembershipRepositoryAuditEntryData,
    OrgRestoreMemberMembershipOrganizationAuditEntryData,
]


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


VerifiableDomainOwner = Union[Organization, Enterprise]


PinnableItem = Union[Repository, Gist]


Sponsor = Union[User, Organization]


SponsorsListingFeatureableItem = Union[User, Repository]


EnterpriseMember = Union[User, EnterpriseUserAccount]


IpAllowListOwner = Union[Organization, Enterprise, App]


BranchActorAllowanceActor = Union[User, Team, App]


PushAllowanceActor = Union[User, Team, App]


ReviewDismissalAllowanceActor = Union[User, Team, App]


Assignee = Union[User, Organization, Mannequin, Bot]


Closer = Union[PullRequest, Commit]


ReferencedSubject = Union[PullRequest, Issue]


MilestoneItem = Union[PullRequest, Issue]


RenamedTitleSubject = Union[PullRequest, Issue]


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


StatusCheckRollupContext = Union[StatusContext, CheckRun]


CreatedIssueOrRestrictedContribution = Union[
    RestrictedContribution, CreatedIssueContribution
]


CreatedPullRequestOrRestrictedContribution = Union[
    RestrictedContribution, CreatedPullRequestContribution
]


CreatedRepositoryOrRestrictedContribution = Union[
    RestrictedContribution, CreatedRepositoryContribution
]


UserListItems = Repository


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


Claimable = Union[User, Mannequin]


OrganizationOrUser = Union[User, Organization]


ProjectV2Actor = Union[User, Team]


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


SponsorableItem = Union[User, Organization]
