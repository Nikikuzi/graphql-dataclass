from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import (
    ActorType,
    CheckAnnotationLevel,
    CheckConclusionState,
    CheckRunState,
    CheckRunType,
    CheckStatusState,
    CommentAuthorAssociation,
    CommentCannotUpdateReason,
    CommitContributionOrderField,
    ComparisonStatus,
    ContributionLevel,
    DefaultRepositoryPermissionField,
    DeploymentOrderField,
    DeploymentProtectionRuleType,
    DeploymentReviewState,
    DeploymentStatusState,
    DiffSide,
    DiscussionPollOptionOrderField,
    DismissReason,
    EnterpriseAdministratorRole,
    EnterpriseAllowPrivateRepositoryForkingPolicyValue,
    EnterpriseDefaultRepositoryPermissionSettingValue,
    EnterpriseEnabledDisabledSettingValue,
    EnterpriseEnabledSettingValue,
    EnterpriseMemberOrderField,
    EnterpriseMembersCanCreateRepositoriesSettingValue,
    EnterpriseMembersCanMakePurchasesSettingValue,
    EnterpriseServerUserAccountEmailOrderField,
    EnterpriseServerUserAccountsUploadOrderField,
    EnterpriseServerUserAccountsUploadSyncState,
    EnterpriseUserAccountMembershipRole,
    GitSignatureState,
    IpAllowListEnabledSettingValue,
    IpAllowListEntryOrderField,
    IpAllowListForInstalledAppsEnabledSettingValue,
    IssueClosedStateReason,
    IssueState,
    IssueStateReason,
    LabelOrderField,
    LanguageOrderField,
    LockReason,
    MergeQueueEntryState,
    MigrationSourceType,
    MigrationState,
    MilestoneState,
    NotificationRestrictionSettingValue,
    OauthApplicationCreateAuditEntryState,
    OIDCProviderType,
    OperationType,
    OrderDirection,
    OrgAddMemberAuditEntryPermission,
    OrganizationInvitationRole,
    OrganizationInvitationSource,
    OrganizationInvitationType,
    OrganizationMemberRole,
    OrganizationOrderField,
    OrgCreateAuditEntryBillingPlan,
    OrgEnterpriseOwnerOrderField,
    OrgRemoveBillingManagerAuditEntryReason,
    OrgRemoveMemberAuditEntryMembershipType,
    OrgRemoveMemberAuditEntryReason,
    OrgRemoveOutsideCollaboratorAuditEntryMembershipType,
    OrgRemoveOutsideCollaboratorAuditEntryReason,
    OrgUpdateDefaultRepositoryPermissionAuditEntryPermission,
    OrgUpdateMemberAuditEntryPermission,
    OrgUpdateMemberRepositoryCreationPermissionAuditEntryVisibility,
    PackageOrderField,
    PackageVersionOrderField,
    PinnedDiscussionGradient,
    PinnedDiscussionPattern,
    ProjectCardState,
    ProjectState,
    ProjectTemplate,
    ProjectV2CustomFieldType,
    ProjectV2FieldOrderField,
    ProjectV2FieldType,
    ProjectV2ItemOrderField,
    ProjectV2OrderField,
    ProjectV2SingleSelectFieldOptionColor,
    ProjectV2State,
    ProjectV2ViewLayout,
    ProjectV2WorkflowsOrderField,
    PullRequestBranchUpdateMethod,
    PullRequestMergeMethod,
    PullRequestOrderField,
    PullRequestReviewEvent,
    PullRequestReviewState,
    PullRequestReviewThreadSubjectType,
    ReactionContent,
    ReactionOrderField,
    ReleaseOrderField,
    RepoAccessAuditEntryVisibility,
    RepoAddMemberAuditEntryVisibility,
    RepoArchivedAuditEntryVisibility,
    RepoChangeMergeSettingAuditEntryMergeType,
    RepoCreateAuditEntryVisibility,
    RepoDestroyAuditEntryVisibility,
    RepoRemoveMemberAuditEntryVisibility,
    RepositoryInteractionLimit,
    RepositoryInteractionLimitExpiry,
    RepositoryInteractionLimitOrigin,
    RepositoryLockReason,
    RepositoryMigrationOrderDirection,
    RepositoryMigrationOrderField,
    RepositoryPermission,
    RepositoryRuleOrderField,
    RepositoryRulesetBypassActorBypassMode,
    RepositoryRulesetTarget,
    RepositoryRuleType,
    RepositoryVisibility,
    RepositoryVulnerabilityAlertDependencyScope,
    RepositoryVulnerabilityAlertState,
    RequestableCheckStatusState,
    RoleInOrganization,
    RuleEnforcement,
    SamlDigestAlgorithm,
    SamlSignatureAlgorithm,
    SecurityAdvisoryOrderField,
    SecurityAdvisorySeverity,
    SecurityVulnerabilityOrderField,
    SponsorableOrderField,
    SponsorAndLifetimeValueOrderField,
    SponsorsActivityAction,
    SponsorsGoalKind,
    SponsorshipNewsletterOrderField,
    SponsorshipPaymentSource,
    SponsorshipPrivacy,
    StarOrderField,
    StatusState,
    SubscriptionState,
    TeamDiscussionCommentOrderField,
    TeamMemberOrderField,
    TeamMemberRole,
    TeamRepositoryOrderField,
    TeamReviewAssignmentAlgorithm,
    UserBlockDuration,
    VerifiableDomainOrderField,
    WorkflowState,
)
from .gql_simple_types import (
    CWE,
    Actor,
    BulkSponsorship,
    CheckAnnotationPosition,
    CheckRunAction,
    CheckRunOutputImage,
    CheckStep,
    CommitAuthorEmailPatternParametersInput,
    CommitMessage,
    CommitMessagePatternParametersInput,
    ContributionCalendarMonth,
    DeployKey,
    DraftPullRequestReviewComment,
    FileAddition,
    Language,
    LicenseRule,
    MarketplaceCategory,
    OrganizationMigration,
    ProjectV2Collaborator,
    ProjectV2FieldValue,
    ProjectV2IterationFieldIteration,
    ProjectV2SingleSelectFieldOption,
    PropertyTargetDefinition,
    PublicKey,
    PullRequestChangedFile,
    RefNameConditionTarget,
    RepositoryIdConditionTargetInput,
    RepositoryNameConditionTarget,
    RepositoryRulesetBypassActorInput,
    RequiredDeploymentsParametersInput,
    SecurityAdvisoryPackage,
    SocialAccount,
    StatusCheckConfiguration,
    StatusContextStateCount,
    Submodule,
    TagNamePatternParametersInput,
    TextMatchHighlight,
    UserEmailMetadata,
    WorkflowFileReference,
)
from .scalars import (
    HTML,
    ID,
    URI,
    Base64String,
    BigInt,
    Date,
    DateTime,
    GitObjectID,
    GitRefname,
    GitTimestamp,
    PreciseDateTime,
    X509Certificate,
)

if TYPE_CHECKING:
    from .user_connection import UserConnection
    from .pull_request import PullRequest
    from .pull_request_connection import PullRequestConnection
    from .branch_protection_rule import BranchProtectionRule
    from .ref import Ref
    from .app import App
    from .enterprise import Enterprise
    from .enterprise_server_user_account import EnterpriseServerUserAccount
    from .enterprise_server_installation import EnterpriseServerInstallation
    from .organization import Organization
    from .user import User
    from .repository import Repository
    from .team import Team
    from .team_discussion import TeamDiscussion
    from .reaction_group import ReactionGroup
    from .reactable import Reactable
    from .project_v2 import ProjectV2
    from .project_v2_item_connection import ProjectV2ItemConnection
    from .issue import Issue
    from .project_v2_item import ProjectV2Item
    from .commit_comment_connection import CommitCommentConnection
    from .commit import Commit
    from .deployment import Deployment
    from .discussion import Discussion
    from .discussion_comment import DiscussionComment
    from .discussion_poll import DiscussionPoll
    from .release import Release
    from .merge_queue import MergeQueue
    from .package_version import PackageVersion
    from .package import Package
    from .project_column import ProjectColumn
    from .project import Project
    from .topic import Topic
    from .repository_ruleset import RepositoryRuleset
    from .security_advisory import SecurityAdvisory
    from .ip_allow_list_entry_connection import IpAllowListEntryConnection
    from .gist import Gist
    from .sponsorable import Sponsorable
    from .sponsors_tier import SponsorsTier
    from .sponsors_listing import SponsorsListing
    from .issue_comment_edge import IssueCommentEdge
    from .issue_comment import IssueComment
    from .pull_request_review import PullRequestReview
    from .pull_request_review_comment import PullRequestReviewComment
    from .check_suite import CheckSuite
    from .workflow_run import WorkflowRun
    from .user_edge import UserEdge
    from .gql_unions import AuditEntryActor
    from .gql_unions import Reactor
    from .gql_unions import ProjectV2FieldConfiguration
    from .gql_unions import RequestedReviewer
    from .gql_unions import ProjectV2ItemFieldValue
    from .gql_unions import PermissionGranter
    from .gql_unions import DeploymentReviewer
    from .gql_unions import IssueOrPullRequest
    from .gql_unions import ProjectCardItem
    from .gql_unions import BypassActor
    from .gql_unions import RuleParameters
    from .gql_unions import OrgRestoreMemberAuditEntryMembership
    from .gql_unions import OrganizationAuditEntry
    from .gql_unions import VerifiableDomainOwner
    from .gql_unions import PinnableItem
    from .gql_unions import Sponsor
    from .gql_unions import SponsorsListingFeatureableItem
    from .gql_unions import EnterpriseMember
    from .gql_unions import IpAllowListOwner
    from .gql_unions import BranchActorAllowanceActor
    from .gql_unions import PushAllowanceActor
    from .gql_unions import ReviewDismissalAllowanceActor
    from .gql_unions import Assignee
    from .gql_unions import Closer
    from .gql_unions import ReferencedSubject
    from .gql_unions import MilestoneItem
    from .gql_unions import RenamedTitleSubject
    from .gql_unions import PullRequestTimelineItem
    from .gql_unions import PullRequestTimelineItems
    from .gql_unions import StatusCheckRollupContext
    from .gql_unions import UserListItems
    from .gql_unions import IssueTimelineItem
    from .gql_unions import IssueTimelineItems
    from .gql_unions import Claimable
    from .gql_unions import ProjectV2Actor
    from .gql_unions import SearchResultItem
    from .gql_unions import SponsorableItem


@dataclass(kw_only=True)
class AbortQueuedMigrationsPayload:
    """
    AbortQueuedMigrationsPayload - Autogenerated return type of AbortQueuedMigrations

    clientMutationId - A unique identifier for the client performing the mutation.

    success - Did the operation succeed?

    """

    client_mutation_id: Optional[str] = None
    success: Optional[bool] = None


@dataclass(kw_only=True)
class AbortRepositoryMigrationPayload:
    """
    AbortRepositoryMigrationPayload - Autogenerated return type of AbortRepositoryMigration

    clientMutationId - A unique identifier for the client performing the mutation.

    success - Did the operation succeed?

    """

    client_mutation_id: Optional[str] = None
    success: Optional[bool] = None


@dataclass(kw_only=True)
class AcceptTopicSuggestionInput:
    """
        AcceptTopicSuggestionInput - Autogenerated input type of AcceptTopicSuggestion

        clientMutationId - A unique identifier for the client performing the mutation.

        name - The name of the suggested topic.

    **Upcoming Change on 2024-04-01 UTC**
    **Description:** `name` will be removed.
    **Reason:** Suggested topics are no longer supported

        repositoryId - The Node ID of the repository.

    **Upcoming Change on 2024-04-01 UTC**
    **Description:** `repositoryId` will be removed.
    **Reason:** Suggested topics are no longer supported

    """

    client_mutation_id: Optional[str] = None
    name: Optional[str] = None
    repository_id: Optional[ID] = None


@dataclass(kw_only=True)
class ActorLocation:
    """
    ActorLocation - Location information for an actor

    city - City

    country - Country name

    countryCode - Country code

    region - Region name

    regionCode - Region or state code

    """

    city: Optional[str] = None
    country: Optional[str] = None
    country_code: Optional[str] = None
    region: Optional[str] = None
    region_code: Optional[str] = None


@dataclass(kw_only=True)
class AddCommentInput:
    """
    AddCommentInput - Autogenerated input type of AddComment

    body - The contents of the comment.

    clientMutationId - A unique identifier for the client performing the mutation.

    subjectId - The Node ID of the subject to modify.

    """

    body: str
    client_mutation_id: Optional[str] = None
    subject_id: ID


@dataclass(kw_only=True)
class AddDiscussionPollVoteInput:
    """
    AddDiscussionPollVoteInput - Autogenerated input type of AddDiscussionPollVote

    clientMutationId - A unique identifier for the client performing the mutation.

    pollOptionId - The Node ID of the discussion poll option to vote for.

    """

    client_mutation_id: Optional[str] = None
    poll_option_id: ID


@dataclass(kw_only=True)
class AddEnterpriseSupportEntitlementInput:
    """
    AddEnterpriseSupportEntitlementInput - Autogenerated input type of AddEnterpriseSupportEntitlement

    clientMutationId - A unique identifier for the client performing the mutation.

    enterpriseId - The ID of the Enterprise which the admin belongs to.

    login - The login of a member who will receive the support entitlement.

    """

    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    login: str


@dataclass(kw_only=True)
class AddLabelsToLabelableInput:
    """
    AddLabelsToLabelableInput - Autogenerated input type of AddLabelsToLabelable

    clientMutationId - A unique identifier for the client performing the mutation.

    labelIds - The ids of the labels to add.

    labelableId - The id of the labelable object to add labels to.

    """

    client_mutation_id: Optional[str] = None
    label_ids: list[ID]
    labelable_id: ID


@dataclass(kw_only=True)
class AddProjectColumnInput:
    """
    AddProjectColumnInput - Autogenerated input type of AddProjectColumn

    clientMutationId - A unique identifier for the client performing the mutation.

    name - The name of the column.

    projectId - The Node ID of the project.

    """

    client_mutation_id: Optional[str] = None
    name: str
    project_id: ID


@dataclass(kw_only=True)
class AddProjectV2ItemByIdInput:
    """
    AddProjectV2ItemByIdInput - Autogenerated input type of AddProjectV2ItemById

    clientMutationId - A unique identifier for the client performing the mutation.

    contentId - The id of the Issue or Pull Request to add.

    projectId - The ID of the Project to add the item to.

    """

    client_mutation_id: Optional[str] = None
    content_id: ID
    project_id: ID


@dataclass(kw_only=True)
class AddPullRequestReviewThreadInput:
    """
        AddPullRequestReviewThreadInput - Autogenerated input type of AddPullRequestReviewThread

        body - Body of the thread's first comment.

        clientMutationId - A unique identifier for the client performing the mutation.

        line - The line of the blob to which the thread refers, required for line-level
    threads. The end of the line range for multi-line comments.

        path - Path to the file being commented on.

        pullRequestId - The node ID of the pull request reviewing

        pullRequestReviewId - The Node ID of the review to modify.

        side - The side of the diff on which the line resides. For multi-line comments, this is the side for the end of the line range.

        startLine - The first line of the range to which the comment refers.

        startSide - The side of the diff on which the start line resides.

        subjectType - The level at which the comments in the corresponding thread are targeted, can be a diff line or a file

    """

    body: str
    client_mutation_id: Optional[str] = None
    line: Optional[int] = None
    path: str
    pull_request_id: Optional[ID] = None
    pull_request_review_id: Optional[ID] = None
    side: Optional[DiffSide] = None
    start_line: Optional[int] = None
    start_side: Optional[DiffSide] = None
    subject_type: Optional[PullRequestReviewThreadSubjectType] = None


@dataclass(kw_only=True)
class AddReactionInput:
    """
    AddReactionInput - Autogenerated input type of AddReaction

    clientMutationId - A unique identifier for the client performing the mutation.

    content - The name of the emoji to react with.

    subjectId - The Node ID of the subject to modify.

    """

    client_mutation_id: Optional[str] = None
    content: ReactionContent
    subject_id: ID


@dataclass(kw_only=True)
class AddUpvoteInput:
    """
    AddUpvoteInput - Autogenerated input type of AddUpvote

    clientMutationId - A unique identifier for the client performing the mutation.

    subjectId - The Node ID of the discussion or comment to upvote.

    """

    client_mutation_id: Optional[str] = None
    subject_id: ID


@dataclass(kw_only=True)
class AnnouncementBanner:
    """
    AnnouncementBanner - Represents an announcement banner.

    announcement - The text of the announcement

    announcementExpiresAt - The expiration date of the announcement, if any

    announcementUserDismissible - Whether the announcement can be dismissed by the user

    """

    announcement: Optional[str] = None
    announcement_expires_at: Optional[DateTime] = None
    announcement_user_dismissible: Optional[bool] = None


@dataclass(kw_only=True)
class ApproveVerifiableDomainInput:
    """
    ApproveVerifiableDomainInput - Autogenerated input type of ApproveVerifiableDomain

    clientMutationId - A unique identifier for the client performing the mutation.

    id - The ID of the verifiable domain to approve.

    """

    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class ArchiveRepositoryInput:
    """
    ArchiveRepositoryInput - Autogenerated input type of ArchiveRepository

    clientMutationId - A unique identifier for the client performing the mutation.

    repositoryId - The ID of the repository to mark as archived.

    """

    client_mutation_id: Optional[str] = None
    repository_id: ID


@dataclass(kw_only=True)
class Bot:
    """
    Bot - A special type of user which takes actions on behalf of GitHub Apps.

    avatarUrl - A URL pointing to the GitHub App's public avatar.

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    id - The Node ID of the Bot object

    login - The username of the actor.

    resourcePath - The HTTP path for this bot

    updatedAt - Identifies the date and time when the object was last updated.

    url - The HTTP URL for this bot

    """

    avatar_url: URI
    created_at: DateTime
    database_id: Optional[int] = None
    id: ID
    login: str
    resource_path: URI
    updated_at: DateTime
    url: URI


@dataclass(kw_only=True)
class BranchNamePatternParametersInput:
    """
    BranchNamePatternParametersInput - Parameters to be used for the branch_name_pattern rule

    name - How this rule will appear to users.

    negate - If true, the rule will fail if the pattern matches.

    operator - The operator to use for matching.

    pattern - The pattern to match with.

    """

    name: Optional[str] = None
    negate: Optional[bool] = None
    operator: str
    pattern: str


@dataclass(kw_only=True)
class CVSS:
    """
    CVSS - The Common Vulnerability Scoring System

    score - The CVSS score associated with this advisory

    vectorString - The CVSS vector string associated with this advisory

    """

    score: float
    vector_string: Optional[str] = None


@dataclass(kw_only=True)
class CancelEnterpriseAdminInvitationInput:
    """
    CancelEnterpriseAdminInvitationInput - Autogenerated input type of CancelEnterpriseAdminInvitation

    clientMutationId - A unique identifier for the client performing the mutation.

    invitationId - The Node ID of the pending enterprise administrator invitation.

    """

    client_mutation_id: Optional[str] = None
    invitation_id: ID


@dataclass(kw_only=True)
class ChangeUserStatusInput:
    """
        ChangeUserStatusInput - Autogenerated input type of ChangeUserStatus

        clientMutationId - A unique identifier for the client performing the mutation.

        emoji - The emoji to represent your status. Can either be a native Unicode emoji or an emoji name with colons, e.g., :grinning:.

        expiresAt - If set, the user status will not be shown after this date.

        limitedAvailability - Whether this status should indicate you are not fully available on GitHub, e.g., you are away.

        message - A short description of your current status.

        organizationId - The ID of the organization whose members will be allowed to see the status. If
    omitted, the status will be publicly visible.

    """

    client_mutation_id: Optional[str] = None
    emoji: Optional[str] = None
    expires_at: Optional[DateTime] = None
    limited_availability: Optional[bool] = None
    message: Optional[str] = None
    organization_id: Optional[ID] = None


@dataclass(kw_only=True)
class CheckAnnotationRange:
    """
    CheckAnnotationRange - Information from a check run analysis to specific lines of code.

    endColumn - The ending column of the range.

    endLine - The ending line of the range.

    startColumn - The starting column of the range.

    startLine - The starting line of the range.

    """

    end_column: Optional[int] = None
    end_line: int
    start_column: Optional[int] = None
    start_line: int


@dataclass(kw_only=True)
class CheckRunFilter:
    """
    CheckRunFilter - The filters that are available when fetching check runs.

    appId - Filters the check runs created by this application ID.

    checkName - Filters the check runs by this name.

    checkType - Filters the check runs by this type.

    conclusions - Filters the check runs by these conclusions.

    status - Filters the check runs by this status. Superceded by statuses.

    statuses - Filters the check runs by this status. Overrides status.

    """

    app_id: Optional[int] = None
    check_name: Optional[str] = None
    check_type: Optional[CheckRunType] = None
    conclusions: Optional[list[CheckConclusionState]] = None
    status: Optional[CheckStatusState] = None
    statuses: Optional[list[CheckStatusState]] = None


@dataclass(kw_only=True)
class CheckRunStateCount:
    """
    CheckRunStateCount - Represents a count of the state of a check run.

    count - The number of check runs with this state.

    state - The state of a check run.

    """

    count: int
    state: CheckRunState


@dataclass(kw_only=True)
class CheckSuiteAutoTriggerPreference:
    """
    CheckSuiteAutoTriggerPreference - The auto-trigger preferences that are available for check suites.

    appId - The node ID of the application that owns the check suite.

    setting - Set to `true` to enable automatic creation of CheckSuite events upon pushes to the repository.

    """

    app_id: ID
    setting: bool


@dataclass(kw_only=True)
class ClearLabelsFromLabelableInput:
    """
    ClearLabelsFromLabelableInput - Autogenerated input type of ClearLabelsFromLabelable

    clientMutationId - A unique identifier for the client performing the mutation.

    labelableId - The id of the labelable object to clear the labels from.

    """

    client_mutation_id: Optional[str] = None
    labelable_id: ID


@dataclass(kw_only=True)
class CloneProjectInput:
    """
    CloneProjectInput - Autogenerated input type of CloneProject

    body - The description of the project.

    clientMutationId - A unique identifier for the client performing the mutation.

    includeWorkflows - Whether or not to clone the source project's workflows.

    name - The name of the project.

    public - The visibility of the project, defaults to false (private).

    sourceId - The source project to clone.

    targetOwnerId - The owner ID to create the project under.

    """

    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    include_workflows: bool
    name: str
    public: Optional[bool] = None
    source_id: ID
    target_owner_id: ID


@dataclass(kw_only=True)
class Closable:
    """
    Closable - An object that can be closed

    closed - Indicates if the object is closed (definition of closed may depend on type)

    closedAt - Identifies the date and time when the object was closed.

    viewerCanClose - Indicates if the object can be closed by the viewer.

    viewerCanReopen - Indicates if the object can be reopened by the viewer.

    """

    closed: bool
    closed_at: Optional[DateTime] = None
    viewer_can_close: bool
    viewer_can_reopen: bool


@dataclass(kw_only=True)
class CloseIssueInput:
    """
    CloseIssueInput - Autogenerated input type of CloseIssue

    clientMutationId - A unique identifier for the client performing the mutation.

    issueId - ID of the issue to be closed.

    stateReason - The reason the issue is to be closed.

    """

    client_mutation_id: Optional[str] = None
    issue_id: ID
    state_reason: Optional[IssueClosedStateReason] = None


@dataclass(kw_only=True)
class CodeOfConduct:
    """
    CodeOfConduct - The Code of Conduct for a repository

    body - The body of the Code of Conduct

    id - The Node ID of the CodeOfConduct object

    key - The key for the Code of Conduct

    name - The formal name of the Code of Conduct

    resourcePath - The HTTP path for this Code of Conduct

    url - The HTTP URL for this Code of Conduct

    """

    body: Optional[str] = None
    id: ID
    key: str
    name: str
    resource_path: Optional[URI] = None
    url: Optional[URI] = None


@dataclass(kw_only=True)
class CommitAuthorEmailPatternParameters:
    """
    CommitAuthorEmailPatternParameters - Parameters to be used for the commit_author_email_pattern rule

    name - How this rule will appear to users.

    negate - If true, the rule will fail if the pattern matches.

    operator - The operator to use for matching.

    pattern - The pattern to match with.

    """

    name: Optional[str] = None
    negate: bool
    operator: str
    pattern: str


@dataclass(kw_only=True)
class CommitContributionOrder:
    """
    CommitContributionOrder - Ordering options for commit contribution connections.

    direction - The ordering direction.

    field - The field by which to order commit contributions.

    """

    direction: OrderDirection
    field: CommitContributionOrderField


@dataclass(kw_only=True)
class CommitMessagePatternParameters:
    """
    CommitMessagePatternParameters - Parameters to be used for the commit_message_pattern rule

    name - How this rule will appear to users.

    negate - If true, the rule will fail if the pattern matches.

    operator - The operator to use for matching.

    pattern - The pattern to match with.

    """

    name: Optional[str] = None
    negate: bool
    operator: str
    pattern: str


@dataclass(kw_only=True)
class CommittableBranch:
    """
        CommittableBranch - A git ref for a commit to be appended to.

    The ref must be a branch, i.e. its fully qualified name must start
    with `refs/heads/` (although the input is not required to be fully
    qualified).

    The Ref may be specified by its global node ID or by the
    `repositoryNameWithOwner` and `branchName`.

    ### Examples

    Specify a branch using a global node ID:

        { "id": "MDM6UmVmMTpyZWZzL2hlYWRzL21haW4=" }

    Specify a branch using `repositoryNameWithOwner` and `branchName`:

        {
          "repositoryNameWithOwner": "github/graphql-client",
          "branchName": "main"
        }

        branchName - The unqualified name of the branch to append the commit to.

        id - The Node ID of the Ref to be updated.

        repositoryNameWithOwner - The nameWithOwner of the repository to commit to.

    """

    branch_name: Optional[str] = None
    id: Optional[ID] = None
    repository_name_with_owner: Optional[str] = None


@dataclass(kw_only=True)
class CommitterEmailPatternParametersInput:
    """
    CommitterEmailPatternParametersInput - Parameters to be used for the committer_email_pattern rule

    name - How this rule will appear to users.

    negate - If true, the rule will fail if the pattern matches.

    operator - The operator to use for matching.

    pattern - The pattern to match with.

    """

    name: Optional[str] = None
    negate: Optional[bool] = None
    operator: str
    pattern: str


@dataclass(kw_only=True)
class ContributionCalendarDay:
    """
        ContributionCalendarDay - Represents a single day of contributions on GitHub by a user.

        color - The hex color code that represents how many contributions were made on this day compared to others in the calendar.

        contributionCount - How many contributions were made by the user on this day.

        contributionLevel - Indication of contributions, relative to other days. Can be used to indicate
    which color to represent this day on a calendar.

        date - The day this square represents.

        weekday - A number representing which day of the week this square represents, e.g., 1 is Monday.

    """

    color: str
    contribution_count: int
    contribution_level: ContributionLevel
    date: Date
    weekday: int


@dataclass(kw_only=True)
class ContributionOrder:
    """
    ContributionOrder - Ordering options for contribution connections.

    direction - The ordering direction.

    """

    direction: OrderDirection


@dataclass(kw_only=True)
class ConvertPullRequestToDraftInput:
    """
    ConvertPullRequestToDraftInput - Autogenerated input type of ConvertPullRequestToDraft

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequestId - ID of the pull request to convert to draft

    """

    client_mutation_id: Optional[str] = None
    pull_request_id: ID


@dataclass(kw_only=True)
class CreateAttributionInvitationInput:
    """
    CreateAttributionInvitationInput - Autogenerated input type of CreateAttributionInvitation

    clientMutationId - A unique identifier for the client performing the mutation.

    ownerId - The Node ID of the owner scoping the reattributable data.

    sourceId - The Node ID of the account owning the data to reattribute.

    targetId - The Node ID of the account which may claim the data.

    """

    client_mutation_id: Optional[str] = None
    owner_id: ID
    source_id: ID
    target_id: ID


@dataclass(kw_only=True)
class CreateDeploymentInput:
    """
        CreateDeploymentInput - Autogenerated input type of CreateDeployment

        autoMerge - Attempt to automatically merge the default branch into the requested ref, defaults to true.

        clientMutationId - A unique identifier for the client performing the mutation.

        description - Short description of the deployment.

        environment - Name for the target deployment environment.

        payload - JSON payload with extra information about the deployment.

        refId - The node ID of the ref to be deployed.

        repositoryId - The node ID of the repository.

        requiredContexts - The status contexts to verify against commit status checks. To bypass required
    contexts, pass an empty array. Defaults to all unique contexts.

        task - Specifies a task to execute.

    """

    auto_merge: Optional[bool] = None
    client_mutation_id: Optional[str] = None
    description: Optional[str] = None
    environment: Optional[str] = None
    payload: Optional[str] = None
    ref_id: ID
    repository_id: ID
    required_contexts: Optional[list[str]] = None
    task: Optional[str] = None


@dataclass(kw_only=True)
class CreateDiscussionInput:
    """
    CreateDiscussionInput - Autogenerated input type of CreateDiscussion

    body - The body of the discussion.

    categoryId - The id of the discussion category to associate with this discussion.

    clientMutationId - A unique identifier for the client performing the mutation.

    repositoryId - The id of the repository on which to create the discussion.

    title - The title of the discussion.

    """

    body: str
    category_id: ID
    client_mutation_id: Optional[str] = None
    repository_id: ID
    title: str


@dataclass(kw_only=True)
class CreateEnvironmentInput:
    """
    CreateEnvironmentInput - Autogenerated input type of CreateEnvironment

    clientMutationId - A unique identifier for the client performing the mutation.

    name - The name of the environment.

    repositoryId - The node ID of the repository.

    """

    client_mutation_id: Optional[str] = None
    name: str
    repository_id: ID


@dataclass(kw_only=True)
class CreateIssueInput:
    """
    CreateIssueInput - Autogenerated input type of CreateIssue

    assigneeIds - The Node ID for the user assignee for this issue.

    body - The body for the issue description.

    clientMutationId - A unique identifier for the client performing the mutation.

    issueTemplate - The name of an issue template in the repository, assigns labels and assignees from the template to the issue

    labelIds - An array of Node IDs of labels for this issue.

    milestoneId - The Node ID of the milestone for this issue.

    projectIds - An array of Node IDs for projects associated with this issue.

    repositoryId - The Node ID of the repository.

    title - The title for the issue.

    """

    assignee_ids: Optional[list[ID]] = None
    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    issue_template: Optional[str] = None
    label_ids: Optional[list[ID]] = None
    milestone_id: Optional[ID] = None
    project_ids: Optional[list[ID]] = None
    repository_id: ID
    title: str


@dataclass(kw_only=True)
class CreateLinkedBranchInput:
    """
    CreateLinkedBranchInput - Autogenerated input type of CreateLinkedBranch

    clientMutationId - A unique identifier for the client performing the mutation.

    issueId - ID of the issue to link to.

    name - The name of the new branch. Defaults to issue number and title.

    oid - The commit SHA to base the new branch on.

    repositoryId - ID of the repository to create the branch in. Defaults to the issue repository.

    """

    client_mutation_id: Optional[str] = None
    issue_id: ID
    name: Optional[str] = None
    oid: GitObjectID
    repository_id: Optional[ID] = None


@dataclass(kw_only=True)
class CreateProjectInput:
    """
    CreateProjectInput - Autogenerated input type of CreateProject

    body - The description of project.

    clientMutationId - A unique identifier for the client performing the mutation.

    name - The name of project.

    ownerId - The owner ID to create the project under.

    repositoryIds - A list of repository IDs to create as linked repositories for the project

    template - The name of the GitHub-provided template.

    """

    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    name: str
    owner_id: ID
    repository_ids: Optional[list[ID]] = None
    template: Optional[ProjectTemplate] = None


@dataclass(kw_only=True)
class CreatePullRequestInput:
    """
        CreatePullRequestInput - Autogenerated input type of CreatePullRequest

        baseRefName - The name of the branch you want your changes pulled into. This should be an existing branch
    on the current repository. You cannot update the base branch on a pull request to point
    to another repository.

        body - The contents of the pull request.

        clientMutationId - A unique identifier for the client performing the mutation.

        draft - Indicates whether this pull request should be a draft.

        headRefName - The name of the branch where your changes are implemented. For cross-repository pull requests
    in the same network, namespace `head_ref_name` with a user like this: `username:branch`.

        headRepositoryId - The Node ID of the head repository.

        maintainerCanModify - Indicates whether maintainers can modify the pull request.

        repositoryId - The Node ID of the repository.

        title - The title of the pull request.

    """

    base_ref_name: str
    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    draft: Optional[bool] = None
    head_ref_name: str
    head_repository_id: Optional[ID] = None
    maintainer_can_modify: Optional[bool] = None
    repository_id: ID
    title: str


@dataclass(kw_only=True)
class CreateRepositoryInput:
    """
        CreateRepositoryInput - Autogenerated input type of CreateRepository

        clientMutationId - A unique identifier for the client performing the mutation.

        description - A short description of the new repository.

        hasIssuesEnabled - Indicates if the repository should have the issues feature enabled.

        hasWikiEnabled - Indicates if the repository should have the wiki feature enabled.

        homepageUrl - The URL for a web page about this repository.

        name - The name of the new repository.

        ownerId - The ID of the owner for the new repository.

        teamId - When an organization is specified as the owner, this ID identifies the team
    that should be granted access to the new repository.

        template - Whether this repository should be marked as a template such that anyone who
    can access it can create new repositories with the same files and directory structure.

        visibility - Indicates the repository's visibility level.

    """

    client_mutation_id: Optional[str] = None
    description: Optional[str] = None
    has_issues_enabled: Optional[bool] = None
    has_wiki_enabled: Optional[bool] = None
    homepage_url: Optional[URI] = None
    name: str
    owner_id: Optional[ID] = None
    team_id: Optional[ID] = None
    template: Optional[bool] = None
    visibility: RepositoryVisibility


@dataclass(kw_only=True)
class CreateSponsorsTierInput:
    """
        CreateSponsorsTierInput - Autogenerated input type of CreateSponsorsTier

        amount - The value of the new tier in US dollars. Valid values: 1-12000.

        clientMutationId - A unique identifier for the client performing the mutation.

        description - A description of what this tier is, what perks sponsors might receive, what a sponsorship at this tier means for you, etc.

        isRecurring - Whether sponsorships using this tier should happen monthly/yearly or just once.

        publish - Whether to make the tier available immediately for sponsors to choose.
    Defaults to creating a draft tier that will not be publicly visible.

        repositoryId - Optional ID of the private repository that sponsors at this tier should gain
    read-only access to. Must be owned by an organization.

        repositoryName - Optional name of the private repository that sponsors at this tier should gain
    read-only access to. Must be owned by an organization. Necessary if
    repositoryOwnerLogin is given. Will be ignored if repositoryId is given.

        repositoryOwnerLogin - Optional login of the organization owner of the private repository that
    sponsors at this tier should gain read-only access to. Necessary if
    repositoryName is given. Will be ignored if repositoryId is given.

        sponsorableId - The ID of the user or organization who owns the GitHub Sponsors profile.
    Defaults to the current user if omitted and sponsorableLogin is not given.

        sponsorableLogin - The username of the user or organization who owns the GitHub Sponsors profile.
    Defaults to the current user if omitted and sponsorableId is not given.

        welcomeMessage - Optional message new sponsors at this tier will receive.

    """

    amount: int
    client_mutation_id: Optional[str] = None
    description: str
    is_recurring: Optional[bool] = None
    publish: Optional[bool] = None
    repository_id: Optional[ID] = None
    repository_name: Optional[str] = None
    repository_owner_login: Optional[str] = None
    sponsorable_id: Optional[ID] = None
    sponsorable_login: Optional[str] = None
    welcome_message: Optional[str] = None


@dataclass(kw_only=True)
class CreateTeamDiscussionCommentInput:
    """
        CreateTeamDiscussionCommentInput - Autogenerated input type of CreateTeamDiscussionComment

        body - The content of the comment. This field is required.

    **Upcoming Change on 2024-07-01 UTC**
    **Description:** `body` will be removed. Follow the guide at
    https://github.blog/changelog/2023-02-08-sunset-notice-team-discussions/ to
    find a suitable replacement.
    **Reason:** The Team Discussions feature is deprecated in favor of Organization Discussions.

        clientMutationId - A unique identifier for the client performing the mutation.

        discussionId - The ID of the discussion to which the comment belongs. This field is required.

    **Upcoming Change on 2024-07-01 UTC**
    **Description:** `discussionId` will be removed. Follow the guide at
    https://github.blog/changelog/2023-02-08-sunset-notice-team-discussions/ to
    find a suitable replacement.
    **Reason:** The Team Discussions feature is deprecated in favor of Organization Discussions.

    """

    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    discussion_id: Optional[ID] = None


@dataclass(kw_only=True)
class CreateUserListInput:
    """
    CreateUserListInput - Autogenerated input type of CreateUserList

    clientMutationId - A unique identifier for the client performing the mutation.

    description - A description of the list

    isPrivate - Whether or not the list is private

    name - The name of the new list

    """

    client_mutation_id: Optional[str] = None
    description: Optional[str] = None
    is_private: Optional[bool] = None
    name: str


@dataclass(kw_only=True)
class Deletable:
    """
    Deletable - Entities that can be deleted.

    viewerCanDelete - Check if the current viewer can delete this object.

    """

    viewer_can_delete: bool


@dataclass(kw_only=True)
class DeleteBranchProtectionRulePayload:
    """
    DeleteBranchProtectionRulePayload - Autogenerated return type of DeleteBranchProtectionRule

    clientMutationId - A unique identifier for the client performing the mutation.

    """

    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class DeleteDeploymentPayload:
    """
    DeleteDeploymentPayload - Autogenerated return type of DeleteDeployment

    clientMutationId - A unique identifier for the client performing the mutation.

    """

    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class DeleteDiscussionInput:
    """
    DeleteDiscussionInput - Autogenerated input type of DeleteDiscussion

    clientMutationId - A unique identifier for the client performing the mutation.

    id - The id of the discussion to delete.

    """

    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class DeleteEnvironmentPayload:
    """
    DeleteEnvironmentPayload - Autogenerated return type of DeleteEnvironment

    clientMutationId - A unique identifier for the client performing the mutation.

    """

    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class DeleteIssueCommentInput:
    """
    DeleteIssueCommentInput - Autogenerated input type of DeleteIssueComment

    clientMutationId - A unique identifier for the client performing the mutation.

    id - The ID of the comment to delete.

    """

    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class DeleteIssueInput:
    """
    DeleteIssueInput - Autogenerated input type of DeleteIssue

    clientMutationId - A unique identifier for the client performing the mutation.

    issueId - The ID of the issue to delete.

    """

    client_mutation_id: Optional[str] = None
    issue_id: ID


@dataclass(kw_only=True)
class DeleteLabelPayload:
    """
    DeleteLabelPayload - Autogenerated return type of DeleteLabel

    clientMutationId - A unique identifier for the client performing the mutation.

    """

    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class DeletePackageVersionInput:
    """
    DeletePackageVersionInput - Autogenerated input type of DeletePackageVersion

    clientMutationId - A unique identifier for the client performing the mutation.

    packageVersionId - The ID of the package version to be deleted.

    """

    client_mutation_id: Optional[str] = None
    package_version_id: ID


@dataclass(kw_only=True)
class DeleteProjectCardInput:
    """
    DeleteProjectCardInput - Autogenerated input type of DeleteProjectCard

    cardId - The id of the card to delete.

    clientMutationId - A unique identifier for the client performing the mutation.

    """

    card_id: ID
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class DeleteProjectInput:
    """
    DeleteProjectInput - Autogenerated input type of DeleteProject

    clientMutationId - A unique identifier for the client performing the mutation.

    projectId - The Project ID to update.

    """

    client_mutation_id: Optional[str] = None
    project_id: ID


@dataclass(kw_only=True)
class DeleteProjectV2Input:
    """
    DeleteProjectV2Input - Autogenerated input type of DeleteProjectV2

    clientMutationId - A unique identifier for the client performing the mutation.

    projectId - The ID of the Project to delete.

    """

    client_mutation_id: Optional[str] = None
    project_id: ID


@dataclass(kw_only=True)
class DeleteProjectV2ItemPayload:
    """
    DeleteProjectV2ItemPayload - Autogenerated return type of DeleteProjectV2Item

    clientMutationId - A unique identifier for the client performing the mutation.

    deletedItemId - The ID of the deleted item.

    """

    client_mutation_id: Optional[str] = None
    deleted_item_id: Optional[ID] = None


@dataclass(kw_only=True)
class DeletePullRequestReviewCommentInput:
    """
    DeletePullRequestReviewCommentInput - Autogenerated input type of DeletePullRequestReviewComment

    clientMutationId - A unique identifier for the client performing the mutation.

    id - The ID of the comment to delete.

    """

    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class DeleteRefInput:
    """
    DeleteRefInput - Autogenerated input type of DeleteRef

    clientMutationId - A unique identifier for the client performing the mutation.

    refId - The Node ID of the Ref to be deleted.

    """

    client_mutation_id: Optional[str] = None
    ref_id: ID


@dataclass(kw_only=True)
class DeleteRepositoryRulesetInput:
    """
    DeleteRepositoryRulesetInput - Autogenerated input type of DeleteRepositoryRuleset

    clientMutationId - A unique identifier for the client performing the mutation.

    repositoryRulesetId - The global relay id of the repository ruleset to be deleted.

    """

    client_mutation_id: Optional[str] = None
    repository_ruleset_id: ID


@dataclass(kw_only=True)
class DeleteTeamDiscussionCommentInput:
    """
    DeleteTeamDiscussionCommentInput - Autogenerated input type of DeleteTeamDiscussionComment

    clientMutationId - A unique identifier for the client performing the mutation.

    id - The ID of the comment to delete.

    """

    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class DeleteTeamDiscussionInput:
    """
    DeleteTeamDiscussionInput - Autogenerated input type of DeleteTeamDiscussion

    clientMutationId - A unique identifier for the client performing the mutation.

    id - The discussion ID to delete.

    """

    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class DeleteUserListInput:
    """
    DeleteUserListInput - Autogenerated input type of DeleteUserList

    clientMutationId - A unique identifier for the client performing the mutation.

    listId - The ID of the list to delete.

    """

    client_mutation_id: Optional[str] = None
    list_id: ID


@dataclass(kw_only=True)
class DependabotUpdateError:
    """
    DependabotUpdateError - An error produced from a Dependabot Update

    body - The body of the error

    errorType - The error code

    title - The title of the error

    """

    body: str
    error_type: str
    title: str


@dataclass(kw_only=True)
class DeploymentOrder:
    """
    DeploymentOrder - Ordering options for deployment connections

    direction - The ordering direction.

    field - The field to order deployments by.

    """

    direction: OrderDirection
    field: DeploymentOrderField


@dataclass(kw_only=True)
class DisablePullRequestAutoMergeInput:
    """
    DisablePullRequestAutoMergeInput - Autogenerated input type of DisablePullRequestAutoMerge

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequestId - ID of the pull request to disable auto merge on.

    """

    client_mutation_id: Optional[str] = None
    pull_request_id: ID


@dataclass(kw_only=True)
class DiscussionPollOptionOrder:
    """
    DiscussionPollOptionOrder - Ordering options for discussion poll option connections.

    direction - The ordering direction.

    field - The field to order poll options by.

    """

    direction: OrderDirection
    field: DiscussionPollOptionOrderField


@dataclass(kw_only=True)
class DismissRepositoryVulnerabilityAlertInput:
    """
    DismissRepositoryVulnerabilityAlertInput - Autogenerated input type of DismissRepositoryVulnerabilityAlert

    clientMutationId - A unique identifier for the client performing the mutation.

    dismissReason - The reason the Dependabot alert is being dismissed.

    repositoryVulnerabilityAlertId - The Dependabot alert ID to dismiss.

    """

    client_mutation_id: Optional[str] = None
    dismiss_reason: DismissReason
    repository_vulnerability_alert_id: ID


@dataclass(kw_only=True)
class DraftPullRequestReviewThread:
    """
    DraftPullRequestReviewThread - Specifies a review comment thread to be left with a Pull Request Review.

    body - Body of the comment to leave.

    line - The line of the blob to which the thread refers. The end of the line range for multi-line comments.

    path - Path to the file being commented on.

    side - The side of the diff on which the line resides. For multi-line comments, this is the side for the end of the line range.

    startLine - The first line of the range to which the comment refers.

    startSide - The side of the diff on which the start line resides.

    """

    body: str
    line: int
    path: str
    side: Optional[DiffSide] = None
    start_line: Optional[int] = None
    start_side: Optional[DiffSide] = None


@dataclass(kw_only=True)
class EnqueuePullRequestInput:
    """
    EnqueuePullRequestInput - Autogenerated input type of EnqueuePullRequest

    clientMutationId - A unique identifier for the client performing the mutation.

    expectedHeadOid - The expected head OID of the pull request.

    jump - Add the pull request to the front of the queue.

    pullRequestId - The ID of the pull request to enqueue.

    """

    client_mutation_id: Optional[str] = None
    expected_head_oid: Optional[GitObjectID] = None
    jump: Optional[bool] = None
    pull_request_id: ID


@dataclass(kw_only=True)
class EnterpriseAuditEntryData:
    """
    EnterpriseAuditEntryData - Metadata for an audit entry containing enterprise account information.

    enterpriseResourcePath - The HTTP path for this enterprise.

    enterpriseSlug - The slug of the enterprise.

    enterpriseUrl - The HTTP URL for this enterprise.

    """

    enterprise_resource_path: Optional[URI] = None
    enterprise_slug: Optional[str] = None
    enterprise_url: Optional[URI] = None


@dataclass(kw_only=True)
class EnterpriseMemberOrder:
    """
    EnterpriseMemberOrder - Ordering options for enterprise member connections.

    direction - The ordering direction.

    field - The field to order enterprise members by.

    """

    direction: OrderDirection
    field: EnterpriseMemberOrderField


@dataclass(kw_only=True)
class EnterpriseRepositoryInfo:
    """
    EnterpriseRepositoryInfo - A subset of repository information queryable from an enterprise.

    id - The Node ID of the EnterpriseRepositoryInfo object

    isPrivate - Identifies if the repository is private or internal.

    name - The repository's name.

    nameWithOwner - The repository's name with owner.

    """

    id: ID
    is_private: bool
    name: str
    name_with_owner: str


@dataclass(kw_only=True)
class EnterpriseServerUserAccountEmailOrder:
    """
    EnterpriseServerUserAccountEmailOrder - Ordering options for Enterprise Server user account email connections.

    direction - The ordering direction.

    field - The field to order emails by.

    """

    direction: OrderDirection
    field: EnterpriseServerUserAccountEmailOrderField


@dataclass(kw_only=True)
class EnterpriseServerUserAccountsUploadOrder:
    """
    EnterpriseServerUserAccountsUploadOrder - Ordering options for Enterprise Server user accounts upload connections.

    direction - The ordering direction.

    field - The field to order user accounts uploads by.

    """

    direction: OrderDirection
    field: EnterpriseServerUserAccountsUploadOrderField


@dataclass(kw_only=True)
class ExternalIdentityAttribute:
    """
    ExternalIdentityAttribute - An attribute for the External Identity attributes collection

    metadata - The attribute metadata as JSON

    name - The attribute name

    value - The attribute value

    """

    metadata: Optional[str] = None
    name: str
    value: str


@dataclass(kw_only=True)
class FileDeletion:
    """
    FileDeletion - A command to delete the file at the given path as part of a commit.

    path - The path to delete

    """

    path: str


@dataclass(kw_only=True)
class FollowUserInput:
    """
    FollowUserInput - Autogenerated input type of FollowUser

    clientMutationId - A unique identifier for the client performing the mutation.

    userId - ID of the user to follow.

    """

    client_mutation_id: Optional[str] = None
    user_id: ID


@dataclass(kw_only=True)
class GenericHovercardContext:
    """
    GenericHovercardContext - A generic hovercard context with a message and icon

    message - A string describing this context

    octicon - An octicon to accompany this context

    """

    message: str
    octicon: str


@dataclass(kw_only=True)
class GitHubMetadata:
    """
    GitHubMetadata - Represents information about the GitHub instance.

    gitHubServicesSha - Returns a String that's a SHA of `github-services`

    gitIpAddresses - IP addresses that users connect to for git operations

    githubEnterpriseImporterIpAddresses - IP addresses that GitHub Enterprise Importer uses for outbound connections

    hookIpAddresses - IP addresses that service hooks are sent from

    importerIpAddresses - IP addresses that the importer connects from

    isPasswordAuthenticationVerifiable - Whether or not users are verified

    pagesIpAddresses - IP addresses for GitHub Pages' A records

    """

    git_hub_services_sha: GitObjectID
    git_ip_addresses: Optional[list[str]] = None
    github_enterprise_importer_ip_addresses: Optional[list[str]] = None
    hook_ip_addresses: Optional[list[str]] = None
    importer_ip_addresses: Optional[list[str]] = None
    is_password_authentication_verifiable: bool
    pages_ip_addresses: Optional[list[str]] = None


@dataclass(kw_only=True)
class GrantMigratorRoleInput:
    """
    GrantMigratorRoleInput - Autogenerated input type of GrantMigratorRole

    actor - The user login or Team slug to grant the migrator role.

    actorType - Specifies the type of the actor, can be either USER or TEAM.

    clientMutationId - A unique identifier for the client performing the mutation.

    organizationId - The ID of the organization that the user/team belongs to.

    """

    actor: str
    actor_type: ActorType
    client_mutation_id: Optional[str] = None
    organization_id: ID


@dataclass(kw_only=True)
class HovercardContext:
    """
    HovercardContext - An individual line of a hovercard

    message - A string describing this context

    octicon - An octicon to accompany this context

    """

    message: str
    octicon: str


@dataclass(kw_only=True)
class IpAllowListEntryOrder:
    """
    IpAllowListEntryOrder - Ordering options for IP allow list entry connections.

    direction - The ordering direction.

    field - The field to order IP allow list entries by.

    """

    direction: OrderDirection
    field: IpAllowListEntryOrderField


@dataclass(kw_only=True)
class IssueFilters:
    """
        IssueFilters - Ways in which to filter lists of issues.

        assignee - List issues assigned to given name. Pass in `null` for issues with no assigned
    user, and `*` for issues assigned to any user.

        createdBy - List issues created by given name.

        labels - List issues where the list of label names exist on the issue.

        mentioned - List issues where the given name is mentioned in the issue.

        milestone - List issues by given milestone argument. If an string representation of an
    integer is passed, it should refer to a milestone by its database ID. Pass in
    `null` for issues with no milestone, and `*` for issues that are assigned to any milestone.

        milestoneNumber - List issues by given milestone argument. If an string representation of an
    integer is passed, it should refer to a milestone by its number field. Pass in
    `null` for issues with no milestone, and `*` for issues that are assigned to any milestone.

        since - List issues that have been updated at or after the given date.

        states - List issues filtered by the list of states given.

        viewerSubscribed - List issues subscribed to by viewer.

    """

    assignee: Optional[str] = None
    created_by: Optional[str] = None
    labels: Optional[list[str]] = None
    mentioned: Optional[str] = None
    milestone: Optional[str] = None
    milestone_number: Optional[str] = None
    since: Optional[DateTime] = None
    states: Optional[list[IssueState]] = None
    viewer_subscribed: Optional[bool] = None


@dataclass(kw_only=True)
class LabelOrder:
    """
    LabelOrder - Ways in which lists of labels can be ordered upon return.

    direction - The direction in which to order labels by the specified field.

    field - The field in which to order labels by.

    """

    direction: OrderDirection
    field: LabelOrderField


@dataclass(kw_only=True)
class LanguageOrder:
    """
    LanguageOrder - Ordering options for language connections.

    direction - The ordering direction.

    field - The field to order languages by.

    """

    direction: OrderDirection
    field: LanguageOrderField


@dataclass(kw_only=True)
class LinkProjectV2ToRepositoryInput:
    """
    LinkProjectV2ToRepositoryInput - Autogenerated input type of LinkProjectV2ToRepository

    clientMutationId - A unique identifier for the client performing the mutation.

    projectId - The ID of the project to link to the repository.

    repositoryId - The ID of the repository to link to the project.

    """

    client_mutation_id: Optional[str] = None
    project_id: ID
    repository_id: ID


@dataclass(kw_only=True)
class LinkRepositoryToProjectInput:
    """
    LinkRepositoryToProjectInput - Autogenerated input type of LinkRepositoryToProject

    clientMutationId - A unique identifier for the client performing the mutation.

    projectId - The ID of the Project to link to a Repository

    repositoryId - The ID of the Repository to link to a Project.

    """

    client_mutation_id: Optional[str] = None
    project_id: ID
    repository_id: ID


@dataclass(kw_only=True)
class Lockable:
    """
    Lockable - An object that can be locked.

    activeLockReason - Reason that the conversation was locked.

    locked - `true` if the object is locked

    """

    active_lock_reason: Optional[LockReason] = None
    locked: bool


@dataclass(kw_only=True)
class MarkDiscussionCommentAsAnswerInput:
    """
    MarkDiscussionCommentAsAnswerInput - Autogenerated input type of MarkDiscussionCommentAsAnswer

    clientMutationId - A unique identifier for the client performing the mutation.

    id - The Node ID of the discussion comment to mark as an answer.

    """

    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class MarkNotificationAsDoneInput:
    """
    MarkNotificationAsDoneInput - Autogenerated input type of MarkNotificationAsDone

    clientMutationId - A unique identifier for the client performing the mutation.

    id - The NotificationThread id.

    """

    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class MarkPullRequestReadyForReviewInput:
    """
    MarkPullRequestReadyForReviewInput - Autogenerated input type of MarkPullRequestReadyForReview

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequestId - ID of the pull request to be marked as ready for review.

    """

    client_mutation_id: Optional[str] = None
    pull_request_id: ID


@dataclass(kw_only=True)
class MemberFeatureRequestNotification:
    """
    MemberFeatureRequestNotification - Represents a member feature request notification

    body - Represents member feature request body containing organization name and the number of feature requests

    id - The Node ID of the MemberFeatureRequestNotification object

    title - Represents member feature request notification title

    updatedAt - Identifies the date and time when the object was last updated.

    """

    body: str
    id: ID
    title: str
    updated_at: DateTime


@dataclass(kw_only=True)
class MergePullRequestInput:
    """
    MergePullRequestInput - Autogenerated input type of MergePullRequest

    authorEmail - The email address to associate with this merge.

    clientMutationId - A unique identifier for the client performing the mutation.

    commitBody - Commit body to use for the merge commit; if omitted, a default message will be used

    commitHeadline - Commit headline to use for the merge commit; if omitted, a default message will be used.

    expectedHeadOid - OID that the pull request head ref must match to allow merge; if omitted, no check is performed.

    mergeMethod - The merge method to use. If omitted, defaults to 'MERGE'

    pullRequestId - ID of the pull request to be merged.

    """

    author_email: Optional[str] = None
    client_mutation_id: Optional[str] = None
    commit_body: Optional[str] = None
    commit_headline: Optional[str] = None
    expected_head_oid: Optional[GitObjectID] = None
    merge_method: Optional[PullRequestMergeMethod] = None
    pull_request_id: ID


@dataclass(kw_only=True)
class MigrationSource:
    """
    MigrationSource - A GitHub Enterprise Importer (GEI) migration source.

    id - The Node ID of the MigrationSource object

    name - The migration source name.

    type - The migration source type.

    url - The migration source URL, for example `https://github.com` or `https://monalisa.ghe.com`.

    """

    id: ID
    name: str
    type: MigrationSourceType
    url: URI


@dataclass(kw_only=True)
class Minimizable:
    """
        Minimizable - Entities that can be minimized.

        isMinimized - Returns whether or not a comment has been minimized.

        minimizedReason - Returns why the comment was minimized. One of `abuse`, `off-topic`,
    `outdated`, `resolved`, `duplicate` and `spam`. Note that the case and
    formatting of these values differs from the inputs to the `MinimizeComment` mutation.

        viewerCanMinimize - Check if the current viewer can minimize this object.

    """

    is_minimized: bool
    minimized_reason: Optional[str] = None
    viewer_can_minimize: bool


@dataclass(kw_only=True)
class MoveProjectCardInput:
    """
    MoveProjectCardInput - Autogenerated input type of MoveProjectCard

    afterCardId - Place the new card after the card with this id. Pass null to place it at the top.

    cardId - The id of the card to move.

    clientMutationId - A unique identifier for the client performing the mutation.

    columnId - The id of the column to move it into.

    """

    after_card_id: Optional[ID] = None
    card_id: ID
    client_mutation_id: Optional[str] = None
    column_id: ID


@dataclass(kw_only=True)
class Node:
    """
    Node - An object with an ID.

    id - ID of the object.

    """

    id: ID


@dataclass(kw_only=True)
class OrgEnterpriseOwnerOrder:
    """
    OrgEnterpriseOwnerOrder - Ordering options for an organization's enterprise owner connections.

    direction - The ordering direction.

    field - The field to order enterprise owners by.

    """

    direction: OrderDirection
    field: OrgEnterpriseOwnerOrderField


@dataclass(kw_only=True)
class OrganizationOrder:
    """
    OrganizationOrder - Ordering options for organization connections.

    direction - The ordering direction.

    field - The field to order organizations by.

    """

    direction: OrderDirection
    field: OrganizationOrderField


@dataclass(kw_only=True)
class PackageOrder:
    """
    PackageOrder - Ways in which lists of packages can be ordered upon return.

    direction - The direction in which to order packages by the specified field.

    field - The field in which to order packages by.

    """

    direction: Optional[OrderDirection] = None
    field: Optional[PackageOrderField] = None


@dataclass(kw_only=True)
class PackageVersionOrder:
    """
    PackageVersionOrder - Ways in which lists of package versions can be ordered upon return.

    direction - The direction in which to order package versions by the specified field.

    field - The field in which to order package versions by.

    """

    direction: Optional[OrderDirection] = None
    field: Optional[PackageVersionOrderField] = None


@dataclass(kw_only=True)
class PageInfo:
    """
    PageInfo - Information about pagination in a connection.

    endCursor - When paginating forwards, the cursor to continue.

    hasNextPage - When paginating forwards, are there more items?

    hasPreviousPage - When paginating backwards, are there more items?

    startCursor - When paginating backwards, the cursor to continue.

    """

    end_cursor: Optional[str] = None
    has_next_page: bool
    has_previous_page: bool
    start_cursor: Optional[str] = None


@dataclass(kw_only=True)
class ProjectCardImport:
    """
    ProjectCardImport - An issue or PR and its owning repository to be used in a project card.

    number - The issue or pull request number.

    repository - Repository name with owner (owner/repository).

    """

    number: int
    repository: str


@dataclass(kw_only=True)
class ProjectProgress:
    """
    ProjectProgress - Project progress stats.

    doneCount - The number of done cards.

    donePercentage - The percentage of done cards.

    enabled - Whether progress tracking is enabled and cards with purpose exist for this project

    inProgressCount - The number of in-progress cards.

    inProgressPercentage - The percentage of in-progress cards.

    todoCount - The number of to do cards.

    todoPercentage - The percentage of to do cards.

    """

    done_count: int
    done_percentage: float
    enabled: bool
    in_progress_count: int
    in_progress_percentage: float
    todo_count: int
    todo_percentage: float


@dataclass(kw_only=True)
class ProjectV2FieldOrder:
    """
    ProjectV2FieldOrder - Ordering options for project v2 field connections

    direction - The ordering direction.

    field - The field to order the project v2 fields by.

    """

    direction: OrderDirection
    field: ProjectV2FieldOrderField


@dataclass(kw_only=True)
class ProjectV2Filters:
    """
    ProjectV2Filters - Ways in which to filter lists of projects.

    state - List project v2 filtered by the state given.

    """

    state: Optional[ProjectV2State] = None


@dataclass(kw_only=True)
class ProjectV2ItemOrder:
    """
    ProjectV2ItemOrder - Ordering options for project v2 item connections

    direction - The ordering direction.

    field - The field to order the project v2 items by.

    """

    direction: OrderDirection
    field: ProjectV2ItemOrderField


@dataclass(kw_only=True)
class ProjectV2Order:
    """
    ProjectV2Order - Ways in which lists of projects can be ordered upon return.

    direction - The direction in which to order projects by the specified field.

    field - The field in which to order projects by.

    """

    direction: OrderDirection
    field: ProjectV2OrderField


@dataclass(kw_only=True)
class ProjectV2SingleSelectFieldOptionInput:
    """
    ProjectV2SingleSelectFieldOptionInput - Represents a single select field option

    color - The display color of the option

    description - The description text of the option

    name - The name of the option

    """

    color: ProjectV2SingleSelectFieldOptionColor
    description: str
    name: str


@dataclass(kw_only=True)
class ProjectV2WorkflowOrder:
    """
    ProjectV2WorkflowOrder - Ordering options for project v2 workflows connections

    direction - The ordering direction.

    field - The field to order the project v2 workflows by.

    """

    direction: OrderDirection
    field: ProjectV2WorkflowsOrderField


@dataclass(kw_only=True)
class PropertyTargetDefinitionInput:
    """
    PropertyTargetDefinitionInput - A property that must match

    name - The name of the property

    propertyValues - The values to match for

    """

    name: str
    property_values: list[str]


@dataclass(kw_only=True)
class PublishSponsorsTierInput:
    """
    PublishSponsorsTierInput - Autogenerated input type of PublishSponsorsTier

    clientMutationId - A unique identifier for the client performing the mutation.

    tierId - The ID of the draft tier to publish.

    """

    client_mutation_id: Optional[str] = None
    tier_id: ID


@dataclass(kw_only=True)
class PullRequestOrder:
    """
    PullRequestOrder - Ways in which lists of issues can be ordered upon return.

    direction - The direction in which to order pull requests by the specified field.

    field - The field in which to order pull requests by.

    """

    direction: OrderDirection
    field: PullRequestOrderField


@dataclass(kw_only=True)
class PullRequestParametersInput:
    """
    PullRequestParametersInput - Require all commits be made to a non-target branch and submitted via a pull request before they can be merged.

    dismissStaleReviewsOnPush - New, reviewable commits pushed will dismiss previous pull request review approvals.

    requireCodeOwnerReview - Require an approving review in pull requests that modify files that have a designated code owner.

    requireLastPushApproval - Whether the most recent reviewable push must be approved by someone other than the person who pushed it.

    requiredApprovingReviewCount - The number of approving reviews that are required before a pull request can be merged.

    requiredReviewThreadResolution - All conversations on code must be resolved before a pull request can be merged.

    """

    dismiss_stale_reviews_on_push: bool
    require_code_owner_review: bool
    require_last_push_approval: bool
    required_approving_review_count: int
    required_review_thread_resolution: bool


@dataclass(kw_only=True)
class ReactionOrder:
    """
    ReactionOrder - Ways in which lists of reactions can be ordered upon return.

    direction - The direction in which to order reactions by the specified field.

    field - The field in which to order reactions by.

    """

    direction: OrderDirection
    field: ReactionOrderField


@dataclass(kw_only=True)
class RefNameConditionTargetInput:
    """
        RefNameConditionTargetInput - Parameters to be used for the ref_name condition

        exclude - Array of ref names or patterns to exclude. The condition will not pass if any of these patterns match.

        include - Array of ref names or patterns to include. One of these patterns must match
    for the condition to pass. Also accepts `~DEFAULT_BRANCH` to include the
    default branch or `~ALL` to include all branches.

    """

    exclude: list[str]
    include: list[str]


@dataclass(kw_only=True)
class RefUpdate:
    """
    RefUpdate - A ref update

    afterOid - The value this ref should be updated to.

    beforeOid - The value this ref needs to point to before the update.

    force - Force a non fast-forward update.

    name - The fully qualified name of the ref to be update. For example `refs/heads/branch-name`

    """

    after_oid: GitObjectID
    before_oid: Optional[GitObjectID] = None
    force: Optional[bool] = None
    name: GitRefname


@dataclass(kw_only=True)
class RegenerateEnterpriseIdentityProviderRecoveryCodesInput:
    """
    RegenerateEnterpriseIdentityProviderRecoveryCodesInput - Autogenerated input type of RegenerateEnterpriseIdentityProviderRecoveryCodes

    clientMutationId - A unique identifier for the client performing the mutation.

    enterpriseId - The ID of the enterprise on which to set an identity provider.

    """

    client_mutation_id: Optional[str] = None
    enterprise_id: ID


@dataclass(kw_only=True)
class RegenerateVerifiableDomainTokenPayload:
    """
    RegenerateVerifiableDomainTokenPayload - Autogenerated return type of RegenerateVerifiableDomainToken

    clientMutationId - A unique identifier for the client performing the mutation.

    verificationToken - The verification token that was generated.

    """

    client_mutation_id: Optional[str] = None
    verification_token: Optional[str] = None


@dataclass(kw_only=True)
class ReleaseOrder:
    """
    ReleaseOrder - Ways in which lists of releases can be ordered upon return.

    direction - The direction in which to order releases by the specified field.

    field - The field in which to order releases by.

    """

    direction: OrderDirection
    field: ReleaseOrderField


@dataclass(kw_only=True)
class RemoveEnterpriseAdminInput:
    """
    RemoveEnterpriseAdminInput - Autogenerated input type of RemoveEnterpriseAdmin

    clientMutationId - A unique identifier for the client performing the mutation.

    enterpriseId - The Enterprise ID from which to remove the administrator.

    login - The login of the user to remove as an administrator.

    """

    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    login: str


@dataclass(kw_only=True)
class RemoveEnterpriseMemberInput:
    """
    RemoveEnterpriseMemberInput - Autogenerated input type of RemoveEnterpriseMember

    clientMutationId - A unique identifier for the client performing the mutation.

    enterpriseId - The ID of the enterprise from which the user should be removed.

    userId - The ID of the user to remove from the enterprise.

    """

    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    user_id: ID


@dataclass(kw_only=True)
class RemoveEnterpriseSupportEntitlementInput:
    """
    RemoveEnterpriseSupportEntitlementInput - Autogenerated input type of RemoveEnterpriseSupportEntitlement

    clientMutationId - A unique identifier for the client performing the mutation.

    enterpriseId - The ID of the Enterprise which the admin belongs to.

    login - The login of a member who will lose the support entitlement.

    """

    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    login: str


@dataclass(kw_only=True)
class RemoveLabelsFromLabelableInput:
    """
    RemoveLabelsFromLabelableInput - Autogenerated input type of RemoveLabelsFromLabelable

    clientMutationId - A unique identifier for the client performing the mutation.

    labelIds - The ids of labels to remove.

    labelableId - The id of the Labelable to remove labels from.

    """

    client_mutation_id: Optional[str] = None
    label_ids: list[ID]
    labelable_id: ID


@dataclass(kw_only=True)
class RemoveReactionInput:
    """
    RemoveReactionInput - Autogenerated input type of RemoveReaction

    clientMutationId - A unique identifier for the client performing the mutation.

    content - The name of the emoji reaction to remove.

    subjectId - The Node ID of the subject to modify.

    """

    client_mutation_id: Optional[str] = None
    content: ReactionContent
    subject_id: ID


@dataclass(kw_only=True)
class RemoveUpvoteInput:
    """
    RemoveUpvoteInput - Autogenerated input type of RemoveUpvote

    clientMutationId - A unique identifier for the client performing the mutation.

    subjectId - The Node ID of the discussion or comment to remove upvote.

    """

    client_mutation_id: Optional[str] = None
    subject_id: ID


@dataclass(kw_only=True)
class ReopenIssueInput:
    """
    ReopenIssueInput - Autogenerated input type of ReopenIssue

    clientMutationId - A unique identifier for the client performing the mutation.

    issueId - ID of the issue to be opened.

    """

    client_mutation_id: Optional[str] = None
    issue_id: ID


@dataclass(kw_only=True)
class RepositoryCodeownersError:
    """
    RepositoryCodeownersError - An error in a `CODEOWNERS` file.

    column - The column number where the error occurs.

    kind - A short string describing the type of error.

    line - The line number where the error occurs.

    message - A complete description of the error, combining information from other fields.

    path - The path to the file when the error occurs.

    source - The content of the line where the error occurs.

    suggestion - A suggestion of how to fix the error.

    """

    column: int
    kind: str
    line: int
    message: str
    path: str
    source: str
    suggestion: Optional[str] = None


@dataclass(kw_only=True)
class RepositoryIdConditionTarget:
    """
    RepositoryIdConditionTarget - Parameters to be used for the repository_id condition

    repositoryIds - One of these repo IDs must match the repo.

    """

    repository_ids: list[ID]


@dataclass(kw_only=True)
class RepositoryInteractionAbility:
    """
    RepositoryInteractionAbility - Repository interaction limit that applies to this object.

    expiresAt - The time the currently active limit expires.

    limit - The current limit that is enabled on this object.

    origin - The origin of the currently active interaction limit.

    """

    expires_at: Optional[DateTime] = None
    limit: RepositoryInteractionLimit
    origin: RepositoryInteractionLimitOrigin


@dataclass(kw_only=True)
class RepositoryMigrationOrder:
    """
    RepositoryMigrationOrder - Ordering options for repository migrations.

    direction - The ordering direction.

    field - The field to order repository migrations by.

    """

    direction: RepositoryMigrationOrderDirection
    field: RepositoryMigrationOrderField


@dataclass(kw_only=True)
class RepositoryNameConditionTargetInput:
    """
        RepositoryNameConditionTargetInput - Parameters to be used for the repository_name condition

        exclude - Array of repository names or patterns to exclude. The condition will not pass if any of these patterns match.

        include - Array of repository names or patterns to include. One of these patterns must
    match for the condition to pass. Also accepts `~ALL` to include all repositories.

        protected - Target changes that match these patterns will be prevented except by those with bypass permissions.

    """

    exclude: list[str]
    include: list[str]
    protected: Optional[bool] = None


@dataclass(kw_only=True)
class RepositoryRuleOrder:
    """
    RepositoryRuleOrder - Ordering options for repository rules.

    direction - The ordering direction.

    field - The field to order repository rules by.

    """

    direction: OrderDirection
    field: RepositoryRuleOrderField


@dataclass(kw_only=True)
class RequestReviewsInput:
    """
    RequestReviewsInput - Autogenerated input type of RequestReviews

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequestId - The Node ID of the pull request to modify.

    teamIds - The Node IDs of the team to request.

    union - Add users to the set rather than replace.

    userIds - The Node IDs of the user to request.

    """

    client_mutation_id: Optional[str] = None
    pull_request_id: ID
    team_ids: Optional[list[ID]] = None
    union: Optional[bool] = None
    user_ids: Optional[list[ID]] = None


@dataclass(kw_only=True)
class RequiredDeploymentsParameters:
    """
    RequiredDeploymentsParameters - Choose which environments must be successfully deployed to before refs can be pushed into a ref that matches this rule.

    requiredDeploymentEnvironments - The environments that must be successfully deployed to before branches can be merged.

    """

    required_deployment_environments: list[str]


@dataclass(kw_only=True)
class RequiredStatusCheckInput:
    """
        RequiredStatusCheckInput - Specifies the attributes for a new or updated required status check.

        appId - The ID of the App that must set the status in order for it to be accepted.
    Omit this value to use whichever app has recently been setting this status, or
    use "any" to allow any app to set the status.

        context - Status check context that must pass for commits to be accepted to the matching branch.

    """

    app_id: Optional[ID] = None
    context: str


@dataclass(kw_only=True)
class ResolveReviewThreadInput:
    """
    ResolveReviewThreadInput - Autogenerated input type of ResolveReviewThread

    clientMutationId - A unique identifier for the client performing the mutation.

    threadId - The ID of the thread to resolve

    """

    client_mutation_id: Optional[str] = None
    thread_id: ID


@dataclass(kw_only=True)
class RevertPullRequestInput:
    """
    RevertPullRequestInput - Autogenerated input type of RevertPullRequest

    body - The description of the revert pull request.

    clientMutationId - A unique identifier for the client performing the mutation.

    draft - Indicates whether the revert pull request should be a draft.

    pullRequestId - The ID of the pull request to revert.

    title - The title of the revert pull request.

    """

    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    draft: Optional[bool] = None
    pull_request_id: ID
    title: Optional[str] = None


@dataclass(kw_only=True)
class RevokeEnterpriseOrganizationsMigratorRoleInput:
    """
    RevokeEnterpriseOrganizationsMigratorRoleInput - Autogenerated input type of RevokeEnterpriseOrganizationsMigratorRole

    clientMutationId - A unique identifier for the client performing the mutation.

    enterpriseId - The ID of the enterprise to which all organizations managed by it will be granted the migrator role.

    login - The login of the user to revoke the migrator role

    """

    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    login: str


@dataclass(kw_only=True)
class RevokeMigratorRolePayload:
    """
    RevokeMigratorRolePayload - Autogenerated return type of RevokeMigratorRole

    clientMutationId - A unique identifier for the client performing the mutation.

    success - Did the operation succeed?

    """

    client_mutation_id: Optional[str] = None
    success: Optional[bool] = None


@dataclass(kw_only=True)
class SecurityAdvisoryIdentifier:
    """
    SecurityAdvisoryIdentifier - A GitHub Security Advisory Identifier

    type - The identifier type, e.g. GHSA, CVE

    value - The identifier

    """

    type: str
    value: str


@dataclass(kw_only=True)
class SecurityAdvisoryOrder:
    """
    SecurityAdvisoryOrder - Ordering options for security advisory connections

    direction - The ordering direction.

    field - The field to order security advisories by.

    """

    direction: OrderDirection
    field: SecurityAdvisoryOrderField


@dataclass(kw_only=True)
class SecurityAdvisoryPackageVersion:
    """
    SecurityAdvisoryPackageVersion - An individual package version

    identifier - The package name or version

    """

    identifier: str


@dataclass(kw_only=True)
class SecurityVulnerabilityOrder:
    """
    SecurityVulnerabilityOrder - Ordering options for security vulnerability connections

    direction - The ordering direction.

    field - The field to order security vulnerabilities by.

    """

    direction: OrderDirection
    field: SecurityVulnerabilityOrderField


@dataclass(kw_only=True)
class SetOrganizationInteractionLimitInput:
    """
    SetOrganizationInteractionLimitInput - Autogenerated input type of SetOrganizationInteractionLimit

    clientMutationId - A unique identifier for the client performing the mutation.

    expiry - When this limit should expire.

    limit - The limit to set.

    organizationId - The ID of the organization to set a limit for.

    """

    client_mutation_id: Optional[str] = None
    expiry: Optional[RepositoryInteractionLimitExpiry] = None
    limit: RepositoryInteractionLimit
    organization_id: ID


@dataclass(kw_only=True)
class SetUserInteractionLimitInput:
    """
    SetUserInteractionLimitInput - Autogenerated input type of SetUserInteractionLimit

    clientMutationId - A unique identifier for the client performing the mutation.

    expiry - When this limit should expire.

    limit - The limit to set.

    userId - The ID of the user to set a limit for.

    """

    client_mutation_id: Optional[str] = None
    expiry: Optional[RepositoryInteractionLimitExpiry] = None
    limit: RepositoryInteractionLimit
    user_id: ID


@dataclass(kw_only=True)
class SponsorAndLifetimeValueOrder:
    """
    SponsorAndLifetimeValueOrder - Ordering options for connections to get sponsor entities and associated USD amounts for GitHub Sponsors.

    direction - The ordering direction.

    field - The field to order results by.

    """

    direction: OrderDirection
    field: SponsorAndLifetimeValueOrderField


@dataclass(kw_only=True)
class SponsorableOrder:
    """
    SponsorableOrder - Ordering options for connections to get sponsorable entities for GitHub Sponsors.

    direction - The ordering direction.

    field - The field to order sponsorable entities by.

    """

    direction: OrderDirection
    field: SponsorableOrderField


@dataclass(kw_only=True)
class SponsorsGoal:
    """
        SponsorsGoal - A goal associated with a GitHub Sponsors listing, representing a target the sponsored maintainer would like to attain.

        description - A description of the goal from the maintainer.

        kind - What the objective of this goal is.

        percentComplete - The percentage representing how complete this goal is, between 0-100.

        targetValue - What the goal amount is. Represents an amount in USD for monthly sponsorship
    amount goals. Represents a count of unique sponsors for total sponsors count goals.

        title - A brief summary of the kind and target value of this goal.

    """

    description: Optional[str] = None
    kind: SponsorsGoalKind
    percent_complete: int
    target_value: int
    title: str


@dataclass(kw_only=True)
class SponsorshipNewsletterOrder:
    """
    SponsorshipNewsletterOrder - Ordering options for sponsorship newsletter connections.

    direction - The ordering direction.

    field - The field to order sponsorship newsletters by.

    """

    direction: OrderDirection
    field: SponsorshipNewsletterOrderField


@dataclass(kw_only=True)
class StarOrder:
    """
    StarOrder - Ways in which star connections can be ordered.

    direction - The direction in which to order nodes.

    field - The field in which to order nodes by.

    """

    direction: OrderDirection
    field: StarOrderField


@dataclass(kw_only=True)
class StartRepositoryMigrationInput:
    """
    StartRepositoryMigrationInput - Autogenerated input type of StartRepositoryMigration

    accessToken - The migration source access token.

    clientMutationId - A unique identifier for the client performing the mutation.

    continueOnError - Whether to continue the migration on error. Defaults to `true`.

    gitArchiveUrl - The signed URL to access the user-uploaded git archive.

    githubPat - The GitHub personal access token of the user importing to the target repository.

    lockSource - Whether to lock the source repository.

    metadataArchiveUrl - The signed URL to access the user-uploaded metadata archive.

    ownerId - The ID of the organization that will own the imported repository.

    repositoryName - The name of the imported repository.

    skipReleases - Whether to skip migrating releases for the repository.

    sourceId - The ID of the migration source.

    sourceRepositoryUrl - The URL of the source repository.

    targetRepoVisibility - The visibility of the imported repository.

    """

    access_token: Optional[str] = None
    client_mutation_id: Optional[str] = None
    continue_on_error: Optional[bool] = None
    git_archive_url: Optional[str] = None
    github_pat: Optional[str] = None
    lock_source: Optional[bool] = None
    metadata_archive_url: Optional[str] = None
    owner_id: ID
    repository_name: str
    skip_releases: Optional[bool] = None
    source_id: ID
    source_repository_url: Optional[URI] = None
    target_repo_visibility: Optional[str] = None


@dataclass(kw_only=True)
class StatusCheckConfigurationInput:
    """
    StatusCheckConfigurationInput - Required status check

    context - The status check context name that must be present on the commit.

    integrationId - The optional integration ID that this status check must originate from.

    """

    context: str
    integration_id: Optional[int] = None


@dataclass(kw_only=True)
class SubmitPullRequestReviewInput:
    """
    SubmitPullRequestReviewInput - Autogenerated input type of SubmitPullRequestReview

    body - The text field to set on the Pull Request Review.

    clientMutationId - A unique identifier for the client performing the mutation.

    event - The event to send to the Pull Request Review.

    pullRequestId - The Pull Request ID to submit any pending reviews.

    pullRequestReviewId - The Pull Request Review ID to submit.

    """

    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    event: PullRequestReviewEvent
    pull_request_id: Optional[ID] = None
    pull_request_review_id: Optional[ID] = None


@dataclass(kw_only=True)
class Subscribable:
    """
    Subscribable - Entities that can be subscribed to for web and email notifications.

    id - The Node ID of the Subscribable object

    viewerCanSubscribe - Check if the viewer is able to change their subscription status for the repository.

    viewerSubscription - Identifies if the viewer is watching, not watching, or ignoring the subscribable entity.

    """

    id: ID
    viewer_can_subscribe: bool
    viewer_subscription: Optional[SubscriptionState] = None


@dataclass(kw_only=True)
class TagNamePatternParameters:
    """
    TagNamePatternParameters - Parameters to be used for the tag_name_pattern rule

    name - How this rule will appear to users.

    negate - If true, the rule will fail if the pattern matches.

    operator - The operator to use for matching.

    pattern - The pattern to match with.

    """

    name: Optional[str] = None
    negate: bool
    operator: str
    pattern: str


@dataclass(kw_only=True)
class TeamDiscussionCommentOrder:
    """
    TeamDiscussionCommentOrder - Ways in which team discussion comment connections can be ordered.

    direction - The direction in which to order nodes.

    field - The field by which to order nodes.

    """

    direction: OrderDirection
    field: TeamDiscussionCommentOrderField


@dataclass(kw_only=True)
class TeamMemberOrder:
    """
    TeamMemberOrder - Ordering options for team member connections

    direction - The ordering direction.

    field - The field to order team members by.

    """

    direction: OrderDirection
    field: TeamMemberOrderField


@dataclass(kw_only=True)
class TeamRepositoryOrder:
    """
    TeamRepositoryOrder - Ordering options for team repository connections

    direction - The ordering direction.

    field - The field to order repositories by.

    """

    direction: OrderDirection
    field: TeamRepositoryOrderField


@dataclass(kw_only=True)
class TransferEnterpriseOrganizationInput:
    """
    TransferEnterpriseOrganizationInput - Autogenerated input type of TransferEnterpriseOrganization

    clientMutationId - A unique identifier for the client performing the mutation.

    destinationEnterpriseId - The ID of the enterprise where the organization should be transferred.

    organizationId - The ID of the organization to transfer.

    """

    client_mutation_id: Optional[str] = None
    destination_enterprise_id: ID
    organization_id: ID


@dataclass(kw_only=True)
class UnarchiveProjectV2ItemInput:
    """
    UnarchiveProjectV2ItemInput - Autogenerated input type of UnarchiveProjectV2Item

    clientMutationId - A unique identifier for the client performing the mutation.

    itemId - The ID of the ProjectV2Item to unarchive.

    projectId - The ID of the Project to archive the item from.

    """

    client_mutation_id: Optional[str] = None
    item_id: ID
    project_id: ID


@dataclass(kw_only=True)
class UnfollowOrganizationInput:
    """
    UnfollowOrganizationInput - Autogenerated input type of UnfollowOrganization

    clientMutationId - A unique identifier for the client performing the mutation.

    organizationId - ID of the organization to unfollow.

    """

    client_mutation_id: Optional[str] = None
    organization_id: ID


@dataclass(kw_only=True)
class UniformResourceLocatable:
    """
    UniformResourceLocatable - Represents a type that can be retrieved by a URL.

    resourcePath - The HTML path to this resource.

    url - The URL to this resource.

    """

    resource_path: URI
    url: URI


@dataclass(kw_only=True)
class UnlinkProjectV2FromTeamInput:
    """
    UnlinkProjectV2FromTeamInput - Autogenerated input type of UnlinkProjectV2FromTeam

    clientMutationId - A unique identifier for the client performing the mutation.

    projectId - The ID of the project to unlink from the team.

    teamId - The ID of the team to unlink from the project.

    """

    client_mutation_id: Optional[str] = None
    project_id: ID
    team_id: ID


@dataclass(kw_only=True)
class UnlockLockableInput:
    """
    UnlockLockableInput - Autogenerated input type of UnlockLockable

    clientMutationId - A unique identifier for the client performing the mutation.

    lockableId - ID of the item to be unlocked.

    """

    client_mutation_id: Optional[str] = None
    lockable_id: ID


@dataclass(kw_only=True)
class UnmarkFileAsViewedInput:
    """
    UnmarkFileAsViewedInput - Autogenerated input type of UnmarkFileAsViewed

    clientMutationId - A unique identifier for the client performing the mutation.

    path - The path of the file to mark as unviewed

    pullRequestId - The Node ID of the pull request.

    """

    client_mutation_id: Optional[str] = None
    path: str
    pull_request_id: ID


@dataclass(kw_only=True)
class UnmarkProjectV2AsTemplateInput:
    """
    UnmarkProjectV2AsTemplateInput - Autogenerated input type of UnmarkProjectV2AsTemplate

    clientMutationId - A unique identifier for the client performing the mutation.

    projectId - The ID of the Project to unmark as a template.

    """

    client_mutation_id: Optional[str] = None
    project_id: ID


@dataclass(kw_only=True)
class UnpinIssueInput:
    """
    UnpinIssueInput - Autogenerated input type of UnpinIssue

    clientMutationId - A unique identifier for the client performing the mutation.

    issueId - The ID of the issue to be unpinned

    """

    client_mutation_id: Optional[str] = None
    issue_id: ID


@dataclass(kw_only=True)
class UnsubscribeFromNotificationsInput:
    """
    UnsubscribeFromNotificationsInput - Autogenerated input type of UnsubscribeFromNotifications

    clientMutationId - A unique identifier for the client performing the mutation.

    ids - The NotificationThread IDs of the objects to unsubscribe from.

    """

    client_mutation_id: Optional[str] = None
    ids: list[ID]


@dataclass(kw_only=True)
class Updatable:
    """
    Updatable - Entities that can be updated.

    viewerCanUpdate - Check if the current viewer can update this object.

    """

    viewer_can_update: bool


@dataclass(kw_only=True)
class UpdateDiscussionCommentInput:
    """
    UpdateDiscussionCommentInput - Autogenerated input type of UpdateDiscussionComment

    body - The new contents of the comment body.

    clientMutationId - A unique identifier for the client performing the mutation.

    commentId - The Node ID of the discussion comment to update.

    """

    body: str
    client_mutation_id: Optional[str] = None
    comment_id: ID


@dataclass(kw_only=True)
class UpdateEnterpriseAdministratorRoleInput:
    """
    UpdateEnterpriseAdministratorRoleInput - Autogenerated input type of UpdateEnterpriseAdministratorRole

    clientMutationId - A unique identifier for the client performing the mutation.

    enterpriseId - The ID of the Enterprise which the admin belongs to.

    login - The login of a administrator whose role is being changed.

    role - The new role for the Enterprise administrator.

    """

    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    login: str
    role: EnterpriseAdministratorRole


@dataclass(kw_only=True)
class UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput:
    """
    UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput - Autogenerated input type of UpdateEnterpriseAllowPrivateRepositoryForkingSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterpriseId - The ID of the enterprise on which to set the allow private repository forking setting.

    policyValue - The value for the allow private repository forking policy on the enterprise.

    settingValue - The value for the allow private repository forking setting on the enterprise.

    """

    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    policy_value: Optional[EnterpriseAllowPrivateRepositoryForkingPolicyValue] = None
    setting_value: EnterpriseEnabledDisabledSettingValue


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput:
    """
    UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput - Autogenerated input type of UpdateEnterpriseMembersCanChangeRepositoryVisibilitySetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterpriseId - The ID of the enterprise on which to set the members can change repository visibility setting.

    settingValue - The value for the members can change repository visibility setting on the enterprise.

    """

    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    setting_value: EnterpriseEnabledDisabledSettingValue


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanDeleteIssuesSettingInput:
    """
    UpdateEnterpriseMembersCanDeleteIssuesSettingInput - Autogenerated input type of UpdateEnterpriseMembersCanDeleteIssuesSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterpriseId - The ID of the enterprise on which to set the members can delete issues setting.

    settingValue - The value for the members can delete issues setting on the enterprise.

    """

    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    setting_value: EnterpriseEnabledDisabledSettingValue


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput:
    """
    UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput - Autogenerated input type of UpdateEnterpriseMembersCanInviteCollaboratorsSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterpriseId - The ID of the enterprise on which to set the members can invite collaborators setting.

    settingValue - The value for the members can invite collaborators setting on the enterprise.

    """

    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    setting_value: EnterpriseEnabledDisabledSettingValue


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput:
    """
    UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput - Autogenerated input type of UpdateEnterpriseMembersCanUpdateProtectedBranchesSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterpriseId - The ID of the enterprise on which to set the members can update protected branches setting.

    settingValue - The value for the members can update protected branches setting on the enterprise.

    """

    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    setting_value: EnterpriseEnabledDisabledSettingValue


@dataclass(kw_only=True)
class UpdateEnterpriseOrganizationProjectsSettingInput:
    """
    UpdateEnterpriseOrganizationProjectsSettingInput - Autogenerated input type of UpdateEnterpriseOrganizationProjectsSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterpriseId - The ID of the enterprise on which to set the organization projects setting.

    settingValue - The value for the organization projects setting on the enterprise.

    """

    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    setting_value: EnterpriseEnabledDisabledSettingValue


@dataclass(kw_only=True)
class UpdateEnterpriseOwnerOrganizationRolePayload:
    """
    UpdateEnterpriseOwnerOrganizationRolePayload - Autogenerated return type of UpdateEnterpriseOwnerOrganizationRole

    clientMutationId - A unique identifier for the client performing the mutation.

    message - A message confirming the result of changing the owner's organization role.

    """

    client_mutation_id: Optional[str] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseRepositoryProjectsSettingInput:
    """
    UpdateEnterpriseRepositoryProjectsSettingInput - Autogenerated input type of UpdateEnterpriseRepositoryProjectsSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterpriseId - The ID of the enterprise on which to set the repository projects setting.

    settingValue - The value for the repository projects setting on the enterprise.

    """

    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    setting_value: EnterpriseEnabledDisabledSettingValue


@dataclass(kw_only=True)
class UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput:
    """
    UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput - Autogenerated input type of UpdateEnterpriseTwoFactorAuthenticationRequiredSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterpriseId - The ID of the enterprise on which to set the two factor authentication required setting.

    settingValue - The value for the two factor authentication required setting on the enterprise.

    """

    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    setting_value: EnterpriseEnabledSettingValue


@dataclass(kw_only=True)
class UpdateIpAllowListEnabledSettingInput:
    """
    UpdateIpAllowListEnabledSettingInput - Autogenerated input type of UpdateIpAllowListEnabledSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    ownerId - The ID of the owner on which to set the IP allow list enabled setting.

    settingValue - The value for the IP allow list enabled setting.

    """

    client_mutation_id: Optional[str] = None
    owner_id: ID
    setting_value: IpAllowListEnabledSettingValue


@dataclass(kw_only=True)
class UpdateIpAllowListForInstalledAppsEnabledSettingInput:
    """
    UpdateIpAllowListForInstalledAppsEnabledSettingInput - Autogenerated input type of UpdateIpAllowListForInstalledAppsEnabledSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    ownerId - The ID of the owner.

    settingValue - The value for the IP allow list configuration for installed GitHub Apps setting.

    """

    client_mutation_id: Optional[str] = None
    owner_id: ID
    setting_value: IpAllowListForInstalledAppsEnabledSettingValue


@dataclass(kw_only=True)
class UpdateIssueInput:
    """
    UpdateIssueInput - Autogenerated input type of UpdateIssue

    assigneeIds - An array of Node IDs of users for this issue.

    body - The body for the issue description.

    clientMutationId - A unique identifier for the client performing the mutation.

    id - The ID of the Issue to modify.

    labelIds - An array of Node IDs of labels for this issue.

    milestoneId - The Node ID of the milestone for this issue.

    projectIds - An array of Node IDs for projects associated with this issue.

    state - The desired issue state.

    title - The title for the issue.

    """

    assignee_ids: Optional[list[ID]] = None
    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    id: ID
    label_ids: Optional[list[ID]] = None
    milestone_id: Optional[ID] = None
    project_ids: Optional[list[ID]] = None
    state: Optional[IssueState] = None
    title: Optional[str] = None


@dataclass(kw_only=True)
class UpdateNotificationRestrictionSettingInput:
    """
    UpdateNotificationRestrictionSettingInput - Autogenerated input type of UpdateNotificationRestrictionSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    ownerId - The ID of the owner on which to set the restrict notifications setting.

    settingValue - The value for the restrict notifications setting.

    """

    client_mutation_id: Optional[str] = None
    owner_id: ID
    setting_value: NotificationRestrictionSettingValue


@dataclass(kw_only=True)
class UpdateOrganizationWebCommitSignoffSettingInput:
    """
    UpdateOrganizationWebCommitSignoffSettingInput - Autogenerated input type of UpdateOrganizationWebCommitSignoffSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    organizationId - The ID of the organization on which to set the web commit signoff setting.

    webCommitSignoffRequired - Enable signoff on web-based commits for repositories in the organization?

    """

    client_mutation_id: Optional[str] = None
    organization_id: ID
    web_commit_signoff_required: bool


@dataclass(kw_only=True)
class UpdateParametersInput:
    """
    UpdateParametersInput - Only allow users with bypass permission to update matching refs.

    updateAllowsFetchAndMerge - Branch can pull changes from its upstream repository

    """

    update_allows_fetch_and_merge: bool


@dataclass(kw_only=True)
class UpdateProjectCardInput:
    """
    UpdateProjectCardInput - Autogenerated input type of UpdateProjectCard

    clientMutationId - A unique identifier for the client performing the mutation.

    isArchived - Whether or not the ProjectCard should be archived

    note - The note of ProjectCard.

    projectCardId - The ProjectCard ID to update.

    """

    client_mutation_id: Optional[str] = None
    is_archived: Optional[bool] = None
    note: Optional[str] = None
    project_card_id: ID


@dataclass(kw_only=True)
class UpdateProjectInput:
    """
    UpdateProjectInput - Autogenerated input type of UpdateProject

    body - The description of project.

    clientMutationId - A unique identifier for the client performing the mutation.

    name - The name of project.

    projectId - The Project ID to update.

    public - Whether the project is public or not.

    state - Whether the project is open or closed.

    """

    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    name: Optional[str] = None
    project_id: ID
    public: Optional[bool] = None
    state: Optional[ProjectState] = None


@dataclass(kw_only=True)
class UpdateProjectV2Input:
    """
    UpdateProjectV2Input - Autogenerated input type of UpdateProjectV2

    clientMutationId - A unique identifier for the client performing the mutation.

    closed - Set the project to closed or open.

    projectId - The ID of the Project to update.

    public - Set the project to public or private.

    readme - Set the readme description of the project.

    shortDescription - Set the short description of the project.

    title - Set the title of the project.

    """

    client_mutation_id: Optional[str] = None
    closed: Optional[bool] = None
    project_id: ID
    public: Optional[bool] = None
    readme: Optional[str] = None
    short_description: Optional[str] = None
    title: Optional[str] = None


@dataclass(kw_only=True)
class UpdatePullRequestBranchInput:
    """
    UpdatePullRequestBranchInput - Autogenerated input type of UpdatePullRequestBranch

    clientMutationId - A unique identifier for the client performing the mutation.

    expectedHeadOid - The head ref oid for the upstream branch.

    pullRequestId - The Node ID of the pull request.

    updateMethod - The update branch method to use. If omitted, defaults to 'MERGE'

    """

    client_mutation_id: Optional[str] = None
    expected_head_oid: Optional[GitObjectID] = None
    pull_request_id: ID
    update_method: Optional[PullRequestBranchUpdateMethod] = None


@dataclass(kw_only=True)
class UpdatePullRequestReviewCommentInput:
    """
    UpdatePullRequestReviewCommentInput - Autogenerated input type of UpdatePullRequestReviewComment

    body - The text of the comment.

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequestReviewCommentId - The Node ID of the comment to modify.

    """

    body: str
    client_mutation_id: Optional[str] = None
    pull_request_review_comment_id: ID


@dataclass(kw_only=True)
class UpdateRefInput:
    """
    UpdateRefInput - Autogenerated input type of UpdateRef

    clientMutationId - A unique identifier for the client performing the mutation.

    force - Permit updates of branch Refs that are not fast-forwards?

    oid - The GitObjectID that the Ref shall be updated to target.

    refId - The Node ID of the Ref to be updated.

    """

    client_mutation_id: Optional[str] = None
    force: Optional[bool] = None
    oid: GitObjectID
    ref_id: ID


@dataclass(kw_only=True)
class UpdateRepositoryInput:
    """
        UpdateRepositoryInput - Autogenerated input type of UpdateRepository

        clientMutationId - A unique identifier for the client performing the mutation.

        description - A new description for the repository. Pass an empty string to erase the existing description.

        hasDiscussionsEnabled - Indicates if the repository should have the discussions feature enabled.

        hasIssuesEnabled - Indicates if the repository should have the issues feature enabled.

        hasProjectsEnabled - Indicates if the repository should have the project boards feature enabled.

        hasSponsorshipsEnabled - Indicates if the repository displays a Sponsor button for financial contributions.

        hasWikiEnabled - Indicates if the repository should have the wiki feature enabled.

        homepageUrl - The URL for a web page about this repository. Pass an empty string to erase the existing URL.

        name - The new name of the repository.

        repositoryId - The ID of the repository to update.

        template - Whether this repository should be marked as a template such that anyone who
    can access it can create new repositories with the same files and directory structure.

    """

    client_mutation_id: Optional[str] = None
    description: Optional[str] = None
    has_discussions_enabled: Optional[bool] = None
    has_issues_enabled: Optional[bool] = None
    has_projects_enabled: Optional[bool] = None
    has_sponsorships_enabled: Optional[bool] = None
    has_wiki_enabled: Optional[bool] = None
    homepage_url: Optional[URI] = None
    name: Optional[str] = None
    repository_id: ID
    template: Optional[bool] = None


@dataclass(kw_only=True)
class UpdateSponsorshipPreferencesInput:
    """
        UpdateSponsorshipPreferencesInput - Autogenerated input type of UpdateSponsorshipPreferences

        clientMutationId - A unique identifier for the client performing the mutation.

        privacyLevel - Specify whether others should be able to see that the sponsor is sponsoring
    the sponsorable. Public visibility still does not reveal which tier is used.

        receiveEmails - Whether the sponsor should receive email updates from the sponsorable.

        sponsorId - The ID of the user or organization who is acting as the sponsor, paying for
    the sponsorship. Required if sponsorLogin is not given.

        sponsorLogin - The username of the user or organization who is acting as the sponsor, paying
    for the sponsorship. Required if sponsorId is not given.

        sponsorableId - The ID of the user or organization who is receiving the sponsorship. Required if sponsorableLogin is not given.

        sponsorableLogin - The username of the user or organization who is receiving the sponsorship. Required if sponsorableId is not given.

    """

    client_mutation_id: Optional[str] = None
    privacy_level: Optional[SponsorshipPrivacy] = None
    receive_emails: Optional[bool] = None
    sponsor_id: Optional[ID] = None
    sponsor_login: Optional[str] = None
    sponsorable_id: Optional[ID] = None
    sponsorable_login: Optional[str] = None


@dataclass(kw_only=True)
class UpdateTeamDiscussionCommentInput:
    """
    UpdateTeamDiscussionCommentInput - Autogenerated input type of UpdateTeamDiscussionComment

    body - The updated text of the comment.

    bodyVersion - The current version of the body content.

    clientMutationId - A unique identifier for the client performing the mutation.

    id - The ID of the comment to modify.

    """

    body: str
    body_version: Optional[str] = None
    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class UpdateTeamReviewAssignmentInput:
    """
    UpdateTeamReviewAssignmentInput - Autogenerated input type of UpdateTeamReviewAssignment

    algorithm - The algorithm to use for review assignment

    clientMutationId - A unique identifier for the client performing the mutation.

    countMembersAlreadyRequested - Count any members whose review has already been requested against the required number of members assigned to review

    enabled - Turn on or off review assignment

    excludedTeamMemberIds - An array of team member IDs to exclude

    id - The Node ID of the team to update review assignments of

    includeChildTeamMembers - Include the members of any child teams when assigning

    notifyTeam - Notify the entire team of the PR if it is delegated

    removeTeamRequest - Remove the team review request when assigning

    teamMemberCount - The number of team members to assign

    """

    algorithm: Optional[TeamReviewAssignmentAlgorithm] = None
    client_mutation_id: Optional[str] = None
    count_members_already_requested: Optional[bool] = None
    enabled: bool
    excluded_team_member_ids: Optional[list[ID]] = None
    id: ID
    include_child_team_members: Optional[bool] = None
    notify_team: Optional[bool] = None
    remove_team_request: Optional[bool] = None
    team_member_count: Optional[int] = None


@dataclass(kw_only=True)
class UpdateTopicsInput:
    """
    UpdateTopicsInput - Autogenerated input type of UpdateTopics

    clientMutationId - A unique identifier for the client performing the mutation.

    repositoryId - The Node ID of the repository.

    topicNames - An array of topic names.

    """

    client_mutation_id: Optional[str] = None
    repository_id: ID
    topic_names: list[str]


@dataclass(kw_only=True)
class UpdateUserListsForItemInput:
    """
    UpdateUserListsForItemInput - Autogenerated input type of UpdateUserListsForItem

    clientMutationId - A unique identifier for the client performing the mutation.

    itemId - The item to add to the list

    listIds - The lists to which this item should belong

    suggestedListIds - The suggested lists to create and add this item to

    """

    client_mutation_id: Optional[str] = None
    item_id: ID
    list_ids: list[ID]
    suggested_list_ids: Optional[list[ID]] = None


@dataclass(kw_only=True)
class UserListSuggestion:
    """
    UserListSuggestion - Represents a suggested user list.

    id - The ID of the suggested user list

    name - The name of the suggested user list

    """

    id: Optional[ID] = None
    name: Optional[str] = None


@dataclass(kw_only=True)
class VerifiableDomainOrder:
    """
    VerifiableDomainOrder - Ordering options for verifiable domain connections.

    direction - The ordering direction.

    field - The field to order verifiable domains by.

    """

    direction: OrderDirection
    field: VerifiableDomainOrderField


@dataclass(kw_only=True)
class Votable:
    """
    Votable - A subject that may be upvoted.

    upvoteCount - Number of upvotes that this subject has received.

    viewerCanUpvote - Whether or not the current user can add or remove an upvote on this subject.

    viewerHasUpvoted - Whether or not the current user has already upvoted this subject.

    """

    upvote_count: int
    viewer_can_upvote: bool
    viewer_has_upvoted: bool


@dataclass(kw_only=True)
class WorkflowFileReferenceInput:
    """
    WorkflowFileReferenceInput - A workflow that must run for this rule to pass

    path - The path to the workflow file

    ref - The ref (branch or tag) of the workflow file to use

    repositoryId - The ID of the repository where the workflow is defined

    sha - The commit SHA of the workflow file to use

    """

    path: str
    ref: Optional[str] = None
    repository_id: int
    sha: Optional[str] = None


@dataclass(kw_only=True)
class AutoMergeRequest:
    """
        AutoMergeRequest - Represents an auto-merge request for a pull request

        authorEmail - The email address of the author of this auto-merge request.

        commitBody - The commit message of the auto-merge request. If a merge queue is required by
    the base branch, this value will be set by the merge queue when merging.

        commitHeadline - The commit title of the auto-merge request. If a merge queue is required by
    the base branch, this value will be set by the merge queue when merging

        enabledAt - When was this auto-merge request was enabled.

        enabledBy - The actor who created the auto-merge request.

        mergeMethod - The merge method of the auto-merge request. If a merge queue is required by
    the base branch, this value will be set by the merge queue when merging.

        pullRequest - The pull request that this auto-merge request is set against.

    """

    author_email: Optional[str] = None
    commit_body: Optional[str] = None
    commit_headline: Optional[str] = None
    enabled_at: Optional[DateTime] = None
    enabled_by: Optional[Actor] = None
    merge_method: PullRequestMergeMethod
    pull_request: PullRequest


@dataclass(kw_only=True)
class BranchProtectionRuleConflict:
    """
    BranchProtectionRuleConflict - A conflict between two branch protection rules.

    branchProtectionRule - Identifies the branch protection rule.

    conflictingBranchProtectionRule - Identifies the conflicting branch protection rule.

    ref - Identifies the branch ref that has conflicting rules

    """

    branch_protection_rule: Optional[BranchProtectionRule] = None
    conflicting_branch_protection_rule: Optional[BranchProtectionRule] = None
    ref: Optional[Ref] = None


@dataclass(kw_only=True)
class BranchProtectionRuleConflictEdge:
    """
    BranchProtectionRuleConflictEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[BranchProtectionRuleConflict] = None


@dataclass(kw_only=True)
class BranchProtectionRuleConflictConnection:
    """
    BranchProtectionRuleConflictConnection - The connection type for BranchProtectionRuleConflict.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[BranchProtectionRuleConflictEdge]] = None
    nodes: Optional[list[BranchProtectionRuleConflict]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseServerUserAccountEmail:
    """
    EnterpriseServerUserAccountEmail - An email belonging to a user account on an Enterprise Server installation.

    createdAt - Identifies the date and time when the object was created.

    email - The email address.

    id - The Node ID of the EnterpriseServerUserAccountEmail object

    isPrimary - Indicates whether this is the primary email of the associated user account.

    updatedAt - Identifies the date and time when the object was last updated.

    userAccount - The user account to which the email belongs.

    """

    created_at: DateTime
    email: str
    id: ID
    is_primary: bool
    updated_at: DateTime
    user_account: EnterpriseServerUserAccount


@dataclass(kw_only=True)
class EnterpriseServerUserAccountEmailEdge:
    """
    EnterpriseServerUserAccountEmailEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[EnterpriseServerUserAccountEmail] = None


@dataclass(kw_only=True)
class EnterpriseServerUserAccountEmailConnection:
    """
    EnterpriseServerUserAccountEmailConnection - The connection type for EnterpriseServerUserAccountEmail.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[EnterpriseServerUserAccountEmailEdge]] = None
    nodes: Optional[list[EnterpriseServerUserAccountEmail]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseServerUserAccountEdge:
    """
    EnterpriseServerUserAccountEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[EnterpriseServerUserAccount] = None


@dataclass(kw_only=True)
class EnterpriseServerUserAccountConnection:
    """
    EnterpriseServerUserAccountConnection - The connection type for EnterpriseServerUserAccount.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[EnterpriseServerUserAccountEdge]] = None
    nodes: Optional[list[EnterpriseServerUserAccount]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseServerUserAccountsUpload:
    """
    EnterpriseServerUserAccountsUpload - A user accounts upload from an Enterprise Server installation.

    createdAt - Identifies the date and time when the object was created.

    enterprise - The enterprise to which this upload belongs.

    enterpriseServerInstallation - The Enterprise Server installation for which this upload was generated.

    id - The Node ID of the EnterpriseServerUserAccountsUpload object

    name - The name of the file uploaded.

    syncState - The synchronization state of the upload

    updatedAt - Identifies the date and time when the object was last updated.

    """

    created_at: DateTime
    enterprise: Enterprise
    enterprise_server_installation: EnterpriseServerInstallation
    id: ID
    name: str
    sync_state: EnterpriseServerUserAccountsUploadSyncState
    updated_at: DateTime


@dataclass(kw_only=True)
class EnterpriseServerUserAccountsUploadEdge:
    """
    EnterpriseServerUserAccountsUploadEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[EnterpriseServerUserAccountsUpload] = None


@dataclass(kw_only=True)
class EnterpriseServerUserAccountsUploadConnection:
    """
    EnterpriseServerUserAccountsUploadConnection - The connection type for EnterpriseServerUserAccountsUpload.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[EnterpriseServerUserAccountsUploadEdge]] = None
    nodes: Optional[list[EnterpriseServerUserAccountsUpload]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseServerInstallationMembershipEdge:
    """
    EnterpriseServerInstallationMembershipEdge - An Enterprise Server installation that a user is a member of.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    role - The role of the user in the enterprise membership.

    """

    cursor: str
    node: Optional[EnterpriseServerInstallation] = None
    role: EnterpriseUserAccountMembershipRole


@dataclass(kw_only=True)
class EnterpriseServerInstallationMembershipConnection:
    """
    EnterpriseServerInstallationMembershipConnection - The connection type for EnterpriseServerInstallation.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[EnterpriseServerInstallationMembershipEdge]] = None
    nodes: Optional[list[EnterpriseServerInstallation]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class MembersCanDeleteReposClearAuditEntry:
    """
    MembersCanDeleteReposClearAuditEntry - Audit log entry for a members_can_delete_repos.clear event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    enterpriseResourcePath - The HTTP path for this enterprise.

    enterpriseSlug - The slug of the enterprise.

    enterpriseUrl - The HTTP URL for this enterprise.

    id - The Node ID of the MembersCanDeleteReposClearAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    enterprise_resource_path: Optional[URI] = None
    enterprise_slug: Optional[str] = None
    enterprise_url: Optional[URI] = None
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class MembersCanDeleteReposDisableAuditEntry:
    """
    MembersCanDeleteReposDisableAuditEntry - Audit log entry for a members_can_delete_repos.disable event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    enterpriseResourcePath - The HTTP path for this enterprise.

    enterpriseSlug - The slug of the enterprise.

    enterpriseUrl - The HTTP URL for this enterprise.

    id - The Node ID of the MembersCanDeleteReposDisableAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    enterprise_resource_path: Optional[URI] = None
    enterprise_slug: Optional[str] = None
    enterprise_url: Optional[URI] = None
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class MembersCanDeleteReposEnableAuditEntry:
    """
    MembersCanDeleteReposEnableAuditEntry - Audit log entry for a members_can_delete_repos.enable event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    enterpriseResourcePath - The HTTP path for this enterprise.

    enterpriseSlug - The slug of the enterprise.

    enterpriseUrl - The HTTP URL for this enterprise.

    id - The Node ID of the MembersCanDeleteReposEnableAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    enterprise_resource_path: Optional[URI] = None
    enterprise_slug: Optional[str] = None
    enterprise_url: Optional[URI] = None
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OauthApplicationCreateAuditEntry:
    """
    OauthApplicationCreateAuditEntry - Audit log entry for a oauth_application.create event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    applicationUrl - The application URL of the OAuth application.

    callbackUrl - The callback URL of the OAuth application.

    createdAt - The time the action was initiated

    id - The Node ID of the OauthApplicationCreateAuditEntry object

    oauthApplicationName - The name of the OAuth application.

    oauthApplicationResourcePath - The HTTP path for the OAuth application

    oauthApplicationUrl - The HTTP URL for the OAuth application

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    rateLimit - The rate limit of the OAuth application.

    state - The state of the OAuth application.

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    application_url: Optional[URI] = None
    callback_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    oauth_application_name: Optional[str] = None
    oauth_application_resource_path: Optional[URI] = None
    oauth_application_url: Optional[URI] = None
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    rate_limit: Optional[int] = None
    state: Optional[OauthApplicationCreateAuditEntryState] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgAddBillingManagerAuditEntry:
    """
    OrgAddBillingManagerAuditEntry - Audit log entry for a org.add_billing_manager

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgAddBillingManagerAuditEntry object

    invitationEmail - The email address used to invite a billing manager for the organization.

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    invitation_email: Optional[str] = None
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgAddMemberAuditEntry:
    """
    OrgAddMemberAuditEntry - Audit log entry for a org.add_member

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgAddMemberAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    permission - The permission level of the member added to the organization.

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    permission: Optional[OrgAddMemberAuditEntryPermission] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgBlockUserAuditEntry:
    """
    OrgBlockUserAuditEntry - Audit log entry for a org.block_user

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    blockedUser - The blocked user.

    blockedUserName - The username of the blocked user.

    blockedUserResourcePath - The HTTP path for the blocked user.

    blockedUserUrl - The HTTP URL for the blocked user.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgBlockUserAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    blocked_user: Optional[User] = None
    blocked_user_name: Optional[str] = None
    blocked_user_resource_path: Optional[URI] = None
    blocked_user_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgConfigDisableCollaboratorsOnlyAuditEntry:
    """
    OrgConfigDisableCollaboratorsOnlyAuditEntry - Audit log entry for a org.config.disable_collaborators_only event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgConfigDisableCollaboratorsOnlyAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgConfigEnableCollaboratorsOnlyAuditEntry:
    """
    OrgConfigEnableCollaboratorsOnlyAuditEntry - Audit log entry for a org.config.enable_collaborators_only event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgConfigEnableCollaboratorsOnlyAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgCreateAuditEntry:
    """
    OrgCreateAuditEntry - Audit log entry for a org.create event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    billingPlan - The billing plan for the Organization.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgCreateAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    billing_plan: Optional[OrgCreateAuditEntryBillingPlan] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgDisableOauthAppRestrictionsAuditEntry:
    """
    OrgDisableOauthAppRestrictionsAuditEntry - Audit log entry for a org.disable_oauth_app_restrictions event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgDisableOauthAppRestrictionsAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgDisableSamlAuditEntry:
    """
    OrgDisableSamlAuditEntry - Audit log entry for a org.disable_saml event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    digestMethodUrl - The SAML provider's digest algorithm URL.

    id - The Node ID of the OrgDisableSamlAuditEntry object

    issuerUrl - The SAML provider's issuer URL.

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    signatureMethodUrl - The SAML provider's signature algorithm URL.

    singleSignOnUrl - The SAML provider's single sign-on URL.

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    digest_method_url: Optional[URI] = None
    id: ID
    issuer_url: Optional[URI] = None
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    signature_method_url: Optional[URI] = None
    single_sign_on_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgDisableTwoFactorRequirementAuditEntry:
    """
    OrgDisableTwoFactorRequirementAuditEntry - Audit log entry for a org.disable_two_factor_requirement event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgDisableTwoFactorRequirementAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgEnableOauthAppRestrictionsAuditEntry:
    """
    OrgEnableOauthAppRestrictionsAuditEntry - Audit log entry for a org.enable_oauth_app_restrictions event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgEnableOauthAppRestrictionsAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgEnableSamlAuditEntry:
    """
    OrgEnableSamlAuditEntry - Audit log entry for a org.enable_saml event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    digestMethodUrl - The SAML provider's digest algorithm URL.

    id - The Node ID of the OrgEnableSamlAuditEntry object

    issuerUrl - The SAML provider's issuer URL.

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    signatureMethodUrl - The SAML provider's signature algorithm URL.

    singleSignOnUrl - The SAML provider's single sign-on URL.

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    digest_method_url: Optional[URI] = None
    id: ID
    issuer_url: Optional[URI] = None
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    signature_method_url: Optional[URI] = None
    single_sign_on_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgEnableTwoFactorRequirementAuditEntry:
    """
    OrgEnableTwoFactorRequirementAuditEntry - Audit log entry for a org.enable_two_factor_requirement event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgEnableTwoFactorRequirementAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrganizationInvitation:
    """
    OrganizationInvitation - An Invitation for a user to an organization.

    createdAt - Identifies the date and time when the object was created.

    email - The email address of the user invited to the organization.

    id - The Node ID of the OrganizationInvitation object

    invitationSource - The source of the invitation.

    invitationType - The type of invitation that was sent (e.g. email, user).

    invitee - The user who was invited to the organization.

    inviterActor - The user who created the invitation.

    organization - The organization the invite is for

    role - The user's pending role in the organization (e.g. member, owner).

    """

    created_at: DateTime
    email: Optional[str] = None
    id: ID
    invitation_source: OrganizationInvitationSource
    invitation_type: OrganizationInvitationType
    invitee: Optional[User] = None
    inviter_actor: Optional[User] = None
    organization: Organization
    role: OrganizationInvitationRole


@dataclass(kw_only=True)
class OrgInviteMemberAuditEntry:
    """
    OrgInviteMemberAuditEntry - Audit log entry for a org.invite_member event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    email - The email address of the organization invitation.

    id - The Node ID of the OrgInviteMemberAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationInvitation - The organization invitation.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    email: Optional[str] = None
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_invitation: Optional[OrganizationInvitation] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgInviteToBusinessAuditEntry:
    """
    OrgInviteToBusinessAuditEntry - Audit log entry for a org.invite_to_business event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    enterpriseResourcePath - The HTTP path for this enterprise.

    enterpriseSlug - The slug of the enterprise.

    enterpriseUrl - The HTTP URL for this enterprise.

    id - The Node ID of the OrgInviteToBusinessAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    enterprise_resource_path: Optional[URI] = None
    enterprise_slug: Optional[str] = None
    enterprise_url: Optional[URI] = None
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgOauthAppAccessApprovedAuditEntry:
    """
    OrgOauthAppAccessApprovedAuditEntry - Audit log entry for a org.oauth_app_access_approved event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgOauthAppAccessApprovedAuditEntry object

    oauthApplicationName - The name of the OAuth application.

    oauthApplicationResourcePath - The HTTP path for the OAuth application

    oauthApplicationUrl - The HTTP URL for the OAuth application

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    oauth_application_name: Optional[str] = None
    oauth_application_resource_path: Optional[URI] = None
    oauth_application_url: Optional[URI] = None
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgOauthAppAccessBlockedAuditEntry:
    """
    OrgOauthAppAccessBlockedAuditEntry - Audit log entry for a org.oauth_app_access_blocked event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgOauthAppAccessBlockedAuditEntry object

    oauthApplicationName - The name of the OAuth application.

    oauthApplicationResourcePath - The HTTP path for the OAuth application

    oauthApplicationUrl - The HTTP URL for the OAuth application

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    oauth_application_name: Optional[str] = None
    oauth_application_resource_path: Optional[URI] = None
    oauth_application_url: Optional[URI] = None
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgOauthAppAccessDeniedAuditEntry:
    """
    OrgOauthAppAccessDeniedAuditEntry - Audit log entry for a org.oauth_app_access_denied event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgOauthAppAccessDeniedAuditEntry object

    oauthApplicationName - The name of the OAuth application.

    oauthApplicationResourcePath - The HTTP path for the OAuth application

    oauthApplicationUrl - The HTTP URL for the OAuth application

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    oauth_application_name: Optional[str] = None
    oauth_application_resource_path: Optional[URI] = None
    oauth_application_url: Optional[URI] = None
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgOauthAppAccessRequestedAuditEntry:
    """
    OrgOauthAppAccessRequestedAuditEntry - Audit log entry for a org.oauth_app_access_requested event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgOauthAppAccessRequestedAuditEntry object

    oauthApplicationName - The name of the OAuth application.

    oauthApplicationResourcePath - The HTTP path for the OAuth application

    oauthApplicationUrl - The HTTP URL for the OAuth application

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    oauth_application_name: Optional[str] = None
    oauth_application_resource_path: Optional[URI] = None
    oauth_application_url: Optional[URI] = None
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgOauthAppAccessUnblockedAuditEntry:
    """
    OrgOauthAppAccessUnblockedAuditEntry - Audit log entry for a org.oauth_app_access_unblocked event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgOauthAppAccessUnblockedAuditEntry object

    oauthApplicationName - The name of the OAuth application.

    oauthApplicationResourcePath - The HTTP path for the OAuth application

    oauthApplicationUrl - The HTTP URL for the OAuth application

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    oauth_application_name: Optional[str] = None
    oauth_application_resource_path: Optional[URI] = None
    oauth_application_url: Optional[URI] = None
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgRemoveBillingManagerAuditEntry:
    """
    OrgRemoveBillingManagerAuditEntry - Audit log entry for a org.remove_billing_manager event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgRemoveBillingManagerAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    reason - The reason for the billing manager being removed.

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    reason: Optional[OrgRemoveBillingManagerAuditEntryReason] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgRemoveMemberAuditEntry:
    """
    OrgRemoveMemberAuditEntry - Audit log entry for a org.remove_member event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgRemoveMemberAuditEntry object

    membershipTypes - The types of membership the member has with the organization.

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    reason - The reason for the member being removed.

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    membership_types: Optional[list[OrgRemoveMemberAuditEntryMembershipType]] = None
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    reason: Optional[OrgRemoveMemberAuditEntryReason] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgRemoveOutsideCollaboratorAuditEntry:
    """
    OrgRemoveOutsideCollaboratorAuditEntry - Audit log entry for a org.remove_outside_collaborator event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgRemoveOutsideCollaboratorAuditEntry object

    membershipTypes - The types of membership the outside collaborator has with the organization.

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    reason - The reason for the outside collaborator being removed from the Organization.

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    membership_types: Optional[
        list[OrgRemoveOutsideCollaboratorAuditEntryMembershipType]
    ] = None
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    reason: Optional[OrgRemoveOutsideCollaboratorAuditEntryReason] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgRestoreMemberMembershipOrganizationAuditEntryData:
    """
    OrgRestoreMemberMembershipOrganizationAuditEntryData - Metadata for an organization membership for org.restore_member actions

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    """

    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None


@dataclass(kw_only=True)
class BranchProtectionRuleEdge:
    """
    BranchProtectionRuleEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[BranchProtectionRule] = None


@dataclass(kw_only=True)
class BranchProtectionRuleConnection:
    """
    BranchProtectionRuleConnection - The connection type for BranchProtectionRule.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[BranchProtectionRuleEdge]] = None
    nodes: Optional[list[BranchProtectionRule]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class RepositoryCodeowners:
    """
    RepositoryCodeowners - Information extracted from a repository's `CODEOWNERS` file.

    errors - Any problems that were encountered while parsing the `CODEOWNERS` file.

    """

    errors: list[RepositoryCodeownersError]


@dataclass(kw_only=True)
class TeamEdge:
    """
    TeamEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Team] = None


@dataclass(kw_only=True)
class TeamConnection:
    """
    TeamConnection - The connection type for Team.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[TeamEdge]] = None
    nodes: Optional[list[Team]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class Mannequin:
    """
    Mannequin - A placeholder user for attribution of imported data on GitHub.

    avatarUrl - A URL pointing to the GitHub App's public avatar.

    claimant - The user that has claimed the data attributed to this mannequin.

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    email - The mannequin's email on the source instance.

    id - The Node ID of the Mannequin object

    login - The username of the actor.

    resourcePath - The HTML path to this resource.

    updatedAt - Identifies the date and time when the object was last updated.

    url - The URL to this resource.

    """

    avatar_url: URI
    claimant: Optional[User] = None
    created_at: DateTime
    database_id: Optional[int] = None
    email: Optional[str] = None
    id: ID
    login: str
    resource_path: URI
    updated_at: DateTime
    url: URI


@dataclass(kw_only=True)
class ReactorEdge:
    """
    ReactorEdge - Represents an author of a reaction.

    cursor - A cursor for use in pagination.

    node - The author of the reaction.

    reactedAt - The moment when the user made the reaction.

    """

    cursor: str
    node: Reactor
    reacted_at: DateTime


@dataclass(kw_only=True)
class ReactorConnection:
    """
    ReactorConnection - The connection type for Reactor.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[ReactorEdge]] = None
    nodes: Optional[list[Reactor]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class Reaction:
    """
    Reaction - An emoji reaction to a particular piece of content.

    content - Identifies the emoji reaction.

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    id - The Node ID of the Reaction object

    reactable - The reactable piece of content

    user - Identifies the user who created this reaction.

    """

    content: ReactionContent
    created_at: DateTime
    database_id: Optional[int] = None
    id: ID
    reactable: Reactable
    user: Optional[User] = None


@dataclass(kw_only=True)
class ReactionEdge:
    """
    ReactionEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Reaction] = None


@dataclass(kw_only=True)
class ReactionConnection:
    """
    ReactionConnection - A list of reactions that have been left on the subject.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    viewerHasReacted - Whether or not the authenticated user has left a reaction on the subject.

    """

    edges: Optional[list[ReactionEdge]] = None
    nodes: Optional[list[Reaction]] = None
    page_info: PageInfo
    total_count: int
    viewer_has_reacted: bool


@dataclass(kw_only=True)
class ReactingUserEdge:
    """
    ReactingUserEdge - Represents a user that's made a reaction.

    cursor - A cursor for use in pagination.

    reactedAt - The moment when the user made the reaction.

    """

    cursor: str
    node: User
    reacted_at: DateTime


@dataclass(kw_only=True)
class ReactingUserConnection:
    """
    ReactingUserConnection - The connection type for User.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[ReactingUserEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class UserContentEdit:
    """
    UserContentEdit - An edit on user content

    createdAt - Identifies the date and time when the object was created.

    deletedAt - Identifies the date and time when the object was deleted.

    deletedBy - The actor who deleted this content

    diff - A summary of the changes for this edit

    editedAt - When this content was edited

    editor - The actor who edited this content

    id - The Node ID of the UserContentEdit object

    updatedAt - Identifies the date and time when the object was last updated.

    """

    created_at: DateTime
    deleted_at: Optional[DateTime] = None
    deleted_by: Optional[Actor] = None
    diff: Optional[str] = None
    edited_at: DateTime
    editor: Optional[Actor] = None
    id: ID
    updated_at: DateTime


@dataclass(kw_only=True)
class UserContentEditEdge:
    """
    UserContentEditEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[UserContentEdit] = None


@dataclass(kw_only=True)
class UserContentEditConnection:
    """
    UserContentEditConnection - A list of edits to content.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[UserContentEditEdge]] = None
    nodes: Optional[list[UserContentEdit]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class TeamDiscussionComment:
    """
    TeamDiscussionComment - A comment on a team discussion.

    author - The actor who authored the comment.

    body - The body as Markdown.

    bodyHTML - The body rendered to HTML.

    bodyText - The body rendered to text.

    createdAt - Identifies the date and time when the object was created.

    createdViaEmail - Check if this comment was created via an email reply.

    databaseId - Identifies the primary key from the database.

    editor - The actor who edited the comment.

    id - The Node ID of the TeamDiscussionComment object

    includesCreatedEdit - Check if this comment was edited and includes an edit with the creation data

    lastEditedAt - The moment the editor made the last edit

    publishedAt - Identifies when the comment was published at.

    reactionGroups - A list of reactions grouped by content left on the subject.

    reactions - A list of Reactions left on the Issue.

    updatedAt - Identifies the date and time when the object was last updated.

    userContentEdits - A list of edits to this content.

    viewerCanDelete - Check if the current viewer can delete this object.

    viewerCanReact - Can user react to this subject

    viewerCanUpdate - Check if the current viewer can update this object.

    viewerCannotUpdateReasons - Reasons why the current viewer can not update this comment.

    viewerDidAuthor - Did the viewer author this comment.

    """

    author: Optional[Actor] = None
    body: str
    body_h_t_m_l: HTML
    body_text: str
    created_at: DateTime
    created_via_email: bool
    database_id: Optional[int] = None
    editor: Optional[Actor] = None
    id: ID
    includes_created_edit: bool
    last_edited_at: Optional[DateTime] = None
    published_at: Optional[DateTime] = None
    reaction_groups: Optional[list[ReactionGroup]] = None
    reactions: ReactionConnection
    updated_at: DateTime
    user_content_edits: Optional[UserContentEditConnection] = None
    viewer_can_delete: bool
    viewer_can_react: bool
    viewer_can_update: bool
    viewer_cannot_update_reasons: list[CommentCannotUpdateReason]
    viewer_did_author: bool


@dataclass(kw_only=True)
class TeamDiscussionCommentEdge:
    """
    TeamDiscussionCommentEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[TeamDiscussionComment] = None


@dataclass(kw_only=True)
class TeamDiscussionCommentConnection:
    """
    TeamDiscussionCommentConnection - The connection type for TeamDiscussionComment.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[TeamDiscussionCommentEdge]] = None
    nodes: Optional[list[TeamDiscussionComment]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class TeamDiscussionEdge:
    """
    TeamDiscussionEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[TeamDiscussion] = None


@dataclass(kw_only=True)
class TeamDiscussionConnection:
    """
    TeamDiscussionConnection - The connection type for TeamDiscussion.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[TeamDiscussionEdge]] = None
    nodes: Optional[list[TeamDiscussion]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class OrganizationInvitationEdge:
    """
    OrganizationInvitationEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[OrganizationInvitation] = None


@dataclass(kw_only=True)
class OrganizationInvitationConnection:
    """
    OrganizationInvitationConnection - The connection type for OrganizationInvitation.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[OrganizationInvitationEdge]] = None
    nodes: Optional[list[OrganizationInvitation]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class UserStatus:
    """
    UserStatus - The user's description of what they're currently doing.

    createdAt - Identifies the date and time when the object was created.

    emoji - An emoji summarizing the user's status.

    emojiHTML - The status emoji as HTML.

    expiresAt - If set, the status will not be shown after this date.

    id - The Node ID of the UserStatus object

    indicatesLimitedAvailability - Whether this status indicates the user is not fully available on GitHub.

    message - A brief message describing what the user is doing.

    organization - The organization whose members can see this status. If null, this status is publicly visible.

    updatedAt - Identifies the date and time when the object was last updated.

    user - The user who has this status.

    """

    created_at: DateTime
    emoji: Optional[str] = None
    emoji_h_t_m_l: Optional[HTML] = None
    expires_at: Optional[DateTime] = None
    id: ID
    indicates_limited_availability: bool
    message: Optional[str] = None
    organization: Optional[Organization] = None
    updated_at: DateTime
    user: User


@dataclass(kw_only=True)
class UserStatusEdge:
    """
    UserStatusEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[UserStatus] = None


@dataclass(kw_only=True)
class UserStatusConnection:
    """
    UserStatusConnection - The connection type for UserStatus.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[UserStatusEdge]] = None
    nodes: Optional[list[UserStatus]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class TeamMemberEdge:
    """
    TeamMemberEdge - Represents a user who is a member of a team.

    cursor - A cursor for use in pagination.

    memberAccessResourcePath - The HTTP path to the organization's member access page.

    memberAccessUrl - The HTTP URL to the organization's member access page.

    role - The role the member has on the team.

    """

    cursor: str
    member_access_resource_path: URI
    member_access_url: URI
    node: User
    role: TeamMemberRole


@dataclass(kw_only=True)
class TeamMemberConnection:
    """
    TeamMemberConnection - The connection type for User.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[TeamMemberEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectV2Field:
    """
    ProjectV2Field - A field inside a project.

    createdAt - Identifies the date and time when the object was created.

    dataType - The field's type.

    databaseId - Identifies the primary key from the database.

    id - The Node ID of the ProjectV2Field object

    name - The project field's name.

    project - The project that contains this field.

    updatedAt - Identifies the date and time when the object was last updated.

    """

    created_at: DateTime
    data_type: ProjectV2FieldType
    database_id: Optional[int] = None
    id: ID
    name: str
    project: ProjectV2
    updated_at: DateTime


@dataclass(kw_only=True)
class ProjectV2IterationFieldConfiguration:
    """
    ProjectV2IterationFieldConfiguration - Iteration field configuration for a project.

    completedIterations - The iteration's completed iterations

    duration - The iteration's duration in days

    iterations - The iteration's iterations

    startDay - The iteration's start day of the week

    """

    completed_iterations: list[ProjectV2IterationFieldIteration]
    duration: int
    iterations: list[ProjectV2IterationFieldIteration]
    start_day: int


@dataclass(kw_only=True)
class ProjectV2IterationField:
    """
    ProjectV2IterationField - An iteration field inside a project.

    configuration - Iteration configuration settings

    createdAt - Identifies the date and time when the object was created.

    dataType - The field's type.

    databaseId - Identifies the primary key from the database.

    id - The Node ID of the ProjectV2IterationField object

    name - The project field's name.

    project - The project that contains this field.

    updatedAt - Identifies the date and time when the object was last updated.

    """

    configuration: ProjectV2IterationFieldConfiguration
    created_at: DateTime
    data_type: ProjectV2FieldType
    database_id: Optional[int] = None
    id: ID
    name: str
    project: ProjectV2
    updated_at: DateTime


@dataclass(kw_only=True)
class ProjectV2SingleSelectField:
    """
    ProjectV2SingleSelectField - A single select field inside a project.

    createdAt - Identifies the date and time when the object was created.

    dataType - The field's type.

    databaseId - Identifies the primary key from the database.

    id - The Node ID of the ProjectV2SingleSelectField object

    name - The project field's name.

    options - Options for the single select field

    project - The project that contains this field.

    updatedAt - Identifies the date and time when the object was last updated.

    """

    created_at: DateTime
    data_type: ProjectV2FieldType
    database_id: Optional[int] = None
    id: ID
    name: str
    options: list[ProjectV2SingleSelectFieldOption]
    project: ProjectV2
    updated_at: DateTime


@dataclass(kw_only=True)
class ProjectV2FieldConfigurationEdge:
    """
    ProjectV2FieldConfigurationEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[ProjectV2FieldConfiguration] = None


@dataclass(kw_only=True)
class ProjectV2FieldConfigurationConnection:
    """
    ProjectV2FieldConfigurationConnection - The connection type for ProjectV2FieldConfiguration.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[ProjectV2FieldConfigurationEdge]] = None
    nodes: Optional[list[ProjectV2FieldConfiguration]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectV2Edge:
    """
    ProjectV2Edge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[ProjectV2] = None


@dataclass(kw_only=True)
class ProjectV2Connection:
    """
    ProjectV2Connection - The connection type for ProjectV2.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[ProjectV2Edge]] = None
    nodes: Optional[list[ProjectV2]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DraftIssue:
    """
    DraftIssue - A draft issue within a project.

    assignees - A list of users to assigned to this draft issue.

    body - The body of the draft issue.

    bodyHTML - The body of the draft issue rendered to HTML.

    bodyText - The body of the draft issue rendered to text.

    createdAt - Identifies the date and time when the object was created.

    creator - The actor who created this draft issue.

    id - The Node ID of the DraftIssue object

    projectV2Items - List of items linked with the draft issue (currently draft issue can be linked to only one item).

    projectsV2 - Projects that link to this draft issue (currently draft issue can be linked to only one project).

    title - The title of the draft issue

    updatedAt - Identifies the date and time when the object was last updated.

    """

    assignees: UserConnection
    body: str
    body_h_t_m_l: HTML
    body_text: str
    created_at: DateTime
    creator: Optional[Actor] = None
    id: ID
    project_v2_items: ProjectV2ItemConnection
    projects_v2: ProjectV2Connection
    title: str
    updated_at: DateTime


@dataclass(kw_only=True)
class ProjectV2ItemFieldDateValue:
    """
    ProjectV2ItemFieldDateValue - The value of a date field in a Project item.

    createdAt - Identifies the date and time when the object was created.

    creator - The actor who created the item.

    databaseId - Identifies the primary key from the database.

    date - Date value for the field

    field - The project field that contains this value.

    id - The Node ID of the ProjectV2ItemFieldDateValue object

    item - The project item that contains this value.

    updatedAt - Identifies the date and time when the object was last updated.

    """

    created_at: DateTime
    creator: Optional[Actor] = None
    database_id: Optional[int] = None
    date: Optional[Date] = None
    field: ProjectV2FieldConfiguration
    id: ID
    item: ProjectV2Item
    updated_at: DateTime


@dataclass(kw_only=True)
class ProjectV2ItemFieldIterationValue:
    """
    ProjectV2ItemFieldIterationValue - The value of an iteration field in a Project item.

    createdAt - Identifies the date and time when the object was created.

    creator - The actor who created the item.

    databaseId - Identifies the primary key from the database.

    duration - The duration of the iteration in days.

    field - The project field that contains this value.

    id - The Node ID of the ProjectV2ItemFieldIterationValue object

    item - The project item that contains this value.

    iterationId - The ID of the iteration.

    startDate - The start date of the iteration.

    title - The title of the iteration.

    titleHTML - The title of the iteration, with HTML.

    updatedAt - Identifies the date and time when the object was last updated.

    """

    created_at: DateTime
    creator: Optional[Actor] = None
    database_id: Optional[int] = None
    duration: int
    field: ProjectV2FieldConfiguration
    id: ID
    item: ProjectV2Item
    iteration_id: str
    start_date: Date
    title: str
    title_h_t_m_l: str
    updated_at: DateTime


@dataclass(kw_only=True)
class IssueEdge:
    """
    IssueEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Issue] = None


@dataclass(kw_only=True)
class IssueConnection:
    """
    IssueConnection - The connection type for Issue.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[IssueEdge]] = None
    nodes: Optional[list[Issue]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class Label:
    """
    Label - A label for categorizing Issues, Pull Requests, Milestones, or Discussions with a given Repository.

    color - Identifies the label color.

    createdAt - Identifies the date and time when the label was created.

    description - A brief description of this label.

    id - The Node ID of the Label object

    isDefault - Indicates whether or not this is a default label.

    issues - A list of issues associated with this label.

    name - Identifies the label name.

    pullRequests - A list of pull requests associated with this label.

    repository - The repository associated with this label.

    resourcePath - The HTTP path for this label.

    updatedAt - Identifies the date and time when the label was last updated.

    url - The HTTP URL for this label.

    """

    color: str
    created_at: Optional[DateTime] = None
    description: Optional[str] = None
    id: ID
    is_default: bool
    issues: IssueConnection
    name: str
    pull_requests: PullRequestConnection
    repository: Repository
    resource_path: URI
    updated_at: Optional[DateTime] = None
    url: URI


@dataclass(kw_only=True)
class LabelEdge:
    """
    LabelEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Label] = None


@dataclass(kw_only=True)
class LabelConnection:
    """
    LabelConnection - The connection type for Label.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[LabelEdge]] = None
    nodes: Optional[list[Label]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectV2ItemFieldLabelValue:
    """
    ProjectV2ItemFieldLabelValue - The value of the labels field in a Project item.

    field - The field that contains this value.

    labels - Labels value of a field

    """

    field: ProjectV2FieldConfiguration
    labels: Optional[LabelConnection] = None


@dataclass(kw_only=True)
class Milestone:
    """
    Milestone - Represents a Milestone object on a given repository.

    closed - Indicates if the object is closed (definition of closed may depend on type)

    closedAt - Identifies the date and time when the object was closed.

    createdAt - Identifies the date and time when the object was created.

    creator - Identifies the actor who created the milestone.

    description - Identifies the description of the milestone.

    dueOn - Identifies the due date of the milestone.

    id - The Node ID of the Milestone object

    issues - A list of issues associated with the milestone.

    number - Identifies the number of the milestone.

    progressPercentage - Identifies the percentage complete for the milestone

    pullRequests - A list of pull requests associated with the milestone.

    repository - The repository associated with this milestone.

    resourcePath - The HTTP path for this milestone

    state - Identifies the state of the milestone.

    title - Identifies the title of the milestone.

    updatedAt - Identifies the date and time when the object was last updated.

    url - The HTTP URL for this milestone

    viewerCanClose - Indicates if the object can be closed by the viewer.

    viewerCanReopen - Indicates if the object can be reopened by the viewer.

    """

    closed: bool
    closed_at: Optional[DateTime] = None
    created_at: DateTime
    creator: Optional[Actor] = None
    description: Optional[str] = None
    due_on: Optional[DateTime] = None
    id: ID
    issues: IssueConnection
    number: int
    progress_percentage: float
    pull_requests: PullRequestConnection
    repository: Repository
    resource_path: URI
    state: MilestoneState
    title: str
    updated_at: DateTime
    url: URI
    viewer_can_close: bool
    viewer_can_reopen: bool


@dataclass(kw_only=True)
class ProjectV2ItemFieldMilestoneValue:
    """
    ProjectV2ItemFieldMilestoneValue - The value of a milestone field in a Project item.

    field - The field that contains this value.

    milestone - Milestone value of a field

    """

    field: ProjectV2FieldConfiguration
    milestone: Optional[Milestone] = None


@dataclass(kw_only=True)
class ProjectV2ItemFieldNumberValue:
    """
    ProjectV2ItemFieldNumberValue - The value of a number field in a Project item.

    createdAt - Identifies the date and time when the object was created.

    creator - The actor who created the item.

    databaseId - Identifies the primary key from the database.

    field - The project field that contains this value.

    id - The Node ID of the ProjectV2ItemFieldNumberValue object

    item - The project item that contains this value.

    number - Number as a float(8)

    updatedAt - Identifies the date and time when the object was last updated.

    """

    created_at: DateTime
    creator: Optional[Actor] = None
    database_id: Optional[int] = None
    field: ProjectV2FieldConfiguration
    id: ID
    item: ProjectV2Item
    number: Optional[float] = None
    updated_at: DateTime


@dataclass(kw_only=True)
class ProjectV2ItemFieldPullRequestValue:
    """
    ProjectV2ItemFieldPullRequestValue - The value of a pull request field in a Project item.

    field - The field that contains this value.

    pullRequests - The pull requests for this field

    """

    field: ProjectV2FieldConfiguration
    pull_requests: Optional[PullRequestConnection] = None


@dataclass(kw_only=True)
class ProjectV2ItemFieldRepositoryValue:
    """
    ProjectV2ItemFieldRepositoryValue - The value of a repository field in a Project item.

    field - The field that contains this value.

    repository - The repository for this field.

    """

    field: ProjectV2FieldConfiguration
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class RequestedReviewerEdge:
    """
    RequestedReviewerEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[RequestedReviewer] = None


@dataclass(kw_only=True)
class RequestedReviewerConnection:
    """
    RequestedReviewerConnection - The connection type for RequestedReviewer.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[RequestedReviewerEdge]] = None
    nodes: Optional[list[RequestedReviewer]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectV2ItemFieldReviewerValue:
    """
    ProjectV2ItemFieldReviewerValue - The value of a reviewers field in a Project item.

    field - The field that contains this value.

    reviewers - The reviewers for this field.

    """

    field: ProjectV2FieldConfiguration
    reviewers: Optional[RequestedReviewerConnection] = None


@dataclass(kw_only=True)
class ProjectV2ItemFieldSingleSelectValue:
    """
    ProjectV2ItemFieldSingleSelectValue - The value of a single select field in a Project item.

    color - The color applied to the selected single-select option.

    createdAt - Identifies the date and time when the object was created.

    creator - The actor who created the item.

    databaseId - Identifies the primary key from the database.

    description - A plain-text description of the selected single-select option, such as what the option means.

    descriptionHTML - The description of the selected single-select option, including HTML tags.

    field - The project field that contains this value.

    id - The Node ID of the ProjectV2ItemFieldSingleSelectValue object

    item - The project item that contains this value.

    name - The name of the selected single select option.

    nameHTML - The html name of the selected single select option.

    optionId - The id of the selected single select option.

    updatedAt - Identifies the date and time when the object was last updated.

    """

    color: ProjectV2SingleSelectFieldOptionColor
    created_at: DateTime
    creator: Optional[Actor] = None
    database_id: Optional[int] = None
    description: Optional[str] = None
    description_h_t_m_l: Optional[str] = None
    field: ProjectV2FieldConfiguration
    id: ID
    item: ProjectV2Item
    name: Optional[str] = None
    name_h_t_m_l: Optional[str] = None
    option_id: Optional[str] = None
    updated_at: DateTime


@dataclass(kw_only=True)
class ProjectV2ItemFieldTextValue:
    """
    ProjectV2ItemFieldTextValue - The value of a text field in a Project item.

    createdAt - Identifies the date and time when the object was created.

    creator - The actor who created the item.

    databaseId - Identifies the primary key from the database.

    field - The project field that contains this value.

    id - The Node ID of the ProjectV2ItemFieldTextValue object

    item - The project item that contains this value.

    text - Text value of a field

    updatedAt - Identifies the date and time when the object was last updated.

    """

    created_at: DateTime
    creator: Optional[Actor] = None
    database_id: Optional[int] = None
    field: ProjectV2FieldConfiguration
    id: ID
    item: ProjectV2Item
    text: Optional[str] = None
    updated_at: DateTime


@dataclass(kw_only=True)
class ProjectV2ItemFieldUserValue:
    """
    ProjectV2ItemFieldUserValue - The value of a user field in a Project item.

    field - The field that contains this value.

    users - The users for this field

    """

    field: ProjectV2FieldConfiguration
    users: Optional[UserConnection] = None


@dataclass(kw_only=True)
class ProjectV2ItemFieldValueEdge:
    """
    ProjectV2ItemFieldValueEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[ProjectV2ItemFieldValue] = None


@dataclass(kw_only=True)
class ProjectV2ItemFieldValueConnection:
    """
    ProjectV2ItemFieldValueConnection - The connection type for ProjectV2ItemFieldValue.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[ProjectV2ItemFieldValueEdge]] = None
    nodes: Optional[list[ProjectV2ItemFieldValue]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectV2ItemEdge:
    """
    ProjectV2ItemEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[ProjectV2Item] = None


@dataclass(kw_only=True)
class ProjectV2Owner:
    """
    ProjectV2Owner - Represents an owner of a project.

    id - The Node ID of the ProjectV2Owner object

    projectV2 - Find a project by number.

    projectsV2 - A list of projects under the owner.

    """

    id: ID
    project_v2: Optional[ProjectV2] = None
    projects_v2: ProjectV2Connection


@dataclass(kw_only=True)
class RepositoryEdge:
    """
    RepositoryEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Repository] = None


@dataclass(kw_only=True)
class RepositoryConnection:
    """
        RepositoryConnection - A list of repositories owned by the subject.

        edges - A list of edges.

        nodes - A list of nodes.

        pageInfo - Information to aid in pagination.

        totalCount - Identifies the total count of items in the connection.

        totalDiskUsage - The total size in kilobytes of all repositories in the connection. Value will
    never be larger than max 32-bit signed integer.

    """

    edges: Optional[list[RepositoryEdge]] = None
    nodes: Optional[list[Repository]] = None
    page_info: PageInfo
    total_count: int
    total_disk_usage: int


@dataclass(kw_only=True)
class ProjectV2FieldEdge:
    """
    ProjectV2FieldEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[ProjectV2Field] = None


@dataclass(kw_only=True)
class ProjectV2FieldConnection:
    """
    ProjectV2FieldConnection - The connection type for ProjectV2Field.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[ProjectV2FieldEdge]] = None
    nodes: Optional[list[ProjectV2Field]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectV2SortBy:
    """
    ProjectV2SortBy - Represents a sort by field and direction.

    direction - The direction of the sorting. Possible values are ASC and DESC.

    field - The field by which items are sorted.

    """

    direction: OrderDirection
    field: ProjectV2Field


@dataclass(kw_only=True)
class ProjectV2SortByEdge:
    """
    ProjectV2SortByEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[ProjectV2SortBy] = None


@dataclass(kw_only=True)
class ProjectV2SortByConnection:
    """
    ProjectV2SortByConnection - The connection type for ProjectV2SortBy.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[ProjectV2SortByEdge]] = None
    nodes: Optional[list[ProjectV2SortBy]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectV2SortByField:
    """
    ProjectV2SortByField - Represents a sort by field and direction.

    direction - The direction of the sorting. Possible values are ASC and DESC.

    field - The field by which items are sorted.

    """

    direction: OrderDirection
    field: ProjectV2FieldConfiguration


@dataclass(kw_only=True)
class ProjectV2SortByFieldEdge:
    """
    ProjectV2SortByFieldEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[ProjectV2SortByField] = None


@dataclass(kw_only=True)
class ProjectV2SortByFieldConnection:
    """
    ProjectV2SortByFieldConnection - The connection type for ProjectV2SortByField.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[ProjectV2SortByFieldEdge]] = None
    nodes: Optional[list[ProjectV2SortByField]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectV2View:
    """
    ProjectV2View - A view within a ProjectV2.

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    fields - The view's visible fields.

    filter - The project view's filter.

    groupByFields - The view's group-by field.

    id - The Node ID of the ProjectV2View object

    layout - The project view's layout.

    name - The project view's name.

    number - The project view's number.

    project - The project that contains this view.

    sortByFields - The view's sort-by config.

    updatedAt - Identifies the date and time when the object was last updated.

    verticalGroupByFields - The view's vertical-group-by field.

    """

    created_at: DateTime
    database_id: Optional[int] = None
    fields: Optional[ProjectV2FieldConfigurationConnection] = None
    filter: Optional[str] = None
    group_by_fields: Optional[ProjectV2FieldConfigurationConnection] = None
    id: ID
    layout: ProjectV2ViewLayout
    name: str
    number: int
    project: ProjectV2
    sort_by_fields: Optional[ProjectV2SortByFieldConnection] = None
    updated_at: DateTime
    vertical_group_by_fields: Optional[ProjectV2FieldConfigurationConnection] = None


@dataclass(kw_only=True)
class ProjectV2ViewEdge:
    """
    ProjectV2ViewEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[ProjectV2View] = None


@dataclass(kw_only=True)
class ProjectV2ViewConnection:
    """
    ProjectV2ViewConnection - The connection type for ProjectV2View.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[ProjectV2ViewEdge]] = None
    nodes: Optional[list[ProjectV2View]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectV2Workflow:
    """
    ProjectV2Workflow - A workflow inside a project.

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    enabled - Whether the workflow is enabled.

    id - The Node ID of the ProjectV2Workflow object

    name - The name of the workflow.

    number - The number of the workflow.

    project - The project that contains this workflow.

    updatedAt - Identifies the date and time when the object was last updated.

    """

    created_at: DateTime
    database_id: Optional[int] = None
    enabled: bool
    id: ID
    name: str
    number: int
    project: ProjectV2
    updated_at: DateTime


@dataclass(kw_only=True)
class ProjectV2WorkflowEdge:
    """
    ProjectV2WorkflowEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[ProjectV2Workflow] = None


@dataclass(kw_only=True)
class ProjectV2WorkflowConnection:
    """
    ProjectV2WorkflowConnection - The connection type for ProjectV2Workflow.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[ProjectV2WorkflowEdge]] = None
    nodes: Optional[list[ProjectV2Workflow]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class TeamRepositoryEdge:
    """
    TeamRepositoryEdge - Represents a team repository.

    cursor - A cursor for use in pagination.

    permission - The permission level the team has on the repository

    """

    cursor: str
    node: Repository
    permission: RepositoryPermission


@dataclass(kw_only=True)
class TeamRepositoryConnection:
    """
    TeamRepositoryConnection - The connection type for Repository.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[TeamRepositoryEdge]] = None
    nodes: Optional[list[Repository]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PermissionSource:
    """
    PermissionSource - A level of permission and source for a user's access to a repository.

    organization - The organization the repository belongs to.

    permission - The level of access this source has granted to the user.

    roleName - The name of the role this source has granted to the user.

    source - The source of this permission.

    """

    organization: Organization
    permission: DefaultRepositoryPermissionField
    role_name: Optional[str] = None
    source: PermissionGranter


@dataclass(kw_only=True)
class RepositoryCollaboratorEdge:
    """
    RepositoryCollaboratorEdge - Represents a user who is a collaborator of a repository.

    cursor - A cursor for use in pagination.

    permission - The permission the user has on the repository.

    permissionSources - A list of sources for the user's access to the repository.

    """

    cursor: str
    node: User
    permission: RepositoryPermission
    permission_sources: Optional[list[PermissionSource]] = None


@dataclass(kw_only=True)
class RepositoryCollaboratorConnection:
    """
    RepositoryCollaboratorConnection - The connection type for User.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[RepositoryCollaboratorEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DependencyGraphDependency:
    """
    DependencyGraphDependency - A dependency manifest entry

    hasDependencies - Does the dependency itself have dependencies?

    packageManager - The dependency package manager

    packageName - The name of the package in the canonical form used by the package manager.

    repository - The repository containing the package

    requirements - The dependency version requirements

    """

    has_dependencies: bool
    package_manager: Optional[str] = None
    package_name: str
    repository: Optional[Repository] = None
    requirements: str


@dataclass(kw_only=True)
class DependencyGraphDependencyEdge:
    """
    DependencyGraphDependencyEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[DependencyGraphDependency] = None


@dataclass(kw_only=True)
class DependencyGraphDependencyConnection:
    """
    DependencyGraphDependencyConnection - The connection type for DependencyGraphDependency.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[DependencyGraphDependencyEdge]] = None
    nodes: Optional[list[DependencyGraphDependency]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DependencyGraphManifest:
    """
    DependencyGraphManifest - Dependency manifest for a repository

    blobPath - Path to view the manifest file blob

    dependencies - A list of manifest dependencies

    dependenciesCount - The number of dependencies listed in the manifest

    exceedsMaxSize - Is the manifest too big to parse?

    filename - Fully qualified manifest filename

    id - The Node ID of the DependencyGraphManifest object

    parseable - Were we able to parse the manifest?

    repository - The repository containing the manifest

    """

    blob_path: str
    dependencies: Optional[DependencyGraphDependencyConnection] = None
    dependencies_count: Optional[int] = None
    exceeds_max_size: bool
    filename: str
    id: ID
    parseable: bool
    repository: Repository


@dataclass(kw_only=True)
class DependencyGraphManifestEdge:
    """
    DependencyGraphManifestEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[DependencyGraphManifest] = None


@dataclass(kw_only=True)
class DependencyGraphManifestConnection:
    """
    DependencyGraphManifestConnection - The connection type for DependencyGraphManifest.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[DependencyGraphManifestEdge]] = None
    nodes: Optional[list[DependencyGraphManifest]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DeployKeyEdge:
    """
    DeployKeyEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[DeployKey] = None


@dataclass(kw_only=True)
class DeployKeyConnection:
    """
    DeployKeyConnection - The connection type for DeployKey.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[DeployKeyEdge]] = None
    nodes: Optional[list[DeployKey]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DeploymentStatus:
    """
    DeploymentStatus - Describes the status of a given deployment attempt.

    createdAt - Identifies the date and time when the object was created.

    creator - Identifies the actor who triggered the deployment.

    deployment - Identifies the deployment associated with status.

    description - Identifies the description of the deployment.

    environment - Identifies the environment of the deployment at the time of this deployment status

    environmentUrl - Identifies the environment URL of the deployment.

    id - The Node ID of the DeploymentStatus object

    logUrl - Identifies the log URL of the deployment.

    state - Identifies the current state of the deployment.

    updatedAt - Identifies the date and time when the object was last updated.

    """

    created_at: DateTime
    creator: Actor
    deployment: Deployment
    description: Optional[str] = None
    environment: Optional[str] = None
    environment_url: Optional[URI] = None
    id: ID
    log_url: Optional[URI] = None
    state: DeploymentStatusState
    updated_at: DateTime


@dataclass(kw_only=True)
class DeploymentStatusEdge:
    """
    DeploymentStatusEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[DeploymentStatus] = None


@dataclass(kw_only=True)
class DeploymentStatusConnection:
    """
    DeploymentStatusConnection - The connection type for DeploymentStatus.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[DeploymentStatusEdge]] = None
    nodes: Optional[list[DeploymentStatus]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DeploymentEdge:
    """
    DeploymentEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Deployment] = None


@dataclass(kw_only=True)
class DeploymentConnection:
    """
    DeploymentConnection - The connection type for Deployment.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[DeploymentEdge]] = None
    nodes: Optional[list[Deployment]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DiscussionCommentEdge:
    """
    DiscussionCommentEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[DiscussionComment] = None


@dataclass(kw_only=True)
class DiscussionCommentConnection:
    """
    DiscussionCommentConnection - The connection type for DiscussionComment.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[DiscussionCommentEdge]] = None
    nodes: Optional[list[DiscussionComment]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DiscussionCategory:
    """
    DiscussionCategory - A category for discussions in a repository.

    createdAt - Identifies the date and time when the object was created.

    description - A description of this category.

    emoji - An emoji representing this category.

    emojiHTML - This category's emoji rendered as HTML.

    id - The Node ID of the DiscussionCategory object

    isAnswerable - Whether or not discussions in this category support choosing an answer with the markDiscussionCommentAsAnswer mutation.

    name - The name of this category.

    repository - The repository associated with this node.

    slug - The slug of this category.

    updatedAt - Identifies the date and time when the object was last updated.

    """

    created_at: DateTime
    description: Optional[str] = None
    emoji: str
    emoji_h_t_m_l: HTML
    id: ID
    is_answerable: bool
    name: str
    repository: Repository
    slug: str
    updated_at: DateTime


@dataclass(kw_only=True)
class DiscussionPollOption:
    """
    DiscussionPollOption - An option for a discussion poll.

    id - The Node ID of the DiscussionPollOption object

    option - The text for this option.

    poll - The discussion poll that this option belongs to.

    totalVoteCount - The total number of votes that have been cast for this option.

    viewerHasVoted - Indicates if the viewer has voted for this option in the poll.

    """

    id: ID
    option: str
    poll: Optional[DiscussionPoll] = None
    total_vote_count: int
    viewer_has_voted: bool


@dataclass(kw_only=True)
class DiscussionPollOptionEdge:
    """
    DiscussionPollOptionEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[DiscussionPollOption] = None


@dataclass(kw_only=True)
class DiscussionPollOptionConnection:
    """
    DiscussionPollOptionConnection - The connection type for DiscussionPollOption.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[DiscussionPollOptionEdge]] = None
    nodes: Optional[list[DiscussionPollOption]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DiscussionCategoryEdge:
    """
    DiscussionCategoryEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[DiscussionCategory] = None


@dataclass(kw_only=True)
class DiscussionCategoryConnection:
    """
    DiscussionCategoryConnection - The connection type for DiscussionCategory.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[DiscussionCategoryEdge]] = None
    nodes: Optional[list[DiscussionCategory]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DiscussionEdge:
    """
    DiscussionEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Discussion] = None


@dataclass(kw_only=True)
class DiscussionConnection:
    """
    DiscussionConnection - The connection type for Discussion.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[DiscussionEdge]] = None
    nodes: Optional[list[Discussion]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DeploymentReviewerEdge:
    """
    DeploymentReviewerEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[DeploymentReviewer] = None


@dataclass(kw_only=True)
class DeploymentReviewerConnection:
    """
    DeploymentReviewerConnection - The connection type for DeploymentReviewer.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[DeploymentReviewerEdge]] = None
    nodes: Optional[list[DeploymentReviewer]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DeploymentProtectionRule:
    """
    DeploymentProtectionRule - A protection rule.

    databaseId - Identifies the primary key from the database.

    preventSelfReview - Whether deployments to this environment can be approved by the user who created the deployment.

    reviewers - The teams or users that can review the deployment

    timeout - The timeout in minutes for this protection rule.

    type - The type of protection rule.

    """

    database_id: Optional[int] = None
    prevent_self_review: Optional[bool] = None
    reviewers: DeploymentReviewerConnection
    timeout: int
    type: DeploymentProtectionRuleType


@dataclass(kw_only=True)
class DeploymentProtectionRuleEdge:
    """
    DeploymentProtectionRuleEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[DeploymentProtectionRule] = None


@dataclass(kw_only=True)
class DeploymentProtectionRuleConnection:
    """
    DeploymentProtectionRuleConnection - The connection type for DeploymentProtectionRule.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[DeploymentProtectionRuleEdge]] = None
    nodes: Optional[list[DeploymentProtectionRule]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class Environment:
    """
    Environment - An environment.

    databaseId - Identifies the primary key from the database.

    id - The Node ID of the Environment object

    name - The name of the environment

    protectionRules - The protection rules defined for this environment

    """

    database_id: Optional[int] = None
    id: ID
    name: str
    protection_rules: DeploymentProtectionRuleConnection


@dataclass(kw_only=True)
class EnvironmentEdge:
    """
    EnvironmentEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Environment] = None


@dataclass(kw_only=True)
class EnvironmentConnection:
    """
    EnvironmentConnection - The connection type for Environment.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[EnvironmentEdge]] = None
    nodes: Optional[list[Environment]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class IssueTemplate:
    """
    IssueTemplate - A repository issue template.

    about - The template purpose.

    assignees - The suggested assignees.

    body - The suggested issue body.

    filename - The template filename.

    labels - The suggested issue labels

    name - The template name.

    title - The suggested issue title.

    """

    about: Optional[str] = None
    assignees: UserConnection
    body: Optional[str] = None
    filename: str
    labels: Optional[LabelConnection] = None
    name: str
    title: Optional[str] = None


@dataclass(kw_only=True)
class LanguageEdge:
    """
    LanguageEdge - Represents the language of a repository.

    size - The number of bytes of code written in the language.

    """

    cursor: str
    node: Language
    size: int


@dataclass(kw_only=True)
class LanguageConnection:
    """
    LanguageConnection - A list of languages associated with the parent.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    totalSize - The total size in bytes of files written in that language.

    """

    edges: Optional[list[LanguageEdge]] = None
    nodes: Optional[list[Language]] = None
    page_info: PageInfo
    total_count: int
    total_size: int


@dataclass(kw_only=True)
class ReleaseAsset:
    """
    ReleaseAsset - A release asset contains the content for a release asset.

    contentType - The asset's content-type

    createdAt - Identifies the date and time when the object was created.

    downloadCount - The number of times this asset was downloaded

    downloadUrl - Identifies the URL where you can download the release asset via the browser.

    id - The Node ID of the ReleaseAsset object

    name - Identifies the title of the release asset.

    release - Release that the asset is associated with

    size - The size (in bytes) of the asset

    updatedAt - Identifies the date and time when the object was last updated.

    uploadedBy - The user that performed the upload

    url - Identifies the URL of the release asset.

    """

    content_type: str
    created_at: DateTime
    download_count: int
    download_url: URI
    id: ID
    name: str
    release: Optional[Release] = None
    size: int
    updated_at: DateTime
    uploaded_by: User
    url: URI


@dataclass(kw_only=True)
class ReleaseAssetEdge:
    """
    ReleaseAssetEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[ReleaseAsset] = None


@dataclass(kw_only=True)
class ReleaseAssetConnection:
    """
    ReleaseAssetConnection - The connection type for ReleaseAsset.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[ReleaseAssetEdge]] = None
    nodes: Optional[list[ReleaseAsset]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class License:
    """
    License - A repository's open source license

    body - The full text of the license

    conditions - The conditions set by the license

    description - A human-readable description of the license

    featured - Whether the license should be featured

    hidden - Whether the license should be displayed in license pickers

    id - The Node ID of the License object

    implementation - Instructions on how to implement the license

    key - The lowercased SPDX ID of the license

    limitations - The limitations set by the license

    name - The license full name specified by <https://spdx.org/licenses>

    nickname - Customary short name if applicable (e.g, GPLv3)

    permissions - The permissions set by the license

    pseudoLicense - Whether the license is a pseudo-license placeholder (e.g., other, no-license)

    spdxId - Short identifier specified by <https://spdx.org/licenses>

    url - URL to the license on <https://choosealicense.com>

    """

    body: str
    conditions: list[LicenseRule]
    description: Optional[str] = None
    featured: bool
    hidden: bool
    id: ID
    implementation: Optional[str] = None
    key: str
    limitations: list[LicenseRule]
    name: str
    nickname: Optional[str] = None
    permissions: list[LicenseRule]
    pseudo_license: bool
    spdx_id: Optional[str] = None
    url: Optional[URI] = None


@dataclass(kw_only=True)
class MergeQueueEntry:
    """
    MergeQueueEntry - Entries in a MergeQueue

    baseCommit - The base commit for this entry

    enqueuedAt - The date and time this entry was added to the merge queue

    enqueuer - The actor that enqueued this entry

    estimatedTimeToMerge - The estimated time in seconds until this entry will be merged

    headCommit - The head commit for this entry

    id - The Node ID of the MergeQueueEntry object

    jump - Whether this pull request should jump the queue

    mergeQueue - The merge queue that this entry belongs to

    position - The position of this entry in the queue

    pullRequest - The pull request that will be added to a merge group

    solo - Does this pull request need to be deployed on its own

    state - The state of this entry in the queue

    """

    base_commit: Optional[Commit] = None
    enqueued_at: DateTime
    enqueuer: Actor
    estimated_time_to_merge: Optional[int] = None
    head_commit: Optional[Commit] = None
    id: ID
    jump: bool
    merge_queue: Optional[MergeQueue] = None
    position: int
    pull_request: Optional[PullRequest] = None
    solo: bool
    state: MergeQueueEntryState


@dataclass(kw_only=True)
class MergeQueueEntryEdge:
    """
    MergeQueueEntryEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[MergeQueueEntry] = None


@dataclass(kw_only=True)
class MergeQueueEntryConnection:
    """
    MergeQueueEntryConnection - The connection type for MergeQueueEntry.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[MergeQueueEntryEdge]] = None
    nodes: Optional[list[MergeQueueEntry]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class MilestoneEdge:
    """
    MilestoneEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Milestone] = None


@dataclass(kw_only=True)
class MilestoneConnection:
    """
    MilestoneConnection - The connection type for Milestone.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[MilestoneEdge]] = None
    nodes: Optional[list[Milestone]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class GitObject:
    """
    GitObject - Represents a Git object.

    abbreviatedOid - An abbreviated version of the Git object ID

    commitResourcePath - The HTTP path for this Git object

    commitUrl - The HTTP URL for this Git object

    id - The Node ID of the GitObject object

    oid - The Git object ID

    repository - The Repository the Git object belongs to

    """

    abbreviated_oid: str
    commit_resource_path: URI
    commit_url: URI
    id: ID
    oid: GitObjectID
    repository: Repository


@dataclass(kw_only=True)
class RepositoryOwner:
    """
    RepositoryOwner - Represents an owner of a Repository.

    avatarUrl - A URL pointing to the owner's public avatar.

    id - The Node ID of the RepositoryOwner object

    login - The username used to login.

    repositories - A list of repositories that the user owns.

    repository - Find Repository.

    resourcePath - The HTTP URL for the owner.

    url - The HTTP URL for the owner.

    """

    avatar_url: URI
    id: ID
    login: str
    repositories: RepositoryConnection
    repository: Optional[Repository] = None
    resource_path: URI
    url: URI


@dataclass(kw_only=True)
class PackageFile:
    """
    PackageFile - A file in a package version.

    id - The Node ID of the PackageFile object

    md5 - MD5 hash of the file.

    name - Name of the file.

    packageVersion - The package version this file belongs to.

    sha1 - SHA1 hash of the file.

    sha256 - SHA256 hash of the file.

    size - Size of the file in bytes.

    updatedAt - Identifies the date and time when the object was last updated.

    url - URL to download the asset.

    """

    id: ID
    md5: Optional[str] = None
    name: str
    package_version: Optional[PackageVersion] = None
    sha1: Optional[str] = None
    sha256: Optional[str] = None
    size: Optional[int] = None
    updated_at: DateTime
    url: Optional[URI] = None


@dataclass(kw_only=True)
class PackageFileEdge:
    """
    PackageFileEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[PackageFile] = None


@dataclass(kw_only=True)
class PackageFileConnection:
    """
    PackageFileConnection - The connection type for PackageFile.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[PackageFileEdge]] = None
    nodes: Optional[list[PackageFile]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PackageVersionEdge:
    """
    PackageVersionEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[PackageVersion] = None


@dataclass(kw_only=True)
class PackageVersionConnection:
    """
    PackageVersionConnection - The connection type for PackageVersion.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[PackageVersionEdge]] = None
    nodes: Optional[list[PackageVersion]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PackageEdge:
    """
    PackageEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Package] = None


@dataclass(kw_only=True)
class PackageConnection:
    """
    PackageConnection - The connection type for Package.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[PackageEdge]] = None
    nodes: Optional[list[Package]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PinnedDiscussion:
    """
    PinnedDiscussion - A Pinned Discussion is a discussion pinned to a repository's index page.

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    discussion - The discussion that was pinned.

    gradientStopColors - Color stops of the chosen gradient

    id - The Node ID of the PinnedDiscussion object

    pattern - Background texture pattern

    pinnedBy - The actor that pinned this discussion.

    preconfiguredGradient - Preconfigured background gradient option

    repository - The repository associated with this node.

    updatedAt - Identifies the date and time when the object was last updated.

    """

    created_at: DateTime
    database_id: Optional[int] = None
    discussion: Discussion
    gradient_stop_colors: list[str]
    id: ID
    pattern: PinnedDiscussionPattern
    pinned_by: Actor
    preconfigured_gradient: Optional[PinnedDiscussionGradient] = None
    repository: Repository
    updated_at: DateTime


@dataclass(kw_only=True)
class PinnedDiscussionEdge:
    """
    PinnedDiscussionEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[PinnedDiscussion] = None


@dataclass(kw_only=True)
class PinnedDiscussionConnection:
    """
    PinnedDiscussionConnection - The connection type for PinnedDiscussion.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[PinnedDiscussionEdge]] = None
    nodes: Optional[list[PinnedDiscussion]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PinnedIssue:
    """
    PinnedIssue - A Pinned Issue is a issue pinned to a repository's index page.

    databaseId - Identifies the primary key from the database.

    fullDatabaseId - Identifies the primary key from the database as a BigInt.

    id - The Node ID of the PinnedIssue object

    issue - The issue that was pinned.

    pinnedBy - The actor that pinned this issue.

    repository - The repository that this issue was pinned to.

    """

    database_id: Optional[int] = None
    full_database_id: Optional[BigInt] = None
    id: ID
    issue: Issue
    pinned_by: Actor
    repository: Repository


@dataclass(kw_only=True)
class PinnedIssueEdge:
    """
    PinnedIssueEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[PinnedIssue] = None


@dataclass(kw_only=True)
class PinnedIssueConnection:
    """
    PinnedIssueConnection - The connection type for PinnedIssue.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[PinnedIssueEdge]] = None
    nodes: Optional[list[PinnedIssue]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectCard:
    """
        ProjectCard - A card in a project.

        column - The project column this card is associated under. A card may only belong to one
    project column at a time. The column field will be null if the card is created
    in a pending state and has yet to be associated with a column. Once cards are
    associated with a column, they will not become pending in the future.

        content - The card content item

        createdAt - Identifies the date and time when the object was created.

        creator - The actor who created this card

        databaseId - Identifies the primary key from the database.

        id - The Node ID of the ProjectCard object

        isArchived - Whether the card is archived

        note - The card note

        project - The project that contains this card.

        resourcePath - The HTTP path for this card

        state - The state of ProjectCard

        updatedAt - Identifies the date and time when the object was last updated.

        url - The HTTP URL for this card

    """

    column: Optional[ProjectColumn] = None
    content: Optional[ProjectCardItem] = None
    created_at: DateTime
    creator: Optional[Actor] = None
    database_id: Optional[int] = None
    id: ID
    is_archived: bool
    note: Optional[str] = None
    project: Project
    resource_path: URI
    state: Optional[ProjectCardState] = None
    updated_at: DateTime
    url: URI


@dataclass(kw_only=True)
class ProjectCardEdge:
    """
    ProjectCardEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[ProjectCard] = None


@dataclass(kw_only=True)
class ProjectCardConnection:
    """
    ProjectCardConnection - The connection type for ProjectCard.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[ProjectCardEdge]] = None
    nodes: Optional[list[ProjectCard]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectColumnEdge:
    """
    ProjectColumnEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[ProjectColumn] = None


@dataclass(kw_only=True)
class ProjectColumnConnection:
    """
    ProjectColumnConnection - The connection type for ProjectColumn.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[ProjectColumnEdge]] = None
    nodes: Optional[list[ProjectColumn]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectEdge:
    """
    ProjectEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Project] = None


@dataclass(kw_only=True)
class ProjectConnection:
    """
    ProjectConnection - A list of projects associated with the owner.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[ProjectEdge]] = None
    nodes: Optional[list[Project]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectOwner:
    """
    ProjectOwner - Represents an owner of a Project.

    id - The Node ID of the ProjectOwner object

    project - Find project by number.

    projects - A list of projects under the owner.

    projectsResourcePath - The HTTP path listing owners projects

    projectsUrl - The HTTP URL listing owners projects

    viewerCanCreateProjects - Can the current viewer create new projects on this owner.

    """

    id: ID
    project: Optional[Project] = None
    projects: ProjectConnection
    projects_resource_path: URI
    projects_url: URI
    viewer_can_create_projects: bool


@dataclass(kw_only=True)
class PullRequestTemplate:
    """
    PullRequestTemplate - A repository pull request template.

    body - The body of the template

    filename - The filename of the template

    repository - The repository the template belongs to

    """

    body: Optional[str] = None
    filename: Optional[str] = None
    repository: Repository


@dataclass(kw_only=True)
class RefEdge:
    """
    RefEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Ref] = None


@dataclass(kw_only=True)
class RefConnection:
    """
    RefConnection - The connection type for Ref.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[RefEdge]] = None
    nodes: Optional[list[Ref]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ReleaseEdge:
    """
    ReleaseEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Release] = None


@dataclass(kw_only=True)
class ReleaseConnection:
    """
    ReleaseConnection - The connection type for Release.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[ReleaseEdge]] = None
    nodes: Optional[list[Release]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class StargazerEdge:
    """
    StargazerEdge - Represents a user that's starred a repository.

    cursor - A cursor for use in pagination.

    starredAt - Identifies when the item was starred.

    """

    cursor: str
    node: User
    starred_at: DateTime


@dataclass(kw_only=True)
class StargazerConnection:
    """
    StargazerConnection - The connection type for User.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[StargazerEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class RepositoryTopic:
    """
    RepositoryTopic - A repository-topic connects a repository to a topic.

    id - The Node ID of the RepositoryTopic object

    resourcePath - The HTTP path for this repository-topic.

    topic - The topic.

    url - The HTTP URL for this repository-topic.

    """

    id: ID
    resource_path: URI
    topic: Topic
    url: URI


@dataclass(kw_only=True)
class RepositoryTopicEdge:
    """
    RepositoryTopicEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[RepositoryTopic] = None


@dataclass(kw_only=True)
class RepositoryTopicConnection:
    """
    RepositoryTopicConnection - The connection type for RepositoryTopic.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[RepositoryTopicEdge]] = None
    nodes: Optional[list[RepositoryTopic]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class RepositoryRulesetBypassActor:
    """
    RepositoryRulesetBypassActor - A team or app that has the ability to bypass a rules defined on a ruleset

    actor - The actor that can bypass rules.

    bypassMode - The mode for the bypass actor

    id - The Node ID of the RepositoryRulesetBypassActor object

    organizationAdmin - This actor represents the ability for an organization owner to bypass

    repositoryRoleDatabaseId - If the actor is a repository role, the repository role's ID that can bypass

    repositoryRoleName - If the actor is a repository role, the repository role's name that can bypass

    repositoryRuleset - Identifies the ruleset associated with the allowed actor

    """

    actor: Optional[BypassActor] = None
    bypass_mode: Optional[RepositoryRulesetBypassActorBypassMode] = None
    id: ID
    organization_admin: bool
    repository_role_database_id: Optional[int] = None
    repository_role_name: Optional[str] = None
    repository_ruleset: Optional[RepositoryRuleset] = None


@dataclass(kw_only=True)
class RepositoryRulesetBypassActorEdge:
    """
    RepositoryRulesetBypassActorEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[RepositoryRulesetBypassActor] = None


@dataclass(kw_only=True)
class RepositoryRulesetBypassActorConnection:
    """
    RepositoryRulesetBypassActorConnection - The connection type for RepositoryRulesetBypassActor.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[RepositoryRulesetBypassActorEdge]] = None
    nodes: Optional[list[RepositoryRulesetBypassActor]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class RepositoryPropertyConditionTarget:
    """
    RepositoryPropertyConditionTarget - Parameters to be used for the repository_property condition

    exclude - Array of repository properties that must not match.

    include - Array of repository properties that must match

    """

    exclude: list[PropertyTargetDefinition]
    include: list[PropertyTargetDefinition]


@dataclass(kw_only=True)
class RepositoryRuleConditions:
    """
    RepositoryRuleConditions - Set of conditions that determine if a ruleset will evaluate

    refName - Configuration for the ref_name condition

    repositoryId - Configuration for the repository_id condition

    repositoryName - Configuration for the repository_name condition

    repositoryProperty - Configuration for the repository_property condition

    """

    ref_name: Optional[RefNameConditionTarget] = None
    repository_id: Optional[RepositoryIdConditionTarget] = None
    repository_name: Optional[RepositoryNameConditionTarget] = None
    repository_property: Optional[RepositoryPropertyConditionTarget] = None


@dataclass(kw_only=True)
class RequiredStatusChecksParameters:
    """
        RequiredStatusChecksParameters - Choose which status checks must pass before the ref is updated. When enabled,
    commits must first be pushed to another ref where the checks pass.

        requiredStatusChecks - Status checks that are required.

        strictRequiredStatusChecksPolicy - Whether pull requests targeting a matching branch must be tested with the
    latest code. This setting will not take effect unless at least one status
    check is enabled.

    """

    required_status_checks: list[StatusCheckConfiguration]
    strict_required_status_checks_policy: bool


@dataclass(kw_only=True)
class WorkflowsParameters:
    """
    WorkflowsParameters - Require all changes made to a targeted branch to pass the specified workflows before they can be merged.

    workflows - Workflows that must pass for this rule to pass.

    """

    workflows: list[WorkflowFileReference]


@dataclass(kw_only=True)
class RepositoryRule:
    """
    RepositoryRule - A repository rule.

    id - The Node ID of the RepositoryRule object

    parameters - The parameters for this rule.

    repositoryRuleset - The repository ruleset associated with this rule configuration

    type - The type of rule.

    """

    id: ID
    parameters: Optional[RuleParameters] = None
    repository_ruleset: Optional[RepositoryRuleset] = None
    type: RepositoryRuleType


@dataclass(kw_only=True)
class RepositoryRuleEdge:
    """
    RepositoryRuleEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[RepositoryRule] = None


@dataclass(kw_only=True)
class RepositoryRuleConnection:
    """
    RepositoryRuleConnection - The connection type for RepositoryRule.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[RepositoryRuleEdge]] = None
    nodes: Optional[list[RepositoryRule]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class RepositoryRulesetEdge:
    """
    RepositoryRulesetEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[RepositoryRuleset] = None


@dataclass(kw_only=True)
class RepositoryRulesetConnection:
    """
    RepositoryRulesetConnection - The connection type for RepositoryRuleset.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[RepositoryRulesetEdge]] = None
    nodes: Optional[list[RepositoryRuleset]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class SubmoduleEdge:
    """
    SubmoduleEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Submodule] = None


@dataclass(kw_only=True)
class SubmoduleConnection:
    """
    SubmoduleConnection - The connection type for Submodule.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[SubmoduleEdge]] = None
    nodes: Optional[list[Submodule]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DependabotUpdate:
    """
    DependabotUpdate - A Dependabot Update for a dependency in a repository

    error - The error from a dependency update

    pullRequest - The associated pull request

    repository - The repository associated with this node.

    """

    error: Optional[DependabotUpdateError] = None
    pull_request: Optional[PullRequest] = None
    repository: Repository


@dataclass(kw_only=True)
class CWEEdge:
    """
    CWEEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[CWE] = None


@dataclass(kw_only=True)
class CWEConnection:
    """
    CWEConnection - The connection type for CWE.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[CWEEdge]] = None
    nodes: Optional[list[CWE]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class SecurityVulnerability:
    """
        SecurityVulnerability - An individual vulnerability within an Advisory

        advisory - The Advisory associated with this Vulnerability

        firstPatchedVersion - The first version containing a fix for the vulnerability

        package - A description of the vulnerable package

        severity - The severity of the vulnerability within this package

        updatedAt - When the vulnerability was last updated

        vulnerableVersionRange - A string that describes the vulnerable package versions.
    This string follows a basic syntax with a few forms.
    + `= 0.2.0` denotes a single vulnerable version.
    + `<= 1.0.8` denotes a version range up to and including the specified version
    + `< 0.1.11` denotes a version range up to, but excluding, the specified version
    + `>= 4.3.0, < 4.3.5` denotes a version range with a known minimum and maximum version.
    + `>= 0.0.1` denotes a version range with a known minimum, but no known maximum

    """

    advisory: SecurityAdvisory
    first_patched_version: Optional[SecurityAdvisoryPackageVersion] = None
    package: SecurityAdvisoryPackage
    severity: SecurityAdvisorySeverity
    updated_at: DateTime
    vulnerable_version_range: str


@dataclass(kw_only=True)
class SecurityVulnerabilityEdge:
    """
    SecurityVulnerabilityEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[SecurityVulnerability] = None


@dataclass(kw_only=True)
class SecurityVulnerabilityConnection:
    """
    SecurityVulnerabilityConnection - The connection type for SecurityVulnerability.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[SecurityVulnerabilityEdge]] = None
    nodes: Optional[list[SecurityVulnerability]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class RepositoryVulnerabilityAlert:
    """
    RepositoryVulnerabilityAlert - A Dependabot alert for a repository with a dependency affected by a security vulnerability.

    autoDismissedAt - When was the alert auto-dismissed?

    createdAt - When was the alert created?

    dependabotUpdate - The associated Dependabot update

    dependencyScope - The scope of an alert's dependency

    dismissComment - Comment explaining the reason the alert was dismissed

    dismissReason - The reason the alert was dismissed

    dismissedAt - When was the alert dismissed?

    dismisser - The user who dismissed the alert

    fixedAt - When was the alert fixed?

    id - The Node ID of the RepositoryVulnerabilityAlert object

    number - Identifies the alert number.

    repository - The associated repository

    securityAdvisory - The associated security advisory

    securityVulnerability - The associated security vulnerability

    state - Identifies the state of the alert.

    vulnerableManifestFilename - The vulnerable manifest filename

    vulnerableManifestPath - The vulnerable manifest path

    vulnerableRequirements - The vulnerable requirements

    """

    auto_dismissed_at: Optional[DateTime] = None
    created_at: DateTime
    dependabot_update: Optional[DependabotUpdate] = None
    dependency_scope: Optional[RepositoryVulnerabilityAlertDependencyScope] = None
    dismiss_comment: Optional[str] = None
    dismiss_reason: Optional[str] = None
    dismissed_at: Optional[DateTime] = None
    dismisser: Optional[User] = None
    fixed_at: Optional[DateTime] = None
    id: ID
    number: int
    repository: Repository
    security_advisory: Optional[SecurityAdvisory] = None
    security_vulnerability: Optional[SecurityVulnerability] = None
    state: RepositoryVulnerabilityAlertState
    vulnerable_manifest_filename: str
    vulnerable_manifest_path: str
    vulnerable_requirements: Optional[str] = None


@dataclass(kw_only=True)
class RepositoryVulnerabilityAlertEdge:
    """
    RepositoryVulnerabilityAlertEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[RepositoryVulnerabilityAlert] = None


@dataclass(kw_only=True)
class RepositoryVulnerabilityAlertConnection:
    """
    RepositoryVulnerabilityAlertConnection - The connection type for RepositoryVulnerabilityAlert.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[RepositoryVulnerabilityAlertEdge]] = None
    nodes: Optional[list[RepositoryVulnerabilityAlert]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class OrgRestoreMemberMembershipRepositoryAuditEntryData:
    """
    OrgRestoreMemberMembershipRepositoryAuditEntryData - Metadata for a repository membership for org.restore_member actions

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    """

    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgRestoreMemberMembershipTeamAuditEntryData:
    """
    OrgRestoreMemberMembershipTeamAuditEntryData - Metadata for a team membership for org.restore_member actions

    team - The team associated with the action

    teamName - The name of the team

    teamResourcePath - The HTTP path for this team

    teamUrl - The HTTP URL for this team

    """

    team: Optional[Team] = None
    team_name: Optional[str] = None
    team_resource_path: Optional[URI] = None
    team_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgRestoreMemberAuditEntry:
    """
    OrgRestoreMemberAuditEntry - Audit log entry for a org.restore_member event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgRestoreMemberAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    restoredCustomEmailRoutingsCount - The number of custom email routings for the restored member.

    restoredIssueAssignmentsCount - The number of issue assignments for the restored member.

    restoredMemberships - Restored organization membership objects.

    restoredMembershipsCount - The number of restored memberships.

    restoredRepositoriesCount - The number of repositories of the restored member.

    restoredRepositoryStarsCount - The number of starred repositories for the restored member.

    restoredRepositoryWatchesCount - The number of watched repositories for the restored member.

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    restored_custom_email_routings_count: Optional[int] = None
    restored_issue_assignments_count: Optional[int] = None
    restored_memberships: Optional[list[OrgRestoreMemberAuditEntryMembership]] = None
    restored_memberships_count: Optional[int] = None
    restored_repositories_count: Optional[int] = None
    restored_repository_stars_count: Optional[int] = None
    restored_repository_watches_count: Optional[int] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgUnblockUserAuditEntry:
    """
    OrgUnblockUserAuditEntry - Audit log entry for a org.unblock_user

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    blockedUser - The user being unblocked by the organization.

    blockedUserName - The username of the blocked user.

    blockedUserResourcePath - The HTTP path for the blocked user.

    blockedUserUrl - The HTTP URL for the blocked user.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgUnblockUserAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    blocked_user: Optional[User] = None
    blocked_user_name: Optional[str] = None
    blocked_user_resource_path: Optional[URI] = None
    blocked_user_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgUpdateDefaultRepositoryPermissionAuditEntry:
    """
    OrgUpdateDefaultRepositoryPermissionAuditEntry - Audit log entry for a org.update_default_repository_permission

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgUpdateDefaultRepositoryPermissionAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    permission - The new base repository permission level for the organization.

    permissionWas - The former base repository permission level for the organization.

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    permission: Optional[
        OrgUpdateDefaultRepositoryPermissionAuditEntryPermission
    ] = None
    permission_was: Optional[
        OrgUpdateDefaultRepositoryPermissionAuditEntryPermission
    ] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgUpdateMemberAuditEntry:
    """
    OrgUpdateMemberAuditEntry - Audit log entry for a org.update_member event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgUpdateMemberAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    permission - The new member permission level for the organization.

    permissionWas - The former member permission level for the organization.

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    permission: Optional[OrgUpdateMemberAuditEntryPermission] = None
    permission_was: Optional[OrgUpdateMemberAuditEntryPermission] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgUpdateMemberRepositoryCreationPermissionAuditEntry:
    """
    OrgUpdateMemberRepositoryCreationPermissionAuditEntry - Audit log entry for a org.update_member_repository_creation_permission event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    canCreateRepositories - Can members create repositories in the organization.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgUpdateMemberRepositoryCreationPermissionAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    visibility - The permission for visibility level of repositories for this organization.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    can_create_repositories: Optional[bool] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None
    visibility: Optional[
        OrgUpdateMemberRepositoryCreationPermissionAuditEntryVisibility
    ] = None


@dataclass(kw_only=True)
class OrgUpdateMemberRepositoryInvitationPermissionAuditEntry:
    """
    OrgUpdateMemberRepositoryInvitationPermissionAuditEntry - Audit log entry for a org.update_member_repository_invitation_permission event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    canInviteOutsideCollaboratorsToRepositories - Can outside collaborators be invited to repositories in the organization.

    createdAt - The time the action was initiated

    id - The Node ID of the OrgUpdateMemberRepositoryInvitationPermissionAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    can_invite_outside_collaborators_to_repositories: Optional[bool] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class PrivateRepositoryForkingDisableAuditEntry:
    """
    PrivateRepositoryForkingDisableAuditEntry - Audit log entry for a private_repository_forking.disable event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    enterpriseResourcePath - The HTTP path for this enterprise.

    enterpriseSlug - The slug of the enterprise.

    enterpriseUrl - The HTTP URL for this enterprise.

    id - The Node ID of the PrivateRepositoryForkingDisableAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    enterprise_resource_path: Optional[URI] = None
    enterprise_slug: Optional[str] = None
    enterprise_url: Optional[URI] = None
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class PrivateRepositoryForkingEnableAuditEntry:
    """
    PrivateRepositoryForkingEnableAuditEntry - Audit log entry for a private_repository_forking.enable event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    enterpriseResourcePath - The HTTP path for this enterprise.

    enterpriseSlug - The slug of the enterprise.

    enterpriseUrl - The HTTP URL for this enterprise.

    id - The Node ID of the PrivateRepositoryForkingEnableAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    enterprise_resource_path: Optional[URI] = None
    enterprise_slug: Optional[str] = None
    enterprise_url: Optional[URI] = None
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class RepoAccessAuditEntry:
    """
    RepoAccessAuditEntry - Audit log entry for a repo.access event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the RepoAccessAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    visibility - The visibility of the repository

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None
    visibility: Optional[RepoAccessAuditEntryVisibility] = None


@dataclass(kw_only=True)
class RepoAddMemberAuditEntry:
    """
    RepoAddMemberAuditEntry - Audit log entry for a repo.add_member event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the RepoAddMemberAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    visibility - The visibility of the repository

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None
    visibility: Optional[RepoAddMemberAuditEntryVisibility] = None


@dataclass(kw_only=True)
class RepoAddTopicAuditEntry:
    """
    RepoAddTopicAuditEntry - Audit log entry for a repo.add_topic event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the RepoAddTopicAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    topic - The name of the topic added to the repository

    topicName - The name of the topic added to the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    topic: Optional[Topic] = None
    topic_name: Optional[str] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class RepoArchivedAuditEntry:
    """
    RepoArchivedAuditEntry - Audit log entry for a repo.archived event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the RepoArchivedAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    visibility - The visibility of the repository

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None
    visibility: Optional[RepoArchivedAuditEntryVisibility] = None


@dataclass(kw_only=True)
class RepoChangeMergeSettingAuditEntry:
    """
    RepoChangeMergeSettingAuditEntry - Audit log entry for a repo.change_merge_setting event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the RepoChangeMergeSettingAuditEntry object

    isEnabled - Whether the change was to enable (true) or disable (false) the merge type

    mergeType - The merge method affected by the change

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    is_enabled: Optional[bool] = None
    merge_type: Optional[RepoChangeMergeSettingAuditEntryMergeType] = None
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class RepoConfigDisableAnonymousGitAccessAuditEntry:
    """
    RepoConfigDisableAnonymousGitAccessAuditEntry - Audit log entry for a repo.config.disable_anonymous_git_access event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the RepoConfigDisableAnonymousGitAccessAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class RepoConfigDisableCollaboratorsOnlyAuditEntry:
    """
    RepoConfigDisableCollaboratorsOnlyAuditEntry - Audit log entry for a repo.config.disable_collaborators_only event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the RepoConfigDisableCollaboratorsOnlyAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class RepoConfigDisableContributorsOnlyAuditEntry:
    """
    RepoConfigDisableContributorsOnlyAuditEntry - Audit log entry for a repo.config.disable_contributors_only event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the RepoConfigDisableContributorsOnlyAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class RepoConfigDisableSockpuppetDisallowedAuditEntry:
    """
    RepoConfigDisableSockpuppetDisallowedAuditEntry - Audit log entry for a repo.config.disable_sockpuppet_disallowed event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the RepoConfigDisableSockpuppetDisallowedAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class RepoConfigEnableAnonymousGitAccessAuditEntry:
    """
    RepoConfigEnableAnonymousGitAccessAuditEntry - Audit log entry for a repo.config.enable_anonymous_git_access event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the RepoConfigEnableAnonymousGitAccessAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class RepoConfigEnableCollaboratorsOnlyAuditEntry:
    """
    RepoConfigEnableCollaboratorsOnlyAuditEntry - Audit log entry for a repo.config.enable_collaborators_only event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the RepoConfigEnableCollaboratorsOnlyAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class RepoConfigEnableContributorsOnlyAuditEntry:
    """
    RepoConfigEnableContributorsOnlyAuditEntry - Audit log entry for a repo.config.enable_contributors_only event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the RepoConfigEnableContributorsOnlyAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class RepoConfigEnableSockpuppetDisallowedAuditEntry:
    """
    RepoConfigEnableSockpuppetDisallowedAuditEntry - Audit log entry for a repo.config.enable_sockpuppet_disallowed event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the RepoConfigEnableSockpuppetDisallowedAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class RepoConfigLockAnonymousGitAccessAuditEntry:
    """
    RepoConfigLockAnonymousGitAccessAuditEntry - Audit log entry for a repo.config.lock_anonymous_git_access event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the RepoConfigLockAnonymousGitAccessAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class RepoConfigUnlockAnonymousGitAccessAuditEntry:
    """
    RepoConfigUnlockAnonymousGitAccessAuditEntry - Audit log entry for a repo.config.unlock_anonymous_git_access event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the RepoConfigUnlockAnonymousGitAccessAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class RepoCreateAuditEntry:
    """
    RepoCreateAuditEntry - Audit log entry for a repo.create event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    forkParentName - The name of the parent repository for this forked repository.

    forkSourceName - The name of the root repository for this network.

    id - The Node ID of the RepoCreateAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    visibility - The visibility of the repository

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    fork_parent_name: Optional[str] = None
    fork_source_name: Optional[str] = None
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None
    visibility: Optional[RepoCreateAuditEntryVisibility] = None


@dataclass(kw_only=True)
class RepoDestroyAuditEntry:
    """
    RepoDestroyAuditEntry - Audit log entry for a repo.destroy event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the RepoDestroyAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    visibility - The visibility of the repository

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None
    visibility: Optional[RepoDestroyAuditEntryVisibility] = None


@dataclass(kw_only=True)
class RepoRemoveMemberAuditEntry:
    """
    RepoRemoveMemberAuditEntry - Audit log entry for a repo.remove_member event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the RepoRemoveMemberAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    visibility - The visibility of the repository

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None
    visibility: Optional[RepoRemoveMemberAuditEntryVisibility] = None


@dataclass(kw_only=True)
class RepoRemoveTopicAuditEntry:
    """
    RepoRemoveTopicAuditEntry - Audit log entry for a repo.remove_topic event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the RepoRemoveTopicAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    topic - The name of the topic added to the repository

    topicName - The name of the topic added to the repository

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    topic: Optional[Topic] = None
    topic_name: Optional[str] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class RepositoryVisibilityChangeDisableAuditEntry:
    """
    RepositoryVisibilityChangeDisableAuditEntry - Audit log entry for a repository_visibility_change.disable event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    enterpriseResourcePath - The HTTP path for this enterprise.

    enterpriseSlug - The slug of the enterprise.

    enterpriseUrl - The HTTP URL for this enterprise.

    id - The Node ID of the RepositoryVisibilityChangeDisableAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    enterprise_resource_path: Optional[URI] = None
    enterprise_slug: Optional[str] = None
    enterprise_url: Optional[URI] = None
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class RepositoryVisibilityChangeEnableAuditEntry:
    """
    RepositoryVisibilityChangeEnableAuditEntry - Audit log entry for a repository_visibility_change.enable event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    enterpriseResourcePath - The HTTP path for this enterprise.

    enterpriseSlug - The slug of the enterprise.

    enterpriseUrl - The HTTP URL for this enterprise.

    id - The Node ID of the RepositoryVisibilityChangeEnableAuditEntry object

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    enterprise_resource_path: Optional[URI] = None
    enterprise_slug: Optional[str] = None
    enterprise_url: Optional[URI] = None
    id: ID
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class TeamAddMemberAuditEntry:
    """
    TeamAddMemberAuditEntry - Audit log entry for a team.add_member event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the TeamAddMemberAuditEntry object

    isLdapMapped - Whether the team was mapped to an LDAP Group.

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    team - The team associated with the action

    teamName - The name of the team

    teamResourcePath - The HTTP path for this team

    teamUrl - The HTTP URL for this team

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    is_ldap_mapped: Optional[bool] = None
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    team: Optional[Team] = None
    team_name: Optional[str] = None
    team_resource_path: Optional[URI] = None
    team_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class TeamAddRepositoryAuditEntry:
    """
    TeamAddRepositoryAuditEntry - Audit log entry for a team.add_repository event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the TeamAddRepositoryAuditEntry object

    isLdapMapped - Whether the team was mapped to an LDAP Group.

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    team - The team associated with the action

    teamName - The name of the team

    teamResourcePath - The HTTP path for this team

    teamUrl - The HTTP URL for this team

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    is_ldap_mapped: Optional[bool] = None
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    team: Optional[Team] = None
    team_name: Optional[str] = None
    team_resource_path: Optional[URI] = None
    team_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class TeamChangeParentTeamAuditEntry:
    """
    TeamChangeParentTeamAuditEntry - Audit log entry for a team.change_parent_team event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the TeamChangeParentTeamAuditEntry object

    isLdapMapped - Whether the team was mapped to an LDAP Group.

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    parentTeam - The new parent team.

    parentTeamName - The name of the new parent team

    parentTeamNameWas - The name of the former parent team

    parentTeamResourcePath - The HTTP path for the parent team

    parentTeamUrl - The HTTP URL for the parent team

    parentTeamWas - The former parent team.

    parentTeamWasResourcePath - The HTTP path for the previous parent team

    parentTeamWasUrl - The HTTP URL for the previous parent team

    team - The team associated with the action

    teamName - The name of the team

    teamResourcePath - The HTTP path for this team

    teamUrl - The HTTP URL for this team

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    is_ldap_mapped: Optional[bool] = None
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    parent_team: Optional[Team] = None
    parent_team_name: Optional[str] = None
    parent_team_name_was: Optional[str] = None
    parent_team_resource_path: Optional[URI] = None
    parent_team_url: Optional[URI] = None
    parent_team_was: Optional[Team] = None
    parent_team_was_resource_path: Optional[URI] = None
    parent_team_was_url: Optional[URI] = None
    team: Optional[Team] = None
    team_name: Optional[str] = None
    team_resource_path: Optional[URI] = None
    team_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class TeamRemoveMemberAuditEntry:
    """
    TeamRemoveMemberAuditEntry - Audit log entry for a team.remove_member event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the TeamRemoveMemberAuditEntry object

    isLdapMapped - Whether the team was mapped to an LDAP Group.

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    team - The team associated with the action

    teamName - The name of the team

    teamResourcePath - The HTTP path for this team

    teamUrl - The HTTP URL for this team

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    is_ldap_mapped: Optional[bool] = None
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    team: Optional[Team] = None
    team_name: Optional[str] = None
    team_resource_path: Optional[URI] = None
    team_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class TeamRemoveRepositoryAuditEntry:
    """
    TeamRemoveRepositoryAuditEntry - Audit log entry for a team.remove_repository event.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    id - The Node ID of the TeamRemoveRepositoryAuditEntry object

    isLdapMapped - Whether the team was mapped to an LDAP Group.

    operationType - The corresponding operation type for the action

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    team - The team associated with the action

    teamName - The name of the team

    teamResourcePath - The HTTP path for this team

    teamUrl - The HTTP URL for this team

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    id: ID
    is_ldap_mapped: Optional[bool] = None
    operation_type: Optional[OperationType] = None
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None
    team: Optional[Team] = None
    team_name: Optional[str] = None
    team_resource_path: Optional[URI] = None
    team_url: Optional[URI] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrganizationAuditEntryEdge:
    """
    OrganizationAuditEntryEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[OrganizationAuditEntry] = None


@dataclass(kw_only=True)
class OrganizationAuditEntryConnection:
    """
    OrganizationAuditEntryConnection - The connection type for OrganizationAuditEntry.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[OrganizationAuditEntryEdge]] = None
    nodes: Optional[list[OrganizationAuditEntry]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class VerifiableDomain:
    """
    VerifiableDomain - A domain that can be verified or approved for an organization or an enterprise.

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    dnsHostName - The DNS host name that should be used for verification.

    domain - The unicode encoded domain.

    hasFoundHostName - Whether a TXT record for verification with the expected host name was found.

    hasFoundVerificationToken - Whether a TXT record for verification with the expected verification token was found.

    id - The Node ID of the VerifiableDomain object

    isApproved - Whether or not the domain is approved.

    isRequiredForPolicyEnforcement - Whether this domain is required to exist for an organization or enterprise policy to be enforced.

    isVerified - Whether or not the domain is verified.

    owner - The owner of the domain.

    punycodeEncodedDomain - The punycode encoded domain.

    tokenExpirationTime - The time that the current verification token will expire.

    updatedAt - Identifies the date and time when the object was last updated.

    verificationToken - The current verification token for the domain.

    """

    created_at: DateTime
    database_id: Optional[int] = None
    dns_host_name: Optional[URI] = None
    domain: URI
    has_found_host_name: bool
    has_found_verification_token: bool
    id: ID
    is_approved: bool
    is_required_for_policy_enforcement: bool
    is_verified: bool
    owner: VerifiableDomainOwner
    punycode_encoded_domain: URI
    token_expiration_time: Optional[DateTime] = None
    updated_at: DateTime
    verification_token: Optional[str] = None


@dataclass(kw_only=True)
class VerifiableDomainEdge:
    """
    VerifiableDomainEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[VerifiableDomain] = None


@dataclass(kw_only=True)
class VerifiableDomainConnection:
    """
    VerifiableDomainConnection - The connection type for VerifiableDomain.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[VerifiableDomainEdge]] = None
    nodes: Optional[list[VerifiableDomain]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class OrganizationEnterpriseOwnerEdge:
    """
    OrganizationEnterpriseOwnerEdge - An enterprise owner in the context of an organization that is part of the enterprise.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    organizationRole - The role of the owner with respect to the organization.

    """

    cursor: str
    node: Optional[User] = None
    organization_role: RoleInOrganization


@dataclass(kw_only=True)
class OrganizationEnterpriseOwnerConnection:
    """
    OrganizationEnterpriseOwnerConnection - The connection type for User.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[OrganizationEnterpriseOwnerEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class GistComment:
    """
        GistComment - Represents a comment on an Gist.

        author - The actor who authored the comment.

        authorAssociation - Author's association with the gist.

        body - Identifies the comment body.

        bodyHTML - The body rendered to HTML.

        bodyText - The body rendered to text.

        createdAt - Identifies the date and time when the object was created.

        createdViaEmail - Check if this comment was created via an email reply.

        databaseId - Identifies the primary key from the database.

        editor - The actor who edited the comment.

        gist - The associated gist.

        id - The Node ID of the GistComment object

        includesCreatedEdit - Check if this comment was edited and includes an edit with the creation data

        isMinimized - Returns whether or not a comment has been minimized.

        lastEditedAt - The moment the editor made the last edit

        minimizedReason - Returns why the comment was minimized. One of `abuse`, `off-topic`,
    `outdated`, `resolved`, `duplicate` and `spam`. Note that the case and
    formatting of these values differs from the inputs to the `MinimizeComment` mutation.

        publishedAt - Identifies when the comment was published at.

        updatedAt - Identifies the date and time when the object was last updated.

        userContentEdits - A list of edits to this content.

        viewerCanDelete - Check if the current viewer can delete this object.

        viewerCanMinimize - Check if the current viewer can minimize this object.

        viewerCanUpdate - Check if the current viewer can update this object.

        viewerCannotUpdateReasons - Reasons why the current viewer can not update this comment.

        viewerDidAuthor - Did the viewer author this comment.

    """

    author: Optional[Actor] = None
    author_association: CommentAuthorAssociation
    body: str
    body_h_t_m_l: HTML
    body_text: str
    created_at: DateTime
    created_via_email: bool
    database_id: Optional[int] = None
    editor: Optional[Actor] = None
    gist: Gist
    id: ID
    includes_created_edit: bool
    is_minimized: bool
    last_edited_at: Optional[DateTime] = None
    minimized_reason: Optional[str] = None
    published_at: Optional[DateTime] = None
    updated_at: DateTime
    user_content_edits: Optional[UserContentEditConnection] = None
    viewer_can_delete: bool
    viewer_can_minimize: bool
    viewer_can_update: bool
    viewer_cannot_update_reasons: list[CommentCannotUpdateReason]
    viewer_did_author: bool


@dataclass(kw_only=True)
class GistCommentEdge:
    """
    GistCommentEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[GistComment] = None


@dataclass(kw_only=True)
class GistCommentConnection:
    """
    GistCommentConnection - The connection type for GistComment.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[GistCommentEdge]] = None
    nodes: Optional[list[GistComment]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class GistFile:
    """
    GistFile - A file in a gist.

    encodedName - The file name encoded to remove characters that are invalid in URL paths.

    encoding - The gist file encoding.

    extension - The file extension from the file name.

    isImage - Indicates if this file is an image.

    isTruncated - Whether the file's contents were truncated.

    language - The programming language this file is written in.

    name - The gist file name.

    size - The gist file size in bytes.

    text - UTF8 text data or null if the file is binary

    """

    encoded_name: Optional[str] = None
    encoding: Optional[str] = None
    extension: Optional[str] = None
    is_image: bool
    is_truncated: bool
    language: Optional[Language] = None
    name: Optional[str] = None
    size: Optional[int] = None
    text: Optional[str] = None


@dataclass(kw_only=True)
class GistEdge:
    """
    GistEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Gist] = None


@dataclass(kw_only=True)
class GistConnection:
    """
    GistConnection - The connection type for Gist.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[GistEdge]] = None
    nodes: Optional[list[Gist]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PinnableItemEdge:
    """
    PinnableItemEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[PinnableItem] = None


@dataclass(kw_only=True)
class PinnableItemConnection:
    """
    PinnableItemConnection - The connection type for PinnableItem.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[PinnableItemEdge]] = None
    nodes: Optional[list[PinnableItem]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProfileItemShowcase:
    """
        ProfileItemShowcase - A curatable list of repositories relating to a repository owner, which defaults
    to showing the most popular repositories they own.

        hasPinnedItems - Whether or not the owner has pinned any repositories or gists.

        items - The repositories and gists in the showcase. If the profile owner has any
    pinned items, those will be returned. Otherwise, the profile owner's popular
    repositories will be returned.

    """

    has_pinned_items: bool
    items: PinnableItemConnection


@dataclass(kw_only=True)
class SponsorEdge:
    """
    SponsorEdge - Represents a user or organization who is sponsoring someone in GitHub Sponsors.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Sponsor] = None


@dataclass(kw_only=True)
class SponsorConnection:
    """
    SponsorConnection - A list of users and organizations sponsoring someone via GitHub Sponsors.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[SponsorEdge]] = None
    nodes: Optional[list[Sponsor]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class Sponsorship:
    """
        Sponsorship - A sponsorship relationship between a sponsor and a maintainer

        createdAt - Identifies the date and time when the object was created.

        id - The Node ID of the Sponsorship object

        isActive - Whether the sponsorship is active. False implies the sponsor is a past sponsor
    of the maintainer, while true implies they are a current sponsor.

        isOneTimePayment - Whether this sponsorship represents a one-time payment versus a recurring sponsorship.

        isSponsorOptedIntoEmail - Whether the sponsor has chosen to receive sponsorship update emails sent from
    the sponsorable. Only returns a non-null value when the viewer has permission to know this.

        paymentSource - The platform that was most recently used to pay for the sponsorship.

        privacyLevel - The privacy level for this sponsorship.

        sponsorEntity - The user or organization that is sponsoring, if you have permission to view them.

        sponsorable - The entity that is being sponsored

        tier - The associated sponsorship tier

        tierSelectedAt - Identifies the date and time when the current tier was chosen for this sponsorship.

    """

    created_at: DateTime
    id: ID
    is_active: bool
    is_one_time_payment: bool
    is_sponsor_opted_into_email: Optional[bool] = None
    payment_source: Optional[SponsorshipPaymentSource] = None
    privacy_level: SponsorshipPrivacy
    sponsor_entity: Optional[Sponsor] = None
    sponsorable: Sponsorable
    tier: Optional[SponsorsTier] = None
    tier_selected_at: Optional[DateTime] = None


@dataclass(kw_only=True)
class SponsorshipEdge:
    """
    SponsorshipEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Sponsorship] = None


@dataclass(kw_only=True)
class SponsorshipConnection:
    """
        SponsorshipConnection - A list of sponsorships either from the subject or received by the subject.

        edges - A list of edges.

        nodes - A list of nodes.

        pageInfo - Information to aid in pagination.

        totalCount - Identifies the total count of items in the connection.

        totalRecurringMonthlyPriceInCents - The total amount in cents of all recurring sponsorships in the connection
    whose amount you can view. Does not include one-time sponsorships.

        totalRecurringMonthlyPriceInDollars - The total amount in USD of all recurring sponsorships in the connection whose
    amount you can view. Does not include one-time sponsorships.

    """

    edges: Optional[list[SponsorshipEdge]] = None
    nodes: Optional[list[Sponsorship]] = None
    page_info: PageInfo
    total_count: int
    total_recurring_monthly_price_in_cents: int
    total_recurring_monthly_price_in_dollars: int


@dataclass(kw_only=True)
class SponsorsTierAdminInfo:
    """
        SponsorsTierAdminInfo - SponsorsTier information only visible to users that can administer the associated Sponsors listing.

        isDraft - Indicates whether this tier is still a work in progress by the sponsorable and
    not yet published to the associated GitHub Sponsors profile. Draft tiers
    cannot be used for new sponsorships and will not be in use on existing
    sponsorships. Draft tiers cannot be seen by anyone but the admins of the
    GitHub Sponsors profile.

        isPublished - Indicates whether this tier is published to the associated GitHub Sponsors
    profile. Published tiers are visible to anyone who can see the GitHub Sponsors
    profile, and are available for use in sponsorships if the GitHub Sponsors
    profile is publicly visible.

        isRetired - Indicates whether this tier has been retired from the associated GitHub
    Sponsors profile. Retired tiers are no longer shown on the GitHub Sponsors
    profile and cannot be chosen for new sponsorships. Existing sponsorships may
    still use retired tiers if the sponsor selected the tier before it was retired.

        sponsorships - The sponsorships using this tier.

    """

    is_draft: bool
    is_published: bool
    is_retired: bool
    sponsorships: SponsorshipConnection


@dataclass(kw_only=True)
class StripeConnectAccount:
    """
        StripeConnectAccount - A Stripe Connect account for receiving sponsorship funds from GitHub Sponsors.

        accountId - The account number used to identify this Stripe Connect account.

        billingCountryOrRegion - The name of the country or region of an external account, such as a bank
    account, tied to the Stripe Connect account. Will only return a value when
    queried by the maintainer of the associated GitHub Sponsors profile
    themselves, or by an admin of the sponsorable organization.

        countryOrRegion - The name of the country or region of the Stripe Connect account. Will only
    return a value when queried by the maintainer of the associated GitHub
    Sponsors profile themselves, or by an admin of the sponsorable organization.

        isActive - Whether this Stripe Connect account is currently in use for the associated GitHub Sponsors profile.

        sponsorsListing - The GitHub Sponsors profile associated with this Stripe Connect account.

        stripeDashboardUrl - The URL to access this Stripe Connect account on Stripe's website.

    """

    account_id: str
    billing_country_or_region: Optional[str] = None
    country_or_region: Optional[str] = None
    is_active: bool
    sponsors_listing: SponsorsListing
    stripe_dashboard_url: URI


@dataclass(kw_only=True)
class SponsorsListingFeaturedItem:
    """
        SponsorsListingFeaturedItem - A record that is promoted on a GitHub Sponsors profile.

        createdAt - Identifies the date and time when the object was created.

        description - Will either be a description from the sponsorable maintainer about why they
    featured this item, or the item's description itself, such as a user's bio
    from their GitHub profile page.

        featureable - The record that is featured on the GitHub Sponsors profile.

        id - The Node ID of the SponsorsListingFeaturedItem object

        position - The position of this featured item on the GitHub Sponsors profile with a lower
    position indicating higher precedence. Starts at 1.

        sponsorsListing - The GitHub Sponsors profile that features this record.

        updatedAt - Identifies the date and time when the object was last updated.

    """

    created_at: DateTime
    description: Optional[str] = None
    featureable: SponsorsListingFeatureableItem
    id: ID
    position: int
    sponsors_listing: SponsorsListing
    updated_at: DateTime


@dataclass(kw_only=True)
class SponsorsTierEdge:
    """
    SponsorsTierEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[SponsorsTier] = None


@dataclass(kw_only=True)
class SponsorsTierConnection:
    """
    SponsorsTierConnection - The connection type for SponsorsTier.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[SponsorsTierEdge]] = None
    nodes: Optional[list[SponsorsTier]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class SponsorsActivity:
    """
    SponsorsActivity - An event related to sponsorship activity.

    action - What action this activity indicates took place.

    currentPrivacyLevel - The sponsor's current privacy level.

    id - The Node ID of the SponsorsActivity object

    paymentSource - The platform that was used to pay for the sponsorship.

    previousSponsorsTier - The tier that the sponsorship used to use, for tier change events.

    sponsor - The user or organization who triggered this activity and was/is sponsoring the sponsorable.

    sponsorable - The user or organization that is being sponsored, the maintainer.

    sponsorsTier - The associated sponsorship tier.

    timestamp - The timestamp of this event.

    viaBulkSponsorship - Was this sponsorship made alongside other sponsorships at the same time from the same sponsor?

    """

    action: SponsorsActivityAction
    current_privacy_level: Optional[SponsorshipPrivacy] = None
    id: ID
    payment_source: Optional[SponsorshipPaymentSource] = None
    previous_sponsors_tier: Optional[SponsorsTier] = None
    sponsor: Optional[Sponsor] = None
    sponsorable: Sponsorable
    sponsors_tier: Optional[SponsorsTier] = None
    timestamp: Optional[DateTime] = None
    via_bulk_sponsorship: bool


@dataclass(kw_only=True)
class SponsorsActivityEdge:
    """
    SponsorsActivityEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[SponsorsActivity] = None


@dataclass(kw_only=True)
class SponsorsActivityConnection:
    """
    SponsorsActivityConnection - The connection type for SponsorsActivity.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[SponsorsActivityEdge]] = None
    nodes: Optional[list[SponsorsActivity]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class SponsorshipNewsletter:
    """
    SponsorshipNewsletter - An update sent to sponsors of a user or organization on GitHub Sponsors.

    author - The author of the newsletter.

    body - The contents of the newsletter, the message the sponsorable wanted to give.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the SponsorshipNewsletter object

    isPublished - Indicates if the newsletter has been made available to sponsors.

    sponsorable - The user or organization this newsletter is from.

    subject - The subject of the newsletter, what it's about.

    updatedAt - Identifies the date and time when the object was last updated.

    """

    author: Optional[User] = None
    body: str
    created_at: DateTime
    id: ID
    is_published: bool
    sponsorable: Sponsorable
    subject: str
    updated_at: DateTime


@dataclass(kw_only=True)
class SponsorshipNewsletterEdge:
    """
    SponsorshipNewsletterEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[SponsorshipNewsletter] = None


@dataclass(kw_only=True)
class SponsorshipNewsletterConnection:
    """
    SponsorshipNewsletterConnection - The connection type for SponsorshipNewsletter.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[SponsorshipNewsletterEdge]] = None
    nodes: Optional[list[SponsorshipNewsletter]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class SponsorAndLifetimeValue:
    """
        SponsorAndLifetimeValue - A GitHub account and the total amount in USD they've paid for sponsorships to a
    particular maintainer. Does not include payments made via Patreon.

        amountInCents - The amount in cents.

        formattedAmount - The amount in USD, formatted as a string.

        sponsor - The sponsor's GitHub account.

        sponsorable - The maintainer's GitHub account.

    """

    amount_in_cents: int
    formatted_amount: str
    sponsor: Sponsorable
    sponsorable: Sponsorable


@dataclass(kw_only=True)
class SponsorAndLifetimeValueEdge:
    """
    SponsorAndLifetimeValueEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[SponsorAndLifetimeValue] = None


@dataclass(kw_only=True)
class MannequinEdge:
    """
    MannequinEdge - Represents a mannequin.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Mannequin] = None


@dataclass(kw_only=True)
class MannequinConnection:
    """
    MannequinConnection - A list of mannequins.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[MannequinEdge]] = None
    nodes: Optional[list[Mannequin]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class OrganizationMemberEdge:
    """
    OrganizationMemberEdge - Represents a user within an organization.

    cursor - A cursor for use in pagination.

    hasTwoFactorEnabled - Whether the organization member has two factor enabled or not. Returns null if information is not available to viewer.

    node - The item at the end of the edge.

    role - The role this user has in the organization.

    """

    cursor: str
    has_two_factor_enabled: Optional[bool] = None
    node: Optional[User] = None
    role: Optional[OrganizationMemberRole] = None


@dataclass(kw_only=True)
class OrganizationMemberConnection:
    """
    OrganizationMemberConnection - A list of users who belong to the organization.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[OrganizationMemberEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class RepositoryMigration:
    """
        RepositoryMigration - A GitHub Enterprise Importer (GEI) repository migration.

        continueOnError - The migration flag to continue on error.

        createdAt - Identifies the date and time when the object was created.

        databaseId - Identifies the primary key from the database.

        failureReason - The reason the migration failed.

        id - The Node ID of the RepositoryMigration object

        migrationLogUrl - The URL for the migration log (expires 1 day after migration completes).

        migrationSource - The migration source.

        repositoryName - The target repository name.

        sourceUrl - The migration source URL, for example `https://github.com` or `https://monalisa.ghe.com`.

        state - The migration state.

        warningsCount - The number of warnings encountered for this migration. To review the warnings,
    check the [Migration Log](https://docs.github.com/migrations/using-github-enterprise-importer/completing-your-migration-with-github-enterprise-importer/accessing-your-migration-logs-for-github-enterprise-importer).

    """

    continue_on_error: bool
    created_at: DateTime
    database_id: Optional[str] = None
    failure_reason: Optional[str] = None
    id: ID
    migration_log_url: Optional[URI] = None
    migration_source: MigrationSource
    repository_name: str
    source_url: URI
    state: MigrationState
    warnings_count: int


@dataclass(kw_only=True)
class RepositoryMigrationEdge:
    """
    RepositoryMigrationEdge - Represents a repository migration.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[RepositoryMigration] = None


@dataclass(kw_only=True)
class RepositoryMigrationConnection:
    """
    RepositoryMigrationConnection - A list of migrations.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[RepositoryMigrationEdge]] = None
    nodes: Optional[list[RepositoryMigration]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ExternalIdentitySamlAttributes:
    """
    ExternalIdentitySamlAttributes - SAML attributes for the External Identity

    attributes - SAML Identity attributes

    emails - The emails associated with the SAML identity

    familyName - Family name of the SAML identity

    givenName - Given name of the SAML identity

    groups - The groups linked to this identity in IDP

    nameId - The NameID of the SAML identity

    username - The userName of the SAML identity

    """

    attributes: list[ExternalIdentityAttribute]
    emails: Optional[list[UserEmailMetadata]] = None
    family_name: Optional[str] = None
    given_name: Optional[str] = None
    groups: Optional[list[str]] = None
    name_id: Optional[str] = None
    username: Optional[str] = None


@dataclass(kw_only=True)
class ExternalIdentityScimAttributes:
    """
    ExternalIdentityScimAttributes - SCIM attributes for the External Identity

    emails - The emails associated with the SCIM identity

    familyName - Family name of the SCIM identity

    givenName - Given name of the SCIM identity

    groups - The groups linked to this identity in IDP

    username - The userName of the SCIM identity

    """

    emails: Optional[list[UserEmailMetadata]] = None
    family_name: Optional[str] = None
    given_name: Optional[str] = None
    groups: Optional[list[str]] = None
    username: Optional[str] = None


@dataclass(kw_only=True)
class ExternalIdentity:
    """
        ExternalIdentity - An external identity provisioned by SAML SSO or SCIM. If SAML is configured on
    the organization, the external identity is visible to (1) organization owners,
    (2) organization owners' personal access tokens (classic) with read:org or
    admin:org scope, (3) GitHub App with an installation token with read or write
    access to members. If SAML is configured on the enterprise, the external
    identity is visible to (1) enterprise owners, (2) enterprise owners' personal
    access tokens (classic) with read:enterprise or admin:enterprise scope.

        guid - The GUID for this identity

        id - The Node ID of the ExternalIdentity object

        organizationInvitation - Organization invitation for this SCIM-provisioned external identity

        samlIdentity - SAML Identity attributes

        scimIdentity - SCIM Identity attributes

        user - User linked to this external identity. Will be NULL if this identity has not been claimed by an organization member.

    """

    guid: str
    id: ID
    organization_invitation: Optional[OrganizationInvitation] = None
    saml_identity: Optional[ExternalIdentitySamlAttributes] = None
    scim_identity: Optional[ExternalIdentityScimAttributes] = None
    user: Optional[User] = None


@dataclass(kw_only=True)
class ExternalIdentityEdge:
    """
    ExternalIdentityEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[ExternalIdentity] = None


@dataclass(kw_only=True)
class ExternalIdentityConnection:
    """
    ExternalIdentityConnection - The connection type for ExternalIdentity.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[ExternalIdentityEdge]] = None
    nodes: Optional[list[ExternalIdentity]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class OrganizationIdentityProvider:
    """
        OrganizationIdentityProvider - An Identity Provider configured to provision SAML and SCIM identities for
    Organizations. Visible to (1) organization owners, (2) organization owners'
    personal access tokens (classic) with read:org or admin:org scope, (3) GitHub
    App with an installation token with read or write access to members.

        digestMethod - The digest algorithm used to sign SAML requests for the Identity Provider.

        externalIdentities - External Identities provisioned by this Identity Provider

        id - The Node ID of the OrganizationIdentityProvider object

        idpCertificate - The x509 certificate used by the Identity Provider to sign assertions and responses.

        issuer - The Issuer Entity ID for the SAML Identity Provider

        organization - Organization this Identity Provider belongs to

        signatureMethod - The signature algorithm used to sign SAML requests for the Identity Provider.

        ssoUrl - The URL endpoint for the Identity Provider's SAML SSO.

    """

    digest_method: Optional[URI] = None
    external_identities: ExternalIdentityConnection
    id: ID
    idp_certificate: Optional[X509Certificate] = None
    issuer: Optional[str] = None
    organization: Optional[Organization] = None
    signature_method: Optional[URI] = None
    sso_url: Optional[URI] = None


@dataclass(kw_only=True)
class EnterpriseOrganizationMembershipEdge:
    """
    EnterpriseOrganizationMembershipEdge - An enterprise organization that a user is a member of.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    role - The role of the user in the enterprise membership.

    """

    cursor: str
    node: Optional[Organization] = None
    role: EnterpriseUserAccountMembershipRole


@dataclass(kw_only=True)
class EnterpriseOrganizationMembershipConnection:
    """
    EnterpriseOrganizationMembershipConnection - The connection type for Organization.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[EnterpriseOrganizationMembershipEdge]] = None
    nodes: Optional[list[Organization]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseUserAccount:
    """
    EnterpriseUserAccount - An account for a user who is an admin of an enterprise or a member of an enterprise through one or more organizations.

    avatarUrl - A URL pointing to the enterprise user account's public avatar.

    createdAt - Identifies the date and time when the object was created.

    enterprise - The enterprise in which this user account exists.

    enterpriseInstallations - A list of Enterprise Server installations this user is a member of.

    id - The Node ID of the EnterpriseUserAccount object

    login - An identifier for the enterprise user account, a login or email address

    name - The name of the enterprise user account

    organizations - A list of enterprise organizations this user is a member of.

    resourcePath - The HTTP path for this user.

    updatedAt - Identifies the date and time when the object was last updated.

    url - The HTTP URL for this user.

    user - The user within the enterprise.

    """

    avatar_url: URI
    created_at: DateTime
    enterprise: Enterprise
    enterprise_installations: EnterpriseServerInstallationMembershipConnection
    id: ID
    login: str
    name: Optional[str] = None
    organizations: EnterpriseOrganizationMembershipConnection
    resource_path: URI
    updated_at: DateTime
    url: URI
    user: Optional[User] = None


@dataclass(kw_only=True)
class EnterpriseMemberEdge:
    """
    EnterpriseMemberEdge - A User who is a member of an enterprise through one or more organizations.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[EnterpriseMember] = None


@dataclass(kw_only=True)
class EnterpriseMemberConnection:
    """
    EnterpriseMemberConnection - The connection type for EnterpriseMember.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[EnterpriseMemberEdge]] = None
    nodes: Optional[list[EnterpriseMember]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class OrganizationEdge:
    """
    OrganizationEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Organization] = None


@dataclass(kw_only=True)
class OrganizationConnection:
    """
    OrganizationConnection - A list of organizations managed by an enterprise.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[OrganizationEdge]] = None
    nodes: Optional[list[Organization]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseAdministratorEdge:
    """
    EnterpriseAdministratorEdge - A User who is an administrator of an enterprise.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    role - The role of the administrator.

    """

    cursor: str
    node: Optional[User] = None
    role: EnterpriseAdministratorRole


@dataclass(kw_only=True)
class EnterpriseAdministratorConnection:
    """
    EnterpriseAdministratorConnection - The connection type for User.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[EnterpriseAdministratorEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseServerInstallationEdge:
    """
    EnterpriseServerInstallationEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[EnterpriseServerInstallation] = None


@dataclass(kw_only=True)
class EnterpriseServerInstallationConnection:
    """
    EnterpriseServerInstallationConnection - The connection type for EnterpriseServerInstallation.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[EnterpriseServerInstallationEdge]] = None
    nodes: Optional[list[EnterpriseServerInstallation]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseFailedInvitationEdge:
    """
    EnterpriseFailedInvitationEdge - A failed invitation to be a member in an enterprise organization.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[OrganizationInvitation] = None


@dataclass(kw_only=True)
class EnterpriseFailedInvitationConnection:
    """
    EnterpriseFailedInvitationConnection - The connection type for OrganizationInvitation.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    totalUniqueUserCount - Identifies the total count of unique users in the connection.

    """

    edges: Optional[list[EnterpriseFailedInvitationEdge]] = None
    nodes: Optional[list[OrganizationInvitation]] = None
    page_info: PageInfo
    total_count: int
    total_unique_user_count: int


@dataclass(kw_only=True)
class OIDCProvider:
    """
        OIDCProvider - An OIDC identity provider configured to provision identities for an enterprise.
    Visible to enterprise owners or enterprise owners' personal access tokens
    (classic) with read:enterprise or admin:enterprise scope.

        enterprise - The enterprise this identity provider belongs to.

        externalIdentities - ExternalIdentities provisioned by this identity provider.

        id - The Node ID of the OIDCProvider object

        providerType - The OIDC identity provider type

        tenantId - The id of the tenant this provider is attached to

    """

    enterprise: Optional[Enterprise] = None
    external_identities: ExternalIdentityConnection
    id: ID
    provider_type: OIDCProviderType
    tenant_id: str


@dataclass(kw_only=True)
class EnterpriseRepositoryInfoEdge:
    """
    EnterpriseRepositoryInfoEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[EnterpriseRepositoryInfo] = None


@dataclass(kw_only=True)
class EnterpriseRepositoryInfoConnection:
    """
    EnterpriseRepositoryInfoConnection - The connection type for EnterpriseRepositoryInfo.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[EnterpriseRepositoryInfoEdge]] = None
    nodes: Optional[list[EnterpriseRepositoryInfo]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseOutsideCollaboratorEdge:
    """
    EnterpriseOutsideCollaboratorEdge - A User who is an outside collaborator of an enterprise through one or more organizations.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    repositories - The enterprise organization repositories this user is a member of.

    """

    cursor: str
    node: Optional[User] = None
    repositories: EnterpriseRepositoryInfoConnection


@dataclass(kw_only=True)
class EnterpriseOutsideCollaboratorConnection:
    """
    EnterpriseOutsideCollaboratorConnection - The connection type for User.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[EnterpriseOutsideCollaboratorEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseAdministratorInvitation:
    """
    EnterpriseAdministratorInvitation - An invitation for a user to become an owner or billing manager of an enterprise.

    createdAt - Identifies the date and time when the object was created.

    email - The email of the person who was invited to the enterprise.

    enterprise - The enterprise the invitation is for.

    id - The Node ID of the EnterpriseAdministratorInvitation object

    invitee - The user who was invited to the enterprise.

    inviter - The user who created the invitation.

    role - The invitee's pending role in the enterprise (owner or billing_manager).

    """

    created_at: DateTime
    email: Optional[str] = None
    enterprise: Enterprise
    id: ID
    invitee: Optional[User] = None
    inviter: Optional[User] = None
    role: EnterpriseAdministratorRole


@dataclass(kw_only=True)
class EnterpriseAdministratorInvitationEdge:
    """
    EnterpriseAdministratorInvitationEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[EnterpriseAdministratorInvitation] = None


@dataclass(kw_only=True)
class EnterpriseAdministratorInvitationConnection:
    """
    EnterpriseAdministratorInvitationConnection - The connection type for EnterpriseAdministratorInvitation.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[EnterpriseAdministratorInvitationEdge]] = None
    nodes: Optional[list[EnterpriseAdministratorInvitation]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class RepositoryInfo:
    """
    RepositoryInfo - A subset of repository info.

    archivedAt - Identifies the date and time when the repository was archived.

    createdAt - Identifies the date and time when the object was created.

    description - The description of the repository.

    descriptionHTML - The description of the repository rendered to HTML.

    forkCount - Returns how many forks there are of this repository in the whole network.

    hasDiscussionsEnabled - Indicates if the repository has the Discussions feature enabled.

    hasIssuesEnabled - Indicates if the repository has issues feature enabled.

    hasProjectsEnabled - Indicates if the repository has the Projects feature enabled.

    hasSponsorshipsEnabled - Indicates if the repository displays a Sponsor button for financial contributions.

    hasWikiEnabled - Indicates if the repository has wiki feature enabled.

    homepageUrl - The repository's URL.

    isArchived - Indicates if the repository is unmaintained.

    isFork - Identifies if the repository is a fork.

    isInOrganization - Indicates if a repository is either owned by an organization, or is a private fork of an organization repository.

    isLocked - Indicates if the repository has been locked or not.

    isMirror - Identifies if the repository is a mirror.

    isPrivate - Identifies if the repository is private or internal.

    isTemplate - Identifies if the repository is a template that can be used to generate new repositories.

    licenseInfo - The license associated with the repository

    lockReason - The reason the repository has been locked.

    mirrorUrl - The repository's original mirror URL.

    name - The name of the repository.

    nameWithOwner - The repository's name with owner.

    openGraphImageUrl - The image used to represent this repository in Open Graph data.

    owner - The User owner of the repository.

    pushedAt - Identifies the date and time when the repository was last pushed to.

    resourcePath - The HTTP path for this repository

    shortDescriptionHTML - A description of the repository, rendered to HTML without any links in it.

    updatedAt - Identifies the date and time when the object was last updated.

    url - The HTTP URL for this repository

    usesCustomOpenGraphImage - Whether this repository has a custom image to use with Open Graph as opposed to being represented by the owner's avatar.

    visibility - Indicates the repository's visibility level.

    """

    archived_at: Optional[DateTime] = None
    created_at: DateTime
    description: Optional[str] = None
    description_h_t_m_l: HTML
    fork_count: int
    has_discussions_enabled: bool
    has_issues_enabled: bool
    has_projects_enabled: bool
    has_sponsorships_enabled: bool
    has_wiki_enabled: bool
    homepage_url: Optional[URI] = None
    is_archived: bool
    is_fork: bool
    is_in_organization: bool
    is_locked: bool
    is_mirror: bool
    is_private: bool
    is_template: bool
    license_info: Optional[License] = None
    lock_reason: Optional[RepositoryLockReason] = None
    mirror_url: Optional[URI] = None
    name: str
    name_with_owner: str
    open_graph_image_url: URI
    owner: RepositoryOwner
    pushed_at: Optional[DateTime] = None
    resource_path: URI
    short_description_h_t_m_l: HTML
    updated_at: DateTime
    url: URI
    uses_custom_open_graph_image: bool
    visibility: RepositoryVisibility


@dataclass(kw_only=True)
class RepositoryInvitation:
    """
    RepositoryInvitation - An invitation for a user to be added to a repository.

    email - The email address that received the invitation.

    id - The Node ID of the RepositoryInvitation object

    invitee - The user who received the invitation.

    inviter - The user who created the invitation.

    permalink - The permalink for this repository invitation.

    permission - The permission granted on this repository by this invitation.

    repository - The Repository the user is invited to.

    """

    email: Optional[str] = None
    id: ID
    invitee: Optional[User] = None
    inviter: User
    permalink: URI
    permission: RepositoryPermission
    repository: Optional[RepositoryInfo] = None


@dataclass(kw_only=True)
class RepositoryInvitationEdge:
    """
    RepositoryInvitationEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[RepositoryInvitation] = None


@dataclass(kw_only=True)
class RepositoryInvitationConnection:
    """
    RepositoryInvitationConnection - A list of repository invitations.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[RepositoryInvitationEdge]] = None
    nodes: Optional[list[RepositoryInvitation]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterprisePendingMemberInvitationEdge:
    """
    EnterprisePendingMemberInvitationEdge - An invitation to be a member in an enterprise organization.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[OrganizationInvitation] = None


@dataclass(kw_only=True)
class EnterprisePendingMemberInvitationConnection:
    """
    EnterprisePendingMemberInvitationConnection - The connection type for OrganizationInvitation.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    totalUniqueUserCount - Identifies the total count of unique users in the connection.

    """

    edges: Optional[list[EnterprisePendingMemberInvitationEdge]] = None
    nodes: Optional[list[OrganizationInvitation]] = None
    page_info: PageInfo
    total_count: int
    total_unique_user_count: int


@dataclass(kw_only=True)
class EnterpriseIdentityProvider:
    """
        EnterpriseIdentityProvider - An identity provider configured to provision identities for an enterprise.
    Visible to enterprise owners or enterprise owners' personal access tokens
    (classic) with read:enterprise or admin:enterprise scope.

        digestMethod - The digest algorithm used to sign SAML requests for the identity provider.

        enterprise - The enterprise this identity provider belongs to.

        externalIdentities - ExternalIdentities provisioned by this identity provider.

        id - The Node ID of the EnterpriseIdentityProvider object

        idpCertificate - The x509 certificate used by the identity provider to sign assertions and responses.

        issuer - The Issuer Entity ID for the SAML identity provider.

        recoveryCodes - Recovery codes that can be used by admins to access the enterprise if the identity provider is unavailable.

        signatureMethod - The signature algorithm used to sign SAML requests for the identity provider.

        ssoUrl - The URL endpoint for the identity provider's SAML SSO.

    """

    digest_method: Optional[SamlDigestAlgorithm] = None
    enterprise: Optional[Enterprise] = None
    external_identities: ExternalIdentityConnection
    id: ID
    idp_certificate: Optional[X509Certificate] = None
    issuer: Optional[str] = None
    recovery_codes: Optional[list[str]] = None
    signature_method: Optional[SamlSignatureAlgorithm] = None
    sso_url: Optional[URI] = None


@dataclass(kw_only=True)
class EnterpriseOwnerInfo:
    """
        EnterpriseOwnerInfo - Enterprise information visible to enterprise owners or enterprise owners'
    personal access tokens (classic) with read:enterprise or admin:enterprise scope.

        admins - A list of all of the administrators for this enterprise.

        affiliatedUsersWithTwoFactorDisabled - A list of users in the enterprise who currently have two-factor authentication disabled.

        affiliatedUsersWithTwoFactorDisabledExist - Whether or not affiliated users with two-factor authentication disabled exist in the enterprise.

        allowPrivateRepositoryForkingSetting - The setting value for whether private repository forking is enabled for repositories in organizations in this enterprise.

        allowPrivateRepositoryForkingSettingOrganizations - A list of enterprise organizations configured with the provided private repository forking setting value.

        allowPrivateRepositoryForkingSettingPolicyValue - The value for the allow private repository forking policy on the enterprise.

        defaultRepositoryPermissionSetting - The setting value for base repository permissions for organizations in this enterprise.

        defaultRepositoryPermissionSettingOrganizations - A list of enterprise organizations configured with the provided base repository permission.

        domains - A list of domains owned by the enterprise. Visible to enterprise owners or
    enterprise owners' personal access tokens (classic) with admin:enterprise scope.

        enterpriseServerInstallations - Enterprise Server installations owned by the enterprise.

        failedInvitations - A list of failed invitations in the enterprise.

        ipAllowListEnabledSetting - The setting value for whether the enterprise has an IP allow list enabled.

        ipAllowListEntries - The IP addresses that are allowed to access resources owned by the enterprise.
    Visible to enterprise owners or enterprise owners' personal access tokens
    (classic) with admin:enterprise scope.

        ipAllowListForInstalledAppsEnabledSetting - The setting value for whether the enterprise has IP allow list configuration for installed GitHub Apps enabled.

        isUpdatingDefaultRepositoryPermission - Whether or not the base repository permission is currently being updated.

        isUpdatingTwoFactorRequirement - Whether the two-factor authentication requirement is currently being enforced.

        membersCanChangeRepositoryVisibilitySetting - The setting value for whether organization members with admin permissions on a
    repository can change repository visibility.

        membersCanChangeRepositoryVisibilitySettingOrganizations - A list of enterprise organizations configured with the provided can change repository visibility setting value.

        membersCanCreateInternalRepositoriesSetting - The setting value for whether members of organizations in the enterprise can create internal repositories.

        membersCanCreatePrivateRepositoriesSetting - The setting value for whether members of organizations in the enterprise can create private repositories.

        membersCanCreatePublicRepositoriesSetting - The setting value for whether members of organizations in the enterprise can create public repositories.

        membersCanCreateRepositoriesSetting - The setting value for whether members of organizations in the enterprise can create repositories.

        membersCanCreateRepositoriesSettingOrganizations - A list of enterprise organizations configured with the provided repository creation setting value.

        membersCanDeleteIssuesSetting - The setting value for whether members with admin permissions for repositories can delete issues.

        membersCanDeleteIssuesSettingOrganizations - A list of enterprise organizations configured with the provided members can delete issues setting value.

        membersCanDeleteRepositoriesSetting - The setting value for whether members with admin permissions for repositories can delete or transfer repositories.

        membersCanDeleteRepositoriesSettingOrganizations - A list of enterprise organizations configured with the provided members can delete repositories setting value.

        membersCanInviteCollaboratorsSetting - The setting value for whether members of organizations in the enterprise can invite outside collaborators.

        membersCanInviteCollaboratorsSettingOrganizations - A list of enterprise organizations configured with the provided members can invite collaborators setting value.

        membersCanMakePurchasesSetting - Indicates whether members of this enterprise's organizations can purchase additional services for those organizations.

        membersCanUpdateProtectedBranchesSetting - The setting value for whether members with admin permissions for repositories can update protected branches.

        membersCanUpdateProtectedBranchesSettingOrganizations - A list of enterprise organizations configured with the provided members can update protected branches setting value.

        membersCanViewDependencyInsightsSetting - The setting value for whether members can view dependency insights.

        membersCanViewDependencyInsightsSettingOrganizations - A list of enterprise organizations configured with the provided members can view dependency insights setting value.

        notificationDeliveryRestrictionEnabledSetting - Indicates if email notification delivery for this enterprise is restricted to verified or approved domains.

        oidcProvider - The OIDC Identity Provider for the enterprise.

        organizationProjectsSetting - The setting value for whether organization projects are enabled for organizations in this enterprise.

        organizationProjectsSettingOrganizations - A list of enterprise organizations configured with the provided organization projects setting value.

        outsideCollaborators - A list of outside collaborators across the repositories in the enterprise.

        pendingAdminInvitations - A list of pending administrator invitations for the enterprise.

        pendingCollaboratorInvitations - A list of pending collaborator invitations across the repositories in the enterprise.

        pendingMemberInvitations - A list of pending member invitations for organizations in the enterprise.

        repositoryProjectsSetting - The setting value for whether repository projects are enabled in this enterprise.

        repositoryProjectsSettingOrganizations - A list of enterprise organizations configured with the provided repository projects setting value.

        samlIdentityProvider - The SAML Identity Provider for the enterprise.

        samlIdentityProviderSettingOrganizations - A list of enterprise organizations configured with the SAML single sign-on setting value.

        supportEntitlements - A list of members with a support entitlement.

        teamDiscussionsSetting - The setting value for whether team discussions are enabled for organizations in this enterprise.

        teamDiscussionsSettingOrganizations - A list of enterprise organizations configured with the provided team discussions setting value.

        twoFactorRequiredSetting - The setting value for whether the enterprise requires two-factor authentication for its organizations and users.

        twoFactorRequiredSettingOrganizations - A list of enterprise organizations configured with the two-factor authentication setting value.

    """

    admins: EnterpriseAdministratorConnection
    affiliated_users_with_two_factor_disabled: UserConnection
    affiliated_users_with_two_factor_disabled_exist: bool
    allow_private_repository_forking_setting: EnterpriseEnabledDisabledSettingValue
    allow_private_repository_forking_setting_organizations: OrganizationConnection
    allow_private_repository_forking_setting_policy_value: Optional[
        EnterpriseAllowPrivateRepositoryForkingPolicyValue
    ] = None
    default_repository_permission_setting: EnterpriseDefaultRepositoryPermissionSettingValue
    default_repository_permission_setting_organizations: OrganizationConnection
    domains: VerifiableDomainConnection
    enterprise_server_installations: EnterpriseServerInstallationConnection
    failed_invitations: EnterpriseFailedInvitationConnection
    ip_allow_list_enabled_setting: IpAllowListEnabledSettingValue
    ip_allow_list_entries: IpAllowListEntryConnection
    ip_allow_list_for_installed_apps_enabled_setting: IpAllowListForInstalledAppsEnabledSettingValue
    is_updating_default_repository_permission: bool
    is_updating_two_factor_requirement: bool
    members_can_change_repository_visibility_setting: EnterpriseEnabledDisabledSettingValue
    members_can_change_repository_visibility_setting_organizations: OrganizationConnection
    members_can_create_internal_repositories_setting: Optional[bool] = None
    members_can_create_private_repositories_setting: Optional[bool] = None
    members_can_create_public_repositories_setting: Optional[bool] = None
    members_can_create_repositories_setting: Optional[
        EnterpriseMembersCanCreateRepositoriesSettingValue
    ] = None
    members_can_create_repositories_setting_organizations: OrganizationConnection
    members_can_delete_issues_setting: EnterpriseEnabledDisabledSettingValue
    members_can_delete_issues_setting_organizations: OrganizationConnection
    members_can_delete_repositories_setting: EnterpriseEnabledDisabledSettingValue
    members_can_delete_repositories_setting_organizations: OrganizationConnection
    members_can_invite_collaborators_setting: EnterpriseEnabledDisabledSettingValue
    members_can_invite_collaborators_setting_organizations: OrganizationConnection
    members_can_make_purchases_setting: EnterpriseMembersCanMakePurchasesSettingValue
    members_can_update_protected_branches_setting: EnterpriseEnabledDisabledSettingValue
    members_can_update_protected_branches_setting_organizations: OrganizationConnection
    members_can_view_dependency_insights_setting: EnterpriseEnabledDisabledSettingValue
    members_can_view_dependency_insights_setting_organizations: OrganizationConnection
    notification_delivery_restriction_enabled_setting: NotificationRestrictionSettingValue
    oidc_provider: Optional[OIDCProvider] = None
    organization_projects_setting: EnterpriseEnabledDisabledSettingValue
    organization_projects_setting_organizations: OrganizationConnection
    outside_collaborators: EnterpriseOutsideCollaboratorConnection
    pending_admin_invitations: EnterpriseAdministratorInvitationConnection
    pending_collaborator_invitations: RepositoryInvitationConnection
    pending_member_invitations: EnterprisePendingMemberInvitationConnection
    repository_projects_setting: EnterpriseEnabledDisabledSettingValue
    repository_projects_setting_organizations: OrganizationConnection
    saml_identity_provider: Optional[EnterpriseIdentityProvider] = None
    saml_identity_provider_setting_organizations: OrganizationConnection
    support_entitlements: EnterpriseMemberConnection
    team_discussions_setting: EnterpriseEnabledDisabledSettingValue
    team_discussions_setting_organizations: OrganizationConnection
    two_factor_required_setting: EnterpriseEnabledSettingValue
    two_factor_required_setting_organizations: OrganizationConnection


@dataclass(kw_only=True)
class IpAllowListEntry:
    """
    IpAllowListEntry - An IP address or range of addresses that is allowed to access an owner's resources.

    allowListValue - A single IP address or range of IP addresses in CIDR notation.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the IpAllowListEntry object

    isActive - Whether the entry is currently active.

    name - The name of the IP allow list entry.

    owner - The owner of the IP allow list entry.

    updatedAt - Identifies the date and time when the object was last updated.

    """

    allow_list_value: str
    created_at: DateTime
    id: ID
    is_active: bool
    name: Optional[str] = None
    owner: IpAllowListOwner
    updated_at: DateTime


@dataclass(kw_only=True)
class IpAllowListEntryEdge:
    """
    IpAllowListEntryEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[IpAllowListEntry] = None


@dataclass(kw_only=True)
class BypassForcePushAllowance:
    """
    BypassForcePushAllowance - A user, team, or app who has the ability to bypass a force push requirement on a protected branch.

    actor - The actor that can force push.

    branchProtectionRule - Identifies the branch protection rule associated with the allowed user, team, or app.

    id - The Node ID of the BypassForcePushAllowance object

    """

    actor: Optional[BranchActorAllowanceActor] = None
    branch_protection_rule: Optional[BranchProtectionRule] = None
    id: ID


@dataclass(kw_only=True)
class BypassForcePushAllowanceEdge:
    """
    BypassForcePushAllowanceEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[BypassForcePushAllowance] = None


@dataclass(kw_only=True)
class BypassForcePushAllowanceConnection:
    """
    BypassForcePushAllowanceConnection - The connection type for BypassForcePushAllowance.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[BypassForcePushAllowanceEdge]] = None
    nodes: Optional[list[BypassForcePushAllowance]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class BypassPullRequestAllowance:
    """
    BypassPullRequestAllowance - A user, team, or app who has the ability to bypass a pull request requirement on a protected branch.

    actor - The actor that can bypass.

    branchProtectionRule - Identifies the branch protection rule associated with the allowed user, team, or app.

    id - The Node ID of the BypassPullRequestAllowance object

    """

    actor: Optional[BranchActorAllowanceActor] = None
    branch_protection_rule: Optional[BranchProtectionRule] = None
    id: ID


@dataclass(kw_only=True)
class BypassPullRequestAllowanceEdge:
    """
    BypassPullRequestAllowanceEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[BypassPullRequestAllowance] = None


@dataclass(kw_only=True)
class BypassPullRequestAllowanceConnection:
    """
    BypassPullRequestAllowanceConnection - The connection type for BypassPullRequestAllowance.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[BypassPullRequestAllowanceEdge]] = None
    nodes: Optional[list[BypassPullRequestAllowance]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PushAllowance:
    """
    PushAllowance - A team, user, or app who has the ability to push to a protected branch.

    actor - The actor that can push.

    branchProtectionRule - Identifies the branch protection rule associated with the allowed user, team, or app.

    id - The Node ID of the PushAllowance object

    """

    actor: Optional[PushAllowanceActor] = None
    branch_protection_rule: Optional[BranchProtectionRule] = None
    id: ID


@dataclass(kw_only=True)
class PushAllowanceEdge:
    """
    PushAllowanceEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[PushAllowance] = None


@dataclass(kw_only=True)
class PushAllowanceConnection:
    """
    PushAllowanceConnection - The connection type for PushAllowance.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[PushAllowanceEdge]] = None
    nodes: Optional[list[PushAllowance]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class RequiredStatusCheckDescription:
    """
    RequiredStatusCheckDescription - Represents a required status check for a protected branch, but not any specific run of that check.

    app - The App that must provide this status in order for it to be accepted.

    context - The name of this status.

    """

    app: Optional[App] = None
    context: str


@dataclass(kw_only=True)
class ReviewDismissalAllowance:
    """
    ReviewDismissalAllowance - A user, team, or app who has the ability to dismiss a review on a protected branch.

    actor - The actor that can dismiss.

    branchProtectionRule - Identifies the branch protection rule associated with the allowed user, team, or app.

    id - The Node ID of the ReviewDismissalAllowance object

    """

    actor: Optional[ReviewDismissalAllowanceActor] = None
    branch_protection_rule: Optional[BranchProtectionRule] = None
    id: ID


@dataclass(kw_only=True)
class ReviewDismissalAllowanceEdge:
    """
    ReviewDismissalAllowanceEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[ReviewDismissalAllowance] = None


@dataclass(kw_only=True)
class ReviewDismissalAllowanceConnection:
    """
    ReviewDismissalAllowanceConnection - The connection type for ReviewDismissalAllowance.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[ReviewDismissalAllowanceEdge]] = None
    nodes: Optional[list[ReviewDismissalAllowance]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class CommitEdge:
    """
    CommitEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Commit] = None


@dataclass(kw_only=True)
class ComparisonCommitConnection:
    """
    ComparisonCommitConnection - The connection type for Commit.

    authorCount - The total count of authors and co-authors across all commits.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    author_count: int
    edges: Optional[list[CommitEdge]] = None
    nodes: Optional[list[Commit]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class Comparison:
    """
    Comparison - Represents a comparison between two commit revisions.

    aheadBy - The number of commits ahead of the base branch.

    baseTarget - The base revision of this comparison.

    behindBy - The number of commits behind the base branch.

    commits - The commits which compose this comparison.

    headTarget - The head revision of this comparison.

    id - The Node ID of the Comparison object

    status - The status of this comparison.

    """

    ahead_by: int
    base_target: GitObject
    behind_by: int
    commits: ComparisonCommitConnection
    head_target: GitObject
    id: ID
    status: ComparisonStatus


@dataclass(kw_only=True)
class IssueCommentConnection:
    """
    IssueCommentConnection - The connection type for IssueComment.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[IssueCommentEdge]] = None
    nodes: Optional[list[IssueComment]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PullRequestCommit:
    """
    PullRequestCommit - Represents a Git commit part of a pull request.

    commit - The Git commit object

    id - The Node ID of the PullRequestCommit object

    pullRequest - The pull request this commit belongs to

    resourcePath - The HTTP path for this pull request commit

    url - The HTTP URL for this pull request commit

    """

    commit: Commit
    id: ID
    pull_request: PullRequest
    resource_path: URI
    url: URI


@dataclass(kw_only=True)
class PullRequestCommitEdge:
    """
    PullRequestCommitEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[PullRequestCommit] = None


@dataclass(kw_only=True)
class PullRequestCommitConnection:
    """
    PullRequestCommitConnection - The connection type for PullRequestCommit.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[PullRequestCommitEdge]] = None
    nodes: Optional[list[PullRequestCommit]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PullRequestChangedFileEdge:
    """
    PullRequestChangedFileEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[PullRequestChangedFile] = None


@dataclass(kw_only=True)
class PullRequestChangedFileConnection:
    """
    PullRequestChangedFileConnection - The connection type for PullRequestChangedFile.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[PullRequestChangedFileEdge]] = None
    nodes: Optional[list[PullRequestChangedFile]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class Hovercard:
    """
    Hovercard - Detail needed to display a hovercard for a user

    contexts - Each of the contexts for this hovercard

    """

    contexts: list[HovercardContext]


@dataclass(kw_only=True)
class PullRequestReviewCommentEdge:
    """
    PullRequestReviewCommentEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[PullRequestReviewComment] = None


@dataclass(kw_only=True)
class PullRequestReviewCommentConnection:
    """
    PullRequestReviewCommentConnection - The connection type for PullRequestReviewComment.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[PullRequestReviewCommentEdge]] = None
    nodes: Optional[list[PullRequestReviewComment]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PullRequestReviewEdge:
    """
    PullRequestReviewEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[PullRequestReview] = None


@dataclass(kw_only=True)
class PullRequestReviewConnection:
    """
    PullRequestReviewConnection - The connection type for PullRequestReview.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[PullRequestReviewEdge]] = None
    nodes: Optional[list[PullRequestReview]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ReviewRequest:
    """
    ReviewRequest - A request for a user to review a pull request.

    asCodeOwner - Whether this request was created for a code owner

    databaseId - Identifies the primary key from the database.

    id - The Node ID of the ReviewRequest object

    pullRequest - Identifies the pull request associated with this review request.

    requestedReviewer - The reviewer that is requested.

    """

    as_code_owner: bool
    database_id: Optional[int] = None
    id: ID
    pull_request: PullRequest
    requested_reviewer: Optional[RequestedReviewer] = None


@dataclass(kw_only=True)
class ReviewRequestEdge:
    """
    ReviewRequestEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[ReviewRequest] = None


@dataclass(kw_only=True)
class ReviewRequestConnection:
    """
    ReviewRequestConnection - The connection type for ReviewRequest.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[ReviewRequestEdge]] = None
    nodes: Optional[list[ReviewRequest]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PullRequestReviewThread:
    """
    PullRequestReviewThread - A threaded list of comments for a given pull request.

    comments - A list of pull request comments associated with the thread.

    diffSide - The side of the diff on which this thread was placed.

    id - The Node ID of the PullRequestReviewThread object

    isCollapsed - Whether or not the thread has been collapsed (resolved)

    isOutdated - Indicates whether this thread was outdated by newer changes.

    isResolved - Whether this thread has been resolved

    line - The line in the file to which this thread refers

    originalLine - The original line in the file to which this thread refers.

    originalStartLine - The original start line in the file to which this thread refers (multi-line only).

    path - Identifies the file path of this thread.

    pullRequest - Identifies the pull request associated with this thread.

    repository - Identifies the repository associated with this thread.

    resolvedBy - The user who resolved this thread

    startDiffSide - The side of the diff that the first line of the thread starts on (multi-line only)

    startLine - The start line in the file to which this thread refers (multi-line only)

    subjectType - The level at which the comments in the corresponding thread are targeted, can be a diff line or a file

    viewerCanReply - Indicates whether the current viewer can reply to this thread.

    viewerCanResolve - Whether or not the viewer can resolve this thread

    viewerCanUnresolve - Whether or not the viewer can unresolve this thread

    """

    comments: PullRequestReviewCommentConnection
    diff_side: DiffSide
    id: ID
    is_collapsed: bool
    is_outdated: bool
    is_resolved: bool
    line: Optional[int] = None
    original_line: Optional[int] = None
    original_start_line: Optional[int] = None
    path: str
    pull_request: PullRequest
    repository: Repository
    resolved_by: Optional[User] = None
    start_diff_side: Optional[DiffSide] = None
    start_line: Optional[int] = None
    subject_type: PullRequestReviewThreadSubjectType
    viewer_can_reply: bool
    viewer_can_resolve: bool
    viewer_can_unresolve: bool


@dataclass(kw_only=True)
class PullRequestReviewThreadEdge:
    """
    PullRequestReviewThreadEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[PullRequestReviewThread] = None


@dataclass(kw_only=True)
class PullRequestReviewThreadConnection:
    """
    PullRequestReviewThreadConnection - Review comment threads for a pull request review.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[PullRequestReviewThreadEdge]] = None
    nodes: Optional[list[PullRequestReviewThread]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class SuggestedReviewer:
    """
    SuggestedReviewer - A suggestion to review a pull request based on a user's commit history and review comments.

    isAuthor - Is this suggestion based on past commits?

    isCommenter - Is this suggestion based on past review comments?

    reviewer - Identifies the user suggested to review the pull request.

    """

    is_author: bool
    is_commenter: bool
    reviewer: User


@dataclass(kw_only=True)
class Assignable:
    """
    Assignable - An object that can have users assigned to it.

    assignees - A list of Users assigned to this object.

    """

    assignees: UserConnection


@dataclass(kw_only=True)
class AssignedEvent:
    """
    AssignedEvent - Represents an 'assigned' event on any assignable object.

    actor - Identifies the actor who performed the event.

    assignable - Identifies the assignable associated with the event.

    assignee - Identifies the user or mannequin that was assigned.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the AssignedEvent object

    """

    actor: Optional[Actor] = None
    assignable: Assignable
    assignee: Optional[Assignee] = None
    created_at: DateTime
    id: ID


@dataclass(kw_only=True)
class BaseRefDeletedEvent:
    """
    BaseRefDeletedEvent - Represents a 'base_ref_deleted' event on a given pull request.

    actor - Identifies the actor who performed the event.

    baseRefName - Identifies the name of the Ref associated with the `base_ref_deleted` event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the BaseRefDeletedEvent object

    pullRequest - PullRequest referenced by event.

    """

    actor: Optional[Actor] = None
    base_ref_name: Optional[str] = None
    created_at: DateTime
    id: ID
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class BaseRefForcePushedEvent:
    """
    BaseRefForcePushedEvent - Represents a 'base_ref_force_pushed' event on a given pull request.

    actor - Identifies the actor who performed the event.

    afterCommit - Identifies the after commit SHA for the 'base_ref_force_pushed' event.

    beforeCommit - Identifies the before commit SHA for the 'base_ref_force_pushed' event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the BaseRefForcePushedEvent object

    pullRequest - PullRequest referenced by event.

    ref - Identifies the fully qualified ref name for the 'base_ref_force_pushed' event.

    """

    actor: Optional[Actor] = None
    after_commit: Optional[Commit] = None
    before_commit: Optional[Commit] = None
    created_at: DateTime
    id: ID
    pull_request: PullRequest
    ref: Optional[Ref] = None


@dataclass(kw_only=True)
class ClosedEvent:
    """
    ClosedEvent - Represents a 'closed' event on any `Closable`.

    actor - Identifies the actor who performed the event.

    closable - Object that was closed.

    closer - Object which triggered the creation of this event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the ClosedEvent object

    resourcePath - The HTTP path for this closed event.

    stateReason - The reason the issue state was changed to closed.

    url - The HTTP URL for this closed event.

    """

    actor: Optional[Actor] = None
    closable: Closable
    closer: Optional[Closer] = None
    created_at: DateTime
    id: ID
    resource_path: URI
    state_reason: Optional[IssueStateReason] = None
    url: URI


@dataclass(kw_only=True)
class CommitCommentThread:
    """
    CommitCommentThread - A thread of comments on a commit.

    comments - The comments that exist in this thread.

    commit - The commit the comments were made on.

    id - The Node ID of the CommitCommentThread object

    path - The file the comments were made on.

    position - The position in the diff for the commit that the comment was made on.

    repository - The repository associated with this node.

    """

    comments: CommitCommentConnection
    commit: Optional[Commit] = None
    id: ID
    path: Optional[str] = None
    position: Optional[int] = None
    repository: Repository


@dataclass(kw_only=True)
class CrossReferencedEvent:
    """
    CrossReferencedEvent - Represents a mention made by one issue or pull request to another.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the CrossReferencedEvent object

    isCrossRepository - Reference originated in a different repository.

    referencedAt - Identifies when the reference was made.

    resourcePath - The HTTP path for this pull request.

    source - Issue or pull request that made the reference.

    target - Issue or pull request to which the reference was made.

    url - The HTTP URL for this pull request.

    willCloseTarget - Checks if the target will be closed when the source is merged.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    is_cross_repository: bool
    referenced_at: DateTime
    resource_path: URI
    source: ReferencedSubject
    target: ReferencedSubject
    url: URI
    will_close_target: bool


@dataclass(kw_only=True)
class DemilestonedEvent:
    """
    DemilestonedEvent - Represents a 'demilestoned' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the DemilestonedEvent object

    milestoneTitle - Identifies the milestone title associated with the 'demilestoned' event.

    subject - Object referenced by event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    milestone_title: str
    subject: MilestoneItem


@dataclass(kw_only=True)
class DeployedEvent:
    """
    DeployedEvent - Represents a 'deployed' event on a given pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    deployment - The deployment associated with the 'deployed' event.

    id - The Node ID of the DeployedEvent object

    pullRequest - PullRequest referenced by event.

    ref - The ref associated with the 'deployed' event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    database_id: Optional[int] = None
    deployment: Deployment
    id: ID
    pull_request: PullRequest
    ref: Optional[Ref] = None


@dataclass(kw_only=True)
class DeploymentEnvironmentChangedEvent:
    """
    DeploymentEnvironmentChangedEvent - Represents a 'deployment_environment_changed' event on a given pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    deploymentStatus - The deployment status that updated the deployment environment.

    id - The Node ID of the DeploymentEnvironmentChangedEvent object

    pullRequest - PullRequest referenced by event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    deployment_status: DeploymentStatus
    id: ID
    pull_request: PullRequest


@dataclass(kw_only=True)
class HeadRefDeletedEvent:
    """
    HeadRefDeletedEvent - Represents a 'head_ref_deleted' event on a given pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    headRef - Identifies the Ref associated with the `head_ref_deleted` event.

    headRefName - Identifies the name of the Ref associated with the `head_ref_deleted` event.

    id - The Node ID of the HeadRefDeletedEvent object

    pullRequest - PullRequest referenced by event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    head_ref: Optional[Ref] = None
    head_ref_name: str
    id: ID
    pull_request: PullRequest


@dataclass(kw_only=True)
class HeadRefForcePushedEvent:
    """
    HeadRefForcePushedEvent - Represents a 'head_ref_force_pushed' event on a given pull request.

    actor - Identifies the actor who performed the event.

    afterCommit - Identifies the after commit SHA for the 'head_ref_force_pushed' event.

    beforeCommit - Identifies the before commit SHA for the 'head_ref_force_pushed' event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the HeadRefForcePushedEvent object

    pullRequest - PullRequest referenced by event.

    ref - Identifies the fully qualified ref name for the 'head_ref_force_pushed' event.

    """

    actor: Optional[Actor] = None
    after_commit: Optional[Commit] = None
    before_commit: Optional[Commit] = None
    created_at: DateTime
    id: ID
    pull_request: PullRequest
    ref: Optional[Ref] = None


@dataclass(kw_only=True)
class HeadRefRestoredEvent:
    """
    HeadRefRestoredEvent - Represents a 'head_ref_restored' event on a given pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the HeadRefRestoredEvent object

    pullRequest - PullRequest referenced by event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    pull_request: PullRequest


@dataclass(kw_only=True)
class Labelable:
    """
    Labelable - An object that can have labels assigned to it.

    labels - A list of labels associated with the object.

    """

    labels: Optional[LabelConnection] = None


@dataclass(kw_only=True)
class LabeledEvent:
    """
    LabeledEvent - Represents a 'labeled' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the LabeledEvent object

    label - Identifies the label associated with the 'labeled' event.

    labelable - Identifies the `Labelable` associated with the event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    label: Label
    labelable: Labelable


@dataclass(kw_only=True)
class LockedEvent:
    """
    LockedEvent - Represents a 'locked' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the LockedEvent object

    lockReason - Reason that the conversation was locked (optional).

    lockable - Object that was locked.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    lock_reason: Optional[LockReason] = None
    lockable: Lockable


@dataclass(kw_only=True)
class MergedEvent:
    """
    MergedEvent - Represents a 'merged' event on a given pull request.

    actor - Identifies the actor who performed the event.

    commit - Identifies the commit associated with the `merge` event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the MergedEvent object

    mergeRef - Identifies the Ref associated with the `merge` event.

    mergeRefName - Identifies the name of the Ref associated with the `merge` event.

    pullRequest - PullRequest referenced by event.

    resourcePath - The HTTP path for this merged event.

    url - The HTTP URL for this merged event.

    """

    actor: Optional[Actor] = None
    commit: Optional[Commit] = None
    created_at: DateTime
    id: ID
    merge_ref: Optional[Ref] = None
    merge_ref_name: str
    pull_request: PullRequest
    resource_path: URI
    url: URI


@dataclass(kw_only=True)
class MilestonedEvent:
    """
    MilestonedEvent - Represents a 'milestoned' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the MilestonedEvent object

    milestoneTitle - Identifies the milestone title associated with the 'milestoned' event.

    subject - Object referenced by event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    milestone_title: str
    subject: MilestoneItem


@dataclass(kw_only=True)
class ReferencedEvent:
    """
    ReferencedEvent - Represents a 'referenced' event on a given `ReferencedSubject`.

    actor - Identifies the actor who performed the event.

    commit - Identifies the commit associated with the 'referenced' event.

    commitRepository - Identifies the repository associated with the 'referenced' event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the ReferencedEvent object

    isCrossRepository - Reference originated in a different repository.

    isDirectReference - Checks if the commit message itself references the subject. Can be false in the case of a commit comment reference.

    subject - Object referenced by event.

    """

    actor: Optional[Actor] = None
    commit: Optional[Commit] = None
    commit_repository: Repository
    created_at: DateTime
    id: ID
    is_cross_repository: bool
    is_direct_reference: bool
    subject: ReferencedSubject


@dataclass(kw_only=True)
class RenamedTitleEvent:
    """
    RenamedTitleEvent - Represents a 'renamed' event on a given issue or pull request

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    currentTitle - Identifies the current title of the issue or pull request.

    id - The Node ID of the RenamedTitleEvent object

    previousTitle - Identifies the previous title of the issue or pull request.

    subject - Subject that was renamed.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    current_title: str
    id: ID
    previous_title: str
    subject: RenamedTitleSubject


@dataclass(kw_only=True)
class ReopenedEvent:
    """
    ReopenedEvent - Represents a 'reopened' event on any `Closable`.

    actor - Identifies the actor who performed the event.

    closable - Object that was reopened.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the ReopenedEvent object

    stateReason - The reason the issue state was changed to open.

    """

    actor: Optional[Actor] = None
    closable: Closable
    created_at: DateTime
    id: ID
    state_reason: Optional[IssueStateReason] = None


@dataclass(kw_only=True)
class ReviewDismissedEvent:
    """
    ReviewDismissedEvent - Represents a 'review_dismissed' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    dismissalMessage - Identifies the optional message associated with the 'review_dismissed' event.

    dismissalMessageHTML - Identifies the optional message associated with the event, rendered to HTML.

    id - The Node ID of the ReviewDismissedEvent object

    previousReviewState - Identifies the previous state of the review with the 'review_dismissed' event.

    pullRequest - PullRequest referenced by event.

    pullRequestCommit - Identifies the commit which caused the review to become stale.

    resourcePath - The HTTP path for this review dismissed event.

    review - Identifies the review associated with the 'review_dismissed' event.

    url - The HTTP URL for this review dismissed event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    database_id: Optional[int] = None
    dismissal_message: Optional[str] = None
    dismissal_message_h_t_m_l: Optional[str] = None
    id: ID
    previous_review_state: PullRequestReviewState
    pull_request: PullRequest
    pull_request_commit: Optional[PullRequestCommit] = None
    resource_path: URI
    review: Optional[PullRequestReview] = None
    url: URI


@dataclass(kw_only=True)
class ReviewRequestRemovedEvent:
    """
    ReviewRequestRemovedEvent - Represents an 'review_request_removed' event on a given pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the ReviewRequestRemovedEvent object

    pullRequest - PullRequest referenced by event.

    requestedReviewer - Identifies the reviewer whose review request was removed.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    pull_request: PullRequest
    requested_reviewer: Optional[RequestedReviewer] = None


@dataclass(kw_only=True)
class ReviewRequestedEvent:
    """
    ReviewRequestedEvent - Represents an 'review_requested' event on a given pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the ReviewRequestedEvent object

    pullRequest - PullRequest referenced by event.

    requestedReviewer - Identifies the reviewer whose review was requested.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    pull_request: PullRequest
    requested_reviewer: Optional[RequestedReviewer] = None


@dataclass(kw_only=True)
class SubscribedEvent:
    """
    SubscribedEvent - Represents a 'subscribed' event on a given `Subscribable`.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the SubscribedEvent object

    subscribable - Object referenced by event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    subscribable: Subscribable


@dataclass(kw_only=True)
class UnassignedEvent:
    """
    UnassignedEvent - Represents an 'unassigned' event on any assignable object.

    actor - Identifies the actor who performed the event.

    assignable - Identifies the assignable associated with the event.

    assignee - Identifies the user or mannequin that was unassigned.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the UnassignedEvent object

    """

    actor: Optional[Actor] = None
    assignable: Assignable
    assignee: Optional[Assignee] = None
    created_at: DateTime
    id: ID


@dataclass(kw_only=True)
class UnlabeledEvent:
    """
    UnlabeledEvent - Represents an 'unlabeled' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the UnlabeledEvent object

    label - Identifies the label associated with the 'unlabeled' event.

    labelable - Identifies the `Labelable` associated with the event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    label: Label
    labelable: Labelable


@dataclass(kw_only=True)
class UnlockedEvent:
    """
    UnlockedEvent - Represents an 'unlocked' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the UnlockedEvent object

    lockable - Object that was unlocked.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    lockable: Lockable


@dataclass(kw_only=True)
class UnsubscribedEvent:
    """
    UnsubscribedEvent - Represents an 'unsubscribed' event on a given `Subscribable`.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the UnsubscribedEvent object

    subscribable - Object referenced by event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    subscribable: Subscribable


@dataclass(kw_only=True)
class UserBlockedEvent:
    """
    UserBlockedEvent - Represents a 'user_blocked' event on a given user.

    actor - Identifies the actor who performed the event.

    blockDuration - Number of days that the user was blocked for.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the UserBlockedEvent object

    subject - The user who was blocked.

    """

    actor: Optional[Actor] = None
    block_duration: UserBlockDuration
    created_at: DateTime
    id: ID
    subject: Optional[User] = None


@dataclass(kw_only=True)
class PullRequestTimelineItemEdge:
    """
    PullRequestTimelineItemEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[PullRequestTimelineItem] = None


@dataclass(kw_only=True)
class PullRequestTimelineConnection:
    """
    PullRequestTimelineConnection - The connection type for PullRequestTimelineItem.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[PullRequestTimelineItemEdge]] = None
    nodes: Optional[list[PullRequestTimelineItem]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class AddedToMergeQueueEvent:
    """
    AddedToMergeQueueEvent - Represents an 'added_to_merge_queue' event on a given pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    enqueuer - The user who added this Pull Request to the merge queue

    id - The Node ID of the AddedToMergeQueueEvent object

    mergeQueue - The merge queue where this pull request was added to.

    pullRequest - PullRequest referenced by event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    enqueuer: Optional[User] = None
    id: ID
    merge_queue: Optional[MergeQueue] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class AddedToProjectEvent:
    """
    AddedToProjectEvent - Represents a 'added_to_project' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    id - The Node ID of the AddedToProjectEvent object

    project - Project referenced by event.

    projectCard - Project card referenced by this project event.

    projectColumnName - Column name referenced by this project event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    database_id: Optional[int] = None
    id: ID
    project: Optional[Project] = None
    project_card: Optional[ProjectCard] = None
    project_column_name: str


@dataclass(kw_only=True)
class AutoMergeDisabledEvent:
    """
    AutoMergeDisabledEvent - Represents a 'auto_merge_disabled' event on a given pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    disabler - The user who disabled auto-merge for this Pull Request

    id - The Node ID of the AutoMergeDisabledEvent object

    pullRequest - PullRequest referenced by event

    reason - The reason auto-merge was disabled

    reasonCode - The reason_code relating to why auto-merge was disabled

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    disabler: Optional[User] = None
    id: ID
    pull_request: Optional[PullRequest] = None
    reason: Optional[str] = None
    reason_code: Optional[str] = None


@dataclass(kw_only=True)
class AutoMergeEnabledEvent:
    """
    AutoMergeEnabledEvent - Represents a 'auto_merge_enabled' event on a given pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    enabler - The user who enabled auto-merge for this Pull Request

    id - The Node ID of the AutoMergeEnabledEvent object

    pullRequest - PullRequest referenced by event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    enabler: Optional[User] = None
    id: ID
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class AutoRebaseEnabledEvent:
    """
    AutoRebaseEnabledEvent - Represents a 'auto_rebase_enabled' event on a given pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    enabler - The user who enabled auto-merge (rebase) for this Pull Request

    id - The Node ID of the AutoRebaseEnabledEvent object

    pullRequest - PullRequest referenced by event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    enabler: Optional[User] = None
    id: ID
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class AutoSquashEnabledEvent:
    """
    AutoSquashEnabledEvent - Represents a 'auto_squash_enabled' event on a given pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    enabler - The user who enabled auto-merge (squash) for this Pull Request

    id - The Node ID of the AutoSquashEnabledEvent object

    pullRequest - PullRequest referenced by event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    enabler: Optional[User] = None
    id: ID
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class AutomaticBaseChangeFailedEvent:
    """
    AutomaticBaseChangeFailedEvent - Represents a 'automatic_base_change_failed' event on a given pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the AutomaticBaseChangeFailedEvent object

    newBase - The new base for this PR

    oldBase - The old base for this PR

    pullRequest - PullRequest referenced by event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    new_base: str
    old_base: str
    pull_request: PullRequest


@dataclass(kw_only=True)
class AutomaticBaseChangeSucceededEvent:
    """
    AutomaticBaseChangeSucceededEvent - Represents a 'automatic_base_change_succeeded' event on a given pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the AutomaticBaseChangeSucceededEvent object

    newBase - The new base for this PR

    oldBase - The old base for this PR

    pullRequest - PullRequest referenced by event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    new_base: str
    old_base: str
    pull_request: PullRequest


@dataclass(kw_only=True)
class BaseRefChangedEvent:
    """
    BaseRefChangedEvent - Represents a 'base_ref_changed' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    currentRefName - Identifies the name of the base ref for the pull request after it was changed.

    databaseId - Identifies the primary key from the database.

    id - The Node ID of the BaseRefChangedEvent object

    previousRefName - Identifies the name of the base ref for the pull request before it was changed.

    pullRequest - PullRequest referenced by event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    current_ref_name: str
    database_id: Optional[int] = None
    id: ID
    previous_ref_name: str
    pull_request: PullRequest


@dataclass(kw_only=True)
class CommentDeletedEvent:
    """
    CommentDeletedEvent - Represents a 'comment_deleted' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    deletedCommentAuthor - The user who authored the deleted comment.

    id - The Node ID of the CommentDeletedEvent object

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    database_id: Optional[int] = None
    deleted_comment_author: Optional[Actor] = None
    id: ID


@dataclass(kw_only=True)
class ConnectedEvent:
    """
    ConnectedEvent - Represents a 'connected' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the ConnectedEvent object

    isCrossRepository - Reference originated in a different repository.

    source - Issue or pull request that made the reference.

    subject - Issue or pull request which was connected.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    is_cross_repository: bool
    source: ReferencedSubject
    subject: ReferencedSubject


@dataclass(kw_only=True)
class ConvertToDraftEvent:
    """
    ConvertToDraftEvent - Represents a 'convert_to_draft' event on a given pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the ConvertToDraftEvent object

    pullRequest - PullRequest referenced by event.

    resourcePath - The HTTP path for this convert to draft event.

    url - The HTTP URL for this convert to draft event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    pull_request: PullRequest
    resource_path: URI
    url: URI


@dataclass(kw_only=True)
class ConvertedNoteToIssueEvent:
    """
    ConvertedNoteToIssueEvent - Represents a 'converted_note_to_issue' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    id - The Node ID of the ConvertedNoteToIssueEvent object

    project - Project referenced by event.

    projectCard - Project card referenced by this project event.

    projectColumnName - Column name referenced by this project event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    database_id: Optional[int] = None
    id: ID
    project: Optional[Project] = None
    project_card: Optional[ProjectCard] = None
    project_column_name: str


@dataclass(kw_only=True)
class ConvertedToDiscussionEvent:
    """
    ConvertedToDiscussionEvent - Represents a 'converted_to_discussion' event on a given issue.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    discussion - The discussion that the issue was converted into.

    id - The Node ID of the ConvertedToDiscussionEvent object

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    discussion: Optional[Discussion] = None
    id: ID


@dataclass(kw_only=True)
class DisconnectedEvent:
    """
    DisconnectedEvent - Represents a 'disconnected' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the DisconnectedEvent object

    isCrossRepository - Reference originated in a different repository.

    source - Issue or pull request from which the issue was disconnected.

    subject - Issue or pull request which was disconnected.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    is_cross_repository: bool
    source: ReferencedSubject
    subject: ReferencedSubject


@dataclass(kw_only=True)
class MarkedAsDuplicateEvent:
    """
    MarkedAsDuplicateEvent - Represents a 'marked_as_duplicate' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    canonical - The authoritative issue or pull request which has been duplicated by another.

    createdAt - Identifies the date and time when the object was created.

    duplicate - The issue or pull request which has been marked as a duplicate of another.

    id - The Node ID of the MarkedAsDuplicateEvent object

    isCrossRepository - Canonical and duplicate belong to different repositories.

    """

    actor: Optional[Actor] = None
    canonical: Optional[IssueOrPullRequest] = None
    created_at: DateTime
    duplicate: Optional[IssueOrPullRequest] = None
    id: ID
    is_cross_repository: bool


@dataclass(kw_only=True)
class MentionedEvent:
    """
    MentionedEvent - Represents a 'mentioned' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    id - The Node ID of the MentionedEvent object

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    database_id: Optional[int] = None
    id: ID


@dataclass(kw_only=True)
class MovedColumnsInProjectEvent:
    """
    MovedColumnsInProjectEvent - Represents a 'moved_columns_in_project' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    id - The Node ID of the MovedColumnsInProjectEvent object

    previousProjectColumnName - Column name the issue or pull request was moved from.

    project - Project referenced by event.

    projectCard - Project card referenced by this project event.

    projectColumnName - Column name the issue or pull request was moved to.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    database_id: Optional[int] = None
    id: ID
    previous_project_column_name: str
    project: Optional[Project] = None
    project_card: Optional[ProjectCard] = None
    project_column_name: str


@dataclass(kw_only=True)
class PinnedEvent:
    """
    PinnedEvent - Represents a 'pinned' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the PinnedEvent object

    issue - Identifies the issue associated with the event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    issue: Issue


@dataclass(kw_only=True)
class PullRequestCommitCommentThread:
    """
    PullRequestCommitCommentThread - Represents a commit comment thread part of a pull request.

    comments - The comments that exist in this thread.

    commit - The commit the comments were made on.

    id - The Node ID of the PullRequestCommitCommentThread object

    path - The file the comments were made on.

    position - The position in the diff for the commit that the comment was made on.

    pullRequest - The pull request this commit comment thread belongs to

    repository - The repository associated with this node.

    """

    comments: CommitCommentConnection
    commit: Commit
    id: ID
    path: Optional[str] = None
    position: Optional[int] = None
    pull_request: PullRequest
    repository: Repository


@dataclass(kw_only=True)
class PullRequestRevisionMarker:
    """
    PullRequestRevisionMarker - Represents the latest point in the pull request timeline for which the viewer has seen the pull request's commits.

    createdAt - Identifies the date and time when the object was created.

    lastSeenCommit - The last commit the viewer has seen.

    pullRequest - The pull request to which the marker belongs.

    """

    created_at: DateTime
    last_seen_commit: Commit
    pull_request: PullRequest


@dataclass(kw_only=True)
class ReadyForReviewEvent:
    """
    ReadyForReviewEvent - Represents a 'ready_for_review' event on a given pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the ReadyForReviewEvent object

    pullRequest - PullRequest referenced by event.

    resourcePath - The HTTP path for this ready for review event.

    url - The HTTP URL for this ready for review event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    pull_request: PullRequest
    resource_path: URI
    url: URI


@dataclass(kw_only=True)
class RemovedFromMergeQueueEvent:
    """
    RemovedFromMergeQueueEvent - Represents a 'removed_from_merge_queue' event on a given pull request.

    actor - Identifies the actor who performed the event.

    beforeCommit - Identifies the before commit SHA for the 'removed_from_merge_queue' event.

    createdAt - Identifies the date and time when the object was created.

    enqueuer - The user who removed this Pull Request from the merge queue

    id - The Node ID of the RemovedFromMergeQueueEvent object

    mergeQueue - The merge queue where this pull request was removed from.

    pullRequest - PullRequest referenced by event.

    reason - The reason this pull request was removed from the queue.

    """

    actor: Optional[Actor] = None
    before_commit: Optional[Commit] = None
    created_at: DateTime
    enqueuer: Optional[User] = None
    id: ID
    merge_queue: Optional[MergeQueue] = None
    pull_request: Optional[PullRequest] = None
    reason: Optional[str] = None


@dataclass(kw_only=True)
class RemovedFromProjectEvent:
    """
    RemovedFromProjectEvent - Represents a 'removed_from_project' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    id - The Node ID of the RemovedFromProjectEvent object

    project - Project referenced by event.

    projectColumnName - Column name referenced by this project event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    database_id: Optional[int] = None
    id: ID
    project: Optional[Project] = None
    project_column_name: str


@dataclass(kw_only=True)
class TransferredEvent:
    """
    TransferredEvent - Represents a 'transferred' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    fromRepository - The repository this came from

    id - The Node ID of the TransferredEvent object

    issue - Identifies the issue associated with the event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    from_repository: Optional[Repository] = None
    id: ID
    issue: Issue


@dataclass(kw_only=True)
class UnmarkedAsDuplicateEvent:
    """
    UnmarkedAsDuplicateEvent - Represents an 'unmarked_as_duplicate' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    canonical - The authoritative issue or pull request which has been duplicated by another.

    createdAt - Identifies the date and time when the object was created.

    duplicate - The issue or pull request which has been marked as a duplicate of another.

    id - The Node ID of the UnmarkedAsDuplicateEvent object

    isCrossRepository - Canonical and duplicate belong to different repositories.

    """

    actor: Optional[Actor] = None
    canonical: Optional[IssueOrPullRequest] = None
    created_at: DateTime
    duplicate: Optional[IssueOrPullRequest] = None
    id: ID
    is_cross_repository: bool


@dataclass(kw_only=True)
class UnpinnedEvent:
    """
    UnpinnedEvent - Represents an 'unpinned' event on a given issue or pull request.

    actor - Identifies the actor who performed the event.

    createdAt - Identifies the date and time when the object was created.

    id - The Node ID of the UnpinnedEvent object

    issue - Identifies the issue associated with the event.

    """

    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    issue: Issue


@dataclass(kw_only=True)
class PullRequestTimelineItemsEdge:
    """
    PullRequestTimelineItemsEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[PullRequestTimelineItems] = None


@dataclass(kw_only=True)
class PullRequestTimelineItemsConnection:
    """
    PullRequestTimelineItemsConnection - The connection type for PullRequestTimelineItems.

    edges - A list of edges.

    filteredCount - Identifies the count of items after applying `before` and `after` filters.

    nodes - A list of nodes.

    pageCount - Identifies the count of items after applying `before`/`after` filters and `first`/`last`/`skip` slicing.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    updatedAt - Identifies the date and time when the timeline was last updated.

    """

    edges: Optional[list[PullRequestTimelineItemsEdge]] = None
    filtered_count: int
    nodes: Optional[list[PullRequestTimelineItems]] = None
    page_count: int
    page_info: PageInfo
    total_count: int
    updated_at: DateTime


@dataclass(kw_only=True)
class PullRequestEdge:
    """
    PullRequestEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[PullRequest] = None


@dataclass(kw_only=True)
class GitActor:
    """
    GitActor - Represents an actor in a Git commit (ie. an author or committer).

    avatarUrl - A URL pointing to the author's public avatar.

    date - The timestamp of the Git action (authoring or committing).

    email - The email in the Git commit.

    name - The name in the Git commit.

    user - The GitHub user corresponding to the email field. Null if no such user exists.

    """

    avatar_url: URI
    date: Optional[GitTimestamp] = None
    email: Optional[str] = None
    name: Optional[str] = None
    user: Optional[User] = None


@dataclass(kw_only=True)
class GitActorEdge:
    """
    GitActorEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[GitActor] = None


@dataclass(kw_only=True)
class GitActorConnection:
    """
    GitActorConnection - The connection type for GitActor.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[GitActorEdge]] = None
    nodes: Optional[list[GitActor]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class BlameRange:
    """
        BlameRange - Represents a range of information from a Git blame.

        age - Identifies the recency of the change, from 1 (new) to 10 (old). This is
    calculated as a 2-quantile and determines the length of distance between the
    median age of all the changes in the file and the recency of the current
    range's change.

        commit - Identifies the line author

        endingLine - The ending line for the range

        startingLine - The starting line for the range

    """

    age: int
    commit: Commit
    ending_line: int
    starting_line: int


@dataclass(kw_only=True)
class Blame:
    """
    Blame - Represents a Git blame.

    ranges - The list of ranges from a Git blame.

    """

    ranges: list[BlameRange]


@dataclass(kw_only=True)
class CheckAnnotationSpan:
    """
    CheckAnnotationSpan - An inclusive pair of positions for a check annotation.

    end - End position (inclusive).

    start - Start position (inclusive).

    """

    end: CheckAnnotationPosition
    start: CheckAnnotationPosition


@dataclass(kw_only=True)
class CheckAnnotation:
    """
    CheckAnnotation - A single check annotation.

    annotationLevel - The annotation's severity level.

    blobUrl - The path to the file that this annotation was made on.

    databaseId - Identifies the primary key from the database.

    location - The position of this annotation.

    message - The annotation's message.

    path - The path that this annotation was made on.

    rawDetails - Additional information about the annotation.

    title - The annotation's title

    """

    annotation_level: Optional[CheckAnnotationLevel] = None
    blob_url: URI
    database_id: Optional[int] = None
    location: CheckAnnotationSpan
    message: str
    path: str
    raw_details: Optional[str] = None
    title: Optional[str] = None


@dataclass(kw_only=True)
class CheckAnnotationEdge:
    """
    CheckAnnotationEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[CheckAnnotation] = None


@dataclass(kw_only=True)
class CheckAnnotationConnection:
    """
    CheckAnnotationConnection - The connection type for CheckAnnotation.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[CheckAnnotationEdge]] = None
    nodes: Optional[list[CheckAnnotation]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DeploymentRequest:
    """
    DeploymentRequest - A request to deploy a workflow run to an environment.

    currentUserCanApprove - Whether or not the current user can approve the deployment

    environment - The target environment of the deployment

    reviewers - The teams or users that can review the deployment

    waitTimer - The wait timer in minutes configured in the environment

    waitTimerStartedAt - The wait timer in minutes configured in the environment

    """

    current_user_can_approve: bool
    environment: Environment
    reviewers: DeploymentReviewerConnection
    wait_timer: int
    wait_timer_started_at: Optional[DateTime] = None


@dataclass(kw_only=True)
class CheckStepEdge:
    """
    CheckStepEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[CheckStep] = None


@dataclass(kw_only=True)
class CheckStepConnection:
    """
    CheckStepConnection - The connection type for CheckStep.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[CheckStepEdge]] = None
    nodes: Optional[list[CheckStep]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class CheckRun:
    """
    CheckRun - A check run.

    annotations - The check run's annotations

    checkSuite - The check suite that this run is a part of.

    completedAt - Identifies the date and time when the check run was completed.

    conclusion - The conclusion of the check run.

    databaseId - Identifies the primary key from the database.

    deployment - The corresponding deployment for this job, if any

    detailsUrl - The URL from which to find full details of the check run on the integrator's site.

    externalId - A reference for the check run on the integrator's system.

    id - The Node ID of the CheckRun object

    isRequired - Whether this is required to pass before merging for a specific pull request.

    name - The name of the check for this check run.

    pendingDeploymentRequest - Information about a pending deployment, if any, in this check run

    permalink - The permalink to the check run summary.

    repository - The repository associated with this check run.

    resourcePath - The HTTP path for this check run.

    startedAt - Identifies the date and time when the check run was started.

    status - The current status of the check run.

    steps - The check run's steps

    summary - A string representing the check run's summary

    text - A string representing the check run's text

    title - A string representing the check run

    url - The HTTP URL for this check run.

    """

    annotations: Optional[CheckAnnotationConnection] = None
    check_suite: CheckSuite
    completed_at: Optional[DateTime] = None
    conclusion: Optional[CheckConclusionState] = None
    database_id: Optional[int] = None
    deployment: Optional[Deployment] = None
    details_url: Optional[URI] = None
    external_id: Optional[str] = None
    id: ID
    is_required: bool
    name: str
    pending_deployment_request: Optional[DeploymentRequest] = None
    permalink: URI
    repository: Repository
    resource_path: URI
    started_at: Optional[DateTime] = None
    status: CheckStatusState
    steps: Optional[CheckStepConnection] = None
    summary: Optional[str] = None
    text: Optional[str] = None
    title: Optional[str] = None
    url: URI


@dataclass(kw_only=True)
class CheckRunEdge:
    """
    CheckRunEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[CheckRun] = None


@dataclass(kw_only=True)
class CheckRunConnection:
    """
    CheckRunConnection - The connection type for CheckRun.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[CheckRunEdge]] = None
    nodes: Optional[list[CheckRun]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class Push:
    """
    Push - A Git push.

    id - The Node ID of the Push object

    nextSha - The SHA after the push

    permalink - The permalink for this push.

    previousSha - The SHA before the push

    pusher - The actor who pushed

    repository - The repository that was pushed to

    """

    id: ID
    next_sha: Optional[GitObjectID] = None
    permalink: URI
    previous_sha: Optional[GitObjectID] = None
    pusher: Actor
    repository: Repository


@dataclass(kw_only=True)
class DeploymentReview:
    """
    DeploymentReview - A deployment review.

    comment - The comment the user left.

    databaseId - Identifies the primary key from the database.

    environments - The environments approved or rejected

    id - The Node ID of the DeploymentReview object

    state - The decision of the user.

    user - The user that reviewed the deployment.

    """

    comment: str
    database_id: Optional[int] = None
    environments: EnvironmentConnection
    id: ID
    state: DeploymentReviewState
    user: User


@dataclass(kw_only=True)
class DeploymentReviewEdge:
    """
    DeploymentReviewEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[DeploymentReview] = None


@dataclass(kw_only=True)
class DeploymentReviewConnection:
    """
    DeploymentReviewConnection - The connection type for DeploymentReview.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[DeploymentReviewEdge]] = None
    nodes: Optional[list[DeploymentReview]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class WorkflowRunFile:
    """
    WorkflowRunFile - An executed workflow file for a workflow run.

    id - The Node ID of the WorkflowRunFile object

    path - The path of the workflow file relative to its repository.

    repositoryFileUrl - The direct link to the file in the repository which stores the workflow file.

    repositoryName - The repository name and owner which stores the workflow file.

    resourcePath - The HTTP path for this workflow run file

    run - The parent workflow run execution for this file.

    url - The HTTP URL for this workflow run file

    viewerCanPushRepository - If the viewer has permissions to push to the repository which stores the workflow.

    viewerCanReadRepository - If the viewer has permissions to read the repository which stores the workflow.

    """

    id: ID
    path: str
    repository_file_url: URI
    repository_name: URI
    resource_path: URI
    run: WorkflowRun
    url: URI
    viewer_can_push_repository: bool
    viewer_can_read_repository: bool


@dataclass(kw_only=True)
class DeploymentRequestEdge:
    """
    DeploymentRequestEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[DeploymentRequest] = None


@dataclass(kw_only=True)
class DeploymentRequestConnection:
    """
    DeploymentRequestConnection - The connection type for DeploymentRequest.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[DeploymentRequestEdge]] = None
    nodes: Optional[list[DeploymentRequest]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class WorkflowRunEdge:
    """
    WorkflowRunEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[WorkflowRun] = None


@dataclass(kw_only=True)
class WorkflowRunConnection:
    """
    WorkflowRunConnection - The connection type for WorkflowRun.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[WorkflowRunEdge]] = None
    nodes: Optional[list[WorkflowRun]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class Workflow:
    """
    Workflow - A workflow contains meta information about an Actions workflow file.

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    id - The Node ID of the Workflow object

    name - The name of the workflow.

    resourcePath - The HTTP path for this workflow

    runs - The runs of the workflow.

    state - The state of the workflow.

    updatedAt - Identifies the date and time when the object was last updated.

    url - The HTTP URL for this workflow

    """

    created_at: DateTime
    database_id: Optional[int] = None
    id: ID
    name: str
    resource_path: URI
    runs: WorkflowRunConnection
    state: WorkflowState
    updated_at: DateTime
    url: URI


@dataclass(kw_only=True)
class CheckSuiteEdge:
    """
    CheckSuiteEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[CheckSuite] = None


@dataclass(kw_only=True)
class CheckSuiteConnection:
    """
    CheckSuiteConnection - The connection type for CheckSuite.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[CheckSuiteEdge]] = None
    nodes: Optional[list[CheckSuite]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class TreeEntry:
    """
    TreeEntry - Represents a Git tree entry.

    extension - The extension of the file

    isGenerated - Whether or not this tree entry is generated

    language - The programming language this file is written in.

    lineCount - Number of lines in the file.

    mode - Entry file mode.

    name - Entry file name.

    nameRaw - Entry file name. (Base64-encoded)

    object - Entry file object.

    oid - Entry file Git object ID.

    path - The full path of the file.

    pathRaw - The full path of the file. (Base64-encoded)

    repository - The Repository the tree entry belongs to

    size - Entry byte size

    submodule - If the TreeEntry is for a directory occupied by a submodule project, this returns the corresponding submodule

    type - Entry file type.

    """

    extension: Optional[str] = None
    is_generated: bool
    language: Optional[Language] = None
    line_count: Optional[int] = None
    mode: int
    name: str
    name_raw: Base64String
    object: Optional[GitObject] = None
    oid: GitObjectID
    path: Optional[str] = None
    path_raw: Optional[Base64String] = None
    repository: Repository
    size: int
    submodule: Optional[Submodule] = None
    type: str


@dataclass(kw_only=True)
class CommitHistoryConnection:
    """
    CommitHistoryConnection - The connection type for Commit.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[CommitEdge]] = None
    nodes: Optional[list[Commit]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class CommitConnection:
    """
    CommitConnection - The connection type for Commit.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[CommitEdge]] = None
    nodes: Optional[list[Commit]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class GitSignature:
    """
        GitSignature - Information about a signature (GPG or S/MIME) on a Commit or Tag.

        email - Email used to sign this object.

        isValid - True if the signature is valid and verified by GitHub.

        payload - Payload for GPG signing object. Raw ODB object without the signature header.

        signature - ASCII-armored signature header from object.

        signer - GitHub user corresponding to the email signing this commit.

        state - The state of this signature. `VALID` if signature is valid and verified by
    GitHub, otherwise represents reason why signature is considered invalid.

        wasSignedByGitHub - True if the signature was made with GitHub's signing key.

    """

    email: str
    is_valid: bool
    payload: str
    signature: str
    signer: Optional[User] = None
    state: GitSignatureState
    was_signed_by_git_hub: bool


@dataclass(kw_only=True)
class StatusContext:
    """
    StatusContext - Represents an individual commit status context

    avatarUrl - The avatar of the OAuth application or the user that created the status

    commit - This commit this status context is attached to.

    context - The name of this status context.

    createdAt - Identifies the date and time when the object was created.

    creator - The actor who created this status context.

    description - The description for this status context.

    id - The Node ID of the StatusContext object

    isRequired - Whether this is required to pass before merging for a specific pull request.

    state - The state of this status context.

    targetUrl - The URL for this status context.

    """

    avatar_url: Optional[URI] = None
    commit: Optional[Commit] = None
    context: str
    created_at: DateTime
    creator: Optional[Actor] = None
    description: Optional[str] = None
    id: ID
    is_required: bool
    state: StatusState
    target_url: Optional[URI] = None


@dataclass(kw_only=True)
class StatusCheckRollupContextEdge:
    """
    StatusCheckRollupContextEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[StatusCheckRollupContext] = None


@dataclass(kw_only=True)
class StatusCheckRollupContextConnection:
    """
    StatusCheckRollupContextConnection - The connection type for StatusCheckRollupContext.

    checkRunCount - The number of check runs in this rollup.

    checkRunCountsByState - Counts of check runs by state.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    statusContextCount - The number of status contexts in this rollup.

    statusContextCountsByState - Counts of status contexts by state.

    totalCount - Identifies the total count of items in the connection.

    """

    check_run_count: int
    check_run_counts_by_state: Optional[list[CheckRunStateCount]] = None
    edges: Optional[list[StatusCheckRollupContextEdge]] = None
    nodes: Optional[list[StatusCheckRollupContext]] = None
    page_info: PageInfo
    status_context_count: int
    status_context_counts_by_state: Optional[list[StatusContextStateCount]] = None
    total_count: int


@dataclass(kw_only=True)
class Status:
    """
    Status - Represents a commit status.

    combinedContexts - A list of status contexts and check runs for this commit.

    commit - The commit this status is attached to.

    context - Looks up an individual status context by context name.

    contexts - The individual status contexts for this commit.

    id - The Node ID of the Status object

    state - The combined commit status.

    """

    combined_contexts: StatusCheckRollupContextConnection
    commit: Optional[Commit] = None
    context: Optional[StatusContext] = None
    contexts: list[StatusContext]
    id: ID
    state: StatusState


@dataclass(kw_only=True)
class StatusCheckRollup:
    """
    StatusCheckRollup - Represents the rollup for both the check runs and status for a commit.

    commit - The commit the status and check runs are attached to.

    contexts - A list of status contexts and check runs for this commit.

    id - The Node ID of the StatusCheckRollup object

    state - The combined status for the commit.

    """

    commit: Optional[Commit] = None
    contexts: StatusCheckRollupContextConnection
    id: ID
    state: StatusState


@dataclass(kw_only=True)
class Tree:
    """
    Tree - Represents a Git tree.

    abbreviatedOid - An abbreviated version of the Git object ID

    commitResourcePath - The HTTP path for this Git object

    commitUrl - The HTTP URL for this Git object

    entries - A list of tree entries.

    id - The Node ID of the Tree object

    oid - The Git object ID

    repository - The Repository the Git object belongs to

    """

    abbreviated_oid: str
    commit_resource_path: URI
    commit_url: URI
    entries: Optional[list[TreeEntry]] = None
    id: ID
    oid: GitObjectID
    repository: Repository


@dataclass(kw_only=True)
class CommitComment:
    """
        CommitComment - Represents a comment on a given Commit.

        author - The actor who authored the comment.

        authorAssociation - Author's association with the subject of the comment.

        body - Identifies the comment body.

        bodyHTML - The body rendered to HTML.

        bodyText - The body rendered to text.

        commit - Identifies the commit associated with the comment, if the commit exists.

        createdAt - Identifies the date and time when the object was created.

        createdViaEmail - Check if this comment was created via an email reply.

        databaseId - Identifies the primary key from the database.

        editor - The actor who edited the comment.

        id - The Node ID of the CommitComment object

        includesCreatedEdit - Check if this comment was edited and includes an edit with the creation data

        isMinimized - Returns whether or not a comment has been minimized.

        lastEditedAt - The moment the editor made the last edit

        minimizedReason - Returns why the comment was minimized. One of `abuse`, `off-topic`,
    `outdated`, `resolved`, `duplicate` and `spam`. Note that the case and
    formatting of these values differs from the inputs to the `MinimizeComment` mutation.

        path - Identifies the file path associated with the comment.

        position - Identifies the line position associated with the comment.

        publishedAt - Identifies when the comment was published at.

        reactionGroups - A list of reactions grouped by content left on the subject.

        reactions - A list of Reactions left on the Issue.

        repository - The repository associated with this node.

        resourcePath - The HTTP path permalink for this commit comment.

        updatedAt - Identifies the date and time when the object was last updated.

        url - The HTTP URL permalink for this commit comment.

        userContentEdits - A list of edits to this content.

        viewerCanDelete - Check if the current viewer can delete this object.

        viewerCanMinimize - Check if the current viewer can minimize this object.

        viewerCanReact - Can user react to this subject

        viewerCanUpdate - Check if the current viewer can update this object.

        viewerCannotUpdateReasons - Reasons why the current viewer can not update this comment.

        viewerDidAuthor - Did the viewer author this comment.

    """

    author: Optional[Actor] = None
    author_association: CommentAuthorAssociation
    body: str
    body_h_t_m_l: HTML
    body_text: str
    commit: Optional[Commit] = None
    created_at: DateTime
    created_via_email: bool
    database_id: Optional[int] = None
    editor: Optional[Actor] = None
    id: ID
    includes_created_edit: bool
    is_minimized: bool
    last_edited_at: Optional[DateTime] = None
    minimized_reason: Optional[str] = None
    path: Optional[str] = None
    position: Optional[int] = None
    published_at: Optional[DateTime] = None
    reaction_groups: Optional[list[ReactionGroup]] = None
    reactions: ReactionConnection
    repository: Repository
    resource_path: URI
    updated_at: DateTime
    url: URI
    user_content_edits: Optional[UserContentEditConnection] = None
    viewer_can_delete: bool
    viewer_can_minimize: bool
    viewer_can_react: bool
    viewer_can_update: bool
    viewer_cannot_update_reasons: list[CommentCannotUpdateReason]
    viewer_did_author: bool


@dataclass(kw_only=True)
class CommitCommentEdge:
    """
    CommitCommentEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[CommitComment] = None


@dataclass(kw_only=True)
class CreatedCommitContribution:
    """
        CreatedCommitContribution - Represents the contribution a user made by committing to a repository.

        commitCount - How many commits were made on this day to this repository by the user.

        isRestricted - Whether this contribution is associated with a record you do not have access to. For
    example, your own 'first issue' contribution may have been made on a repository you can no
    longer access.

        occurredAt - When this contribution was made.

        repository - The repository the user made a commit in.

        resourcePath - The HTTP path for this contribution.

        url - The HTTP URL for this contribution.

        user - The user who made this contribution.

    """

    commit_count: int
    is_restricted: bool
    occurred_at: DateTime
    repository: Repository
    resource_path: URI
    url: URI
    user: User


@dataclass(kw_only=True)
class CreatedCommitContributionEdge:
    """
    CreatedCommitContributionEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[CreatedCommitContribution] = None


@dataclass(kw_only=True)
class CreatedCommitContributionConnection:
    """
    CreatedCommitContributionConnection - The connection type for CreatedCommitContribution.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of commits across days and repositories in the connection.

    """

    edges: Optional[list[CreatedCommitContributionEdge]] = None
    nodes: Optional[list[CreatedCommitContribution]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class CommitContributionsByRepository:
    """
    CommitContributionsByRepository - This aggregates commits made by a user within one repository.

    contributions - The commit contributions, each representing a day.

    repository - The repository in which the commits were made.

    resourcePath - The HTTP path for the user's commits to the repository in this time range.

    url - The HTTP URL for the user's commits to the repository in this time range.

    """

    contributions: CreatedCommitContributionConnection
    repository: Repository
    resource_path: URI
    url: URI


@dataclass(kw_only=True)
class ContributionCalendarWeek:
    """
    ContributionCalendarWeek - A week of contributions in a user's contribution graph.

    contributionDays - The days of contributions in this week.

    firstDay - The date of the earliest square in this week.

    """

    contribution_days: list[ContributionCalendarDay]
    first_day: Date


@dataclass(kw_only=True)
class ContributionCalendar:
    """
    ContributionCalendar - A calendar of contributions made on GitHub by a user.

    colors - A list of hex color codes used in this calendar. The darker the color, the more contributions it represents.

    isHalloween - Determine if the color set was chosen because it's currently Halloween.

    months - A list of the months of contributions in this calendar.

    totalContributions - The count of total contributions in the calendar.

    weeks - A list of the weeks of contributions in this calendar.

    """

    colors: list[str]
    is_halloween: bool
    months: list[ContributionCalendarMonth]
    total_contributions: int
    weeks: list[ContributionCalendarWeek]


@dataclass(kw_only=True)
class CreatedIssueContribution:
    """
        CreatedIssueContribution - Represents the contribution a user made on GitHub by opening an issue.

        isRestricted - Whether this contribution is associated with a record you do not have access to. For
    example, your own 'first issue' contribution may have been made on a repository you can no
    longer access.

        issue - The issue that was opened.

        occurredAt - When this contribution was made.

        resourcePath - The HTTP path for this contribution.

        url - The HTTP URL for this contribution.

        user - The user who made this contribution.

    """

    is_restricted: bool
    issue: Issue
    occurred_at: DateTime
    resource_path: URI
    url: URI
    user: User


@dataclass(kw_only=True)
class RestrictedContribution:
    """
        RestrictedContribution - Represents a private contribution a user made on GitHub.

        isRestricted - Whether this contribution is associated with a record you do not have access to. For
    example, your own 'first issue' contribution may have been made on a repository you can no
    longer access.

        occurredAt - When this contribution was made.

        resourcePath - The HTTP path for this contribution.

        url - The HTTP URL for this contribution.

        user - The user who made this contribution.

    """

    is_restricted: bool
    occurred_at: DateTime
    resource_path: URI
    url: URI
    user: User


@dataclass(kw_only=True)
class CreatedPullRequestContribution:
    """
        CreatedPullRequestContribution - Represents the contribution a user made on GitHub by opening a pull request.

        isRestricted - Whether this contribution is associated with a record you do not have access to. For
    example, your own 'first issue' contribution may have been made on a repository you can no
    longer access.

        occurredAt - When this contribution was made.

        pullRequest - The pull request that was opened.

        resourcePath - The HTTP path for this contribution.

        url - The HTTP URL for this contribution.

        user - The user who made this contribution.

    """

    is_restricted: bool
    occurred_at: DateTime
    pull_request: PullRequest
    resource_path: URI
    url: URI
    user: User


@dataclass(kw_only=True)
class CreatedRepositoryContribution:
    """
        CreatedRepositoryContribution - Represents the contribution a user made on GitHub by creating a repository.

        isRestricted - Whether this contribution is associated with a record you do not have access to. For
    example, your own 'first issue' contribution may have been made on a repository you can no
    longer access.

        occurredAt - When this contribution was made.

        repository - The repository that was created.

        resourcePath - The HTTP path for this contribution.

        url - The HTTP URL for this contribution.

        user - The user who made this contribution.

    """

    is_restricted: bool
    occurred_at: DateTime
    repository: Repository
    resource_path: URI
    url: URI
    user: User


@dataclass(kw_only=True)
class CreatedIssueContributionEdge:
    """
    CreatedIssueContributionEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[CreatedIssueContribution] = None


@dataclass(kw_only=True)
class CreatedIssueContributionConnection:
    """
    CreatedIssueContributionConnection - The connection type for CreatedIssueContribution.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[CreatedIssueContributionEdge]] = None
    nodes: Optional[list[CreatedIssueContribution]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class IssueContributionsByRepository:
    """
    IssueContributionsByRepository - This aggregates issues opened by a user within one repository.

    contributions - The issue contributions.

    repository - The repository in which the issues were opened.

    """

    contributions: CreatedIssueContributionConnection
    repository: Repository


@dataclass(kw_only=True)
class JoinedGitHubContribution:
    """
        JoinedGitHubContribution - Represents a user signing up for a GitHub account.

        isRestricted - Whether this contribution is associated with a record you do not have access to. For
    example, your own 'first issue' contribution may have been made on a repository you can no
    longer access.

        occurredAt - When this contribution was made.

        resourcePath - The HTTP path for this contribution.

        url - The HTTP URL for this contribution.

        user - The user who made this contribution.

    """

    is_restricted: bool
    occurred_at: DateTime
    resource_path: URI
    url: URI
    user: User


@dataclass(kw_only=True)
class CreatedPullRequestContributionEdge:
    """
    CreatedPullRequestContributionEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[CreatedPullRequestContribution] = None


@dataclass(kw_only=True)
class CreatedPullRequestContributionConnection:
    """
    CreatedPullRequestContributionConnection - The connection type for CreatedPullRequestContribution.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[CreatedPullRequestContributionEdge]] = None
    nodes: Optional[list[CreatedPullRequestContribution]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PullRequestContributionsByRepository:
    """
    PullRequestContributionsByRepository - This aggregates pull requests opened by a user within one repository.

    contributions - The pull request contributions.

    repository - The repository in which the pull requests were opened.

    """

    contributions: CreatedPullRequestContributionConnection
    repository: Repository


@dataclass(kw_only=True)
class CreatedPullRequestReviewContribution:
    """
        CreatedPullRequestReviewContribution - Represents the contribution a user made by leaving a review on a pull request.

        isRestricted - Whether this contribution is associated with a record you do not have access to. For
    example, your own 'first issue' contribution may have been made on a repository you can no
    longer access.

        occurredAt - When this contribution was made.

        pullRequest - The pull request the user reviewed.

        pullRequestReview - The review the user left on the pull request.

        repository - The repository containing the pull request that the user reviewed.

        resourcePath - The HTTP path for this contribution.

        url - The HTTP URL for this contribution.

        user - The user who made this contribution.

    """

    is_restricted: bool
    occurred_at: DateTime
    pull_request: PullRequest
    pull_request_review: PullRequestReview
    repository: Repository
    resource_path: URI
    url: URI
    user: User


@dataclass(kw_only=True)
class CreatedPullRequestReviewContributionEdge:
    """
    CreatedPullRequestReviewContributionEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[CreatedPullRequestReviewContribution] = None


@dataclass(kw_only=True)
class CreatedPullRequestReviewContributionConnection:
    """
    CreatedPullRequestReviewContributionConnection - The connection type for CreatedPullRequestReviewContribution.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[CreatedPullRequestReviewContributionEdge]] = None
    nodes: Optional[list[CreatedPullRequestReviewContribution]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PullRequestReviewContributionsByRepository:
    """
    PullRequestReviewContributionsByRepository - This aggregates pull request reviews made by a user within one repository.

    contributions - The pull request review contributions.

    repository - The repository in which the pull request reviews were made.

    """

    contributions: CreatedPullRequestReviewContributionConnection
    repository: Repository


@dataclass(kw_only=True)
class CreatedRepositoryContributionEdge:
    """
    CreatedRepositoryContributionEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[CreatedRepositoryContribution] = None


@dataclass(kw_only=True)
class CreatedRepositoryContributionConnection:
    """
    CreatedRepositoryContributionConnection - The connection type for CreatedRepositoryContribution.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[CreatedRepositoryContributionEdge]] = None
    nodes: Optional[list[CreatedRepositoryContribution]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseEdge:
    """
    EnterpriseEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[Enterprise] = None


@dataclass(kw_only=True)
class EnterpriseConnection:
    """
    EnterpriseConnection - The connection type for Enterprise.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[EnterpriseEdge]] = None
    nodes: Optional[list[Enterprise]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class FollowerConnection:
    """
    FollowerConnection - The connection type for User.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[UserEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class FollowingConnection:
    """
    FollowingConnection - The connection type for User.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[UserEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class UserListItemsEdge:
    """
    UserListItemsEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[UserListItems] = None


@dataclass(kw_only=True)
class UserListItemsConnection:
    """
    UserListItemsConnection - The connection type for UserListItems.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[UserListItemsEdge]] = None
    nodes: Optional[list[UserListItems]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class UserList:
    """
    UserList - A user-curated list of repositories

    createdAt - Identifies the date and time when the object was created.

    description - The description of this list

    id - The Node ID of the UserList object

    isPrivate - Whether or not this list is private

    items - The items associated with this list

    lastAddedAt - The date and time at which this list was created or last had items added to it

    name - The name of this list

    slug - The slug of this list

    updatedAt - Identifies the date and time when the object was last updated.

    user - The user to which this list belongs

    """

    created_at: DateTime
    description: Optional[str] = None
    id: ID
    is_private: bool
    items: UserListItemsConnection
    last_added_at: DateTime
    name: str
    slug: str
    updated_at: DateTime
    user: User


@dataclass(kw_only=True)
class UserListEdge:
    """
    UserListEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[UserList] = None


@dataclass(kw_only=True)
class UserListConnection:
    """
    UserListConnection - The connection type for UserList.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[UserListEdge]] = None
    nodes: Optional[list[UserList]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PublicKeyEdge:
    """
    PublicKeyEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[PublicKey] = None


@dataclass(kw_only=True)
class PublicKeyConnection:
    """
    PublicKeyConnection - The connection type for PublicKey.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[PublicKeyEdge]] = None
    nodes: Optional[list[PublicKey]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class SavedReply:
    """
    SavedReply - A Saved Reply is text a user can use to reply quickly.

    body - The body of the saved reply.

    bodyHTML - The saved reply body rendered to HTML.

    databaseId - Identifies the primary key from the database.

    id - The Node ID of the SavedReply object

    title - The title of the saved reply.

    user - The user that saved this reply.

    """

    body: str
    body_h_t_m_l: HTML
    database_id: Optional[int] = None
    id: ID
    title: str
    user: Optional[Actor] = None


@dataclass(kw_only=True)
class SavedReplyEdge:
    """
    SavedReplyEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[SavedReply] = None


@dataclass(kw_only=True)
class SavedReplyConnection:
    """
    SavedReplyConnection - The connection type for SavedReply.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[SavedReplyEdge]] = None
    nodes: Optional[list[SavedReply]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class SocialAccountEdge:
    """
    SocialAccountEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[SocialAccount] = None


@dataclass(kw_only=True)
class SocialAccountConnection:
    """
    SocialAccountConnection - The connection type for SocialAccount.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[SocialAccountEdge]] = None
    nodes: Optional[list[SocialAccount]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class StarredRepositoryEdge:
    """
    StarredRepositoryEdge - Represents a starred repository.

    cursor - A cursor for use in pagination.

    starredAt - Identifies when the item was starred.

    """

    cursor: str
    node: Repository
    starred_at: DateTime


@dataclass(kw_only=True)
class StarredRepositoryConnection:
    """
    StarredRepositoryConnection - The connection type for Repository.

    edges - A list of edges.

    isOverLimit - Is the list of stars for this user truncated? This is true for users that have many stars.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[StarredRepositoryEdge]] = None
    is_over_limit: bool
    nodes: Optional[list[Repository]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class LinkedBranch:
    """
    LinkedBranch - A branch linked to an issue.

    id - The Node ID of the LinkedBranch object

    ref - The branch's ref.

    """

    id: ID
    ref: Optional[Ref] = None


@dataclass(kw_only=True)
class LinkedBranchEdge:
    """
    LinkedBranchEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[LinkedBranch] = None


@dataclass(kw_only=True)
class LinkedBranchConnection:
    """
    LinkedBranchConnection - A list of branches linked to an issue.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[LinkedBranchEdge]] = None
    nodes: Optional[list[LinkedBranch]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class IssueTimelineItemEdge:
    """
    IssueTimelineItemEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[IssueTimelineItem] = None


@dataclass(kw_only=True)
class IssueTimelineConnection:
    """
    IssueTimelineConnection - The connection type for IssueTimelineItem.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[IssueTimelineItemEdge]] = None
    nodes: Optional[list[IssueTimelineItem]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class IssueTimelineItemsEdge:
    """
    IssueTimelineItemsEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[IssueTimelineItems] = None


@dataclass(kw_only=True)
class IssueTimelineItemsConnection:
    """
    IssueTimelineItemsConnection - The connection type for IssueTimelineItems.

    edges - A list of edges.

    filteredCount - Identifies the count of items after applying `before` and `after` filters.

    nodes - A list of nodes.

    pageCount - Identifies the count of items after applying `before`/`after` filters and `first`/`last`/`skip` slicing.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    updatedAt - Identifies the date and time when the timeline was last updated.

    """

    edges: Optional[list[IssueTimelineItemsEdge]] = None
    filtered_count: int
    nodes: Optional[list[IssueTimelineItems]] = None
    page_count: int
    page_info: PageInfo
    total_count: int
    updated_at: DateTime


@dataclass(kw_only=True)
class AddCommentPayload:
    """
    AddCommentPayload - Autogenerated return type of AddComment

    clientMutationId - A unique identifier for the client performing the mutation.

    commentEdge - The edge from the subject's comment connection.

    subject - The subject

    timelineEdge - The edge from the subject's timeline connection.

    """

    client_mutation_id: Optional[str] = None
    comment_edge: Optional[IssueCommentEdge] = None
    subject: Optional[Node] = None
    timeline_edge: Optional[IssueTimelineItemEdge] = None


@dataclass(kw_only=True)
class AddProjectCardPayload:
    """
    AddProjectCardPayload - Autogenerated return type of AddProjectCard

    cardEdge - The edge from the ProjectColumn's card connection.

    clientMutationId - A unique identifier for the client performing the mutation.

    projectColumn - The ProjectColumn

    """

    card_edge: Optional[ProjectCardEdge] = None
    client_mutation_id: Optional[str] = None
    project_column: Optional[ProjectColumn] = None


@dataclass(kw_only=True)
class AddProjectColumnPayload:
    """
    AddProjectColumnPayload - Autogenerated return type of AddProjectColumn

    clientMutationId - A unique identifier for the client performing the mutation.

    columnEdge - The edge from the project's column connection.

    project - The project

    """

    client_mutation_id: Optional[str] = None
    column_edge: Optional[ProjectColumnEdge] = None
    project: Optional[Project] = None


@dataclass(kw_only=True)
class AddPullRequestReviewCommentPayload:
    """
    AddPullRequestReviewCommentPayload - Autogenerated return type of AddPullRequestReviewComment

    clientMutationId - A unique identifier for the client performing the mutation.

    comment - The newly created comment.

    commentEdge - The edge from the review's comment connection.

    """

    client_mutation_id: Optional[str] = None
    comment: Optional[PullRequestReviewComment] = None
    comment_edge: Optional[PullRequestReviewCommentEdge] = None


@dataclass(kw_only=True)
class AddPullRequestReviewInput:
    """
        AddPullRequestReviewInput - Autogenerated input type of AddPullRequestReview

        body - The contents of the review body comment.

        clientMutationId - A unique identifier for the client performing the mutation.

        comments - The review line comments.

    **Upcoming Change on 2023-10-01 UTC**
    **Description:** `comments` will be removed. use the `threads` argument instead
    **Reason:** We are deprecating comment fields that use diff-relative positioning

        commitOID - The commit OID the review pertains to.

        event - The event to perform on the pull request review.

        pullRequestId - The Node ID of the pull request to modify.

        threads - The review line comment threads.

    """

    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    comments: Optional[list[DraftPullRequestReviewComment]] = None
    commit_o_i_d: Optional[GitObjectID] = None
    event: Optional[PullRequestReviewEvent] = None
    pull_request_id: ID
    threads: Optional[list[DraftPullRequestReviewThread]] = None


@dataclass(kw_only=True)
class AddPullRequestReviewPayload:
    """
    AddPullRequestReviewPayload - Autogenerated return type of AddPullRequestReview

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequestReview - The newly created pull request review.

    reviewEdge - The edge from the pull request's review connection.

    """

    client_mutation_id: Optional[str] = None
    pull_request_review: Optional[PullRequestReview] = None
    review_edge: Optional[PullRequestReviewEdge] = None


@dataclass(kw_only=True)
class AddReactionPayload:
    """
    AddReactionPayload - Autogenerated return type of AddReaction

    clientMutationId - A unique identifier for the client performing the mutation.

    reaction - The reaction object.

    reactionGroups - The reaction groups for the subject.

    subject - The reactable subject.

    """

    client_mutation_id: Optional[str] = None
    reaction: Optional[Reaction] = None
    reaction_groups: Optional[list[ReactionGroup]] = None
    subject: Optional[Reactable] = None


@dataclass(kw_only=True)
class AuditEntry:
    """
    AuditEntry - An entry in the audit log.

    action - The action name

    actor - The user who initiated the action

    actorIp - The IP address of the actor

    actorLocation - A readable representation of the actor's location

    actorLogin - The username of the user who initiated the action

    actorResourcePath - The HTTP path for the actor.

    actorUrl - The HTTP URL for the actor.

    createdAt - The time the action was initiated

    operationType - The corresponding operation type for the action

    user - The user affected by the action

    userLogin - For actions involving two users, the actor is the initiator and the user is the affected user.

    userResourcePath - The HTTP path for the user.

    userUrl - The HTTP URL for the user.

    """

    action: str
    actor: Optional[AuditEntryActor] = None
    actor_ip: Optional[str] = None
    actor_location: Optional[ActorLocation] = None
    actor_login: Optional[str] = None
    actor_resource_path: Optional[URI] = None
    actor_url: Optional[URI] = None
    created_at: PreciseDateTime
    operation_type: Optional[OperationType] = None
    user: Optional[User] = None
    user_login: Optional[str] = None
    user_resource_path: Optional[URI] = None
    user_url: Optional[URI] = None


@dataclass(kw_only=True)
class CheckAnnotationData:
    """
    CheckAnnotationData - Information from a check run analysis to specific lines of code.

    annotationLevel - Represents an annotation's information level

    location - The location of the annotation

    message - A short description of the feedback for these lines of code.

    path - The path of the file to add an annotation to.

    rawDetails - Details about this annotation.

    title - The title that represents the annotation.

    """

    annotation_level: CheckAnnotationLevel
    location: CheckAnnotationRange
    message: str
    path: str
    raw_details: Optional[str] = None
    title: Optional[str] = None


@dataclass(kw_only=True)
class CheckRunOutput:
    """
    CheckRunOutput - Descriptive details about the check run.

    annotations - The annotations that are made as part of the check run.

    images - Images attached to the check run output displayed in the GitHub pull request UI.

    summary - The summary of the check run (supports Commonmark).

    text - The details of the check run (supports Commonmark).

    title - A title to provide for this check run.

    """

    annotations: Optional[list[CheckAnnotationData]] = None
    images: Optional[list[CheckRunOutputImage]] = None
    summary: str
    text: Optional[str] = None
    title: str


@dataclass(kw_only=True)
class Comment:
    """
    Comment - Represents a comment.

    author - The actor who authored the comment.

    authorAssociation - Author's association with the subject of the comment.

    body - The body as Markdown.

    bodyHTML - The body rendered to HTML.

    bodyText - The body rendered to text.

    createdAt - Identifies the date and time when the object was created.

    createdViaEmail - Check if this comment was created via an email reply.

    editor - The actor who edited the comment.

    id - The Node ID of the Comment object

    includesCreatedEdit - Check if this comment was edited and includes an edit with the creation data

    lastEditedAt - The moment the editor made the last edit

    publishedAt - Identifies when the comment was published at.

    updatedAt - Identifies the date and time when the object was last updated.

    userContentEdits - A list of edits to this content.

    viewerDidAuthor - Did the viewer author this comment.

    """

    author: Optional[Actor] = None
    author_association: CommentAuthorAssociation
    body: str
    body_h_t_m_l: HTML
    body_text: str
    created_at: DateTime
    created_via_email: bool
    editor: Optional[Actor] = None
    id: ID
    includes_created_edit: bool
    last_edited_at: Optional[DateTime] = None
    published_at: Optional[DateTime] = None
    updated_at: DateTime
    user_content_edits: Optional[UserContentEditConnection] = None
    viewer_did_author: bool


@dataclass(kw_only=True)
class CreateAttributionInvitationPayload:
    """
    CreateAttributionInvitationPayload - Autogenerated return type of CreateAttributionInvitation

    clientMutationId - A unique identifier for the client performing the mutation.

    owner - The owner scoping the reattributable data.

    source - The account owning the data to reattribute.

    target - The account which may claim the data.

    """

    client_mutation_id: Optional[str] = None
    owner: Optional[Organization] = None
    source: Optional[Claimable] = None
    target: Optional[Claimable] = None


@dataclass(kw_only=True)
class CreateCheckRunInput:
    """
    CreateCheckRunInput - Autogenerated input type of CreateCheckRun

    actions - Possible further actions the integrator can perform, which a user may trigger.

    clientMutationId - A unique identifier for the client performing the mutation.

    completedAt - The time that the check run finished.

    conclusion - The final conclusion of the check.

    detailsUrl - The URL of the integrator's site that has the full details of the check.

    externalId - A reference for the run on the integrator's system.

    headSha - The SHA of the head commit.

    name - The name of the check.

    output - Descriptive details about the run.

    repositoryId - The node ID of the repository.

    startedAt - The time that the check run began.

    status - The current status.

    """

    actions: Optional[list[CheckRunAction]] = None
    client_mutation_id: Optional[str] = None
    completed_at: Optional[DateTime] = None
    conclusion: Optional[CheckConclusionState] = None
    details_url: Optional[URI] = None
    external_id: Optional[str] = None
    head_sha: GitObjectID
    name: str
    output: Optional[CheckRunOutput] = None
    repository_id: ID
    started_at: Optional[DateTime] = None
    status: Optional[RequestableCheckStatusState] = None


@dataclass(kw_only=True)
class FileChanges:
    """
        FileChanges - A description of a set of changes to a file tree to be made as part of
    a git commit, modeled as zero or more file `additions` and zero or more
    file `deletions`.

    Both fields are optional; omitting both will produce a commit with no
    file changes.

    `deletions` and `additions` describe changes to files identified
    by their path in the git tree using unix-style path separators, i.e.
    `/`.  The root of a git tree is an empty string, so paths are not
    slash-prefixed.

    `path` values must be unique across all `additions` and `deletions`
    provided.  Any duplication will result in a validation error.

    ### Encoding

    File contents must be provided in full for each `FileAddition`.

    The `contents` of a `FileAddition` must be encoded using RFC 4648
    compliant base64, i.e. correct padding is required and no characters
    outside the standard alphabet may be used.  Invalid base64
    encoding will be rejected with a validation error.

    The encoded contents may be binary.

    For text files, no assumptions are made about the character encoding of
    the file contents (after base64 decoding).  No charset transcoding or
    line-ending normalization will be performed; it is the client's
    responsibility to manage the character encoding of files they provide.
    However, for maximum compatibility we recommend using UTF-8 encoding
    and ensuring that all files in a repository use a consistent
    line-ending convention (`\n` or `\r\n`), and that all files end
    with a newline.

    ### Modeling file changes

    Each of the the five types of conceptual changes that can be made in a
    git commit can be described using the `FileChanges` type as follows:

    1. New file addition: create file `hello world\n` at path `docs/README.txt`:

           {
             "additions" [
               {
                 "path": "docs/README.txt",
                 "contents": base64encode("hello world\n")
               }
             ]
           }

    2. Existing file modification: change existing `docs/README.txt` to have new
       content `new content here\n`:

           {
             "additions" [
               {
                 "path": "docs/README.txt",
                 "contents": base64encode("new content here\n")
               }
             ]
           }

    3. Existing file deletion: remove existing file `docs/README.txt`.
       Note that the path is required to exist -- specifying a
       path that does not exist on the given branch will abort the
       commit and return an error.

           {
             "deletions" [
               {
                 "path": "docs/README.txt"
               }
             ]
           }


    4. File rename with no changes: rename `docs/README.txt` with
       previous content `hello world\n` to the same content at
       `newdocs/README.txt`:

           {
             "deletions" [
               {
                 "path": "docs/README.txt",
               }
             ],
             "additions" [
               {
                 "path": "newdocs/README.txt",
                 "contents": base64encode("hello world\n")
               }
             ]
           }


    5. File rename with changes: rename `docs/README.txt` with
       previous content `hello world\n` to a file at path
       `newdocs/README.txt` with content `new contents\n`:

           {
             "deletions" [
               {
                 "path": "docs/README.txt",
               }
             ],
             "additions" [
               {
                 "path": "newdocs/README.txt",
                 "contents": base64encode("new contents\n")
               }
             ]
           }

        additions - File to add or change.

        deletions - Files to delete.

    """

    additions: Optional[list[FileAddition]] = None
    deletions: Optional[list[FileDeletion]] = None


@dataclass(kw_only=True)
class CreateCommitOnBranchInput:
    """
    CreateCommitOnBranchInput - Autogenerated input type of CreateCommitOnBranch

    branch - The Ref to be updated.  Must be a branch.

    clientMutationId - A unique identifier for the client performing the mutation.

    expectedHeadOid - The git commit oid expected at the head of the branch prior to the commit

    fileChanges - A description of changes to files in this commit.

    message - The commit message the be included with the commit.

    """

    branch: CommittableBranch
    client_mutation_id: Optional[str] = None
    expected_head_oid: GitObjectID
    file_changes: Optional[FileChanges] = None
    message: CommitMessage


@dataclass(kw_only=True)
class CreateCommitOnBranchPayload:
    """
    CreateCommitOnBranchPayload - Autogenerated return type of CreateCommitOnBranch

    clientMutationId - A unique identifier for the client performing the mutation.

    commit - The new commit.

    ref - The ref which has been updated to point to the new commit.

    """

    client_mutation_id: Optional[str] = None
    commit: Optional[Commit] = None
    ref: Optional[Ref] = None


@dataclass(kw_only=True)
class CreateEnterpriseOrganizationPayload:
    """
    CreateEnterpriseOrganizationPayload - Autogenerated return type of CreateEnterpriseOrganization

    clientMutationId - A unique identifier for the client performing the mutation.

    enterprise - The enterprise that owns the created organization.

    organization - The organization that was created.

    """

    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    organization: Optional[Organization] = None


@dataclass(kw_only=True)
class CreateLinkedBranchPayload:
    """
    CreateLinkedBranchPayload - Autogenerated return type of CreateLinkedBranch

    clientMutationId - A unique identifier for the client performing the mutation.

    issue - The issue that was linked to.

    linkedBranch - The new branch issue reference.

    """

    client_mutation_id: Optional[str] = None
    issue: Optional[Issue] = None
    linked_branch: Optional[LinkedBranch] = None


@dataclass(kw_only=True)
class RepositoryPropertyConditionTargetInput:
    """
    RepositoryPropertyConditionTargetInput - Parameters to be used for the repository_property condition

    exclude - Array of repository properties that must not match.

    include - Array of repository properties that must match

    """

    exclude: list[PropertyTargetDefinitionInput]
    include: list[PropertyTargetDefinitionInput]


@dataclass(kw_only=True)
class RepositoryRuleConditionsInput:
    """
    RepositoryRuleConditionsInput - Specifies the conditions required for a ruleset to evaluate

    refName - Configuration for the ref_name condition

    repositoryId - Configuration for the repository_id condition

    repositoryName - Configuration for the repository_name condition

    repositoryProperty - Configuration for the repository_property condition

    """

    ref_name: Optional[RefNameConditionTargetInput] = None
    repository_id: Optional[RepositoryIdConditionTargetInput] = None
    repository_name: Optional[RepositoryNameConditionTargetInput] = None
    repository_property: Optional[RepositoryPropertyConditionTargetInput] = None


@dataclass(kw_only=True)
class RequiredStatusChecksParametersInput:
    """
        RequiredStatusChecksParametersInput - Choose which status checks must pass before the ref is updated. When enabled,
    commits must first be pushed to another ref where the checks pass.

        requiredStatusChecks - Status checks that are required.

        strictRequiredStatusChecksPolicy - Whether pull requests targeting a matching branch must be tested with the
    latest code. This setting will not take effect unless at least one status
    check is enabled.

    """

    required_status_checks: list[StatusCheckConfigurationInput]
    strict_required_status_checks_policy: bool


@dataclass(kw_only=True)
class WorkflowsParametersInput:
    """
    WorkflowsParametersInput - Require all changes made to a targeted branch to pass the specified workflows before they can be merged.

    workflows - Workflows that must pass for this rule to pass.

    """

    workflows: list[WorkflowFileReferenceInput]


@dataclass(kw_only=True)
class RuleParametersInput:
    """
    RuleParametersInput - Specifies the parameters for a `RepositoryRule` object. Only one of the fields should be specified.

    branchNamePattern - Parameters used for the `branch_name_pattern` rule type

    commitAuthorEmailPattern - Parameters used for the `commit_author_email_pattern` rule type

    commitMessagePattern - Parameters used for the `commit_message_pattern` rule type

    committerEmailPattern - Parameters used for the `committer_email_pattern` rule type

    pullRequest - Parameters used for the `pull_request` rule type

    requiredDeployments - Parameters used for the `required_deployments` rule type

    requiredStatusChecks - Parameters used for the `required_status_checks` rule type

    tagNamePattern - Parameters used for the `tag_name_pattern` rule type

    update - Parameters used for the `update` rule type

    workflows - Parameters used for the `workflows` rule type

    """

    branch_name_pattern: Optional[BranchNamePatternParametersInput] = None
    commit_author_email_pattern: Optional[
        CommitAuthorEmailPatternParametersInput
    ] = None
    commit_message_pattern: Optional[CommitMessagePatternParametersInput] = None
    committer_email_pattern: Optional[CommitterEmailPatternParametersInput] = None
    pull_request: Optional[PullRequestParametersInput] = None
    required_deployments: Optional[RequiredDeploymentsParametersInput] = None
    required_status_checks: Optional[RequiredStatusChecksParametersInput] = None
    tag_name_pattern: Optional[TagNamePatternParametersInput] = None
    update: Optional[UpdateParametersInput] = None
    workflows: Optional[WorkflowsParametersInput] = None


@dataclass(kw_only=True)
class RepositoryRuleInput:
    """
    RepositoryRuleInput - Specifies the attributes for a new or updated rule.

    id - Optional ID of this rule when updating

    parameters - The parameters for the rule.

    type - The type of rule to create.

    """

    id: Optional[ID] = None
    parameters: Optional[RuleParametersInput] = None
    type: RepositoryRuleType


@dataclass(kw_only=True)
class CreateRepositoryRulesetInput:
    """
    CreateRepositoryRulesetInput - Autogenerated input type of CreateRepositoryRuleset

    bypassActors - A list of actors that are allowed to bypass rules in this ruleset.

    clientMutationId - A unique identifier for the client performing the mutation.

    conditions - The set of conditions for this ruleset

    enforcement - The enforcement level for this ruleset

    name - The name of the ruleset.

    rules - The list of rules for this ruleset

    sourceId - The global relay id of the source in which a new ruleset should be created in.

    target - The target of the ruleset.

    """

    bypass_actors: Optional[list[RepositoryRulesetBypassActorInput]] = None
    client_mutation_id: Optional[str] = None
    conditions: RepositoryRuleConditionsInput
    enforcement: RuleEnforcement
    name: str
    rules: Optional[list[RepositoryRuleInput]] = None
    source_id: ID
    target: Optional[RepositoryRulesetTarget] = None


@dataclass(kw_only=True)
class CreateUserListPayload:
    """
    CreateUserListPayload - Autogenerated return type of CreateUserList

    clientMutationId - A unique identifier for the client performing the mutation.

    list - The list that was just created

    viewer - The user who created the list

    """

    client_mutation_id: Optional[str] = None
    list: Optional[UserList] = None
    viewer: Optional[User] = None


@dataclass(kw_only=True)
class DeletePullRequestReviewCommentPayload:
    """
    DeletePullRequestReviewCommentPayload - Autogenerated return type of DeletePullRequestReviewComment

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequestReview - The pull request review the deleted comment belonged to.

    pullRequestReviewComment - The deleted pull request review comment.

    """

    client_mutation_id: Optional[str] = None
    pull_request_review: Optional[PullRequestReview] = None
    pull_request_review_comment: Optional[PullRequestReviewComment] = None


@dataclass(kw_only=True)
class DisablePullRequestAutoMergePayload:
    """
    DisablePullRequestAutoMergePayload - Autogenerated return type of DisablePullRequestAutoMerge

    actor - Identifies the actor who performed the event.

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequest - The pull request auto merge was disabled on.

    """

    actor: Optional[Actor] = None
    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class EnablePullRequestAutoMergePayload:
    """
    EnablePullRequestAutoMergePayload - Autogenerated return type of EnablePullRequestAutoMerge

    actor - Identifies the actor who performed the event.

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequest - The pull request auto-merge was enabled on.

    """

    actor: Optional[Actor] = None
    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class LinkRepositoryToProjectPayload:
    """
    LinkRepositoryToProjectPayload - Autogenerated return type of LinkRepositoryToProject

    clientMutationId - A unique identifier for the client performing the mutation.

    project - The linked Project.

    repository - The linked Repository.

    """

    client_mutation_id: Optional[str] = None
    project: Optional[Project] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class LockLockablePayload:
    """
    LockLockablePayload - Autogenerated return type of LockLockable

    actor - Identifies the actor who performed the event.

    clientMutationId - A unique identifier for the client performing the mutation.

    lockedRecord - The item that was locked.

    """

    actor: Optional[Actor] = None
    client_mutation_id: Optional[str] = None
    locked_record: Optional[Lockable] = None


@dataclass(kw_only=True)
class MarketplaceListing:
    """
        MarketplaceListing - A listing in the GitHub integration marketplace.

        app - The GitHub App this listing represents.

        companyUrl - URL to the listing owner's company site.

        configurationResourcePath - The HTTP path for configuring access to the listing's integration or OAuth app

        configurationUrl - The HTTP URL for configuring access to the listing's integration or OAuth app

        documentationUrl - URL to the listing's documentation.

        extendedDescription - The listing's detailed description.

        extendedDescriptionHTML - The listing's detailed description rendered to HTML.

        fullDescription - The listing's introductory description.

        fullDescriptionHTML - The listing's introductory description rendered to HTML.

        hasPublishedFreeTrialPlans - Does this listing have any plans with a free trial?

        hasTermsOfService - Does this listing have a terms of service link?

        hasVerifiedOwner - Whether the creator of the app is a verified org

        howItWorks - A technical description of how this app works with GitHub.

        howItWorksHTML - The listing's technical description rendered to HTML.

        id - The Node ID of the MarketplaceListing object

        installationUrl - URL to install the product to the viewer's account or organization.

        installedForViewer - Whether this listing's app has been installed for the current viewer

        isArchived - Whether this listing has been removed from the Marketplace.

        isDraft - Whether this listing is still an editable draft that has not been submitted
    for review and is not publicly visible in the Marketplace.

        isPaid - Whether the product this listing represents is available as part of a paid plan.

        isPublic - Whether this listing has been approved for display in the Marketplace.

        isRejected - Whether this listing has been rejected by GitHub for display in the Marketplace.

        isUnverified - Whether this listing has been approved for unverified display in the Marketplace.

        isUnverifiedPending - Whether this draft listing has been submitted for review for approval to be unverified in the Marketplace.

        isVerificationPendingFromDraft - Whether this draft listing has been submitted for review from GitHub for approval to be verified in the Marketplace.

        isVerificationPendingFromUnverified - Whether this unverified listing has been submitted for review from GitHub for approval to be verified in the Marketplace.

        isVerified - Whether this listing has been approved for verified display in the Marketplace.

        logoBackgroundColor - The hex color code, without the leading '#', for the logo background.

        logoUrl - URL for the listing's logo image.

        name - The listing's full name.

        normalizedShortDescription - The listing's very short description without a trailing period or ampersands.

        pricingUrl - URL to the listing's detailed pricing.

        primaryCategory - The category that best describes the listing.

        privacyPolicyUrl - URL to the listing's privacy policy, may return an empty string for listings that do not require a privacy policy URL.

        resourcePath - The HTTP path for the Marketplace listing.

        screenshotUrls - The URLs for the listing's screenshots.

        secondaryCategory - An alternate category that describes the listing.

        shortDescription - The listing's very short description.

        slug - The short name of the listing used in its URL.

        statusUrl - URL to the listing's status page.

        supportEmail - An email address for support for this listing's app.

        supportUrl - Either a URL or an email address for support for this listing's app, may
    return an empty string for listings that do not require a support URL.

        termsOfServiceUrl - URL to the listing's terms of service.

        url - The HTTP URL for the Marketplace listing.

        viewerCanAddPlans - Can the current viewer add plans for this Marketplace listing.

        viewerCanApprove - Can the current viewer approve this Marketplace listing.

        viewerCanDelist - Can the current viewer delist this Marketplace listing.

        viewerCanEdit - Can the current viewer edit this Marketplace listing.

        viewerCanEditCategories - Can the current viewer edit the primary and secondary category of this
    Marketplace listing.

        viewerCanEditPlans - Can the current viewer edit the plans for this Marketplace listing.

        viewerCanRedraft - Can the current viewer return this Marketplace listing to draft state
    so it becomes editable again.

        viewerCanReject - Can the current viewer reject this Marketplace listing by returning it to
    an editable draft state or rejecting it entirely.

        viewerCanRequestApproval - Can the current viewer request this listing be reviewed for display in
    the Marketplace as verified.

        viewerHasPurchased - Indicates whether the current user has an active subscription to this Marketplace listing.

        viewerHasPurchasedForAllOrganizations - Indicates if the current user has purchased a subscription to this Marketplace listing
    for all of the organizations the user owns.

        viewerIsListingAdmin - Does the current viewer role allow them to administer this Marketplace listing.

    """

    app: Optional[App] = None
    company_url: Optional[URI] = None
    configuration_resource_path: URI
    configuration_url: URI
    documentation_url: Optional[URI] = None
    extended_description: Optional[str] = None
    extended_description_h_t_m_l: HTML
    full_description: str
    full_description_h_t_m_l: HTML
    has_published_free_trial_plans: bool
    has_terms_of_service: bool
    has_verified_owner: bool
    how_it_works: Optional[str] = None
    how_it_works_h_t_m_l: HTML
    id: ID
    installation_url: Optional[URI] = None
    installed_for_viewer: bool
    is_archived: bool
    is_draft: bool
    is_paid: bool
    is_public: bool
    is_rejected: bool
    is_unverified: bool
    is_unverified_pending: bool
    is_verification_pending_from_draft: bool
    is_verification_pending_from_unverified: bool
    is_verified: bool
    logo_background_color: str
    logo_url: Optional[URI] = None
    name: str
    normalized_short_description: str
    pricing_url: Optional[URI] = None
    primary_category: MarketplaceCategory
    privacy_policy_url: URI
    resource_path: URI
    screenshot_urls: list[str]
    secondary_category: Optional[MarketplaceCategory] = None
    short_description: str
    slug: str
    status_url: Optional[URI] = None
    support_email: Optional[str] = None
    support_url: URI
    terms_of_service_url: Optional[URI] = None
    url: URI
    viewer_can_add_plans: bool
    viewer_can_approve: bool
    viewer_can_delist: bool
    viewer_can_edit: bool
    viewer_can_edit_categories: bool
    viewer_can_edit_plans: bool
    viewer_can_redraft: bool
    viewer_can_reject: bool
    viewer_can_request_approval: bool
    viewer_has_purchased: bool
    viewer_has_purchased_for_all_organizations: bool
    viewer_is_listing_admin: bool


@dataclass(kw_only=True)
class MarketplaceListingEdge:
    """
    MarketplaceListingEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[MarketplaceListing] = None


@dataclass(kw_only=True)
class MarketplaceListingConnection:
    """
    MarketplaceListingConnection - Look up Marketplace Listings

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[MarketplaceListingEdge]] = None
    nodes: Optional[list[MarketplaceListing]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class MergePullRequestPayload:
    """
    MergePullRequestPayload - Autogenerated return type of MergePullRequest

    actor - Identifies the actor who performed the event.

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequest - The pull request that was merged.

    """

    actor: Optional[Actor] = None
    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class ProfileOwner:
    """
        ProfileOwner - Represents any entity on GitHub that has a profile page.

        anyPinnableItems - Determine if this repository owner has any items that can be pinned to their profile.

        email - The public profile email.

        id - The Node ID of the ProfileOwner object

        itemShowcase - Showcases a selection of repositories and gists that the profile owner has
    either curated or that have been selected automatically based on popularity.

        location - The public profile location.

        login - The username used to login.

        name - The public profile name.

        pinnableItems - A list of repositories and gists this profile owner can pin to their profile.

        pinnedItems - A list of repositories and gists this profile owner has pinned to their profile

        pinnedItemsRemaining - Returns how many more items this profile owner can pin to their profile.

        viewerCanChangePinnedItems - Can the viewer pin repositories and gists to the profile?

        websiteUrl - The public profile website URL.

    """

    any_pinnable_items: bool
    email: Optional[str] = None
    id: ID
    item_showcase: ProfileItemShowcase
    location: Optional[str] = None
    login: str
    name: Optional[str] = None
    pinnable_items: PinnableItemConnection
    pinned_items: PinnableItemConnection
    pinned_items_remaining: int
    viewer_can_change_pinned_items: bool
    website_url: Optional[URI] = None


@dataclass(kw_only=True)
class ProjectV2ActorEdge:
    """
    ProjectV2ActorEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[ProjectV2Actor] = None


@dataclass(kw_only=True)
class ProjectV2ActorConnection:
    """
    ProjectV2ActorConnection - The connection type for ProjectV2Actor.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[ProjectV2ActorEdge]] = None
    nodes: Optional[list[ProjectV2Actor]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectV2ItemFieldValueCommon:
    """
    ProjectV2ItemFieldValueCommon - Common fields across different project field value types

    createdAt - Identifies the date and time when the object was created.

    creator - The actor who created the item.

    databaseId - Identifies the primary key from the database.

    field - The project field that contains this value.

    id - The Node ID of the ProjectV2ItemFieldValueCommon object

    item - The project item that contains this value.

    updatedAt - Identifies the date and time when the object was last updated.

    """

    created_at: DateTime
    creator: Optional[Actor] = None
    database_id: Optional[int] = None
    field: ProjectV2FieldConfiguration
    id: ID
    item: ProjectV2Item
    updated_at: DateTime


@dataclass(kw_only=True)
class PullRequestThread:
    """
    PullRequestThread - A threaded list of comments for a given pull request.

    comments - A list of pull request comments associated with the thread.

    diffSide - The side of the diff on which this thread was placed.

    id - The Node ID of the PullRequestThread object

    isCollapsed - Whether or not the thread has been collapsed (resolved)

    isOutdated - Indicates whether this thread was outdated by newer changes.

    isResolved - Whether this thread has been resolved

    line - The line in the file to which this thread refers

    path - Identifies the file path of this thread.

    pullRequest - Identifies the pull request associated with this thread.

    repository - Identifies the repository associated with this thread.

    resolvedBy - The user who resolved this thread

    startDiffSide - The side of the diff that the first line of the thread starts on (multi-line only)

    startLine - The line of the first file diff in the thread.

    subjectType - The level at which the comments in the corresponding thread are targeted, can be a diff line or a file

    viewerCanReply - Indicates whether the current viewer can reply to this thread.

    viewerCanResolve - Whether or not the viewer can resolve this thread

    viewerCanUnresolve - Whether or not the viewer can unresolve this thread

    """

    comments: PullRequestReviewCommentConnection
    diff_side: DiffSide
    id: ID
    is_collapsed: bool
    is_outdated: bool
    is_resolved: bool
    line: Optional[int] = None
    path: str
    pull_request: PullRequest
    repository: Repository
    resolved_by: Optional[User] = None
    start_diff_side: Optional[DiffSide] = None
    start_line: Optional[int] = None
    subject_type: PullRequestReviewThreadSubjectType
    viewer_can_reply: bool
    viewer_can_resolve: bool
    viewer_can_unresolve: bool


@dataclass(kw_only=True)
class RemoveEnterpriseAdminPayload:
    """
    RemoveEnterpriseAdminPayload - Autogenerated return type of RemoveEnterpriseAdmin

    admin - The user who was removed as an administrator.

    clientMutationId - A unique identifier for the client performing the mutation.

    enterprise - The updated enterprise.

    message - A message confirming the result of removing an administrator.

    viewer - The viewer performing the mutation.

    """

    admin: Optional[User] = None
    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None
    viewer: Optional[User] = None


@dataclass(kw_only=True)
class RemoveEnterpriseMemberPayload:
    """
    RemoveEnterpriseMemberPayload - Autogenerated return type of RemoveEnterpriseMember

    clientMutationId - A unique identifier for the client performing the mutation.

    enterprise - The updated enterprise.

    user - The user that was removed from the enterprise.

    viewer - The viewer performing the mutation.

    """

    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    user: Optional[User] = None
    viewer: Optional[User] = None


@dataclass(kw_only=True)
class RemoveEnterpriseOrganizationPayload:
    """
    RemoveEnterpriseOrganizationPayload - Autogenerated return type of RemoveEnterpriseOrganization

    clientMutationId - A unique identifier for the client performing the mutation.

    enterprise - The updated enterprise.

    organization - The organization that was removed from the enterprise.

    viewer - The viewer performing the mutation.

    """

    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    organization: Optional[Organization] = None
    viewer: Optional[User] = None


@dataclass(kw_only=True)
class RemoveReactionPayload:
    """
    RemoveReactionPayload - Autogenerated return type of RemoveReaction

    clientMutationId - A unique identifier for the client performing the mutation.

    reaction - The reaction object.

    reactionGroups - The reaction groups for the subject.

    subject - The reactable subject.

    """

    client_mutation_id: Optional[str] = None
    reaction: Optional[Reaction] = None
    reaction_groups: Optional[list[ReactionGroup]] = None
    subject: Optional[Reactable] = None


@dataclass(kw_only=True)
class RequestReviewsPayload:
    """
    RequestReviewsPayload - Autogenerated return type of RequestReviews

    actor - Identifies the actor who performed the event.

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequest - The pull request that is getting requests.

    requestedReviewersEdge - The edge from the pull request to the requested reviewers.

    """

    actor: Optional[Actor] = None
    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None
    requested_reviewers_edge: Optional[UserEdge] = None


@dataclass(kw_only=True)
class RevertPullRequestPayload:
    """
    RevertPullRequestPayload - Autogenerated return type of RevertPullRequest

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequest - The pull request that was reverted.

    revertPullRequest - The new pull request that reverts the input pull request.

    """

    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None
    revert_pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class TextMatch:
    """
    TextMatch - A text match within a search result.

    fragment - The specific text fragment within the property matched on.

    highlights - Highlights within the matched fragment.

    property - The property matched on.

    """

    fragment: str
    highlights: list[TextMatchHighlight]
    property: str


@dataclass(kw_only=True)
class SearchResultItemEdge:
    """
    SearchResultItemEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    textMatches - Text matches on the result found.

    """

    cursor: str
    node: Optional[SearchResultItem] = None
    text_matches: Optional[list[TextMatch]] = None


@dataclass(kw_only=True)
class SearchResultItemConnection:
    """
        SearchResultItemConnection - A list of results that matched against a search query. Regardless of the number
    of matches, a maximum of 1,000 results will be available across all types,
    potentially split across many pages.

        codeCount - The total number of pieces of code that matched the search query. Regardless
    of the total number of matches, a maximum of 1,000 results will be available
    across all types.

        discussionCount - The total number of discussions that matched the search query. Regardless of
    the total number of matches, a maximum of 1,000 results will be available
    across all types.

        edges - A list of edges.

        issueCount - The total number of issues that matched the search query. Regardless of the
    total number of matches, a maximum of 1,000 results will be available across all types.

        nodes - A list of nodes.

        pageInfo - Information to aid in pagination.

        repositoryCount - The total number of repositories that matched the search query. Regardless of
    the total number of matches, a maximum of 1,000 results will be available
    across all types.

        userCount - The total number of users that matched the search query. Regardless of the
    total number of matches, a maximum of 1,000 results will be available across all types.

        wikiCount - The total number of wiki pages that matched the search query. Regardless of
    the total number of matches, a maximum of 1,000 results will be available
    across all types.

    """

    code_count: int
    discussion_count: int
    edges: Optional[list[SearchResultItemEdge]] = None
    issue_count: int
    nodes: Optional[list[SearchResultItem]] = None
    page_info: PageInfo
    repository_count: int
    user_count: int
    wiki_count: int


@dataclass(kw_only=True)
class SecurityAdvisoryEdge:
    """
    SecurityAdvisoryEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[SecurityAdvisory] = None


@dataclass(kw_only=True)
class SecurityAdvisoryConnection:
    """
    SecurityAdvisoryConnection - The connection type for SecurityAdvisory.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[SecurityAdvisoryEdge]] = None
    nodes: Optional[list[SecurityAdvisory]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class SponsorableItemEdge:
    """
    SponsorableItemEdge - An edge in a connection.

    cursor - A cursor for use in pagination.

    node - The item at the end of the edge.

    """

    cursor: str
    node: Optional[SponsorableItem] = None


@dataclass(kw_only=True)
class SponsorableItemConnection:
    """
    SponsorableItemConnection - The connection type for SponsorableItem.

    edges - A list of edges.

    nodes - A list of nodes.

    pageInfo - Information to aid in pagination.

    totalCount - Identifies the total count of items in the connection.

    """

    edges: Optional[list[SponsorableItemEdge]] = None
    nodes: Optional[list[SponsorableItem]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class Tag:
    """
    Tag - Represents a Git tag.

    abbreviatedOid - An abbreviated version of the Git object ID

    commitResourcePath - The HTTP path for this Git object

    commitUrl - The HTTP URL for this Git object

    id - The Node ID of the Tag object

    message - The Git tag message.

    name - The Git tag name.

    oid - The Git object ID

    repository - The Repository the Git object belongs to

    tagger - Details about the tag author.

    target - The Git object the tag points to.

    """

    abbreviated_oid: str
    commit_resource_path: URI
    commit_url: URI
    id: ID
    message: Optional[str] = None
    name: str
    oid: GitObjectID
    repository: Repository
    tagger: Optional[GitActor] = None
    target: GitObject


@dataclass(kw_only=True)
class UnlinkRepositoryFromProjectPayload:
    """
    UnlinkRepositoryFromProjectPayload - Autogenerated return type of UnlinkRepositoryFromProject

    clientMutationId - A unique identifier for the client performing the mutation.

    project - The linked Project.

    repository - The linked Repository.

    """

    client_mutation_id: Optional[str] = None
    project: Optional[Project] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class UnlockLockablePayload:
    """
    UnlockLockablePayload - Autogenerated return type of UnlockLockable

    actor - Identifies the actor who performed the event.

    clientMutationId - A unique identifier for the client performing the mutation.

    unlockedRecord - The item that was unlocked.

    """

    actor: Optional[Actor] = None
    client_mutation_id: Optional[str] = None
    unlocked_record: Optional[Lockable] = None


@dataclass(kw_only=True)
class UpdateCheckRunInput:
    """
    UpdateCheckRunInput - Autogenerated input type of UpdateCheckRun

    actions - Possible further actions the integrator can perform, which a user may trigger.

    checkRunId - The node of the check.

    clientMutationId - A unique identifier for the client performing the mutation.

    completedAt - The time that the check run finished.

    conclusion - The final conclusion of the check.

    detailsUrl - The URL of the integrator's site that has the full details of the check.

    externalId - A reference for the run on the integrator's system.

    name - The name of the check.

    output - Descriptive details about the run.

    repositoryId - The node ID of the repository.

    startedAt - The time that the check run began.

    status - The current status.

    """

    actions: Optional[list[CheckRunAction]] = None
    check_run_id: ID
    client_mutation_id: Optional[str] = None
    completed_at: Optional[DateTime] = None
    conclusion: Optional[CheckConclusionState] = None
    details_url: Optional[URI] = None
    external_id: Optional[str] = None
    name: Optional[str] = None
    output: Optional[CheckRunOutput] = None
    repository_id: ID
    started_at: Optional[DateTime] = None
    status: Optional[RequestableCheckStatusState] = None


@dataclass(kw_only=True)
class UpdateIssuePayload:
    """
    UpdateIssuePayload - Autogenerated return type of UpdateIssue

    actor - Identifies the actor who performed the event.

    clientMutationId - A unique identifier for the client performing the mutation.

    issue - The issue.

    """

    actor: Optional[Actor] = None
    client_mutation_id: Optional[str] = None
    issue: Optional[Issue] = None


@dataclass(kw_only=True)
class UpdatePullRequestPayload:
    """
    UpdatePullRequestPayload - Autogenerated return type of UpdatePullRequest

    actor - Identifies the actor who performed the event.

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequest - The updated pull request.

    """

    actor: Optional[Actor] = None
    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class UpdateRepositoryRulesetInput:
    """
    UpdateRepositoryRulesetInput - Autogenerated input type of UpdateRepositoryRuleset

    bypassActors - A list of actors that are allowed to bypass rules in this ruleset.

    clientMutationId - A unique identifier for the client performing the mutation.

    conditions - The list of conditions for this ruleset

    enforcement - The enforcement level for this ruleset

    name - The name of the ruleset.

    repositoryRulesetId - The global relay id of the repository ruleset to be updated.

    rules - The list of rules for this ruleset

    target - The target of the ruleset.

    """

    bypass_actors: Optional[list[RepositoryRulesetBypassActorInput]] = None
    client_mutation_id: Optional[str] = None
    conditions: Optional[RepositoryRuleConditionsInput] = None
    enforcement: Optional[RuleEnforcement] = None
    name: Optional[str] = None
    repository_ruleset_id: ID
    rules: Optional[list[RepositoryRuleInput]] = None
    target: Optional[RepositoryRulesetTarget] = None


@dataclass(kw_only=True)
class UpdateTeamsRepositoryPayload:
    """
    UpdateTeamsRepositoryPayload - Autogenerated return type of UpdateTeamsRepository

    clientMutationId - A unique identifier for the client performing the mutation.

    repository - The repository that was updated.

    teams - The teams granted permission on the repository.

    """

    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None
    teams: Optional[list[Team]] = None


@dataclass(kw_only=True)
class UpdateUserListsForItemPayload:
    """
    UpdateUserListsForItemPayload - Autogenerated return type of UpdateUserListsForItem

    clientMutationId - A unique identifier for the client performing the mutation.

    item - The item that was added

    lists - The lists to which this item belongs

    user - The user who owns the lists

    """

    client_mutation_id: Optional[str] = None
    item: Optional[UserListItems] = None
    lists: Optional[list[UserList]] = None
    user: Optional[User] = None


@dataclass(kw_only=True)
class ViewerHovercardContext:
    """
    ViewerHovercardContext - A hovercard context with a message describing how the viewer is related.

    message - A string describing this context

    octicon - An octicon to accompany this context

    viewer - Identifies the user who is related to this context.

    """

    message: str
    octicon: str
    viewer: User


@dataclass(kw_only=True)
class VerifyVerifiableDomainPayload:
    """
    VerifyVerifiableDomainPayload - Autogenerated return type of VerifyVerifiableDomain

    clientMutationId - A unique identifier for the client performing the mutation.

    domain - The verifiable domain that was verified.

    """

    client_mutation_id: Optional[str] = None
    domain: Optional[VerifiableDomain] = None


@dataclass(kw_only=True)
class UpdateUserListPayload:
    """
    UpdateUserListPayload - Autogenerated return type of UpdateUserList

    clientMutationId - A unique identifier for the client performing the mutation.

    list - The list that was just updated

    """

    client_mutation_id: Optional[str] = None
    list: Optional[UserList] = None


@dataclass(kw_only=True)
class UpdateTopicsPayload:
    """
    UpdateTopicsPayload - Autogenerated return type of UpdateTopics

    clientMutationId - A unique identifier for the client performing the mutation.

    invalidTopicNames - Names of the provided topics that are not valid.

    repository - The updated repository.

    """

    client_mutation_id: Optional[str] = None
    invalid_topic_names: Optional[list[str]] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class UpdateTeamReviewAssignmentPayload:
    """
    UpdateTeamReviewAssignmentPayload - Autogenerated return type of UpdateTeamReviewAssignment

    clientMutationId - A unique identifier for the client performing the mutation.

    team - The team that was modified

    """

    client_mutation_id: Optional[str] = None
    team: Optional[Team] = None


@dataclass(kw_only=True)
class UpdateTeamDiscussionPayload:
    """
    UpdateTeamDiscussionPayload - Autogenerated return type of UpdateTeamDiscussion

    clientMutationId - A unique identifier for the client performing the mutation.

    teamDiscussion - The updated discussion.

    """

    client_mutation_id: Optional[str] = None
    team_discussion: Optional[TeamDiscussion] = None


@dataclass(kw_only=True)
class UpdateTeamDiscussionCommentPayload:
    """
    UpdateTeamDiscussionCommentPayload - Autogenerated return type of UpdateTeamDiscussionComment

    clientMutationId - A unique identifier for the client performing the mutation.

    teamDiscussionComment - The updated comment.

    """

    client_mutation_id: Optional[str] = None
    team_discussion_comment: Optional[TeamDiscussionComment] = None


@dataclass(kw_only=True)
class UpdateSubscriptionPayload:
    """
    UpdateSubscriptionPayload - Autogenerated return type of UpdateSubscription

    clientMutationId - A unique identifier for the client performing the mutation.

    subscribable - The input subscribable entity.

    """

    client_mutation_id: Optional[str] = None
    subscribable: Optional[Subscribable] = None


@dataclass(kw_only=True)
class UpdateSponsorshipPreferencesPayload:
    """
    UpdateSponsorshipPreferencesPayload - Autogenerated return type of UpdateSponsorshipPreferences

    clientMutationId - A unique identifier for the client performing the mutation.

    sponsorship - The sponsorship that was updated.

    """

    client_mutation_id: Optional[str] = None
    sponsorship: Optional[Sponsorship] = None


@dataclass(kw_only=True)
class UpdateRepositoryWebCommitSignoffSettingPayload:
    """
    UpdateRepositoryWebCommitSignoffSettingPayload - Autogenerated return type of UpdateRepositoryWebCommitSignoffSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    message - A message confirming the result of updating the web commit signoff setting.

    repository - The updated repository.

    """

    client_mutation_id: Optional[str] = None
    message: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class UpdateRepositoryRulesetPayload:
    """
    UpdateRepositoryRulesetPayload - Autogenerated return type of UpdateRepositoryRuleset

    clientMutationId - A unique identifier for the client performing the mutation.

    ruleset - The newly created Ruleset.

    """

    client_mutation_id: Optional[str] = None
    ruleset: Optional[RepositoryRuleset] = None


@dataclass(kw_only=True)
class UpdateRepositoryPayload:
    """
    UpdateRepositoryPayload - Autogenerated return type of UpdateRepository

    clientMutationId - A unique identifier for the client performing the mutation.

    repository - The updated repository.

    """

    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class UpdateRefsInput:
    """
    UpdateRefsInput - Autogenerated input type of UpdateRefs

    clientMutationId - A unique identifier for the client performing the mutation.

    refUpdates - A list of ref updates.

    repositoryId - The Node ID of the repository.

    """

    client_mutation_id: Optional[str] = None
    ref_updates: list[RefUpdate]
    repository_id: ID


@dataclass(kw_only=True)
class UpdateRefPayload:
    """
    UpdateRefPayload - Autogenerated return type of UpdateRef

    clientMutationId - A unique identifier for the client performing the mutation.

    ref - The updated Ref.

    """

    client_mutation_id: Optional[str] = None
    ref: Optional[Ref] = None


@dataclass(kw_only=True)
class UpdatePullRequestReviewPayload:
    """
    UpdatePullRequestReviewPayload - Autogenerated return type of UpdatePullRequestReview

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequestReview - The updated pull request review.

    """

    client_mutation_id: Optional[str] = None
    pull_request_review: Optional[PullRequestReview] = None


@dataclass(kw_only=True)
class UpdatePullRequestReviewCommentPayload:
    """
    UpdatePullRequestReviewCommentPayload - Autogenerated return type of UpdatePullRequestReviewComment

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequestReviewComment - The updated comment.

    """

    client_mutation_id: Optional[str] = None
    pull_request_review_comment: Optional[PullRequestReviewComment] = None


@dataclass(kw_only=True)
class UpdatePullRequestBranchPayload:
    """
    UpdatePullRequestBranchPayload - Autogenerated return type of UpdatePullRequestBranch

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequest - The updated pull request.

    """

    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class UpdateProjectV2Payload:
    """
    UpdateProjectV2Payload - Autogenerated return type of UpdateProjectV2

    clientMutationId - A unique identifier for the client performing the mutation.

    projectV2 - The updated Project.

    """

    client_mutation_id: Optional[str] = None
    project_v2: Optional[ProjectV2] = None


@dataclass(kw_only=True)
class UpdateProjectV2ItemPositionPayload:
    """
    UpdateProjectV2ItemPositionPayload - Autogenerated return type of UpdateProjectV2ItemPosition

    clientMutationId - A unique identifier for the client performing the mutation.

    items - The items in the new order

    """

    client_mutation_id: Optional[str] = None
    items: Optional[ProjectV2ItemConnection] = None


@dataclass(kw_only=True)
class UpdateProjectV2ItemFieldValuePayload:
    """
    UpdateProjectV2ItemFieldValuePayload - Autogenerated return type of UpdateProjectV2ItemFieldValue

    clientMutationId - A unique identifier for the client performing the mutation.

    projectV2Item - The updated item.

    """

    client_mutation_id: Optional[str] = None
    project_v2_item: Optional[ProjectV2Item] = None


@dataclass(kw_only=True)
class UpdateProjectV2ItemFieldValueInput:
    """
    UpdateProjectV2ItemFieldValueInput - Autogenerated input type of UpdateProjectV2ItemFieldValue

    clientMutationId - A unique identifier for the client performing the mutation.

    fieldId - The ID of the field to be updated.

    itemId - The ID of the item to be updated.

    projectId - The ID of the Project.

    value - The value which will be set on the field.

    """

    client_mutation_id: Optional[str] = None
    field_id: ID
    item_id: ID
    project_id: ID
    value: ProjectV2FieldValue


@dataclass(kw_only=True)
class UpdateProjectV2DraftIssuePayload:
    """
    UpdateProjectV2DraftIssuePayload - Autogenerated return type of UpdateProjectV2DraftIssue

    clientMutationId - A unique identifier for the client performing the mutation.

    draftIssue - The draft issue updated in the project.

    """

    client_mutation_id: Optional[str] = None
    draft_issue: Optional[DraftIssue] = None


@dataclass(kw_only=True)
class UpdateProjectV2CollaboratorsPayload:
    """
    UpdateProjectV2CollaboratorsPayload - Autogenerated return type of UpdateProjectV2Collaborators

    clientMutationId - A unique identifier for the client performing the mutation.

    collaborators - The collaborators granted a role

    """

    client_mutation_id: Optional[str] = None
    collaborators: Optional[ProjectV2ActorConnection] = None


@dataclass(kw_only=True)
class UpdateProjectV2CollaboratorsInput:
    """
    UpdateProjectV2CollaboratorsInput - Autogenerated input type of UpdateProjectV2Collaborators

    clientMutationId - A unique identifier for the client performing the mutation.

    collaborators - The collaborators to update.

    projectId - The ID of the project to update the collaborators for.

    """

    client_mutation_id: Optional[str] = None
    collaborators: list[ProjectV2Collaborator]
    project_id: ID


@dataclass(kw_only=True)
class UpdateProjectPayload:
    """
    UpdateProjectPayload - Autogenerated return type of UpdateProject

    clientMutationId - A unique identifier for the client performing the mutation.

    project - The updated project.

    """

    client_mutation_id: Optional[str] = None
    project: Optional[Project] = None


@dataclass(kw_only=True)
class UpdateProjectColumnPayload:
    """
    UpdateProjectColumnPayload - Autogenerated return type of UpdateProjectColumn

    clientMutationId - A unique identifier for the client performing the mutation.

    projectColumn - The updated project column.

    """

    client_mutation_id: Optional[str] = None
    project_column: Optional[ProjectColumn] = None


@dataclass(kw_only=True)
class UpdateProjectCardPayload:
    """
    UpdateProjectCardPayload - Autogenerated return type of UpdateProjectCard

    clientMutationId - A unique identifier for the client performing the mutation.

    projectCard - The updated ProjectCard.

    """

    client_mutation_id: Optional[str] = None
    project_card: Optional[ProjectCard] = None


@dataclass(kw_only=True)
class UpdatePatreonSponsorabilityPayload:
    """
    UpdatePatreonSponsorabilityPayload - Autogenerated return type of UpdatePatreonSponsorability

    clientMutationId - A unique identifier for the client performing the mutation.

    sponsorsListing - The GitHub Sponsors profile.

    """

    client_mutation_id: Optional[str] = None
    sponsors_listing: Optional[SponsorsListing] = None


@dataclass(kw_only=True)
class UpdateOrganizationWebCommitSignoffSettingPayload:
    """
    UpdateOrganizationWebCommitSignoffSettingPayload - Autogenerated return type of UpdateOrganizationWebCommitSignoffSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    message - A message confirming the result of updating the web commit signoff setting.

    organization - The organization with the updated web commit signoff setting.

    """

    client_mutation_id: Optional[str] = None
    message: Optional[str] = None
    organization: Optional[Organization] = None


@dataclass(kw_only=True)
class UpdateOrganizationAllowPrivateRepositoryForkingSettingPayload:
    """
    UpdateOrganizationAllowPrivateRepositoryForkingSettingPayload - Autogenerated return type of UpdateOrganizationAllowPrivateRepositoryForkingSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    message - A message confirming the result of updating the allow private repository forking setting.

    organization - The organization with the updated allow private repository forking setting.

    """

    client_mutation_id: Optional[str] = None
    message: Optional[str] = None
    organization: Optional[Organization] = None


@dataclass(kw_only=True)
class UpdateNotificationRestrictionSettingPayload:
    """
    UpdateNotificationRestrictionSettingPayload - Autogenerated return type of UpdateNotificationRestrictionSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    owner - The owner on which the setting was updated.

    """

    client_mutation_id: Optional[str] = None
    owner: Optional[VerifiableDomainOwner] = None


@dataclass(kw_only=True)
class UpdateLabelPayload:
    """
    UpdateLabelPayload - Autogenerated return type of UpdateLabel

    clientMutationId - A unique identifier for the client performing the mutation.

    label - The updated label.

    """

    client_mutation_id: Optional[str] = None
    label: Optional[Label] = None


@dataclass(kw_only=True)
class UpdateIssueCommentPayload:
    """
    UpdateIssueCommentPayload - Autogenerated return type of UpdateIssueComment

    clientMutationId - A unique identifier for the client performing the mutation.

    issueComment - The updated comment.

    """

    client_mutation_id: Optional[str] = None
    issue_comment: Optional[IssueComment] = None


@dataclass(kw_only=True)
class UpdateIpAllowListForInstalledAppsEnabledSettingPayload:
    """
    UpdateIpAllowListForInstalledAppsEnabledSettingPayload - Autogenerated return type of UpdateIpAllowListForInstalledAppsEnabledSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    owner - The IP allow list owner on which the setting was updated.

    """

    client_mutation_id: Optional[str] = None
    owner: Optional[IpAllowListOwner] = None


@dataclass(kw_only=True)
class UpdateIpAllowListEntryPayload:
    """
    UpdateIpAllowListEntryPayload - Autogenerated return type of UpdateIpAllowListEntry

    clientMutationId - A unique identifier for the client performing the mutation.

    ipAllowListEntry - The IP allow list entry that was updated.

    """

    client_mutation_id: Optional[str] = None
    ip_allow_list_entry: Optional[IpAllowListEntry] = None


@dataclass(kw_only=True)
class UpdateIpAllowListEnabledSettingPayload:
    """
    UpdateIpAllowListEnabledSettingPayload - Autogenerated return type of UpdateIpAllowListEnabledSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    owner - The IP allow list owner on which the setting was updated.

    """

    client_mutation_id: Optional[str] = None
    owner: Optional[IpAllowListOwner] = None


@dataclass(kw_only=True)
class UpdateEnvironmentPayload:
    """
    UpdateEnvironmentPayload - Autogenerated return type of UpdateEnvironment

    clientMutationId - A unique identifier for the client performing the mutation.

    environment - The updated environment.

    """

    client_mutation_id: Optional[str] = None
    environment: Optional[Environment] = None


@dataclass(kw_only=True)
class UpdateEnterpriseTwoFactorAuthenticationRequiredSettingPayload:
    """
    UpdateEnterpriseTwoFactorAuthenticationRequiredSettingPayload - Autogenerated return type of UpdateEnterpriseTwoFactorAuthenticationRequiredSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterprise - The enterprise with the updated two factor authentication required setting.

    message - A message confirming the result of updating the two factor authentication required setting.

    """

    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseTeamDiscussionsSettingPayload:
    """
    UpdateEnterpriseTeamDiscussionsSettingPayload - Autogenerated return type of UpdateEnterpriseTeamDiscussionsSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterprise - The enterprise with the updated team discussions setting.

    message - A message confirming the result of updating the team discussions setting.

    """

    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseRepositoryProjectsSettingPayload:
    """
    UpdateEnterpriseRepositoryProjectsSettingPayload - Autogenerated return type of UpdateEnterpriseRepositoryProjectsSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterprise - The enterprise with the updated repository projects setting.

    message - A message confirming the result of updating the repository projects setting.

    """

    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseProfilePayload:
    """
    UpdateEnterpriseProfilePayload - Autogenerated return type of UpdateEnterpriseProfile

    clientMutationId - A unique identifier for the client performing the mutation.

    enterprise - The updated enterprise.

    """

    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None


@dataclass(kw_only=True)
class UpdateEnterpriseOrganizationProjectsSettingPayload:
    """
    UpdateEnterpriseOrganizationProjectsSettingPayload - Autogenerated return type of UpdateEnterpriseOrganizationProjectsSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterprise - The enterprise with the updated organization projects setting.

    message - A message confirming the result of updating the organization projects setting.

    """

    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanViewDependencyInsightsSettingPayload:
    """
    UpdateEnterpriseMembersCanViewDependencyInsightsSettingPayload - Autogenerated return type of UpdateEnterpriseMembersCanViewDependencyInsightsSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterprise - The enterprise with the updated members can view dependency insights setting.

    message - A message confirming the result of updating the members can view dependency insights setting.

    """

    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingPayload:
    """
    UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingPayload - Autogenerated return type of UpdateEnterpriseMembersCanUpdateProtectedBranchesSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterprise - The enterprise with the updated members can update protected branches setting.

    message - A message confirming the result of updating the members can update protected branches setting.

    """

    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanMakePurchasesSettingPayload:
    """
    UpdateEnterpriseMembersCanMakePurchasesSettingPayload - Autogenerated return type of UpdateEnterpriseMembersCanMakePurchasesSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterprise - The enterprise with the updated members can make purchases setting.

    message - A message confirming the result of updating the members can make purchases setting.

    """

    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanInviteCollaboratorsSettingPayload:
    """
    UpdateEnterpriseMembersCanInviteCollaboratorsSettingPayload - Autogenerated return type of UpdateEnterpriseMembersCanInviteCollaboratorsSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterprise - The enterprise with the updated members can invite collaborators setting.

    message - A message confirming the result of updating the members can invite collaborators setting.

    """

    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanDeleteRepositoriesSettingPayload:
    """
    UpdateEnterpriseMembersCanDeleteRepositoriesSettingPayload - Autogenerated return type of UpdateEnterpriseMembersCanDeleteRepositoriesSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterprise - The enterprise with the updated members can delete repositories setting.

    message - A message confirming the result of updating the members can delete repositories setting.

    """

    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanDeleteIssuesSettingPayload:
    """
    UpdateEnterpriseMembersCanDeleteIssuesSettingPayload - Autogenerated return type of UpdateEnterpriseMembersCanDeleteIssuesSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterprise - The enterprise with the updated members can delete issues setting.

    message - A message confirming the result of updating the members can delete issues setting.

    """

    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanCreateRepositoriesSettingPayload:
    """
    UpdateEnterpriseMembersCanCreateRepositoriesSettingPayload - Autogenerated return type of UpdateEnterpriseMembersCanCreateRepositoriesSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterprise - The enterprise with the updated members can create repositories setting.

    message - A message confirming the result of updating the members can create repositories setting.

    """

    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingPayload:
    """
    UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingPayload - Autogenerated return type of UpdateEnterpriseMembersCanChangeRepositoryVisibilitySetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterprise - The enterprise with the updated members can change repository visibility setting.

    message - A message confirming the result of updating the members can change repository visibility setting.

    """

    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseDefaultRepositoryPermissionSettingPayload:
    """
    UpdateEnterpriseDefaultRepositoryPermissionSettingPayload - Autogenerated return type of UpdateEnterpriseDefaultRepositoryPermissionSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterprise - The enterprise with the updated base repository permission setting.

    message - A message confirming the result of updating the base repository permission setting.

    """

    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseAllowPrivateRepositoryForkingSettingPayload:
    """
    UpdateEnterpriseAllowPrivateRepositoryForkingSettingPayload - Autogenerated return type of UpdateEnterpriseAllowPrivateRepositoryForkingSetting

    clientMutationId - A unique identifier for the client performing the mutation.

    enterprise - The enterprise with the updated allow private repository forking setting.

    message - A message confirming the result of updating the allow private repository forking setting.

    """

    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateDiscussionPayload:
    """
    UpdateDiscussionPayload - Autogenerated return type of UpdateDiscussion

    clientMutationId - A unique identifier for the client performing the mutation.

    discussion - The modified discussion.

    """

    client_mutation_id: Optional[str] = None
    discussion: Optional[Discussion] = None


@dataclass(kw_only=True)
class UpdateDiscussionCommentPayload:
    """
    UpdateDiscussionCommentPayload - Autogenerated return type of UpdateDiscussionComment

    clientMutationId - A unique identifier for the client performing the mutation.

    comment - The modified discussion comment.

    """

    client_mutation_id: Optional[str] = None
    comment: Optional[DiscussionComment] = None


@dataclass(kw_only=True)
class UpdateCheckSuitePreferencesPayload:
    """
    UpdateCheckSuitePreferencesPayload - Autogenerated return type of UpdateCheckSuitePreferences

    clientMutationId - A unique identifier for the client performing the mutation.

    repository - The updated repository.

    """

    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class UpdateCheckSuitePreferencesInput:
    """
    UpdateCheckSuitePreferencesInput - Autogenerated input type of UpdateCheckSuitePreferences

    autoTriggerPreferences - The check suite preferences to modify.

    clientMutationId - A unique identifier for the client performing the mutation.

    repositoryId - The Node ID of the repository.

    """

    auto_trigger_preferences: list[CheckSuiteAutoTriggerPreference]
    client_mutation_id: Optional[str] = None
    repository_id: ID


@dataclass(kw_only=True)
class UpdateCheckRunPayload:
    """
    UpdateCheckRunPayload - Autogenerated return type of UpdateCheckRun

    checkRun - The updated check run.

    clientMutationId - A unique identifier for the client performing the mutation.

    """

    check_run: Optional[CheckRun] = None
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class UpdateBranchProtectionRulePayload:
    """
    UpdateBranchProtectionRulePayload - Autogenerated return type of UpdateBranchProtectionRule

    branchProtectionRule - The newly created BranchProtectionRule.

    clientMutationId - A unique identifier for the client performing the mutation.

    """

    branch_protection_rule: Optional[BranchProtectionRule] = None
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class UpdateBranchProtectionRuleInput:
    """
        UpdateBranchProtectionRuleInput - Autogenerated input type of UpdateBranchProtectionRule

        allowsDeletions - Can this branch be deleted.

        allowsForcePushes - Are force pushes allowed on this branch.

        blocksCreations - Is branch creation a protected operation.

        branchProtectionRuleId - The global relay id of the branch protection rule to be updated.

        bypassForcePushActorIds - A list of User, Team, or App IDs allowed to bypass force push targeting matching branches.

        bypassPullRequestActorIds - A list of User, Team, or App IDs allowed to bypass pull requests targeting matching branches.

        clientMutationId - A unique identifier for the client performing the mutation.

        dismissesStaleReviews - Will new commits pushed to matching branches dismiss pull request review approvals.

        isAdminEnforced - Can admins override branch protection.

        lockAllowsFetchAndMerge - Whether users can pull changes from upstream when the branch is locked. Set to
    `true` to allow fork syncing. Set to `false` to prevent fork syncing.

        lockBranch - Whether to set the branch as read-only. If this is true, users will not be able to push to the branch.

        pattern - The glob-like pattern used to determine matching branches.

        pushActorIds - A list of User, Team, or App IDs allowed to push to matching branches.

        requireLastPushApproval - Whether the most recent push must be approved by someone other than the person who pushed it

        requiredApprovingReviewCount - Number of approving reviews required to update matching branches.

        requiredDeploymentEnvironments - The list of required deployment environments

        requiredStatusCheckContexts - List of required status check contexts that must pass for commits to be accepted to matching branches.

        requiredStatusChecks - The list of required status checks

        requiresApprovingReviews - Are approving reviews required to update matching branches.

        requiresCodeOwnerReviews - Are reviews from code owners required to update matching branches.

        requiresCommitSignatures - Are commits required to be signed.

        requiresConversationResolution - Are conversations required to be resolved before merging.

        requiresDeployments - Are successful deployments required before merging.

        requiresLinearHistory - Are merge commits prohibited from being pushed to this branch.

        requiresStatusChecks - Are status checks required to update matching branches.

        requiresStrictStatusChecks - Are branches required to be up to date before merging.

        restrictsPushes - Is pushing to matching branches restricted.

        restrictsReviewDismissals - Is dismissal of pull request reviews restricted.

        reviewDismissalActorIds - A list of User, Team, or App IDs allowed to dismiss reviews on pull requests targeting matching branches.

    """

    allows_deletions: Optional[bool] = None
    allows_force_pushes: Optional[bool] = None
    blocks_creations: Optional[bool] = None
    branch_protection_rule_id: ID
    bypass_force_push_actor_ids: Optional[list[ID]] = None
    bypass_pull_request_actor_ids: Optional[list[ID]] = None
    client_mutation_id: Optional[str] = None
    dismisses_stale_reviews: Optional[bool] = None
    is_admin_enforced: Optional[bool] = None
    lock_allows_fetch_and_merge: Optional[bool] = None
    lock_branch: Optional[bool] = None
    pattern: Optional[str] = None
    push_actor_ids: Optional[list[ID]] = None
    require_last_push_approval: Optional[bool] = None
    required_approving_review_count: Optional[int] = None
    required_deployment_environments: Optional[list[str]] = None
    required_status_check_contexts: Optional[list[str]] = None
    required_status_checks: Optional[list[RequiredStatusCheckInput]] = None
    requires_approving_reviews: Optional[bool] = None
    requires_code_owner_reviews: Optional[bool] = None
    requires_commit_signatures: Optional[bool] = None
    requires_conversation_resolution: Optional[bool] = None
    requires_deployments: Optional[bool] = None
    requires_linear_history: Optional[bool] = None
    requires_status_checks: Optional[bool] = None
    requires_strict_status_checks: Optional[bool] = None
    restricts_pushes: Optional[bool] = None
    restricts_review_dismissals: Optional[bool] = None
    review_dismissal_actor_ids: Optional[list[ID]] = None


@dataclass(kw_only=True)
class UnresolveReviewThreadPayload:
    """
    UnresolveReviewThreadPayload - Autogenerated return type of UnresolveReviewThread

    clientMutationId - A unique identifier for the client performing the mutation.

    thread - The thread to resolve.

    """

    client_mutation_id: Optional[str] = None
    thread: Optional[PullRequestReviewThread] = None


@dataclass(kw_only=True)
class UnpinIssuePayload:
    """
    UnpinIssuePayload - Autogenerated return type of UnpinIssue

    clientMutationId - A unique identifier for the client performing the mutation.

    id - The id of the pinned issue that was unpinned

    issue - The issue that was unpinned

    """

    client_mutation_id: Optional[str] = None
    id: Optional[ID] = None
    issue: Optional[Issue] = None


@dataclass(kw_only=True)
class UnminimizeCommentPayload:
    """
    UnminimizeCommentPayload - Autogenerated return type of UnminimizeComment

    clientMutationId - A unique identifier for the client performing the mutation.

    unminimizedComment - The comment that was unminimized.

    """

    client_mutation_id: Optional[str] = None
    unminimized_comment: Optional[Minimizable] = None


@dataclass(kw_only=True)
class UnmarkProjectV2AsTemplatePayload:
    """
    UnmarkProjectV2AsTemplatePayload - Autogenerated return type of UnmarkProjectV2AsTemplate

    clientMutationId - A unique identifier for the client performing the mutation.

    projectV2 - The project.

    """

    client_mutation_id: Optional[str] = None
    project_v2: Optional[ProjectV2] = None


@dataclass(kw_only=True)
class UnmarkIssueAsDuplicatePayload:
    """
    UnmarkIssueAsDuplicatePayload - Autogenerated return type of UnmarkIssueAsDuplicate

    clientMutationId - A unique identifier for the client performing the mutation.

    duplicate - The issue or pull request that was marked as a duplicate.

    """

    client_mutation_id: Optional[str] = None
    duplicate: Optional[IssueOrPullRequest] = None


@dataclass(kw_only=True)
class UnmarkFileAsViewedPayload:
    """
    UnmarkFileAsViewedPayload - Autogenerated return type of UnmarkFileAsViewed

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequest - The updated pull request.

    """

    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class UnmarkDiscussionCommentAsAnswerPayload:
    """
    UnmarkDiscussionCommentAsAnswerPayload - Autogenerated return type of UnmarkDiscussionCommentAsAnswer

    clientMutationId - A unique identifier for the client performing the mutation.

    discussion - The discussion that includes the comment.

    """

    client_mutation_id: Optional[str] = None
    discussion: Optional[Discussion] = None


@dataclass(kw_only=True)
class UnlinkProjectV2FromTeamPayload:
    """
    UnlinkProjectV2FromTeamPayload - Autogenerated return type of UnlinkProjectV2FromTeam

    clientMutationId - A unique identifier for the client performing the mutation.

    team - The team the project is unlinked from

    """

    client_mutation_id: Optional[str] = None
    team: Optional[Team] = None


@dataclass(kw_only=True)
class UnlinkProjectV2FromRepositoryPayload:
    """
    UnlinkProjectV2FromRepositoryPayload - Autogenerated return type of UnlinkProjectV2FromRepository

    clientMutationId - A unique identifier for the client performing the mutation.

    repository - The repository the project is no longer linked to.

    """

    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class UnknownSignature:
    """
        UnknownSignature - Represents an unknown signature on a Commit or Tag.

        email - Email used to sign this object.

        isValid - True if the signature is valid and verified by GitHub.

        payload - Payload for GPG signing object. Raw ODB object without the signature header.

        signature - ASCII-armored signature header from object.

        signer - GitHub user corresponding to the email signing this commit.

        state - The state of this signature. `VALID` if signature is valid and verified by
    GitHub, otherwise represents reason why signature is considered invalid.

        wasSignedByGitHub - True if the signature was made with GitHub's signing key.

    """

    email: str
    is_valid: bool
    payload: str
    signature: str
    signer: Optional[User] = None
    state: GitSignatureState
    was_signed_by_git_hub: bool


@dataclass(kw_only=True)
class UnfollowUserPayload:
    """
    UnfollowUserPayload - Autogenerated return type of UnfollowUser

    clientMutationId - A unique identifier for the client performing the mutation.

    user - The user that was unfollowed.

    """

    client_mutation_id: Optional[str] = None
    user: Optional[User] = None


@dataclass(kw_only=True)
class UnfollowOrganizationPayload:
    """
    UnfollowOrganizationPayload - Autogenerated return type of UnfollowOrganization

    clientMutationId - A unique identifier for the client performing the mutation.

    organization - The organization that was unfollowed.

    """

    client_mutation_id: Optional[str] = None
    organization: Optional[Organization] = None


@dataclass(kw_only=True)
class UnarchiveRepositoryPayload:
    """
    UnarchiveRepositoryPayload - Autogenerated return type of UnarchiveRepository

    clientMutationId - A unique identifier for the client performing the mutation.

    repository - The repository that was unarchived.

    """

    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class UnarchiveProjectV2ItemPayload:
    """
    UnarchiveProjectV2ItemPayload - Autogenerated return type of UnarchiveProjectV2Item

    clientMutationId - A unique identifier for the client performing the mutation.

    item - The item unarchived from the project.

    """

    client_mutation_id: Optional[str] = None
    item: Optional[ProjectV2Item] = None


@dataclass(kw_only=True)
class TransferIssuePayload:
    """
    TransferIssuePayload - Autogenerated return type of TransferIssue

    clientMutationId - A unique identifier for the client performing the mutation.

    issue - The issue that was transferred

    """

    client_mutation_id: Optional[str] = None
    issue: Optional[Issue] = None


@dataclass(kw_only=True)
class TransferEnterpriseOrganizationPayload:
    """
    TransferEnterpriseOrganizationPayload - Autogenerated return type of TransferEnterpriseOrganization

    clientMutationId - A unique identifier for the client performing the mutation.

    organization - The organization for which a transfer was initiated.

    """

    client_mutation_id: Optional[str] = None
    organization: Optional[Organization] = None


@dataclass(kw_only=True)
class TopicAuditEntryData:
    """
    TopicAuditEntryData - Metadata for an audit entry with a topic.

    topic - The name of the topic added to the repository

    topicName - The name of the topic added to the repository

    """

    topic: Optional[Topic] = None
    topic_name: Optional[str] = None


@dataclass(kw_only=True)
class TeamAuditEntryData:
    """
    TeamAuditEntryData - Metadata for an audit entry with action team.*

    team - The team associated with the action

    teamName - The name of the team

    teamResourcePath - The HTTP path for this team

    teamUrl - The HTTP URL for this team

    """

    team: Optional[Team] = None
    team_name: Optional[str] = None
    team_resource_path: Optional[URI] = None
    team_url: Optional[URI] = None


@dataclass(kw_only=True)
class SubmitPullRequestReviewPayload:
    """
    SubmitPullRequestReviewPayload - Autogenerated return type of SubmitPullRequestReview

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequestReview - The submitted pull request review.

    """

    client_mutation_id: Optional[str] = None
    pull_request_review: Optional[PullRequestReview] = None


@dataclass(kw_only=True)
class StartRepositoryMigrationPayload:
    """
    StartRepositoryMigrationPayload - Autogenerated return type of StartRepositoryMigration

    clientMutationId - A unique identifier for the client performing the mutation.

    repositoryMigration - The new repository migration.

    """

    client_mutation_id: Optional[str] = None
    repository_migration: Optional[RepositoryMigration] = None


@dataclass(kw_only=True)
class StartOrganizationMigrationPayload:
    """
    StartOrganizationMigrationPayload - Autogenerated return type of StartOrganizationMigration

    clientMutationId - A unique identifier for the client performing the mutation.

    orgMigration - The new organization migration.

    """

    client_mutation_id: Optional[str] = None
    org_migration: Optional[OrganizationMigration] = None


@dataclass(kw_only=True)
class Starrable:
    """
    Starrable - Things that can be starred.

    id - The Node ID of the Starrable object

    stargazerCount - Returns a count of how many stargazers there are on this object

    stargazers - A list of users who have starred this starrable.

    viewerHasStarred - Returns a boolean indicating whether the viewing user has starred this starrable.

    """

    id: ID
    stargazer_count: int
    stargazers: StargazerConnection
    viewer_has_starred: bool


@dataclass(kw_only=True)
class SshSignature:
    """
        SshSignature - Represents an SSH signature on a Commit or Tag.

        email - Email used to sign this object.

        isValid - True if the signature is valid and verified by GitHub.

        keyFingerprint - Hex-encoded fingerprint of the key that signed this object.

        payload - Payload for GPG signing object. Raw ODB object without the signature header.

        signature - ASCII-armored signature header from object.

        signer - GitHub user corresponding to the email signing this commit.

        state - The state of this signature. `VALID` if signature is valid and verified by
    GitHub, otherwise represents reason why signature is considered invalid.

        wasSignedByGitHub - True if the signature was made with GitHub's signing key.

    """

    email: str
    is_valid: bool
    key_fingerprint: Optional[str] = None
    payload: str
    signature: str
    signer: Optional[User] = None
    state: GitSignatureState
    was_signed_by_git_hub: bool


@dataclass(kw_only=True)
class SmimeSignature:
    """
        SmimeSignature - Represents an S/MIME signature on a Commit or Tag.

        email - Email used to sign this object.

        isValid - True if the signature is valid and verified by GitHub.

        payload - Payload for GPG signing object. Raw ODB object without the signature header.

        signature - ASCII-armored signature header from object.

        signer - GitHub user corresponding to the email signing this commit.

        state - The state of this signature. `VALID` if signature is valid and verified by
    GitHub, otherwise represents reason why signature is considered invalid.

        wasSignedByGitHub - True if the signature was made with GitHub's signing key.

    """

    email: str
    is_valid: bool
    payload: str
    signature: str
    signer: Optional[User] = None
    state: GitSignatureState
    was_signed_by_git_hub: bool


@dataclass(kw_only=True)
class SetUserInteractionLimitPayload:
    """
    SetUserInteractionLimitPayload - Autogenerated return type of SetUserInteractionLimit

    clientMutationId - A unique identifier for the client performing the mutation.

    user - The user that the interaction limit was set for.

    """

    client_mutation_id: Optional[str] = None
    user: Optional[User] = None


@dataclass(kw_only=True)
class SetRepositoryInteractionLimitPayload:
    """
    SetRepositoryInteractionLimitPayload - Autogenerated return type of SetRepositoryInteractionLimit

    clientMutationId - A unique identifier for the client performing the mutation.

    repository - The repository that the interaction limit was set for.

    """

    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class SetOrganizationInteractionLimitPayload:
    """
    SetOrganizationInteractionLimitPayload - Autogenerated return type of SetOrganizationInteractionLimit

    clientMutationId - A unique identifier for the client performing the mutation.

    organization - The organization that the interaction limit was set for.

    """

    client_mutation_id: Optional[str] = None
    organization: Optional[Organization] = None


@dataclass(kw_only=True)
class SetEnterpriseIdentityProviderPayload:
    """
    SetEnterpriseIdentityProviderPayload - Autogenerated return type of SetEnterpriseIdentityProvider

    clientMutationId - A unique identifier for the client performing the mutation.

    identityProvider - The identity provider for the enterprise.

    """

    client_mutation_id: Optional[str] = None
    identity_provider: Optional[EnterpriseIdentityProvider] = None


@dataclass(kw_only=True)
class RevokeEnterpriseOrganizationsMigratorRolePayload:
    """
    RevokeEnterpriseOrganizationsMigratorRolePayload - Autogenerated return type of RevokeEnterpriseOrganizationsMigratorRole

    clientMutationId - A unique identifier for the client performing the mutation.

    organizations - The organizations that had the migrator role revoked for the given user.

    """

    client_mutation_id: Optional[str] = None
    organizations: Optional[OrganizationConnection] = None


@dataclass(kw_only=True)
class RetireSponsorsTierPayload:
    """
    RetireSponsorsTierPayload - Autogenerated return type of RetireSponsorsTier

    clientMutationId - A unique identifier for the client performing the mutation.

    sponsorsTier - The tier that was retired.

    """

    client_mutation_id: Optional[str] = None
    sponsors_tier: Optional[SponsorsTier] = None


@dataclass(kw_only=True)
class ResolveReviewThreadPayload:
    """
    ResolveReviewThreadPayload - Autogenerated return type of ResolveReviewThread

    clientMutationId - A unique identifier for the client performing the mutation.

    thread - The thread to resolve.

    """

    client_mutation_id: Optional[str] = None
    thread: Optional[PullRequestReviewThread] = None


@dataclass(kw_only=True)
class RerequestCheckSuitePayload:
    """
    RerequestCheckSuitePayload - Autogenerated return type of RerequestCheckSuite

    checkSuite - The requested check suite.

    clientMutationId - A unique identifier for the client performing the mutation.

    """

    check_suite: Optional[CheckSuite] = None
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class RepositoryNode:
    """
    RepositoryNode - Represents a object that belongs to a repository.

    repository - The repository associated with this node.

    """

    repository: Repository


@dataclass(kw_only=True)
class RepositoryDiscussionCommentAuthor:
    """
    RepositoryDiscussionCommentAuthor - Represents an author of discussion comments in repositories.

    repositoryDiscussionComments - Discussion comments this user has authored.

    """

    repository_discussion_comments: DiscussionCommentConnection


@dataclass(kw_only=True)
class RepositoryDiscussionAuthor:
    """
    RepositoryDiscussionAuthor - Represents an author of discussions in repositories.

    repositoryDiscussions - Discussions this user has started.

    """

    repository_discussions: DiscussionConnection


@dataclass(kw_only=True)
class RepositoryAuditEntryData:
    """
    RepositoryAuditEntryData - Metadata for an audit entry with action repo.*

    repository - The repository associated with the action

    repositoryName - The name of the repository

    repositoryResourcePath - The HTTP path for the repository

    repositoryUrl - The HTTP URL for the repository

    """

    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None


@dataclass(kw_only=True)
class ReopenPullRequestPayload:
    """
    ReopenPullRequestPayload - Autogenerated return type of ReopenPullRequest

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequest - The pull request that was reopened.

    """

    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class ReopenIssuePayload:
    """
    ReopenIssuePayload - Autogenerated return type of ReopenIssue

    clientMutationId - A unique identifier for the client performing the mutation.

    issue - The issue that was opened.

    """

    client_mutation_id: Optional[str] = None
    issue: Optional[Issue] = None


@dataclass(kw_only=True)
class ReopenDiscussionPayload:
    """
    ReopenDiscussionPayload - Autogenerated return type of ReopenDiscussion

    clientMutationId - A unique identifier for the client performing the mutation.

    discussion - The discussion that was reopened.

    """

    client_mutation_id: Optional[str] = None
    discussion: Optional[Discussion] = None


@dataclass(kw_only=True)
class RemoveUpvotePayload:
    """
    RemoveUpvotePayload - Autogenerated return type of RemoveUpvote

    clientMutationId - A unique identifier for the client performing the mutation.

    subject - The votable subject.

    """

    client_mutation_id: Optional[str] = None
    subject: Optional[Votable] = None


@dataclass(kw_only=True)
class RemoveStarPayload:
    """
    RemoveStarPayload - Autogenerated return type of RemoveStar

    clientMutationId - A unique identifier for the client performing the mutation.

    starrable - The starrable.

    """

    client_mutation_id: Optional[str] = None
    starrable: Optional[Starrable] = None


@dataclass(kw_only=True)
class RemoveOutsideCollaboratorPayload:
    """
    RemoveOutsideCollaboratorPayload - Autogenerated return type of RemoveOutsideCollaborator

    clientMutationId - A unique identifier for the client performing the mutation.

    removedUser - The user that was removed as an outside collaborator.

    """

    client_mutation_id: Optional[str] = None
    removed_user: Optional[User] = None


@dataclass(kw_only=True)
class RemoveLabelsFromLabelablePayload:
    """
    RemoveLabelsFromLabelablePayload - Autogenerated return type of RemoveLabelsFromLabelable

    clientMutationId - A unique identifier for the client performing the mutation.

    labelable - The Labelable the labels were removed from.

    """

    client_mutation_id: Optional[str] = None
    labelable: Optional[Labelable] = None


@dataclass(kw_only=True)
class RemoveEnterpriseIdentityProviderPayload:
    """
    RemoveEnterpriseIdentityProviderPayload - Autogenerated return type of RemoveEnterpriseIdentityProvider

    clientMutationId - A unique identifier for the client performing the mutation.

    identityProvider - The identity provider that was removed from the enterprise.

    """

    client_mutation_id: Optional[str] = None
    identity_provider: Optional[EnterpriseIdentityProvider] = None


@dataclass(kw_only=True)
class RemoveAssigneesFromAssignablePayload:
    """
    RemoveAssigneesFromAssignablePayload - Autogenerated return type of RemoveAssigneesFromAssignable

    assignable - The item that was unassigned.

    clientMutationId - A unique identifier for the client performing the mutation.

    """

    assignable: Optional[Assignable] = None
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class RejectDeploymentsPayload:
    """
    RejectDeploymentsPayload - Autogenerated return type of RejectDeployments

    clientMutationId - A unique identifier for the client performing the mutation.

    deployments - The affected deployments.

    """

    client_mutation_id: Optional[str] = None
    deployments: Optional[list[Deployment]] = None


@dataclass(kw_only=True)
class RegenerateEnterpriseIdentityProviderRecoveryCodesPayload:
    """
    RegenerateEnterpriseIdentityProviderRecoveryCodesPayload - Autogenerated return type of RegenerateEnterpriseIdentityProviderRecoveryCodes

    clientMutationId - A unique identifier for the client performing the mutation.

    identityProvider - The identity provider for the enterprise.

    """

    client_mutation_id: Optional[str] = None
    identity_provider: Optional[EnterpriseIdentityProvider] = None


@dataclass(kw_only=True)
class PublishSponsorsTierPayload:
    """
    PublishSponsorsTierPayload - Autogenerated return type of PublishSponsorsTier

    clientMutationId - A unique identifier for the client performing the mutation.

    sponsorsTier - The tier that was published.

    """

    client_mutation_id: Optional[str] = None
    sponsors_tier: Optional[SponsorsTier] = None


@dataclass(kw_only=True)
class ProjectV2Recent:
    """
    ProjectV2Recent - Recent projects for the owner.

    recentProjects - Recent projects that this user has modified in the context of the owner.

    """

    recent_projects: ProjectV2Connection


@dataclass(kw_only=True)
class ProjectV2FieldCommon:
    """
    ProjectV2FieldCommon - Common fields across different project field types

    createdAt - Identifies the date and time when the object was created.

    dataType - The field's type.

    databaseId - Identifies the primary key from the database.

    id - The Node ID of the ProjectV2FieldCommon object

    name - The project field's name.

    project - The project that contains this field.

    updatedAt - Identifies the date and time when the object was last updated.

    """

    created_at: DateTime
    data_type: ProjectV2FieldType
    database_id: Optional[int] = None
    id: ID
    name: str
    project: ProjectV2
    updated_at: DateTime


@dataclass(kw_only=True)
class ProjectColumnImport:
    """
    ProjectColumnImport - A project column and a list of its issues and PRs.

    columnName - The name of the column.

    issues - A list of issues and pull requests in the column.

    position - The position of the column, starting from 0.

    """

    column_name: str
    issues: Optional[list[ProjectCardImport]] = None
    position: int


@dataclass(kw_only=True)
class PinIssuePayload:
    """
    PinIssuePayload - Autogenerated return type of PinIssue

    clientMutationId - A unique identifier for the client performing the mutation.

    issue - The issue that was pinned

    """

    client_mutation_id: Optional[str] = None
    issue: Optional[Issue] = None


@dataclass(kw_only=True)
class PackageTag:
    """
    PackageTag - A version tag contains the mapping between a tag name and a version.

    id - The Node ID of the PackageTag object

    name - Identifies the tag name of the version.

    version - Version that the tag is associated with.

    """

    id: ID
    name: str
    version: Optional[PackageVersion] = None


@dataclass(kw_only=True)
class PackageOwner:
    """
    PackageOwner - Represents an owner of a package.

    id - The Node ID of the PackageOwner object

    packages - A list of packages under the owner.

    """

    id: ID
    packages: PackageConnection


@dataclass(kw_only=True)
class OrganizationsHovercardContext:
    """
    OrganizationsHovercardContext - An organization list hovercard context

    message - A string describing this context

    octicon - An octicon to accompany this context

    relevantOrganizations - Organizations this user is a member of that are relevant

    totalOrganizationCount - The total number of organizations this user is in

    """

    message: str
    octicon: str
    relevant_organizations: OrganizationConnection
    total_organization_count: int


@dataclass(kw_only=True)
class OrganizationTeamsHovercardContext:
    """
    OrganizationTeamsHovercardContext - An organization teams hovercard context

    message - A string describing this context

    octicon - An octicon to accompany this context

    relevantTeams - Teams in this organization the user is a member of that are relevant

    teamsResourcePath - The path for the full team list for this user

    teamsUrl - The URL for the full team list for this user

    totalTeamCount - The total number of teams the user is on in the organization

    """

    message: str
    octicon: str
    relevant_teams: TeamConnection
    teams_resource_path: URI
    teams_url: URI
    total_team_count: int


@dataclass(kw_only=True)
class OrganizationAuditEntryData:
    """
    OrganizationAuditEntryData - Metadata for an audit entry with action org.*

    organization - The Organization associated with the Audit Entry.

    organizationName - The name of the Organization.

    organizationResourcePath - The HTTP path for the organization

    organizationUrl - The HTTP URL for the organization

    """

    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None


@dataclass(kw_only=True)
class MoveProjectColumnPayload:
    """
    MoveProjectColumnPayload - Autogenerated return type of MoveProjectColumn

    clientMutationId - A unique identifier for the client performing the mutation.

    columnEdge - The new edge of the moved column.

    """

    client_mutation_id: Optional[str] = None
    column_edge: Optional[ProjectColumnEdge] = None


@dataclass(kw_only=True)
class MoveProjectCardPayload:
    """
    MoveProjectCardPayload - Autogenerated return type of MoveProjectCard

    cardEdge - The new edge of the moved card.

    clientMutationId - A unique identifier for the client performing the mutation.

    """

    card_edge: Optional[ProjectCardEdge] = None
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class MinimizeCommentPayload:
    """
    MinimizeCommentPayload - Autogenerated return type of MinimizeComment

    clientMutationId - A unique identifier for the client performing the mutation.

    minimizedComment - The comment that was minimized.

    """

    client_mutation_id: Optional[str] = None
    minimized_comment: Optional[Minimizable] = None


@dataclass(kw_only=True)
class Migration:
    """
        Migration - Represents a GitHub Enterprise Importer (GEI) migration.

        continueOnError - The migration flag to continue on error.

        createdAt - Identifies the date and time when the object was created.

        databaseId - Identifies the primary key from the database.

        failureReason - The reason the migration failed.

        id - The Node ID of the Migration object

        migrationLogUrl - The URL for the migration log (expires 1 day after migration completes).

        migrationSource - The migration source.

        repositoryName - The target repository name.

        sourceUrl - The migration source URL, for example `https://github.com` or `https://monalisa.ghe.com`.

        state - The migration state.

        warningsCount - The number of warnings encountered for this migration. To review the warnings,
    check the [Migration Log](https://docs.github.com/migrations/using-github-enterprise-importer/completing-your-migration-with-github-enterprise-importer/accessing-your-migration-logs-for-github-enterprise-importer).

    """

    continue_on_error: bool
    created_at: DateTime
    database_id: Optional[str] = None
    failure_reason: Optional[str] = None
    id: ID
    migration_log_url: Optional[URI] = None
    migration_source: MigrationSource
    repository_name: str
    source_url: URI
    state: MigrationState
    warnings_count: int


@dataclass(kw_only=True)
class MergeBranchPayload:
    """
    MergeBranchPayload - Autogenerated return type of MergeBranch

    clientMutationId - A unique identifier for the client performing the mutation.

    mergeCommit - The resulting merge Commit.

    """

    client_mutation_id: Optional[str] = None
    merge_commit: Optional[Commit] = None


@dataclass(kw_only=True)
class MemberStatusable:
    """
    MemberStatusable - Entities that have members who can set status messages.

    memberStatuses - Get the status messages members of this entity have set that are either public or visible only to the organization.

    """

    member_statuses: UserStatusConnection


@dataclass(kw_only=True)
class MarkPullRequestReadyForReviewPayload:
    """
    MarkPullRequestReadyForReviewPayload - Autogenerated return type of MarkPullRequestReadyForReview

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequest - The pull request that is ready for review.

    """

    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class MarkProjectV2AsTemplatePayload:
    """
    MarkProjectV2AsTemplatePayload - Autogenerated return type of MarkProjectV2AsTemplate

    clientMutationId - A unique identifier for the client performing the mutation.

    projectV2 - The project.

    """

    client_mutation_id: Optional[str] = None
    project_v2: Optional[ProjectV2] = None


@dataclass(kw_only=True)
class MarkNotificationAsDonePayload:
    """
    MarkNotificationAsDonePayload - Autogenerated return type of MarkNotificationAsDone

    clientMutationId - A unique identifier for the client performing the mutation.

    success - Did the operation succeed?

    viewer - The user that the notification belongs to.

    """

    client_mutation_id: Optional[str] = None
    success: Optional[bool] = None
    viewer: Optional[User] = None


@dataclass(kw_only=True)
class MarkFileAsViewedPayload:
    """
    MarkFileAsViewedPayload - Autogenerated return type of MarkFileAsViewed

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequest - The updated pull request.

    """

    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class MarkDiscussionCommentAsAnswerPayload:
    """
    MarkDiscussionCommentAsAnswerPayload - Autogenerated return type of MarkDiscussionCommentAsAnswer

    clientMutationId - A unique identifier for the client performing the mutation.

    discussion - The discussion that includes the chosen comment.

    """

    client_mutation_id: Optional[str] = None
    discussion: Optional[Discussion] = None


@dataclass(kw_only=True)
class LinkProjectV2ToTeamPayload:
    """
    LinkProjectV2ToTeamPayload - Autogenerated return type of LinkProjectV2ToTeam

    clientMutationId - A unique identifier for the client performing the mutation.

    team - The team the project is linked to

    """

    client_mutation_id: Optional[str] = None
    team: Optional[Team] = None


@dataclass(kw_only=True)
class LinkProjectV2ToRepositoryPayload:
    """
    LinkProjectV2ToRepositoryPayload - Autogenerated return type of LinkProjectV2ToRepository

    clientMutationId - A unique identifier for the client performing the mutation.

    repository - The repository the project is linked to.

    """

    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class InviteEnterpriseAdminPayload:
    """
    InviteEnterpriseAdminPayload - Autogenerated return type of InviteEnterpriseAdmin

    clientMutationId - A unique identifier for the client performing the mutation.

    invitation - The created enterprise administrator invitation.

    """

    client_mutation_id: Optional[str] = None
    invitation: Optional[EnterpriseAdministratorInvitation] = None


@dataclass(kw_only=True)
class ImportProjectPayload:
    """
    ImportProjectPayload - Autogenerated return type of ImportProject

    clientMutationId - A unique identifier for the client performing the mutation.

    project - The new Project!

    """

    client_mutation_id: Optional[str] = None
    project: Optional[Project] = None


@dataclass(kw_only=True)
class ImportProjectInput:
    """
    ImportProjectInput - Autogenerated input type of ImportProject

    body - The description of Project.

    clientMutationId - A unique identifier for the client performing the mutation.

    columnImports - A list of columns containing issues and pull requests.

    name - The name of Project.

    ownerName - The name of the Organization or User to create the Project under.

    public - Whether the Project is public or not.

    """

    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    column_imports: list[ProjectColumnImport]
    name: str
    owner_name: str
    public: Optional[bool] = None


@dataclass(kw_only=True)
class GrantEnterpriseOrganizationsMigratorRolePayload:
    """
    GrantEnterpriseOrganizationsMigratorRolePayload - Autogenerated return type of GrantEnterpriseOrganizationsMigratorRole

    clientMutationId - A unique identifier for the client performing the mutation.

    organizations - The organizations that had the migrator role applied to for the given user.

    """

    client_mutation_id: Optional[str] = None
    organizations: Optional[OrganizationConnection] = None


@dataclass(kw_only=True)
class GpgSignature:
    """
        GpgSignature - Represents a GPG signature on a Commit or Tag.

        email - Email used to sign this object.

        isValid - True if the signature is valid and verified by GitHub.

        keyId - Hex-encoded ID of the key that signed this object.

        payload - Payload for GPG signing object. Raw ODB object without the signature header.

        signature - ASCII-armored signature header from object.

        signer - GitHub user corresponding to the email signing this commit.

        state - The state of this signature. `VALID` if signature is valid and verified by
    GitHub, otherwise represents reason why signature is considered invalid.

        wasSignedByGitHub - True if the signature was made with GitHub's signing key.

    """

    email: str
    is_valid: bool
    key_id: Optional[str] = None
    payload: str
    signature: str
    signer: Optional[User] = None
    state: GitSignatureState
    was_signed_by_git_hub: bool


@dataclass(kw_only=True)
class FollowUserPayload:
    """
    FollowUserPayload - Autogenerated return type of FollowUser

    clientMutationId - A unique identifier for the client performing the mutation.

    user - The user that was followed.

    """

    client_mutation_id: Optional[str] = None
    user: Optional[User] = None


@dataclass(kw_only=True)
class FollowOrganizationPayload:
    """
    FollowOrganizationPayload - Autogenerated return type of FollowOrganization

    clientMutationId - A unique identifier for the client performing the mutation.

    organization - The organization that was followed.

    """

    client_mutation_id: Optional[str] = None
    organization: Optional[Organization] = None


@dataclass(kw_only=True)
class EnqueuePullRequestPayload:
    """
    EnqueuePullRequestPayload - Autogenerated return type of EnqueuePullRequest

    clientMutationId - A unique identifier for the client performing the mutation.

    mergeQueueEntry - The merge queue entry for the enqueued pull request.

    """

    client_mutation_id: Optional[str] = None
    merge_queue_entry: Optional[MergeQueueEntry] = None


@dataclass(kw_only=True)
class DismissRepositoryVulnerabilityAlertPayload:
    """
    DismissRepositoryVulnerabilityAlertPayload - Autogenerated return type of DismissRepositoryVulnerabilityAlert

    clientMutationId - A unique identifier for the client performing the mutation.

    repositoryVulnerabilityAlert - The Dependabot alert that was dismissed

    """

    client_mutation_id: Optional[str] = None
    repository_vulnerability_alert: Optional[RepositoryVulnerabilityAlert] = None


@dataclass(kw_only=True)
class DismissPullRequestReviewPayload:
    """
    DismissPullRequestReviewPayload - Autogenerated return type of DismissPullRequestReview

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequestReview - The dismissed pull request review.

    """

    client_mutation_id: Optional[str] = None
    pull_request_review: Optional[PullRequestReview] = None


@dataclass(kw_only=True)
class DequeuePullRequestPayload:
    """
    DequeuePullRequestPayload - Autogenerated return type of DequeuePullRequest

    clientMutationId - A unique identifier for the client performing the mutation.

    mergeQueueEntry - The merge queue entry of the dequeued pull request.

    """

    client_mutation_id: Optional[str] = None
    merge_queue_entry: Optional[MergeQueueEntry] = None


@dataclass(kw_only=True)
class DeleteVerifiableDomainPayload:
    """
    DeleteVerifiableDomainPayload - Autogenerated return type of DeleteVerifiableDomain

    clientMutationId - A unique identifier for the client performing the mutation.

    owner - The owning account from which the domain was deleted.

    """

    client_mutation_id: Optional[str] = None
    owner: Optional[VerifiableDomainOwner] = None


@dataclass(kw_only=True)
class DeleteUserListPayload:
    """
    DeleteUserListPayload - Autogenerated return type of DeleteUserList

    clientMutationId - A unique identifier for the client performing the mutation.

    user - The owner of the list that will be deleted

    """

    client_mutation_id: Optional[str] = None
    user: Optional[User] = None


@dataclass(kw_only=True)
class DeletePullRequestReviewPayload:
    """
    DeletePullRequestReviewPayload - Autogenerated return type of DeletePullRequestReview

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequestReview - The deleted pull request review.

    """

    client_mutation_id: Optional[str] = None
    pull_request_review: Optional[PullRequestReview] = None


@dataclass(kw_only=True)
class DeleteProjectV2WorkflowPayload:
    """
    DeleteProjectV2WorkflowPayload - Autogenerated return type of DeleteProjectV2Workflow

    clientMutationId - A unique identifier for the client performing the mutation.

    deletedWorkflowId - The ID of the deleted workflow.

    projectV2 - The project the deleted workflow was in.

    """

    client_mutation_id: Optional[str] = None
    deleted_workflow_id: Optional[ID] = None
    project_v2: Optional[ProjectV2] = None


@dataclass(kw_only=True)
class DeleteProjectV2Payload:
    """
    DeleteProjectV2Payload - Autogenerated return type of DeleteProjectV2

    clientMutationId - A unique identifier for the client performing the mutation.

    projectV2 - The deleted Project.

    """

    client_mutation_id: Optional[str] = None
    project_v2: Optional[ProjectV2] = None


@dataclass(kw_only=True)
class DeleteProjectV2FieldPayload:
    """
    DeleteProjectV2FieldPayload - Autogenerated return type of DeleteProjectV2Field

    clientMutationId - A unique identifier for the client performing the mutation.

    projectV2Field - The deleted field.

    """

    client_mutation_id: Optional[str] = None
    project_v2_field: Optional[ProjectV2FieldConfiguration] = None


@dataclass(kw_only=True)
class DeleteProjectPayload:
    """
    DeleteProjectPayload - Autogenerated return type of DeleteProject

    clientMutationId - A unique identifier for the client performing the mutation.

    owner - The repository or organization the project was removed from.

    """

    client_mutation_id: Optional[str] = None
    owner: Optional[ProjectOwner] = None


@dataclass(kw_only=True)
class DeleteProjectColumnPayload:
    """
    DeleteProjectColumnPayload - Autogenerated return type of DeleteProjectColumn

    clientMutationId - A unique identifier for the client performing the mutation.

    deletedColumnId - The deleted column ID.

    project - The project the deleted column was in.

    """

    client_mutation_id: Optional[str] = None
    deleted_column_id: Optional[ID] = None
    project: Optional[Project] = None


@dataclass(kw_only=True)
class DeleteProjectCardPayload:
    """
    DeleteProjectCardPayload - Autogenerated return type of DeleteProjectCard

    clientMutationId - A unique identifier for the client performing the mutation.

    column - The column the deleted card was in.

    deletedCardId - The deleted card ID.

    """

    client_mutation_id: Optional[str] = None
    column: Optional[ProjectColumn] = None
    deleted_card_id: Optional[ID] = None


@dataclass(kw_only=True)
class DeleteLinkedBranchPayload:
    """
    DeleteLinkedBranchPayload - Autogenerated return type of DeleteLinkedBranch

    clientMutationId - A unique identifier for the client performing the mutation.

    issue - The issue the linked branch was unlinked from.

    """

    client_mutation_id: Optional[str] = None
    issue: Optional[Issue] = None


@dataclass(kw_only=True)
class DeleteIssuePayload:
    """
    DeleteIssuePayload - Autogenerated return type of DeleteIssue

    clientMutationId - A unique identifier for the client performing the mutation.

    repository - The repository the issue belonged to

    """

    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class DeleteIpAllowListEntryPayload:
    """
    DeleteIpAllowListEntryPayload - Autogenerated return type of DeleteIpAllowListEntry

    clientMutationId - A unique identifier for the client performing the mutation.

    ipAllowListEntry - The IP allow list entry that was deleted.

    """

    client_mutation_id: Optional[str] = None
    ip_allow_list_entry: Optional[IpAllowListEntry] = None


@dataclass(kw_only=True)
class DeleteDiscussionPayload:
    """
    DeleteDiscussionPayload - Autogenerated return type of DeleteDiscussion

    clientMutationId - A unique identifier for the client performing the mutation.

    discussion - The discussion that was just deleted.

    """

    client_mutation_id: Optional[str] = None
    discussion: Optional[Discussion] = None


@dataclass(kw_only=True)
class DeleteDiscussionCommentPayload:
    """
    DeleteDiscussionCommentPayload - Autogenerated return type of DeleteDiscussionComment

    clientMutationId - A unique identifier for the client performing the mutation.

    comment - The discussion comment that was just deleted.

    """

    client_mutation_id: Optional[str] = None
    comment: Optional[DiscussionComment] = None


@dataclass(kw_only=True)
class DeclineTopicSuggestionPayload:
    """
    DeclineTopicSuggestionPayload - Autogenerated return type of DeclineTopicSuggestion

    clientMutationId - A unique identifier for the client performing the mutation.

    """

    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class CreateTeamDiscussionPayload:
    """
    CreateTeamDiscussionPayload - Autogenerated return type of CreateTeamDiscussion

    clientMutationId - A unique identifier for the client performing the mutation.

    """

    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class CreateTeamDiscussionCommentPayload:
    """
    CreateTeamDiscussionCommentPayload - Autogenerated return type of CreateTeamDiscussionComment

    clientMutationId - A unique identifier for the client performing the mutation.

    """

    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class CreateSponsorshipsPayload:
    """
    CreateSponsorshipsPayload - Autogenerated return type of CreateSponsorships

    clientMutationId - A unique identifier for the client performing the mutation.

    sponsorables - The users and organizations who received a sponsorship.

    """

    client_mutation_id: Optional[str] = None
    sponsorables: Optional[list[Sponsorable]] = None


@dataclass(kw_only=True)
class CreateSponsorshipsInput:
    """
        CreateSponsorshipsInput - Autogenerated input type of CreateSponsorships

        clientMutationId - A unique identifier for the client performing the mutation.

        privacyLevel - Specify whether others should be able to see that the sponsor is sponsoring
    the sponsorables. Public visibility still does not reveal the dollar value of
    the sponsorship.

        receiveEmails - Whether the sponsor should receive email updates from the sponsorables.

        recurring - Whether the sponsorships created should continue each billing cycle for the
    sponsor (monthly or annually), versus lasting only a single month. Defaults to
    one-time sponsorships.

        sponsorLogin - The username of the user or organization who is acting as the sponsor, paying for the sponsorships.

        sponsorships - The list of maintainers to sponsor and for how much apiece.

    """

    client_mutation_id: Optional[str] = None
    privacy_level: Optional[SponsorshipPrivacy] = None
    receive_emails: Optional[bool] = None
    recurring: Optional[bool] = None
    sponsor_login: str
    sponsorships: list[BulkSponsorship]


@dataclass(kw_only=True)
class CreateSponsorshipPayload:
    """
    CreateSponsorshipPayload - Autogenerated return type of CreateSponsorship

    clientMutationId - A unique identifier for the client performing the mutation.

    sponsorship - The sponsorship that was started.

    """

    client_mutation_id: Optional[str] = None
    sponsorship: Optional[Sponsorship] = None


@dataclass(kw_only=True)
class CreateSponsorsTierPayload:
    """
    CreateSponsorsTierPayload - Autogenerated return type of CreateSponsorsTier

    clientMutationId - A unique identifier for the client performing the mutation.

    sponsorsTier - The new tier.

    """

    client_mutation_id: Optional[str] = None
    sponsors_tier: Optional[SponsorsTier] = None


@dataclass(kw_only=True)
class CreateSponsorsListingPayload:
    """
    CreateSponsorsListingPayload - Autogenerated return type of CreateSponsorsListing

    clientMutationId - A unique identifier for the client performing the mutation.

    sponsorsListing - The new GitHub Sponsors profile.

    """

    client_mutation_id: Optional[str] = None
    sponsors_listing: Optional[SponsorsListing] = None


@dataclass(kw_only=True)
class CreateRepositoryRulesetPayload:
    """
    CreateRepositoryRulesetPayload - Autogenerated return type of CreateRepositoryRuleset

    clientMutationId - A unique identifier for the client performing the mutation.

    ruleset - The newly created Ruleset.

    """

    client_mutation_id: Optional[str] = None
    ruleset: Optional[RepositoryRuleset] = None


@dataclass(kw_only=True)
class CreateRepositoryPayload:
    """
    CreateRepositoryPayload - Autogenerated return type of CreateRepository

    clientMutationId - A unique identifier for the client performing the mutation.

    repository - The new repository.

    """

    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class CreateRefPayload:
    """
    CreateRefPayload - Autogenerated return type of CreateRef

    clientMutationId - A unique identifier for the client performing the mutation.

    ref - The newly created ref.

    """

    client_mutation_id: Optional[str] = None
    ref: Optional[Ref] = None


@dataclass(kw_only=True)
class CreatePullRequestPayload:
    """
    CreatePullRequestPayload - Autogenerated return type of CreatePullRequest

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequest - The new pull request.

    """

    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class CreateProjectV2Payload:
    """
    CreateProjectV2Payload - Autogenerated return type of CreateProjectV2

    clientMutationId - A unique identifier for the client performing the mutation.

    projectV2 - The new project.

    """

    client_mutation_id: Optional[str] = None
    project_v2: Optional[ProjectV2] = None


@dataclass(kw_only=True)
class CreateProjectV2FieldPayload:
    """
    CreateProjectV2FieldPayload - Autogenerated return type of CreateProjectV2Field

    clientMutationId - A unique identifier for the client performing the mutation.

    projectV2Field - The new field.

    """

    client_mutation_id: Optional[str] = None
    project_v2_field: Optional[ProjectV2FieldConfiguration] = None


@dataclass(kw_only=True)
class CreateProjectV2FieldInput:
    """
    CreateProjectV2FieldInput - Autogenerated input type of CreateProjectV2Field

    clientMutationId - A unique identifier for the client performing the mutation.

    dataType - The data type of the field.

    name - The name of the field.

    projectId - The ID of the Project to create the field in.

    singleSelectOptions - Options for a single select field. At least one value is required if data_type is SINGLE_SELECT

    """

    client_mutation_id: Optional[str] = None
    data_type: ProjectV2CustomFieldType
    name: str
    project_id: ID
    single_select_options: Optional[list[ProjectV2SingleSelectFieldOptionInput]] = None


@dataclass(kw_only=True)
class CreateProjectPayload:
    """
    CreateProjectPayload - Autogenerated return type of CreateProject

    clientMutationId - A unique identifier for the client performing the mutation.

    project - The new project.

    """

    client_mutation_id: Optional[str] = None
    project: Optional[Project] = None


@dataclass(kw_only=True)
class CreateMigrationSourcePayload:
    """
    CreateMigrationSourcePayload - Autogenerated return type of CreateMigrationSource

    clientMutationId - A unique identifier for the client performing the mutation.

    migrationSource - The created migration source.

    """

    client_mutation_id: Optional[str] = None
    migration_source: Optional[MigrationSource] = None


@dataclass(kw_only=True)
class CreateLabelPayload:
    """
    CreateLabelPayload - Autogenerated return type of CreateLabel

    clientMutationId - A unique identifier for the client performing the mutation.

    label - The new label.

    """

    client_mutation_id: Optional[str] = None
    label: Optional[Label] = None


@dataclass(kw_only=True)
class CreateIssuePayload:
    """
    CreateIssuePayload - Autogenerated return type of CreateIssue

    clientMutationId - A unique identifier for the client performing the mutation.

    issue - The new issue.

    """

    client_mutation_id: Optional[str] = None
    issue: Optional[Issue] = None


@dataclass(kw_only=True)
class CreateIpAllowListEntryPayload:
    """
    CreateIpAllowListEntryPayload - Autogenerated return type of CreateIpAllowListEntry

    clientMutationId - A unique identifier for the client performing the mutation.

    ipAllowListEntry - The IP allow list entry that was created.

    """

    client_mutation_id: Optional[str] = None
    ip_allow_list_entry: Optional[IpAllowListEntry] = None


@dataclass(kw_only=True)
class CreateEnvironmentPayload:
    """
    CreateEnvironmentPayload - Autogenerated return type of CreateEnvironment

    clientMutationId - A unique identifier for the client performing the mutation.

    environment - The new or existing environment.

    """

    client_mutation_id: Optional[str] = None
    environment: Optional[Environment] = None


@dataclass(kw_only=True)
class CreateDiscussionPayload:
    """
    CreateDiscussionPayload - Autogenerated return type of CreateDiscussion

    clientMutationId - A unique identifier for the client performing the mutation.

    discussion - The discussion that was just created.

    """

    client_mutation_id: Optional[str] = None
    discussion: Optional[Discussion] = None


@dataclass(kw_only=True)
class CreateDeploymentStatusPayload:
    """
    CreateDeploymentStatusPayload - Autogenerated return type of CreateDeploymentStatus

    clientMutationId - A unique identifier for the client performing the mutation.

    deploymentStatus - The new deployment status.

    """

    client_mutation_id: Optional[str] = None
    deployment_status: Optional[DeploymentStatus] = None


@dataclass(kw_only=True)
class CreateDeploymentPayload:
    """
    CreateDeploymentPayload - Autogenerated return type of CreateDeployment

    autoMerged - True if the default branch has been auto-merged into the deployment ref.

    clientMutationId - A unique identifier for the client performing the mutation.

    deployment - The new deployment.

    """

    auto_merged: Optional[bool] = None
    client_mutation_id: Optional[str] = None
    deployment: Optional[Deployment] = None


@dataclass(kw_only=True)
class CreateCheckSuitePayload:
    """
    CreateCheckSuitePayload - Autogenerated return type of CreateCheckSuite

    checkSuite - The newly created check suite.

    clientMutationId - A unique identifier for the client performing the mutation.

    """

    check_suite: Optional[CheckSuite] = None
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class CreateCheckRunPayload:
    """
    CreateCheckRunPayload - Autogenerated return type of CreateCheckRun

    checkRun - The newly created check run.

    clientMutationId - A unique identifier for the client performing the mutation.

    """

    check_run: Optional[CheckRun] = None
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class CreateBranchProtectionRulePayload:
    """
    CreateBranchProtectionRulePayload - Autogenerated return type of CreateBranchProtectionRule

    branchProtectionRule - The newly created BranchProtectionRule.

    clientMutationId - A unique identifier for the client performing the mutation.

    """

    branch_protection_rule: Optional[BranchProtectionRule] = None
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class CreateBranchProtectionRuleInput:
    """
        CreateBranchProtectionRuleInput - Autogenerated input type of CreateBranchProtectionRule

        allowsDeletions - Can this branch be deleted.

        allowsForcePushes - Are force pushes allowed on this branch.

        blocksCreations - Is branch creation a protected operation.

        bypassForcePushActorIds - A list of User, Team, or App IDs allowed to bypass force push targeting matching branches.

        bypassPullRequestActorIds - A list of User, Team, or App IDs allowed to bypass pull requests targeting matching branches.

        clientMutationId - A unique identifier for the client performing the mutation.

        dismissesStaleReviews - Will new commits pushed to matching branches dismiss pull request review approvals.

        isAdminEnforced - Can admins override branch protection.

        lockAllowsFetchAndMerge - Whether users can pull changes from upstream when the branch is locked. Set to
    `true` to allow fork syncing. Set to `false` to prevent fork syncing.

        lockBranch - Whether to set the branch as read-only. If this is true, users will not be able to push to the branch.

        pattern - The glob-like pattern used to determine matching branches.

        pushActorIds - A list of User, Team, or App IDs allowed to push to matching branches.

        repositoryId - The global relay id of the repository in which a new branch protection rule should be created in.

        requireLastPushApproval - Whether the most recent push must be approved by someone other than the person who pushed it

        requiredApprovingReviewCount - Number of approving reviews required to update matching branches.

        requiredDeploymentEnvironments - The list of required deployment environments

        requiredStatusCheckContexts - List of required status check contexts that must pass for commits to be accepted to matching branches.

        requiredStatusChecks - The list of required status checks

        requiresApprovingReviews - Are approving reviews required to update matching branches.

        requiresCodeOwnerReviews - Are reviews from code owners required to update matching branches.

        requiresCommitSignatures - Are commits required to be signed.

        requiresConversationResolution - Are conversations required to be resolved before merging.

        requiresDeployments - Are successful deployments required before merging.

        requiresLinearHistory - Are merge commits prohibited from being pushed to this branch.

        requiresStatusChecks - Are status checks required to update matching branches.

        requiresStrictStatusChecks - Are branches required to be up to date before merging.

        restrictsPushes - Is pushing to matching branches restricted.

        restrictsReviewDismissals - Is dismissal of pull request reviews restricted.

        reviewDismissalActorIds - A list of User, Team, or App IDs allowed to dismiss reviews on pull requests targeting matching branches.

    """

    allows_deletions: Optional[bool] = None
    allows_force_pushes: Optional[bool] = None
    blocks_creations: Optional[bool] = None
    bypass_force_push_actor_ids: Optional[list[ID]] = None
    bypass_pull_request_actor_ids: Optional[list[ID]] = None
    client_mutation_id: Optional[str] = None
    dismisses_stale_reviews: Optional[bool] = None
    is_admin_enforced: Optional[bool] = None
    lock_allows_fetch_and_merge: Optional[bool] = None
    lock_branch: Optional[bool] = None
    pattern: str
    push_actor_ids: Optional[list[ID]] = None
    repository_id: ID
    require_last_push_approval: Optional[bool] = None
    required_approving_review_count: Optional[int] = None
    required_deployment_environments: Optional[list[str]] = None
    required_status_check_contexts: Optional[list[str]] = None
    required_status_checks: Optional[list[RequiredStatusCheckInput]] = None
    requires_approving_reviews: Optional[bool] = None
    requires_code_owner_reviews: Optional[bool] = None
    requires_commit_signatures: Optional[bool] = None
    requires_conversation_resolution: Optional[bool] = None
    requires_deployments: Optional[bool] = None
    requires_linear_history: Optional[bool] = None
    requires_status_checks: Optional[bool] = None
    requires_strict_status_checks: Optional[bool] = None
    restricts_pushes: Optional[bool] = None
    restricts_review_dismissals: Optional[bool] = None
    review_dismissal_actor_ids: Optional[list[ID]] = None


@dataclass(kw_only=True)
class CopyProjectV2Payload:
    """
    CopyProjectV2Payload - Autogenerated return type of CopyProjectV2

    clientMutationId - A unique identifier for the client performing the mutation.

    projectV2 - The copied project.

    """

    client_mutation_id: Optional[str] = None
    project_v2: Optional[ProjectV2] = None


@dataclass(kw_only=True)
class ConvertPullRequestToDraftPayload:
    """
    ConvertPullRequestToDraftPayload - Autogenerated return type of ConvertPullRequestToDraft

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequest - The pull request that is now a draft.

    """

    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class ConvertProjectCardNoteToIssuePayload:
    """
    ConvertProjectCardNoteToIssuePayload - Autogenerated return type of ConvertProjectCardNoteToIssue

    clientMutationId - A unique identifier for the client performing the mutation.

    projectCard - The updated ProjectCard.

    """

    client_mutation_id: Optional[str] = None
    project_card: Optional[ProjectCard] = None


@dataclass(kw_only=True)
class Contribution:
    """
        Contribution - Represents a contribution a user made on GitHub, such as opening an issue.

        isRestricted - Whether this contribution is associated with a record you do not have access to. For
    example, your own 'first issue' contribution may have been made on a repository you can no
    longer access.

        occurredAt - When this contribution was made.

        resourcePath - The HTTP path for this contribution.

        url - The HTTP URL for this contribution.

        user - The user who made this contribution.

    """

    is_restricted: bool
    occurred_at: DateTime
    resource_path: URI
    url: URI
    user: User


@dataclass(kw_only=True)
class ClosePullRequestPayload:
    """
    ClosePullRequestPayload - Autogenerated return type of ClosePullRequest

    clientMutationId - A unique identifier for the client performing the mutation.

    pullRequest - The pull request that was closed.

    """

    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class CloseIssuePayload:
    """
    CloseIssuePayload - Autogenerated return type of CloseIssue

    clientMutationId - A unique identifier for the client performing the mutation.

    issue - The issue that was closed.

    """

    client_mutation_id: Optional[str] = None
    issue: Optional[Issue] = None


@dataclass(kw_only=True)
class CloseDiscussionPayload:
    """
    CloseDiscussionPayload - Autogenerated return type of CloseDiscussion

    clientMutationId - A unique identifier for the client performing the mutation.

    discussion - The discussion that was closed.

    """

    client_mutation_id: Optional[str] = None
    discussion: Optional[Discussion] = None


@dataclass(kw_only=True)
class CloneTemplateRepositoryPayload:
    """
    CloneTemplateRepositoryPayload - Autogenerated return type of CloneTemplateRepository

    clientMutationId - A unique identifier for the client performing the mutation.

    repository - The new repository.

    """

    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class CloneProjectPayload:
    """
    CloneProjectPayload - Autogenerated return type of CloneProject

    clientMutationId - A unique identifier for the client performing the mutation.

    jobStatusId - The id of the JobStatus for populating cloned fields.

    project - The new cloned project.

    """

    client_mutation_id: Optional[str] = None
    job_status_id: Optional[str] = None
    project: Optional[Project] = None


@dataclass(kw_only=True)
class ClearProjectV2ItemFieldValuePayload:
    """
    ClearProjectV2ItemFieldValuePayload - Autogenerated return type of ClearProjectV2ItemFieldValue

    clientMutationId - A unique identifier for the client performing the mutation.

    projectV2Item - The updated item.

    """

    client_mutation_id: Optional[str] = None
    project_v2_item: Optional[ProjectV2Item] = None


@dataclass(kw_only=True)
class ClearLabelsFromLabelablePayload:
    """
    ClearLabelsFromLabelablePayload - Autogenerated return type of ClearLabelsFromLabelable

    clientMutationId - A unique identifier for the client performing the mutation.

    labelable - The item that was unlabeled.

    """

    client_mutation_id: Optional[str] = None
    labelable: Optional[Labelable] = None


@dataclass(kw_only=True)
class ChangeUserStatusPayload:
    """
    ChangeUserStatusPayload - Autogenerated return type of ChangeUserStatus

    clientMutationId - A unique identifier for the client performing the mutation.

    status - Your updated status.

    """

    client_mutation_id: Optional[str] = None
    status: Optional[UserStatus] = None


@dataclass(kw_only=True)
class CancelSponsorshipPayload:
    """
    CancelSponsorshipPayload - Autogenerated return type of CancelSponsorship

    clientMutationId - A unique identifier for the client performing the mutation.

    sponsorsTier - The tier that was being used at the time of cancellation.

    """

    client_mutation_id: Optional[str] = None
    sponsors_tier: Optional[SponsorsTier] = None


@dataclass(kw_only=True)
class CancelEnterpriseAdminInvitationPayload:
    """
    CancelEnterpriseAdminInvitationPayload - Autogenerated return type of CancelEnterpriseAdminInvitation

    clientMutationId - A unique identifier for the client performing the mutation.

    invitation - The invitation that was canceled.

    message - A message confirming the result of canceling an administrator invitation.

    """

    client_mutation_id: Optional[str] = None
    invitation: Optional[EnterpriseAdministratorInvitation] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class Blob:
    """
    Blob - Represents a Git blob.

    abbreviatedOid - An abbreviated version of the Git object ID

    byteSize - Byte size of Blob object

    commitResourcePath - The HTTP path for this Git object

    commitUrl - The HTTP URL for this Git object

    id - The Node ID of the Blob object

    isBinary - Indicates whether the Blob is binary or text. Returns null if unable to determine the encoding.

    isTruncated - Indicates whether the contents is truncated

    oid - The Git object ID

    repository - The Repository the Git object belongs to

    text - UTF8 text data or null if the Blob is binary

    """

    abbreviated_oid: str
    byte_size: int
    commit_resource_path: URI
    commit_url: URI
    id: ID
    is_binary: Optional[bool] = None
    is_truncated: bool
    oid: GitObjectID
    repository: Repository
    text: Optional[str] = None


@dataclass(kw_only=True)
class ArchiveRepositoryPayload:
    """
    ArchiveRepositoryPayload - Autogenerated return type of ArchiveRepository

    clientMutationId - A unique identifier for the client performing the mutation.

    repository - The repository that was marked as archived.

    """

    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class ArchiveProjectV2ItemPayload:
    """
    ArchiveProjectV2ItemPayload - Autogenerated return type of ArchiveProjectV2Item

    clientMutationId - A unique identifier for the client performing the mutation.

    item - The item archived from the project.

    """

    client_mutation_id: Optional[str] = None
    item: Optional[ProjectV2Item] = None


@dataclass(kw_only=True)
class ApproveVerifiableDomainPayload:
    """
    ApproveVerifiableDomainPayload - Autogenerated return type of ApproveVerifiableDomain

    clientMutationId - A unique identifier for the client performing the mutation.

    domain - The verifiable domain that was approved.

    """

    client_mutation_id: Optional[str] = None
    domain: Optional[VerifiableDomain] = None


@dataclass(kw_only=True)
class ApproveDeploymentsPayload:
    """
    ApproveDeploymentsPayload - Autogenerated return type of ApproveDeployments

    clientMutationId - A unique identifier for the client performing the mutation.

    deployments - The affected deployments.

    """

    client_mutation_id: Optional[str] = None
    deployments: Optional[list[Deployment]] = None


@dataclass(kw_only=True)
class AddVerifiableDomainPayload:
    """
    AddVerifiableDomainPayload - Autogenerated return type of AddVerifiableDomain

    clientMutationId - A unique identifier for the client performing the mutation.

    domain - The verifiable domain that was added.

    """

    client_mutation_id: Optional[str] = None
    domain: Optional[VerifiableDomain] = None


@dataclass(kw_only=True)
class AddUpvotePayload:
    """
    AddUpvotePayload - Autogenerated return type of AddUpvote

    clientMutationId - A unique identifier for the client performing the mutation.

    subject - The votable subject.

    """

    client_mutation_id: Optional[str] = None
    subject: Optional[Votable] = None


@dataclass(kw_only=True)
class AddStarPayload:
    """
    AddStarPayload - Autogenerated return type of AddStar

    clientMutationId - A unique identifier for the client performing the mutation.

    starrable - The starrable.

    """

    client_mutation_id: Optional[str] = None
    starrable: Optional[Starrable] = None


@dataclass(kw_only=True)
class AddPullRequestReviewThreadReplyPayload:
    """
    AddPullRequestReviewThreadReplyPayload - Autogenerated return type of AddPullRequestReviewThreadReply

    clientMutationId - A unique identifier for the client performing the mutation.

    comment - The newly created reply.

    """

    client_mutation_id: Optional[str] = None
    comment: Optional[PullRequestReviewComment] = None


@dataclass(kw_only=True)
class AddPullRequestReviewThreadPayload:
    """
    AddPullRequestReviewThreadPayload - Autogenerated return type of AddPullRequestReviewThread

    clientMutationId - A unique identifier for the client performing the mutation.

    thread - The newly created thread.

    """

    client_mutation_id: Optional[str] = None
    thread: Optional[PullRequestReviewThread] = None


@dataclass(kw_only=True)
class AddProjectV2ItemByIdPayload:
    """
    AddProjectV2ItemByIdPayload - Autogenerated return type of AddProjectV2ItemById

    clientMutationId - A unique identifier for the client performing the mutation.

    item - The item added to the project.

    """

    client_mutation_id: Optional[str] = None
    item: Optional[ProjectV2Item] = None


@dataclass(kw_only=True)
class AddProjectV2DraftIssuePayload:
    """
    AddProjectV2DraftIssuePayload - Autogenerated return type of AddProjectV2DraftIssue

    clientMutationId - A unique identifier for the client performing the mutation.

    projectItem - The draft issue added to the project.

    """

    client_mutation_id: Optional[str] = None
    project_item: Optional[ProjectV2Item] = None


@dataclass(kw_only=True)
class AddLabelsToLabelablePayload:
    """
    AddLabelsToLabelablePayload - Autogenerated return type of AddLabelsToLabelable

    clientMutationId - A unique identifier for the client performing the mutation.

    labelable - The item that was labeled.

    """

    client_mutation_id: Optional[str] = None
    labelable: Optional[Labelable] = None


@dataclass(kw_only=True)
class AddEnterpriseOrganizationMemberPayload:
    """
    AddEnterpriseOrganizationMemberPayload - Autogenerated return type of AddEnterpriseOrganizationMember

    clientMutationId - A unique identifier for the client performing the mutation.

    users - The users who were added to the organization.

    """

    client_mutation_id: Optional[str] = None
    users: Optional[list[User]] = None


@dataclass(kw_only=True)
class AddDiscussionPollVotePayload:
    """
    AddDiscussionPollVotePayload - Autogenerated return type of AddDiscussionPollVote

    clientMutationId - A unique identifier for the client performing the mutation.

    pollOption - The poll option that a vote was added to.

    """

    client_mutation_id: Optional[str] = None
    poll_option: Optional[DiscussionPollOption] = None


@dataclass(kw_only=True)
class AddDiscussionCommentPayload:
    """
    AddDiscussionCommentPayload - Autogenerated return type of AddDiscussionComment

    clientMutationId - A unique identifier for the client performing the mutation.

    comment - The newly created discussion comment.

    """

    client_mutation_id: Optional[str] = None
    comment: Optional[DiscussionComment] = None


@dataclass(kw_only=True)
class AddAssigneesToAssignablePayload:
    """
    AddAssigneesToAssignablePayload - Autogenerated return type of AddAssigneesToAssignable

    assignable - The item that was assigned.

    clientMutationId - A unique identifier for the client performing the mutation.

    """

    assignable: Optional[Assignable] = None
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class AcceptTopicSuggestionPayload:
    """
    AcceptTopicSuggestionPayload - Autogenerated return type of AcceptTopicSuggestion

    clientMutationId - A unique identifier for the client performing the mutation.

    """

    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class AcceptEnterpriseAdministratorInvitationPayload:
    """
    AcceptEnterpriseAdministratorInvitationPayload - Autogenerated return type of AcceptEnterpriseAdministratorInvitation

    clientMutationId - A unique identifier for the client performing the mutation.

    invitation - The invitation that was accepted.

    message - A message confirming the result of accepting an administrator invitation.

    """

    client_mutation_id: Optional[str] = None
    invitation: Optional[EnterpriseAdministratorInvitation] = None
    message: Optional[str] = None
