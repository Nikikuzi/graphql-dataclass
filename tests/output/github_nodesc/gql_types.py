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
    client_mutation_id: Optional[str] = None
    success: Optional[bool] = None


@dataclass(kw_only=True)
class AbortRepositoryMigrationPayload:
    client_mutation_id: Optional[str] = None
    success: Optional[bool] = None


@dataclass(kw_only=True)
class AcceptTopicSuggestionInput:
    client_mutation_id: Optional[str] = None
    name: Optional[str] = None
    repository_id: Optional[ID] = None


@dataclass(kw_only=True)
class ActorLocation:
    city: Optional[str] = None
    country: Optional[str] = None
    country_code: Optional[str] = None
    region: Optional[str] = None
    region_code: Optional[str] = None


@dataclass(kw_only=True)
class AddCommentInput:
    body: str
    client_mutation_id: Optional[str] = None
    subject_id: ID


@dataclass(kw_only=True)
class AddDiscussionPollVoteInput:
    client_mutation_id: Optional[str] = None
    poll_option_id: ID


@dataclass(kw_only=True)
class AddEnterpriseSupportEntitlementInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    login: str


@dataclass(kw_only=True)
class AddLabelsToLabelableInput:
    client_mutation_id: Optional[str] = None
    label_ids: list[ID]
    labelable_id: ID


@dataclass(kw_only=True)
class AddProjectColumnInput:
    client_mutation_id: Optional[str] = None
    name: str
    project_id: ID


@dataclass(kw_only=True)
class AddProjectV2ItemByIdInput:
    client_mutation_id: Optional[str] = None
    content_id: ID
    project_id: ID


@dataclass(kw_only=True)
class AddPullRequestReviewThreadInput:
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
    client_mutation_id: Optional[str] = None
    content: ReactionContent
    subject_id: ID


@dataclass(kw_only=True)
class AddUpvoteInput:
    client_mutation_id: Optional[str] = None
    subject_id: ID


@dataclass(kw_only=True)
class AnnouncementBanner:
    announcement: Optional[str] = None
    announcement_expires_at: Optional[DateTime] = None
    announcement_user_dismissible: Optional[bool] = None


@dataclass(kw_only=True)
class ApproveVerifiableDomainInput:
    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class ArchiveRepositoryInput:
    client_mutation_id: Optional[str] = None
    repository_id: ID


@dataclass(kw_only=True)
class Bot:
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
    name: Optional[str] = None
    negate: Optional[bool] = None
    operator: str
    pattern: str


@dataclass(kw_only=True)
class CVSS:
    score: float
    vector_string: Optional[str] = None


@dataclass(kw_only=True)
class CancelEnterpriseAdminInvitationInput:
    client_mutation_id: Optional[str] = None
    invitation_id: ID


@dataclass(kw_only=True)
class ChangeUserStatusInput:
    client_mutation_id: Optional[str] = None
    emoji: Optional[str] = None
    expires_at: Optional[DateTime] = None
    limited_availability: Optional[bool] = None
    message: Optional[str] = None
    organization_id: Optional[ID] = None


@dataclass(kw_only=True)
class CheckAnnotationRange:
    end_column: Optional[int] = None
    end_line: int
    start_column: Optional[int] = None
    start_line: int


@dataclass(kw_only=True)
class CheckRunFilter:
    app_id: Optional[int] = None
    check_name: Optional[str] = None
    check_type: Optional[CheckRunType] = None
    conclusions: Optional[list[CheckConclusionState]] = None
    status: Optional[CheckStatusState] = None
    statuses: Optional[list[CheckStatusState]] = None


@dataclass(kw_only=True)
class CheckRunStateCount:
    count: int
    state: CheckRunState


@dataclass(kw_only=True)
class CheckSuiteAutoTriggerPreference:
    app_id: ID
    setting: bool


@dataclass(kw_only=True)
class ClearLabelsFromLabelableInput:
    client_mutation_id: Optional[str] = None
    labelable_id: ID


@dataclass(kw_only=True)
class CloneProjectInput:
    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    include_workflows: bool
    name: str
    public: Optional[bool] = None
    source_id: ID
    target_owner_id: ID


@dataclass(kw_only=True)
class Closable:
    closed: bool
    closed_at: Optional[DateTime] = None
    viewer_can_close: bool
    viewer_can_reopen: bool


@dataclass(kw_only=True)
class CloseIssueInput:
    client_mutation_id: Optional[str] = None
    issue_id: ID
    state_reason: Optional[IssueClosedStateReason] = None


@dataclass(kw_only=True)
class CodeOfConduct:
    body: Optional[str] = None
    id: ID
    key: str
    name: str
    resource_path: Optional[URI] = None
    url: Optional[URI] = None


@dataclass(kw_only=True)
class CommitAuthorEmailPatternParameters:
    name: Optional[str] = None
    negate: bool
    operator: str
    pattern: str


@dataclass(kw_only=True)
class CommitContributionOrder:
    direction: OrderDirection
    field: CommitContributionOrderField


@dataclass(kw_only=True)
class CommitMessagePatternParameters:
    name: Optional[str] = None
    negate: bool
    operator: str
    pattern: str


@dataclass(kw_only=True)
class CommittableBranch:
    branch_name: Optional[str] = None
    id: Optional[ID] = None
    repository_name_with_owner: Optional[str] = None


@dataclass(kw_only=True)
class CommitterEmailPatternParametersInput:
    name: Optional[str] = None
    negate: Optional[bool] = None
    operator: str
    pattern: str


@dataclass(kw_only=True)
class ContributionCalendarDay:
    color: str
    contribution_count: int
    contribution_level: ContributionLevel
    date: Date
    weekday: int


@dataclass(kw_only=True)
class ContributionOrder:
    direction: OrderDirection


@dataclass(kw_only=True)
class ConvertPullRequestToDraftInput:
    client_mutation_id: Optional[str] = None
    pull_request_id: ID


@dataclass(kw_only=True)
class CreateAttributionInvitationInput:
    client_mutation_id: Optional[str] = None
    owner_id: ID
    source_id: ID
    target_id: ID


@dataclass(kw_only=True)
class CreateDeploymentInput:
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
    body: str
    category_id: ID
    client_mutation_id: Optional[str] = None
    repository_id: ID
    title: str


@dataclass(kw_only=True)
class CreateEnvironmentInput:
    client_mutation_id: Optional[str] = None
    name: str
    repository_id: ID


@dataclass(kw_only=True)
class CreateIssueInput:
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
    client_mutation_id: Optional[str] = None
    issue_id: ID
    name: Optional[str] = None
    oid: GitObjectID
    repository_id: Optional[ID] = None


@dataclass(kw_only=True)
class CreateProjectInput:
    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    name: str
    owner_id: ID
    repository_ids: Optional[list[ID]] = None
    template: Optional[ProjectTemplate] = None


@dataclass(kw_only=True)
class CreatePullRequestInput:
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
    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    discussion_id: Optional[ID] = None


@dataclass(kw_only=True)
class CreateUserListInput:
    client_mutation_id: Optional[str] = None
    description: Optional[str] = None
    is_private: Optional[bool] = None
    name: str


@dataclass(kw_only=True)
class Deletable:
    viewer_can_delete: bool


@dataclass(kw_only=True)
class DeleteBranchProtectionRulePayload:
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class DeleteDeploymentPayload:
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class DeleteDiscussionInput:
    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class DeleteEnvironmentPayload:
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class DeleteIssueCommentInput:
    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class DeleteIssueInput:
    client_mutation_id: Optional[str] = None
    issue_id: ID


@dataclass(kw_only=True)
class DeleteLabelPayload:
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class DeletePackageVersionInput:
    client_mutation_id: Optional[str] = None
    package_version_id: ID


@dataclass(kw_only=True)
class DeleteProjectCardInput:
    card_id: ID
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class DeleteProjectInput:
    client_mutation_id: Optional[str] = None
    project_id: ID


@dataclass(kw_only=True)
class DeleteProjectV2Input:
    client_mutation_id: Optional[str] = None
    project_id: ID


@dataclass(kw_only=True)
class DeleteProjectV2ItemPayload:
    client_mutation_id: Optional[str] = None
    deleted_item_id: Optional[ID] = None


@dataclass(kw_only=True)
class DeletePullRequestReviewCommentInput:
    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class DeleteRefInput:
    client_mutation_id: Optional[str] = None
    ref_id: ID


@dataclass(kw_only=True)
class DeleteRepositoryRulesetInput:
    client_mutation_id: Optional[str] = None
    repository_ruleset_id: ID


@dataclass(kw_only=True)
class DeleteTeamDiscussionCommentInput:
    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class DeleteTeamDiscussionInput:
    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class DeleteUserListInput:
    client_mutation_id: Optional[str] = None
    list_id: ID


@dataclass(kw_only=True)
class DependabotUpdateError:
    body: str
    error_type: str
    title: str


@dataclass(kw_only=True)
class DeploymentOrder:
    direction: OrderDirection
    field: DeploymentOrderField


@dataclass(kw_only=True)
class DisablePullRequestAutoMergeInput:
    client_mutation_id: Optional[str] = None
    pull_request_id: ID


@dataclass(kw_only=True)
class DiscussionPollOptionOrder:
    direction: OrderDirection
    field: DiscussionPollOptionOrderField


@dataclass(kw_only=True)
class DismissRepositoryVulnerabilityAlertInput:
    client_mutation_id: Optional[str] = None
    dismiss_reason: DismissReason
    repository_vulnerability_alert_id: ID


@dataclass(kw_only=True)
class DraftPullRequestReviewThread:
    body: str
    line: int
    path: str
    side: Optional[DiffSide] = None
    start_line: Optional[int] = None
    start_side: Optional[DiffSide] = None


@dataclass(kw_only=True)
class EnqueuePullRequestInput:
    client_mutation_id: Optional[str] = None
    expected_head_oid: Optional[GitObjectID] = None
    jump: Optional[bool] = None
    pull_request_id: ID


@dataclass(kw_only=True)
class EnterpriseAuditEntryData:
    enterprise_resource_path: Optional[URI] = None
    enterprise_slug: Optional[str] = None
    enterprise_url: Optional[URI] = None


@dataclass(kw_only=True)
class EnterpriseMemberOrder:
    direction: OrderDirection
    field: EnterpriseMemberOrderField


@dataclass(kw_only=True)
class EnterpriseRepositoryInfo:
    id: ID
    is_private: bool
    name: str
    name_with_owner: str


@dataclass(kw_only=True)
class EnterpriseServerUserAccountEmailOrder:
    direction: OrderDirection
    field: EnterpriseServerUserAccountEmailOrderField


@dataclass(kw_only=True)
class EnterpriseServerUserAccountsUploadOrder:
    direction: OrderDirection
    field: EnterpriseServerUserAccountsUploadOrderField


@dataclass(kw_only=True)
class ExternalIdentityAttribute:
    metadata: Optional[str] = None
    name: str
    value: str


@dataclass(kw_only=True)
class FileDeletion:
    path: str


@dataclass(kw_only=True)
class FollowUserInput:
    client_mutation_id: Optional[str] = None
    user_id: ID


@dataclass(kw_only=True)
class GenericHovercardContext:
    message: str
    octicon: str


@dataclass(kw_only=True)
class GitHubMetadata:
    git_hub_services_sha: GitObjectID
    git_ip_addresses: Optional[list[str]] = None
    github_enterprise_importer_ip_addresses: Optional[list[str]] = None
    hook_ip_addresses: Optional[list[str]] = None
    importer_ip_addresses: Optional[list[str]] = None
    is_password_authentication_verifiable: bool
    pages_ip_addresses: Optional[list[str]] = None


@dataclass(kw_only=True)
class GrantMigratorRoleInput:
    actor: str
    actor_type: ActorType
    client_mutation_id: Optional[str] = None
    organization_id: ID


@dataclass(kw_only=True)
class HovercardContext:
    message: str
    octicon: str


@dataclass(kw_only=True)
class IpAllowListEntryOrder:
    direction: OrderDirection
    field: IpAllowListEntryOrderField


@dataclass(kw_only=True)
class IssueFilters:
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
    direction: OrderDirection
    field: LabelOrderField


@dataclass(kw_only=True)
class LanguageOrder:
    direction: OrderDirection
    field: LanguageOrderField


@dataclass(kw_only=True)
class LinkProjectV2ToRepositoryInput:
    client_mutation_id: Optional[str] = None
    project_id: ID
    repository_id: ID


@dataclass(kw_only=True)
class LinkRepositoryToProjectInput:
    client_mutation_id: Optional[str] = None
    project_id: ID
    repository_id: ID


@dataclass(kw_only=True)
class Lockable:
    active_lock_reason: Optional[LockReason] = None
    locked: bool


@dataclass(kw_only=True)
class MarkDiscussionCommentAsAnswerInput:
    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class MarkNotificationAsDoneInput:
    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class MarkPullRequestReadyForReviewInput:
    client_mutation_id: Optional[str] = None
    pull_request_id: ID


@dataclass(kw_only=True)
class MemberFeatureRequestNotification:
    body: str
    id: ID
    title: str
    updated_at: DateTime


@dataclass(kw_only=True)
class MergePullRequestInput:
    author_email: Optional[str] = None
    client_mutation_id: Optional[str] = None
    commit_body: Optional[str] = None
    commit_headline: Optional[str] = None
    expected_head_oid: Optional[GitObjectID] = None
    merge_method: Optional[PullRequestMergeMethod] = None
    pull_request_id: ID


@dataclass(kw_only=True)
class MigrationSource:
    id: ID
    name: str
    type: MigrationSourceType
    url: URI


@dataclass(kw_only=True)
class Minimizable:
    is_minimized: bool
    minimized_reason: Optional[str] = None
    viewer_can_minimize: bool


@dataclass(kw_only=True)
class MoveProjectCardInput:
    after_card_id: Optional[ID] = None
    card_id: ID
    client_mutation_id: Optional[str] = None
    column_id: ID


@dataclass(kw_only=True)
class Node:
    id: ID


@dataclass(kw_only=True)
class OrgEnterpriseOwnerOrder:
    direction: OrderDirection
    field: OrgEnterpriseOwnerOrderField


@dataclass(kw_only=True)
class OrganizationOrder:
    direction: OrderDirection
    field: OrganizationOrderField


@dataclass(kw_only=True)
class PackageOrder:
    direction: Optional[OrderDirection] = None
    field: Optional[PackageOrderField] = None


@dataclass(kw_only=True)
class PackageVersionOrder:
    direction: Optional[OrderDirection] = None
    field: Optional[PackageVersionOrderField] = None


@dataclass(kw_only=True)
class PageInfo:
    end_cursor: Optional[str] = None
    has_next_page: bool
    has_previous_page: bool
    start_cursor: Optional[str] = None


@dataclass(kw_only=True)
class ProjectCardImport:
    number: int
    repository: str


@dataclass(kw_only=True)
class ProjectProgress:
    done_count: int
    done_percentage: float
    enabled: bool
    in_progress_count: int
    in_progress_percentage: float
    todo_count: int
    todo_percentage: float


@dataclass(kw_only=True)
class ProjectV2FieldOrder:
    direction: OrderDirection
    field: ProjectV2FieldOrderField


@dataclass(kw_only=True)
class ProjectV2Filters:
    state: Optional[ProjectV2State] = None


@dataclass(kw_only=True)
class ProjectV2ItemOrder:
    direction: OrderDirection
    field: ProjectV2ItemOrderField


@dataclass(kw_only=True)
class ProjectV2Order:
    direction: OrderDirection
    field: ProjectV2OrderField


@dataclass(kw_only=True)
class ProjectV2SingleSelectFieldOptionInput:
    color: ProjectV2SingleSelectFieldOptionColor
    description: str
    name: str


@dataclass(kw_only=True)
class ProjectV2WorkflowOrder:
    direction: OrderDirection
    field: ProjectV2WorkflowsOrderField


@dataclass(kw_only=True)
class PropertyTargetDefinitionInput:
    name: str
    property_values: list[str]


@dataclass(kw_only=True)
class PublishSponsorsTierInput:
    client_mutation_id: Optional[str] = None
    tier_id: ID


@dataclass(kw_only=True)
class PullRequestOrder:
    direction: OrderDirection
    field: PullRequestOrderField


@dataclass(kw_only=True)
class PullRequestParametersInput:
    dismiss_stale_reviews_on_push: bool
    require_code_owner_review: bool
    require_last_push_approval: bool
    required_approving_review_count: int
    required_review_thread_resolution: bool


@dataclass(kw_only=True)
class ReactionOrder:
    direction: OrderDirection
    field: ReactionOrderField


@dataclass(kw_only=True)
class RefNameConditionTargetInput:
    exclude: list[str]
    include: list[str]


@dataclass(kw_only=True)
class RefUpdate:
    after_oid: GitObjectID
    before_oid: Optional[GitObjectID] = None
    force: Optional[bool] = None
    name: GitRefname


@dataclass(kw_only=True)
class RegenerateEnterpriseIdentityProviderRecoveryCodesInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID


@dataclass(kw_only=True)
class RegenerateVerifiableDomainTokenPayload:
    client_mutation_id: Optional[str] = None
    verification_token: Optional[str] = None


@dataclass(kw_only=True)
class ReleaseOrder:
    direction: OrderDirection
    field: ReleaseOrderField


@dataclass(kw_only=True)
class RemoveEnterpriseAdminInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    login: str


@dataclass(kw_only=True)
class RemoveEnterpriseMemberInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    user_id: ID


@dataclass(kw_only=True)
class RemoveEnterpriseSupportEntitlementInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    login: str


@dataclass(kw_only=True)
class RemoveLabelsFromLabelableInput:
    client_mutation_id: Optional[str] = None
    label_ids: list[ID]
    labelable_id: ID


@dataclass(kw_only=True)
class RemoveReactionInput:
    client_mutation_id: Optional[str] = None
    content: ReactionContent
    subject_id: ID


@dataclass(kw_only=True)
class RemoveUpvoteInput:
    client_mutation_id: Optional[str] = None
    subject_id: ID


@dataclass(kw_only=True)
class ReopenIssueInput:
    client_mutation_id: Optional[str] = None
    issue_id: ID


@dataclass(kw_only=True)
class RepositoryCodeownersError:
    column: int
    kind: str
    line: int
    message: str
    path: str
    source: str
    suggestion: Optional[str] = None


@dataclass(kw_only=True)
class RepositoryIdConditionTarget:
    repository_ids: list[ID]


@dataclass(kw_only=True)
class RepositoryInteractionAbility:
    expires_at: Optional[DateTime] = None
    limit: RepositoryInteractionLimit
    origin: RepositoryInteractionLimitOrigin


@dataclass(kw_only=True)
class RepositoryMigrationOrder:
    direction: RepositoryMigrationOrderDirection
    field: RepositoryMigrationOrderField


@dataclass(kw_only=True)
class RepositoryNameConditionTargetInput:
    exclude: list[str]
    include: list[str]
    protected: Optional[bool] = None


@dataclass(kw_only=True)
class RepositoryRuleOrder:
    direction: OrderDirection
    field: RepositoryRuleOrderField


@dataclass(kw_only=True)
class RequestReviewsInput:
    client_mutation_id: Optional[str] = None
    pull_request_id: ID
    team_ids: Optional[list[ID]] = None
    union: Optional[bool] = None
    user_ids: Optional[list[ID]] = None


@dataclass(kw_only=True)
class RequiredDeploymentsParameters:
    required_deployment_environments: list[str]


@dataclass(kw_only=True)
class RequiredStatusCheckInput:
    app_id: Optional[ID] = None
    context: str


@dataclass(kw_only=True)
class ResolveReviewThreadInput:
    client_mutation_id: Optional[str] = None
    thread_id: ID


@dataclass(kw_only=True)
class RevertPullRequestInput:
    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    draft: Optional[bool] = None
    pull_request_id: ID
    title: Optional[str] = None


@dataclass(kw_only=True)
class RevokeEnterpriseOrganizationsMigratorRoleInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    login: str


@dataclass(kw_only=True)
class RevokeMigratorRolePayload:
    client_mutation_id: Optional[str] = None
    success: Optional[bool] = None


@dataclass(kw_only=True)
class SecurityAdvisoryIdentifier:
    type: str
    value: str


@dataclass(kw_only=True)
class SecurityAdvisoryOrder:
    direction: OrderDirection
    field: SecurityAdvisoryOrderField


@dataclass(kw_only=True)
class SecurityAdvisoryPackageVersion:
    identifier: str


@dataclass(kw_only=True)
class SecurityVulnerabilityOrder:
    direction: OrderDirection
    field: SecurityVulnerabilityOrderField


@dataclass(kw_only=True)
class SetOrganizationInteractionLimitInput:
    client_mutation_id: Optional[str] = None
    expiry: Optional[RepositoryInteractionLimitExpiry] = None
    limit: RepositoryInteractionLimit
    organization_id: ID


@dataclass(kw_only=True)
class SetUserInteractionLimitInput:
    client_mutation_id: Optional[str] = None
    expiry: Optional[RepositoryInteractionLimitExpiry] = None
    limit: RepositoryInteractionLimit
    user_id: ID


@dataclass(kw_only=True)
class SponsorAndLifetimeValueOrder:
    direction: OrderDirection
    field: SponsorAndLifetimeValueOrderField


@dataclass(kw_only=True)
class SponsorableOrder:
    direction: OrderDirection
    field: SponsorableOrderField


@dataclass(kw_only=True)
class SponsorsGoal:
    description: Optional[str] = None
    kind: SponsorsGoalKind
    percent_complete: int
    target_value: int
    title: str


@dataclass(kw_only=True)
class SponsorshipNewsletterOrder:
    direction: OrderDirection
    field: SponsorshipNewsletterOrderField


@dataclass(kw_only=True)
class StarOrder:
    direction: OrderDirection
    field: StarOrderField


@dataclass(kw_only=True)
class StartRepositoryMigrationInput:
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
    context: str
    integration_id: Optional[int] = None


@dataclass(kw_only=True)
class SubmitPullRequestReviewInput:
    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    event: PullRequestReviewEvent
    pull_request_id: Optional[ID] = None
    pull_request_review_id: Optional[ID] = None


@dataclass(kw_only=True)
class Subscribable:
    id: ID
    viewer_can_subscribe: bool
    viewer_subscription: Optional[SubscriptionState] = None


@dataclass(kw_only=True)
class TagNamePatternParameters:
    name: Optional[str] = None
    negate: bool
    operator: str
    pattern: str


@dataclass(kw_only=True)
class TeamDiscussionCommentOrder:
    direction: OrderDirection
    field: TeamDiscussionCommentOrderField


@dataclass(kw_only=True)
class TeamMemberOrder:
    direction: OrderDirection
    field: TeamMemberOrderField


@dataclass(kw_only=True)
class TeamRepositoryOrder:
    direction: OrderDirection
    field: TeamRepositoryOrderField


@dataclass(kw_only=True)
class TransferEnterpriseOrganizationInput:
    client_mutation_id: Optional[str] = None
    destination_enterprise_id: ID
    organization_id: ID


@dataclass(kw_only=True)
class UnarchiveProjectV2ItemInput:
    client_mutation_id: Optional[str] = None
    item_id: ID
    project_id: ID


@dataclass(kw_only=True)
class UnfollowOrganizationInput:
    client_mutation_id: Optional[str] = None
    organization_id: ID


@dataclass(kw_only=True)
class UniformResourceLocatable:
    resource_path: URI
    url: URI


@dataclass(kw_only=True)
class UnlinkProjectV2FromTeamInput:
    client_mutation_id: Optional[str] = None
    project_id: ID
    team_id: ID


@dataclass(kw_only=True)
class UnlockLockableInput:
    client_mutation_id: Optional[str] = None
    lockable_id: ID


@dataclass(kw_only=True)
class UnmarkFileAsViewedInput:
    client_mutation_id: Optional[str] = None
    path: str
    pull_request_id: ID


@dataclass(kw_only=True)
class UnmarkProjectV2AsTemplateInput:
    client_mutation_id: Optional[str] = None
    project_id: ID


@dataclass(kw_only=True)
class UnpinIssueInput:
    client_mutation_id: Optional[str] = None
    issue_id: ID


@dataclass(kw_only=True)
class UnsubscribeFromNotificationsInput:
    client_mutation_id: Optional[str] = None
    ids: list[ID]


@dataclass(kw_only=True)
class Updatable:
    viewer_can_update: bool


@dataclass(kw_only=True)
class UpdateDiscussionCommentInput:
    body: str
    client_mutation_id: Optional[str] = None
    comment_id: ID


@dataclass(kw_only=True)
class UpdateEnterpriseAdministratorRoleInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    login: str
    role: EnterpriseAdministratorRole


@dataclass(kw_only=True)
class UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    policy_value: Optional[EnterpriseAllowPrivateRepositoryForkingPolicyValue] = None
    setting_value: EnterpriseEnabledDisabledSettingValue


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    setting_value: EnterpriseEnabledDisabledSettingValue


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanDeleteIssuesSettingInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    setting_value: EnterpriseEnabledDisabledSettingValue


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    setting_value: EnterpriseEnabledDisabledSettingValue


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    setting_value: EnterpriseEnabledDisabledSettingValue


@dataclass(kw_only=True)
class UpdateEnterpriseOrganizationProjectsSettingInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    setting_value: EnterpriseEnabledDisabledSettingValue


@dataclass(kw_only=True)
class UpdateEnterpriseOwnerOrganizationRolePayload:
    client_mutation_id: Optional[str] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseRepositoryProjectsSettingInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    setting_value: EnterpriseEnabledDisabledSettingValue


@dataclass(kw_only=True)
class UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    setting_value: EnterpriseEnabledSettingValue


@dataclass(kw_only=True)
class UpdateIpAllowListEnabledSettingInput:
    client_mutation_id: Optional[str] = None
    owner_id: ID
    setting_value: IpAllowListEnabledSettingValue


@dataclass(kw_only=True)
class UpdateIpAllowListForInstalledAppsEnabledSettingInput:
    client_mutation_id: Optional[str] = None
    owner_id: ID
    setting_value: IpAllowListForInstalledAppsEnabledSettingValue


@dataclass(kw_only=True)
class UpdateIssueInput:
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
    client_mutation_id: Optional[str] = None
    owner_id: ID
    setting_value: NotificationRestrictionSettingValue


@dataclass(kw_only=True)
class UpdateOrganizationWebCommitSignoffSettingInput:
    client_mutation_id: Optional[str] = None
    organization_id: ID
    web_commit_signoff_required: bool


@dataclass(kw_only=True)
class UpdateParametersInput:
    update_allows_fetch_and_merge: bool


@dataclass(kw_only=True)
class UpdateProjectCardInput:
    client_mutation_id: Optional[str] = None
    is_archived: Optional[bool] = None
    note: Optional[str] = None
    project_card_id: ID


@dataclass(kw_only=True)
class UpdateProjectInput:
    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    name: Optional[str] = None
    project_id: ID
    public: Optional[bool] = None
    state: Optional[ProjectState] = None


@dataclass(kw_only=True)
class UpdateProjectV2Input:
    client_mutation_id: Optional[str] = None
    closed: Optional[bool] = None
    project_id: ID
    public: Optional[bool] = None
    readme: Optional[str] = None
    short_description: Optional[str] = None
    title: Optional[str] = None


@dataclass(kw_only=True)
class UpdatePullRequestBranchInput:
    client_mutation_id: Optional[str] = None
    expected_head_oid: Optional[GitObjectID] = None
    pull_request_id: ID
    update_method: Optional[PullRequestBranchUpdateMethod] = None


@dataclass(kw_only=True)
class UpdatePullRequestReviewCommentInput:
    body: str
    client_mutation_id: Optional[str] = None
    pull_request_review_comment_id: ID


@dataclass(kw_only=True)
class UpdateRefInput:
    client_mutation_id: Optional[str] = None
    force: Optional[bool] = None
    oid: GitObjectID
    ref_id: ID


@dataclass(kw_only=True)
class UpdateRepositoryInput:
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
    client_mutation_id: Optional[str] = None
    privacy_level: Optional[SponsorshipPrivacy] = None
    receive_emails: Optional[bool] = None
    sponsor_id: Optional[ID] = None
    sponsor_login: Optional[str] = None
    sponsorable_id: Optional[ID] = None
    sponsorable_login: Optional[str] = None


@dataclass(kw_only=True)
class UpdateTeamDiscussionCommentInput:
    body: str
    body_version: Optional[str] = None
    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class UpdateTeamReviewAssignmentInput:
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
    client_mutation_id: Optional[str] = None
    repository_id: ID
    topic_names: list[str]


@dataclass(kw_only=True)
class UpdateUserListsForItemInput:
    client_mutation_id: Optional[str] = None
    item_id: ID
    list_ids: list[ID]
    suggested_list_ids: Optional[list[ID]] = None


@dataclass(kw_only=True)
class UserListSuggestion:
    id: Optional[ID] = None
    name: Optional[str] = None


@dataclass(kw_only=True)
class VerifiableDomainOrder:
    direction: OrderDirection
    field: VerifiableDomainOrderField


@dataclass(kw_only=True)
class Votable:
    upvote_count: int
    viewer_can_upvote: bool
    viewer_has_upvoted: bool


@dataclass(kw_only=True)
class WorkflowFileReferenceInput:
    path: str
    ref: Optional[str] = None
    repository_id: int
    sha: Optional[str] = None


@dataclass(kw_only=True)
class AutoMergeRequest:
    author_email: Optional[str] = None
    commit_body: Optional[str] = None
    commit_headline: Optional[str] = None
    enabled_at: Optional[DateTime] = None
    enabled_by: Optional[Actor] = None
    merge_method: PullRequestMergeMethod
    pull_request: PullRequest


@dataclass(kw_only=True)
class BranchProtectionRuleConflict:
    branch_protection_rule: Optional[BranchProtectionRule] = None
    conflicting_branch_protection_rule: Optional[BranchProtectionRule] = None
    ref: Optional[Ref] = None


@dataclass(kw_only=True)
class BranchProtectionRuleConflictEdge:
    cursor: str
    node: Optional[BranchProtectionRuleConflict] = None


@dataclass(kw_only=True)
class BranchProtectionRuleConflictConnection:
    edges: Optional[list[BranchProtectionRuleConflictEdge]] = None
    nodes: Optional[list[BranchProtectionRuleConflict]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseServerUserAccountEmail:
    created_at: DateTime
    email: str
    id: ID
    is_primary: bool
    updated_at: DateTime
    user_account: EnterpriseServerUserAccount


@dataclass(kw_only=True)
class EnterpriseServerUserAccountEmailEdge:
    cursor: str
    node: Optional[EnterpriseServerUserAccountEmail] = None


@dataclass(kw_only=True)
class EnterpriseServerUserAccountEmailConnection:
    edges: Optional[list[EnterpriseServerUserAccountEmailEdge]] = None
    nodes: Optional[list[EnterpriseServerUserAccountEmail]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseServerUserAccountEdge:
    cursor: str
    node: Optional[EnterpriseServerUserAccount] = None


@dataclass(kw_only=True)
class EnterpriseServerUserAccountConnection:
    edges: Optional[list[EnterpriseServerUserAccountEdge]] = None
    nodes: Optional[list[EnterpriseServerUserAccount]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseServerUserAccountsUpload:
    created_at: DateTime
    enterprise: Enterprise
    enterprise_server_installation: EnterpriseServerInstallation
    id: ID
    name: str
    sync_state: EnterpriseServerUserAccountsUploadSyncState
    updated_at: DateTime


@dataclass(kw_only=True)
class EnterpriseServerUserAccountsUploadEdge:
    cursor: str
    node: Optional[EnterpriseServerUserAccountsUpload] = None


@dataclass(kw_only=True)
class EnterpriseServerUserAccountsUploadConnection:
    edges: Optional[list[EnterpriseServerUserAccountsUploadEdge]] = None
    nodes: Optional[list[EnterpriseServerUserAccountsUpload]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseServerInstallationMembershipEdge:
    cursor: str
    node: Optional[EnterpriseServerInstallation] = None
    role: EnterpriseUserAccountMembershipRole


@dataclass(kw_only=True)
class EnterpriseServerInstallationMembershipConnection:
    edges: Optional[list[EnterpriseServerInstallationMembershipEdge]] = None
    nodes: Optional[list[EnterpriseServerInstallation]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class MembersCanDeleteReposClearAuditEntry:
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
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None


@dataclass(kw_only=True)
class BranchProtectionRuleEdge:
    cursor: str
    node: Optional[BranchProtectionRule] = None


@dataclass(kw_only=True)
class BranchProtectionRuleConnection:
    edges: Optional[list[BranchProtectionRuleEdge]] = None
    nodes: Optional[list[BranchProtectionRule]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class RepositoryCodeowners:
    errors: list[RepositoryCodeownersError]


@dataclass(kw_only=True)
class TeamEdge:
    cursor: str
    node: Optional[Team] = None


@dataclass(kw_only=True)
class TeamConnection:
    edges: Optional[list[TeamEdge]] = None
    nodes: Optional[list[Team]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class Mannequin:
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
    cursor: str
    node: Reactor
    reacted_at: DateTime


@dataclass(kw_only=True)
class ReactorConnection:
    edges: Optional[list[ReactorEdge]] = None
    nodes: Optional[list[Reactor]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class Reaction:
    content: ReactionContent
    created_at: DateTime
    database_id: Optional[int] = None
    id: ID
    reactable: Reactable
    user: Optional[User] = None


@dataclass(kw_only=True)
class ReactionEdge:
    cursor: str
    node: Optional[Reaction] = None


@dataclass(kw_only=True)
class ReactionConnection:
    edges: Optional[list[ReactionEdge]] = None
    nodes: Optional[list[Reaction]] = None
    page_info: PageInfo
    total_count: int
    viewer_has_reacted: bool


@dataclass(kw_only=True)
class ReactingUserEdge:
    cursor: str
    node: User
    reacted_at: DateTime


@dataclass(kw_only=True)
class ReactingUserConnection:
    edges: Optional[list[ReactingUserEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class UserContentEdit:
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
    cursor: str
    node: Optional[UserContentEdit] = None


@dataclass(kw_only=True)
class UserContentEditConnection:
    edges: Optional[list[UserContentEditEdge]] = None
    nodes: Optional[list[UserContentEdit]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class TeamDiscussionComment:
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
    cursor: str
    node: Optional[TeamDiscussionComment] = None


@dataclass(kw_only=True)
class TeamDiscussionCommentConnection:
    edges: Optional[list[TeamDiscussionCommentEdge]] = None
    nodes: Optional[list[TeamDiscussionComment]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class TeamDiscussionEdge:
    cursor: str
    node: Optional[TeamDiscussion] = None


@dataclass(kw_only=True)
class TeamDiscussionConnection:
    edges: Optional[list[TeamDiscussionEdge]] = None
    nodes: Optional[list[TeamDiscussion]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class OrganizationInvitationEdge:
    cursor: str
    node: Optional[OrganizationInvitation] = None


@dataclass(kw_only=True)
class OrganizationInvitationConnection:
    edges: Optional[list[OrganizationInvitationEdge]] = None
    nodes: Optional[list[OrganizationInvitation]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class UserStatus:
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
    cursor: str
    node: Optional[UserStatus] = None


@dataclass(kw_only=True)
class UserStatusConnection:
    edges: Optional[list[UserStatusEdge]] = None
    nodes: Optional[list[UserStatus]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class TeamMemberEdge:
    cursor: str
    member_access_resource_path: URI
    member_access_url: URI
    node: User
    role: TeamMemberRole


@dataclass(kw_only=True)
class TeamMemberConnection:
    edges: Optional[list[TeamMemberEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectV2Field:
    created_at: DateTime
    data_type: ProjectV2FieldType
    database_id: Optional[int] = None
    id: ID
    name: str
    project: ProjectV2
    updated_at: DateTime


@dataclass(kw_only=True)
class ProjectV2IterationFieldConfiguration:
    completed_iterations: list[ProjectV2IterationFieldIteration]
    duration: int
    iterations: list[ProjectV2IterationFieldIteration]
    start_day: int


@dataclass(kw_only=True)
class ProjectV2IterationField:
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
    cursor: str
    node: Optional[ProjectV2FieldConfiguration] = None


@dataclass(kw_only=True)
class ProjectV2FieldConfigurationConnection:
    edges: Optional[list[ProjectV2FieldConfigurationEdge]] = None
    nodes: Optional[list[ProjectV2FieldConfiguration]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectV2Edge:
    cursor: str
    node: Optional[ProjectV2] = None


@dataclass(kw_only=True)
class ProjectV2Connection:
    edges: Optional[list[ProjectV2Edge]] = None
    nodes: Optional[list[ProjectV2]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DraftIssue:
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
    cursor: str
    node: Optional[Issue] = None


@dataclass(kw_only=True)
class IssueConnection:
    edges: Optional[list[IssueEdge]] = None
    nodes: Optional[list[Issue]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class Label:
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
    cursor: str
    node: Optional[Label] = None


@dataclass(kw_only=True)
class LabelConnection:
    edges: Optional[list[LabelEdge]] = None
    nodes: Optional[list[Label]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectV2ItemFieldLabelValue:
    field: ProjectV2FieldConfiguration
    labels: Optional[LabelConnection] = None


@dataclass(kw_only=True)
class Milestone:
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
    field: ProjectV2FieldConfiguration
    milestone: Optional[Milestone] = None


@dataclass(kw_only=True)
class ProjectV2ItemFieldNumberValue:
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
    field: ProjectV2FieldConfiguration
    pull_requests: Optional[PullRequestConnection] = None


@dataclass(kw_only=True)
class ProjectV2ItemFieldRepositoryValue:
    field: ProjectV2FieldConfiguration
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class RequestedReviewerEdge:
    cursor: str
    node: Optional[RequestedReviewer] = None


@dataclass(kw_only=True)
class RequestedReviewerConnection:
    edges: Optional[list[RequestedReviewerEdge]] = None
    nodes: Optional[list[RequestedReviewer]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectV2ItemFieldReviewerValue:
    field: ProjectV2FieldConfiguration
    reviewers: Optional[RequestedReviewerConnection] = None


@dataclass(kw_only=True)
class ProjectV2ItemFieldSingleSelectValue:
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
    field: ProjectV2FieldConfiguration
    users: Optional[UserConnection] = None


@dataclass(kw_only=True)
class ProjectV2ItemFieldValueEdge:
    cursor: str
    node: Optional[ProjectV2ItemFieldValue] = None


@dataclass(kw_only=True)
class ProjectV2ItemFieldValueConnection:
    edges: Optional[list[ProjectV2ItemFieldValueEdge]] = None
    nodes: Optional[list[ProjectV2ItemFieldValue]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectV2ItemEdge:
    cursor: str
    node: Optional[ProjectV2Item] = None


@dataclass(kw_only=True)
class ProjectV2Owner:
    id: ID
    project_v2: Optional[ProjectV2] = None
    projects_v2: ProjectV2Connection


@dataclass(kw_only=True)
class RepositoryEdge:
    cursor: str
    node: Optional[Repository] = None


@dataclass(kw_only=True)
class RepositoryConnection:
    edges: Optional[list[RepositoryEdge]] = None
    nodes: Optional[list[Repository]] = None
    page_info: PageInfo
    total_count: int
    total_disk_usage: int


@dataclass(kw_only=True)
class ProjectV2FieldEdge:
    cursor: str
    node: Optional[ProjectV2Field] = None


@dataclass(kw_only=True)
class ProjectV2FieldConnection:
    edges: Optional[list[ProjectV2FieldEdge]] = None
    nodes: Optional[list[ProjectV2Field]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectV2SortBy:
    direction: OrderDirection
    field: ProjectV2Field


@dataclass(kw_only=True)
class ProjectV2SortByEdge:
    cursor: str
    node: Optional[ProjectV2SortBy] = None


@dataclass(kw_only=True)
class ProjectV2SortByConnection:
    edges: Optional[list[ProjectV2SortByEdge]] = None
    nodes: Optional[list[ProjectV2SortBy]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectV2SortByField:
    direction: OrderDirection
    field: ProjectV2FieldConfiguration


@dataclass(kw_only=True)
class ProjectV2SortByFieldEdge:
    cursor: str
    node: Optional[ProjectV2SortByField] = None


@dataclass(kw_only=True)
class ProjectV2SortByFieldConnection:
    edges: Optional[list[ProjectV2SortByFieldEdge]] = None
    nodes: Optional[list[ProjectV2SortByField]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectV2View:
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
    cursor: str
    node: Optional[ProjectV2View] = None


@dataclass(kw_only=True)
class ProjectV2ViewConnection:
    edges: Optional[list[ProjectV2ViewEdge]] = None
    nodes: Optional[list[ProjectV2View]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectV2Workflow:
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
    cursor: str
    node: Optional[ProjectV2Workflow] = None


@dataclass(kw_only=True)
class ProjectV2WorkflowConnection:
    edges: Optional[list[ProjectV2WorkflowEdge]] = None
    nodes: Optional[list[ProjectV2Workflow]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class TeamRepositoryEdge:
    cursor: str
    node: Repository
    permission: RepositoryPermission


@dataclass(kw_only=True)
class TeamRepositoryConnection:
    edges: Optional[list[TeamRepositoryEdge]] = None
    nodes: Optional[list[Repository]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PermissionSource:
    organization: Organization
    permission: DefaultRepositoryPermissionField
    role_name: Optional[str] = None
    source: PermissionGranter


@dataclass(kw_only=True)
class RepositoryCollaboratorEdge:
    cursor: str
    node: User
    permission: RepositoryPermission
    permission_sources: Optional[list[PermissionSource]] = None


@dataclass(kw_only=True)
class RepositoryCollaboratorConnection:
    edges: Optional[list[RepositoryCollaboratorEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DependencyGraphDependency:
    has_dependencies: bool
    package_manager: Optional[str] = None
    package_name: str
    repository: Optional[Repository] = None
    requirements: str


@dataclass(kw_only=True)
class DependencyGraphDependencyEdge:
    cursor: str
    node: Optional[DependencyGraphDependency] = None


@dataclass(kw_only=True)
class DependencyGraphDependencyConnection:
    edges: Optional[list[DependencyGraphDependencyEdge]] = None
    nodes: Optional[list[DependencyGraphDependency]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DependencyGraphManifest:
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
    cursor: str
    node: Optional[DependencyGraphManifest] = None


@dataclass(kw_only=True)
class DependencyGraphManifestConnection:
    edges: Optional[list[DependencyGraphManifestEdge]] = None
    nodes: Optional[list[DependencyGraphManifest]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DeployKeyEdge:
    cursor: str
    node: Optional[DeployKey] = None


@dataclass(kw_only=True)
class DeployKeyConnection:
    edges: Optional[list[DeployKeyEdge]] = None
    nodes: Optional[list[DeployKey]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DeploymentStatus:
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
    cursor: str
    node: Optional[DeploymentStatus] = None


@dataclass(kw_only=True)
class DeploymentStatusConnection:
    edges: Optional[list[DeploymentStatusEdge]] = None
    nodes: Optional[list[DeploymentStatus]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DeploymentEdge:
    cursor: str
    node: Optional[Deployment] = None


@dataclass(kw_only=True)
class DeploymentConnection:
    edges: Optional[list[DeploymentEdge]] = None
    nodes: Optional[list[Deployment]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DiscussionCommentEdge:
    cursor: str
    node: Optional[DiscussionComment] = None


@dataclass(kw_only=True)
class DiscussionCommentConnection:
    edges: Optional[list[DiscussionCommentEdge]] = None
    nodes: Optional[list[DiscussionComment]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DiscussionCategory:
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
    id: ID
    option: str
    poll: Optional[DiscussionPoll] = None
    total_vote_count: int
    viewer_has_voted: bool


@dataclass(kw_only=True)
class DiscussionPollOptionEdge:
    cursor: str
    node: Optional[DiscussionPollOption] = None


@dataclass(kw_only=True)
class DiscussionPollOptionConnection:
    edges: Optional[list[DiscussionPollOptionEdge]] = None
    nodes: Optional[list[DiscussionPollOption]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DiscussionCategoryEdge:
    cursor: str
    node: Optional[DiscussionCategory] = None


@dataclass(kw_only=True)
class DiscussionCategoryConnection:
    edges: Optional[list[DiscussionCategoryEdge]] = None
    nodes: Optional[list[DiscussionCategory]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DiscussionEdge:
    cursor: str
    node: Optional[Discussion] = None


@dataclass(kw_only=True)
class DiscussionConnection:
    edges: Optional[list[DiscussionEdge]] = None
    nodes: Optional[list[Discussion]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DeploymentReviewerEdge:
    cursor: str
    node: Optional[DeploymentReviewer] = None


@dataclass(kw_only=True)
class DeploymentReviewerConnection:
    edges: Optional[list[DeploymentReviewerEdge]] = None
    nodes: Optional[list[DeploymentReviewer]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DeploymentProtectionRule:
    database_id: Optional[int] = None
    prevent_self_review: Optional[bool] = None
    reviewers: DeploymentReviewerConnection
    timeout: int
    type: DeploymentProtectionRuleType


@dataclass(kw_only=True)
class DeploymentProtectionRuleEdge:
    cursor: str
    node: Optional[DeploymentProtectionRule] = None


@dataclass(kw_only=True)
class DeploymentProtectionRuleConnection:
    edges: Optional[list[DeploymentProtectionRuleEdge]] = None
    nodes: Optional[list[DeploymentProtectionRule]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class Environment:
    database_id: Optional[int] = None
    id: ID
    name: str
    protection_rules: DeploymentProtectionRuleConnection


@dataclass(kw_only=True)
class EnvironmentEdge:
    cursor: str
    node: Optional[Environment] = None


@dataclass(kw_only=True)
class EnvironmentConnection:
    edges: Optional[list[EnvironmentEdge]] = None
    nodes: Optional[list[Environment]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class IssueTemplate:
    about: Optional[str] = None
    assignees: UserConnection
    body: Optional[str] = None
    filename: str
    labels: Optional[LabelConnection] = None
    name: str
    title: Optional[str] = None


@dataclass(kw_only=True)
class LanguageEdge:
    cursor: str
    node: Language
    size: int


@dataclass(kw_only=True)
class LanguageConnection:
    edges: Optional[list[LanguageEdge]] = None
    nodes: Optional[list[Language]] = None
    page_info: PageInfo
    total_count: int
    total_size: int


@dataclass(kw_only=True)
class ReleaseAsset:
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
    cursor: str
    node: Optional[ReleaseAsset] = None


@dataclass(kw_only=True)
class ReleaseAssetConnection:
    edges: Optional[list[ReleaseAssetEdge]] = None
    nodes: Optional[list[ReleaseAsset]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class License:
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
    cursor: str
    node: Optional[MergeQueueEntry] = None


@dataclass(kw_only=True)
class MergeQueueEntryConnection:
    edges: Optional[list[MergeQueueEntryEdge]] = None
    nodes: Optional[list[MergeQueueEntry]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class MilestoneEdge:
    cursor: str
    node: Optional[Milestone] = None


@dataclass(kw_only=True)
class MilestoneConnection:
    edges: Optional[list[MilestoneEdge]] = None
    nodes: Optional[list[Milestone]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class GitObject:
    abbreviated_oid: str
    commit_resource_path: URI
    commit_url: URI
    id: ID
    oid: GitObjectID
    repository: Repository


@dataclass(kw_only=True)
class RepositoryOwner:
    avatar_url: URI
    id: ID
    login: str
    repositories: RepositoryConnection
    repository: Optional[Repository] = None
    resource_path: URI
    url: URI


@dataclass(kw_only=True)
class PackageFile:
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
    cursor: str
    node: Optional[PackageFile] = None


@dataclass(kw_only=True)
class PackageFileConnection:
    edges: Optional[list[PackageFileEdge]] = None
    nodes: Optional[list[PackageFile]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PackageVersionEdge:
    cursor: str
    node: Optional[PackageVersion] = None


@dataclass(kw_only=True)
class PackageVersionConnection:
    edges: Optional[list[PackageVersionEdge]] = None
    nodes: Optional[list[PackageVersion]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PackageEdge:
    cursor: str
    node: Optional[Package] = None


@dataclass(kw_only=True)
class PackageConnection:
    edges: Optional[list[PackageEdge]] = None
    nodes: Optional[list[Package]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PinnedDiscussion:
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
    cursor: str
    node: Optional[PinnedDiscussion] = None


@dataclass(kw_only=True)
class PinnedDiscussionConnection:
    edges: Optional[list[PinnedDiscussionEdge]] = None
    nodes: Optional[list[PinnedDiscussion]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PinnedIssue:
    database_id: Optional[int] = None
    full_database_id: Optional[BigInt] = None
    id: ID
    issue: Issue
    pinned_by: Actor
    repository: Repository


@dataclass(kw_only=True)
class PinnedIssueEdge:
    cursor: str
    node: Optional[PinnedIssue] = None


@dataclass(kw_only=True)
class PinnedIssueConnection:
    edges: Optional[list[PinnedIssueEdge]] = None
    nodes: Optional[list[PinnedIssue]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectCard:
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
    cursor: str
    node: Optional[ProjectCard] = None


@dataclass(kw_only=True)
class ProjectCardConnection:
    edges: Optional[list[ProjectCardEdge]] = None
    nodes: Optional[list[ProjectCard]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectColumnEdge:
    cursor: str
    node: Optional[ProjectColumn] = None


@dataclass(kw_only=True)
class ProjectColumnConnection:
    edges: Optional[list[ProjectColumnEdge]] = None
    nodes: Optional[list[ProjectColumn]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectEdge:
    cursor: str
    node: Optional[Project] = None


@dataclass(kw_only=True)
class ProjectConnection:
    edges: Optional[list[ProjectEdge]] = None
    nodes: Optional[list[Project]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectOwner:
    id: ID
    project: Optional[Project] = None
    projects: ProjectConnection
    projects_resource_path: URI
    projects_url: URI
    viewer_can_create_projects: bool


@dataclass(kw_only=True)
class PullRequestTemplate:
    body: Optional[str] = None
    filename: Optional[str] = None
    repository: Repository


@dataclass(kw_only=True)
class RefEdge:
    cursor: str
    node: Optional[Ref] = None


@dataclass(kw_only=True)
class RefConnection:
    edges: Optional[list[RefEdge]] = None
    nodes: Optional[list[Ref]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ReleaseEdge:
    cursor: str
    node: Optional[Release] = None


@dataclass(kw_only=True)
class ReleaseConnection:
    edges: Optional[list[ReleaseEdge]] = None
    nodes: Optional[list[Release]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class StargazerEdge:
    cursor: str
    node: User
    starred_at: DateTime


@dataclass(kw_only=True)
class StargazerConnection:
    edges: Optional[list[StargazerEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class RepositoryTopic:
    id: ID
    resource_path: URI
    topic: Topic
    url: URI


@dataclass(kw_only=True)
class RepositoryTopicEdge:
    cursor: str
    node: Optional[RepositoryTopic] = None


@dataclass(kw_only=True)
class RepositoryTopicConnection:
    edges: Optional[list[RepositoryTopicEdge]] = None
    nodes: Optional[list[RepositoryTopic]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class RepositoryRulesetBypassActor:
    actor: Optional[BypassActor] = None
    bypass_mode: Optional[RepositoryRulesetBypassActorBypassMode] = None
    id: ID
    organization_admin: bool
    repository_role_database_id: Optional[int] = None
    repository_role_name: Optional[str] = None
    repository_ruleset: Optional[RepositoryRuleset] = None


@dataclass(kw_only=True)
class RepositoryRulesetBypassActorEdge:
    cursor: str
    node: Optional[RepositoryRulesetBypassActor] = None


@dataclass(kw_only=True)
class RepositoryRulesetBypassActorConnection:
    edges: Optional[list[RepositoryRulesetBypassActorEdge]] = None
    nodes: Optional[list[RepositoryRulesetBypassActor]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class RepositoryPropertyConditionTarget:
    exclude: list[PropertyTargetDefinition]
    include: list[PropertyTargetDefinition]


@dataclass(kw_only=True)
class RepositoryRuleConditions:
    ref_name: Optional[RefNameConditionTarget] = None
    repository_id: Optional[RepositoryIdConditionTarget] = None
    repository_name: Optional[RepositoryNameConditionTarget] = None
    repository_property: Optional[RepositoryPropertyConditionTarget] = None


@dataclass(kw_only=True)
class RequiredStatusChecksParameters:
    required_status_checks: list[StatusCheckConfiguration]
    strict_required_status_checks_policy: bool


@dataclass(kw_only=True)
class WorkflowsParameters:
    workflows: list[WorkflowFileReference]


@dataclass(kw_only=True)
class RepositoryRule:
    id: ID
    parameters: Optional[RuleParameters] = None
    repository_ruleset: Optional[RepositoryRuleset] = None
    type: RepositoryRuleType


@dataclass(kw_only=True)
class RepositoryRuleEdge:
    cursor: str
    node: Optional[RepositoryRule] = None


@dataclass(kw_only=True)
class RepositoryRuleConnection:
    edges: Optional[list[RepositoryRuleEdge]] = None
    nodes: Optional[list[RepositoryRule]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class RepositoryRulesetEdge:
    cursor: str
    node: Optional[RepositoryRuleset] = None


@dataclass(kw_only=True)
class RepositoryRulesetConnection:
    edges: Optional[list[RepositoryRulesetEdge]] = None
    nodes: Optional[list[RepositoryRuleset]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class SubmoduleEdge:
    cursor: str
    node: Optional[Submodule] = None


@dataclass(kw_only=True)
class SubmoduleConnection:
    edges: Optional[list[SubmoduleEdge]] = None
    nodes: Optional[list[Submodule]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DependabotUpdate:
    error: Optional[DependabotUpdateError] = None
    pull_request: Optional[PullRequest] = None
    repository: Repository


@dataclass(kw_only=True)
class CWEEdge:
    cursor: str
    node: Optional[CWE] = None


@dataclass(kw_only=True)
class CWEConnection:
    edges: Optional[list[CWEEdge]] = None
    nodes: Optional[list[CWE]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class SecurityVulnerability:
    advisory: SecurityAdvisory
    first_patched_version: Optional[SecurityAdvisoryPackageVersion] = None
    package: SecurityAdvisoryPackage
    severity: SecurityAdvisorySeverity
    updated_at: DateTime
    vulnerable_version_range: str


@dataclass(kw_only=True)
class SecurityVulnerabilityEdge:
    cursor: str
    node: Optional[SecurityVulnerability] = None


@dataclass(kw_only=True)
class SecurityVulnerabilityConnection:
    edges: Optional[list[SecurityVulnerabilityEdge]] = None
    nodes: Optional[list[SecurityVulnerability]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class RepositoryVulnerabilityAlert:
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
    cursor: str
    node: Optional[RepositoryVulnerabilityAlert] = None


@dataclass(kw_only=True)
class RepositoryVulnerabilityAlertConnection:
    edges: Optional[list[RepositoryVulnerabilityAlertEdge]] = None
    nodes: Optional[list[RepositoryVulnerabilityAlert]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class OrgRestoreMemberMembershipRepositoryAuditEntryData:
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgRestoreMemberMembershipTeamAuditEntryData:
    team: Optional[Team] = None
    team_name: Optional[str] = None
    team_resource_path: Optional[URI] = None
    team_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrgRestoreMemberAuditEntry:
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
    cursor: str
    node: Optional[OrganizationAuditEntry] = None


@dataclass(kw_only=True)
class OrganizationAuditEntryConnection:
    edges: Optional[list[OrganizationAuditEntryEdge]] = None
    nodes: Optional[list[OrganizationAuditEntry]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class VerifiableDomain:
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
    cursor: str
    node: Optional[VerifiableDomain] = None


@dataclass(kw_only=True)
class VerifiableDomainConnection:
    edges: Optional[list[VerifiableDomainEdge]] = None
    nodes: Optional[list[VerifiableDomain]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class OrganizationEnterpriseOwnerEdge:
    cursor: str
    node: Optional[User] = None
    organization_role: RoleInOrganization


@dataclass(kw_only=True)
class OrganizationEnterpriseOwnerConnection:
    edges: Optional[list[OrganizationEnterpriseOwnerEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class GistComment:
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
    cursor: str
    node: Optional[GistComment] = None


@dataclass(kw_only=True)
class GistCommentConnection:
    edges: Optional[list[GistCommentEdge]] = None
    nodes: Optional[list[GistComment]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class GistFile:
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
    cursor: str
    node: Optional[Gist] = None


@dataclass(kw_only=True)
class GistConnection:
    edges: Optional[list[GistEdge]] = None
    nodes: Optional[list[Gist]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PinnableItemEdge:
    cursor: str
    node: Optional[PinnableItem] = None


@dataclass(kw_only=True)
class PinnableItemConnection:
    edges: Optional[list[PinnableItemEdge]] = None
    nodes: Optional[list[PinnableItem]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProfileItemShowcase:
    has_pinned_items: bool
    items: PinnableItemConnection


@dataclass(kw_only=True)
class SponsorEdge:
    cursor: str
    node: Optional[Sponsor] = None


@dataclass(kw_only=True)
class SponsorConnection:
    edges: Optional[list[SponsorEdge]] = None
    nodes: Optional[list[Sponsor]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class Sponsorship:
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
    cursor: str
    node: Optional[Sponsorship] = None


@dataclass(kw_only=True)
class SponsorshipConnection:
    edges: Optional[list[SponsorshipEdge]] = None
    nodes: Optional[list[Sponsorship]] = None
    page_info: PageInfo
    total_count: int
    total_recurring_monthly_price_in_cents: int
    total_recurring_monthly_price_in_dollars: int


@dataclass(kw_only=True)
class SponsorsTierAdminInfo:
    is_draft: bool
    is_published: bool
    is_retired: bool
    sponsorships: SponsorshipConnection


@dataclass(kw_only=True)
class StripeConnectAccount:
    account_id: str
    billing_country_or_region: Optional[str] = None
    country_or_region: Optional[str] = None
    is_active: bool
    sponsors_listing: SponsorsListing
    stripe_dashboard_url: URI


@dataclass(kw_only=True)
class SponsorsListingFeaturedItem:
    created_at: DateTime
    description: Optional[str] = None
    featureable: SponsorsListingFeatureableItem
    id: ID
    position: int
    sponsors_listing: SponsorsListing
    updated_at: DateTime


@dataclass(kw_only=True)
class SponsorsTierEdge:
    cursor: str
    node: Optional[SponsorsTier] = None


@dataclass(kw_only=True)
class SponsorsTierConnection:
    edges: Optional[list[SponsorsTierEdge]] = None
    nodes: Optional[list[SponsorsTier]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class SponsorsActivity:
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
    cursor: str
    node: Optional[SponsorsActivity] = None


@dataclass(kw_only=True)
class SponsorsActivityConnection:
    edges: Optional[list[SponsorsActivityEdge]] = None
    nodes: Optional[list[SponsorsActivity]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class SponsorshipNewsletter:
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
    cursor: str
    node: Optional[SponsorshipNewsletter] = None


@dataclass(kw_only=True)
class SponsorshipNewsletterConnection:
    edges: Optional[list[SponsorshipNewsletterEdge]] = None
    nodes: Optional[list[SponsorshipNewsletter]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class SponsorAndLifetimeValue:
    amount_in_cents: int
    formatted_amount: str
    sponsor: Sponsorable
    sponsorable: Sponsorable


@dataclass(kw_only=True)
class SponsorAndLifetimeValueEdge:
    cursor: str
    node: Optional[SponsorAndLifetimeValue] = None


@dataclass(kw_only=True)
class MannequinEdge:
    cursor: str
    node: Optional[Mannequin] = None


@dataclass(kw_only=True)
class MannequinConnection:
    edges: Optional[list[MannequinEdge]] = None
    nodes: Optional[list[Mannequin]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class OrganizationMemberEdge:
    cursor: str
    has_two_factor_enabled: Optional[bool] = None
    node: Optional[User] = None
    role: Optional[OrganizationMemberRole] = None


@dataclass(kw_only=True)
class OrganizationMemberConnection:
    edges: Optional[list[OrganizationMemberEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class RepositoryMigration:
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
    cursor: str
    node: Optional[RepositoryMigration] = None


@dataclass(kw_only=True)
class RepositoryMigrationConnection:
    edges: Optional[list[RepositoryMigrationEdge]] = None
    nodes: Optional[list[RepositoryMigration]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ExternalIdentitySamlAttributes:
    attributes: list[ExternalIdentityAttribute]
    emails: Optional[list[UserEmailMetadata]] = None
    family_name: Optional[str] = None
    given_name: Optional[str] = None
    groups: Optional[list[str]] = None
    name_id: Optional[str] = None
    username: Optional[str] = None


@dataclass(kw_only=True)
class ExternalIdentityScimAttributes:
    emails: Optional[list[UserEmailMetadata]] = None
    family_name: Optional[str] = None
    given_name: Optional[str] = None
    groups: Optional[list[str]] = None
    username: Optional[str] = None


@dataclass(kw_only=True)
class ExternalIdentity:
    guid: str
    id: ID
    organization_invitation: Optional[OrganizationInvitation] = None
    saml_identity: Optional[ExternalIdentitySamlAttributes] = None
    scim_identity: Optional[ExternalIdentityScimAttributes] = None
    user: Optional[User] = None


@dataclass(kw_only=True)
class ExternalIdentityEdge:
    cursor: str
    node: Optional[ExternalIdentity] = None


@dataclass(kw_only=True)
class ExternalIdentityConnection:
    edges: Optional[list[ExternalIdentityEdge]] = None
    nodes: Optional[list[ExternalIdentity]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class OrganizationIdentityProvider:
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
    cursor: str
    node: Optional[Organization] = None
    role: EnterpriseUserAccountMembershipRole


@dataclass(kw_only=True)
class EnterpriseOrganizationMembershipConnection:
    edges: Optional[list[EnterpriseOrganizationMembershipEdge]] = None
    nodes: Optional[list[Organization]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseUserAccount:
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
    cursor: str
    node: Optional[EnterpriseMember] = None


@dataclass(kw_only=True)
class EnterpriseMemberConnection:
    edges: Optional[list[EnterpriseMemberEdge]] = None
    nodes: Optional[list[EnterpriseMember]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class OrganizationEdge:
    cursor: str
    node: Optional[Organization] = None


@dataclass(kw_only=True)
class OrganizationConnection:
    edges: Optional[list[OrganizationEdge]] = None
    nodes: Optional[list[Organization]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseAdministratorEdge:
    cursor: str
    node: Optional[User] = None
    role: EnterpriseAdministratorRole


@dataclass(kw_only=True)
class EnterpriseAdministratorConnection:
    edges: Optional[list[EnterpriseAdministratorEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseServerInstallationEdge:
    cursor: str
    node: Optional[EnterpriseServerInstallation] = None


@dataclass(kw_only=True)
class EnterpriseServerInstallationConnection:
    edges: Optional[list[EnterpriseServerInstallationEdge]] = None
    nodes: Optional[list[EnterpriseServerInstallation]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseFailedInvitationEdge:
    cursor: str
    node: Optional[OrganizationInvitation] = None


@dataclass(kw_only=True)
class EnterpriseFailedInvitationConnection:
    edges: Optional[list[EnterpriseFailedInvitationEdge]] = None
    nodes: Optional[list[OrganizationInvitation]] = None
    page_info: PageInfo
    total_count: int
    total_unique_user_count: int


@dataclass(kw_only=True)
class OIDCProvider:
    enterprise: Optional[Enterprise] = None
    external_identities: ExternalIdentityConnection
    id: ID
    provider_type: OIDCProviderType
    tenant_id: str


@dataclass(kw_only=True)
class EnterpriseRepositoryInfoEdge:
    cursor: str
    node: Optional[EnterpriseRepositoryInfo] = None


@dataclass(kw_only=True)
class EnterpriseRepositoryInfoConnection:
    edges: Optional[list[EnterpriseRepositoryInfoEdge]] = None
    nodes: Optional[list[EnterpriseRepositoryInfo]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseOutsideCollaboratorEdge:
    cursor: str
    node: Optional[User] = None
    repositories: EnterpriseRepositoryInfoConnection


@dataclass(kw_only=True)
class EnterpriseOutsideCollaboratorConnection:
    edges: Optional[list[EnterpriseOutsideCollaboratorEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseAdministratorInvitation:
    created_at: DateTime
    email: Optional[str] = None
    enterprise: Enterprise
    id: ID
    invitee: Optional[User] = None
    inviter: Optional[User] = None
    role: EnterpriseAdministratorRole


@dataclass(kw_only=True)
class EnterpriseAdministratorInvitationEdge:
    cursor: str
    node: Optional[EnterpriseAdministratorInvitation] = None


@dataclass(kw_only=True)
class EnterpriseAdministratorInvitationConnection:
    edges: Optional[list[EnterpriseAdministratorInvitationEdge]] = None
    nodes: Optional[list[EnterpriseAdministratorInvitation]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class RepositoryInfo:
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
    email: Optional[str] = None
    id: ID
    invitee: Optional[User] = None
    inviter: User
    permalink: URI
    permission: RepositoryPermission
    repository: Optional[RepositoryInfo] = None


@dataclass(kw_only=True)
class RepositoryInvitationEdge:
    cursor: str
    node: Optional[RepositoryInvitation] = None


@dataclass(kw_only=True)
class RepositoryInvitationConnection:
    edges: Optional[list[RepositoryInvitationEdge]] = None
    nodes: Optional[list[RepositoryInvitation]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterprisePendingMemberInvitationEdge:
    cursor: str
    node: Optional[OrganizationInvitation] = None


@dataclass(kw_only=True)
class EnterprisePendingMemberInvitationConnection:
    edges: Optional[list[EnterprisePendingMemberInvitationEdge]] = None
    nodes: Optional[list[OrganizationInvitation]] = None
    page_info: PageInfo
    total_count: int
    total_unique_user_count: int


@dataclass(kw_only=True)
class EnterpriseIdentityProvider:
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
    allow_list_value: str
    created_at: DateTime
    id: ID
    is_active: bool
    name: Optional[str] = None
    owner: IpAllowListOwner
    updated_at: DateTime


@dataclass(kw_only=True)
class IpAllowListEntryEdge:
    cursor: str
    node: Optional[IpAllowListEntry] = None


@dataclass(kw_only=True)
class BypassForcePushAllowance:
    actor: Optional[BranchActorAllowanceActor] = None
    branch_protection_rule: Optional[BranchProtectionRule] = None
    id: ID


@dataclass(kw_only=True)
class BypassForcePushAllowanceEdge:
    cursor: str
    node: Optional[BypassForcePushAllowance] = None


@dataclass(kw_only=True)
class BypassForcePushAllowanceConnection:
    edges: Optional[list[BypassForcePushAllowanceEdge]] = None
    nodes: Optional[list[BypassForcePushAllowance]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class BypassPullRequestAllowance:
    actor: Optional[BranchActorAllowanceActor] = None
    branch_protection_rule: Optional[BranchProtectionRule] = None
    id: ID


@dataclass(kw_only=True)
class BypassPullRequestAllowanceEdge:
    cursor: str
    node: Optional[BypassPullRequestAllowance] = None


@dataclass(kw_only=True)
class BypassPullRequestAllowanceConnection:
    edges: Optional[list[BypassPullRequestAllowanceEdge]] = None
    nodes: Optional[list[BypassPullRequestAllowance]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PushAllowance:
    actor: Optional[PushAllowanceActor] = None
    branch_protection_rule: Optional[BranchProtectionRule] = None
    id: ID


@dataclass(kw_only=True)
class PushAllowanceEdge:
    cursor: str
    node: Optional[PushAllowance] = None


@dataclass(kw_only=True)
class PushAllowanceConnection:
    edges: Optional[list[PushAllowanceEdge]] = None
    nodes: Optional[list[PushAllowance]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class RequiredStatusCheckDescription:
    app: Optional[App] = None
    context: str


@dataclass(kw_only=True)
class ReviewDismissalAllowance:
    actor: Optional[ReviewDismissalAllowanceActor] = None
    branch_protection_rule: Optional[BranchProtectionRule] = None
    id: ID


@dataclass(kw_only=True)
class ReviewDismissalAllowanceEdge:
    cursor: str
    node: Optional[ReviewDismissalAllowance] = None


@dataclass(kw_only=True)
class ReviewDismissalAllowanceConnection:
    edges: Optional[list[ReviewDismissalAllowanceEdge]] = None
    nodes: Optional[list[ReviewDismissalAllowance]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class CommitEdge:
    cursor: str
    node: Optional[Commit] = None


@dataclass(kw_only=True)
class ComparisonCommitConnection:
    author_count: int
    edges: Optional[list[CommitEdge]] = None
    nodes: Optional[list[Commit]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class Comparison:
    ahead_by: int
    base_target: GitObject
    behind_by: int
    commits: ComparisonCommitConnection
    head_target: GitObject
    id: ID
    status: ComparisonStatus


@dataclass(kw_only=True)
class IssueCommentConnection:
    edges: Optional[list[IssueCommentEdge]] = None
    nodes: Optional[list[IssueComment]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PullRequestCommit:
    commit: Commit
    id: ID
    pull_request: PullRequest
    resource_path: URI
    url: URI


@dataclass(kw_only=True)
class PullRequestCommitEdge:
    cursor: str
    node: Optional[PullRequestCommit] = None


@dataclass(kw_only=True)
class PullRequestCommitConnection:
    edges: Optional[list[PullRequestCommitEdge]] = None
    nodes: Optional[list[PullRequestCommit]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PullRequestChangedFileEdge:
    cursor: str
    node: Optional[PullRequestChangedFile] = None


@dataclass(kw_only=True)
class PullRequestChangedFileConnection:
    edges: Optional[list[PullRequestChangedFileEdge]] = None
    nodes: Optional[list[PullRequestChangedFile]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class Hovercard:
    contexts: list[HovercardContext]


@dataclass(kw_only=True)
class PullRequestReviewCommentEdge:
    cursor: str
    node: Optional[PullRequestReviewComment] = None


@dataclass(kw_only=True)
class PullRequestReviewCommentConnection:
    edges: Optional[list[PullRequestReviewCommentEdge]] = None
    nodes: Optional[list[PullRequestReviewComment]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PullRequestReviewEdge:
    cursor: str
    node: Optional[PullRequestReview] = None


@dataclass(kw_only=True)
class PullRequestReviewConnection:
    edges: Optional[list[PullRequestReviewEdge]] = None
    nodes: Optional[list[PullRequestReview]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ReviewRequest:
    as_code_owner: bool
    database_id: Optional[int] = None
    id: ID
    pull_request: PullRequest
    requested_reviewer: Optional[RequestedReviewer] = None


@dataclass(kw_only=True)
class ReviewRequestEdge:
    cursor: str
    node: Optional[ReviewRequest] = None


@dataclass(kw_only=True)
class ReviewRequestConnection:
    edges: Optional[list[ReviewRequestEdge]] = None
    nodes: Optional[list[ReviewRequest]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PullRequestReviewThread:
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
    cursor: str
    node: Optional[PullRequestReviewThread] = None


@dataclass(kw_only=True)
class PullRequestReviewThreadConnection:
    edges: Optional[list[PullRequestReviewThreadEdge]] = None
    nodes: Optional[list[PullRequestReviewThread]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class SuggestedReviewer:
    is_author: bool
    is_commenter: bool
    reviewer: User


@dataclass(kw_only=True)
class Assignable:
    assignees: UserConnection


@dataclass(kw_only=True)
class AssignedEvent:
    actor: Optional[Actor] = None
    assignable: Assignable
    assignee: Optional[Assignee] = None
    created_at: DateTime
    id: ID


@dataclass(kw_only=True)
class BaseRefDeletedEvent:
    actor: Optional[Actor] = None
    base_ref_name: Optional[str] = None
    created_at: DateTime
    id: ID
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class BaseRefForcePushedEvent:
    actor: Optional[Actor] = None
    after_commit: Optional[Commit] = None
    before_commit: Optional[Commit] = None
    created_at: DateTime
    id: ID
    pull_request: PullRequest
    ref: Optional[Ref] = None


@dataclass(kw_only=True)
class ClosedEvent:
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
    comments: CommitCommentConnection
    commit: Optional[Commit] = None
    id: ID
    path: Optional[str] = None
    position: Optional[int] = None
    repository: Repository


@dataclass(kw_only=True)
class CrossReferencedEvent:
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
    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    milestone_title: str
    subject: MilestoneItem


@dataclass(kw_only=True)
class DeployedEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    database_id: Optional[int] = None
    deployment: Deployment
    id: ID
    pull_request: PullRequest
    ref: Optional[Ref] = None


@dataclass(kw_only=True)
class DeploymentEnvironmentChangedEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    deployment_status: DeploymentStatus
    id: ID
    pull_request: PullRequest


@dataclass(kw_only=True)
class HeadRefDeletedEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    head_ref: Optional[Ref] = None
    head_ref_name: str
    id: ID
    pull_request: PullRequest


@dataclass(kw_only=True)
class HeadRefForcePushedEvent:
    actor: Optional[Actor] = None
    after_commit: Optional[Commit] = None
    before_commit: Optional[Commit] = None
    created_at: DateTime
    id: ID
    pull_request: PullRequest
    ref: Optional[Ref] = None


@dataclass(kw_only=True)
class HeadRefRestoredEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    pull_request: PullRequest


@dataclass(kw_only=True)
class Labelable:
    labels: Optional[LabelConnection] = None


@dataclass(kw_only=True)
class LabeledEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    label: Label
    labelable: Labelable


@dataclass(kw_only=True)
class LockedEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    lock_reason: Optional[LockReason] = None
    lockable: Lockable


@dataclass(kw_only=True)
class MergedEvent:
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
    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    milestone_title: str
    subject: MilestoneItem


@dataclass(kw_only=True)
class ReferencedEvent:
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
    actor: Optional[Actor] = None
    created_at: DateTime
    current_title: str
    id: ID
    previous_title: str
    subject: RenamedTitleSubject


@dataclass(kw_only=True)
class ReopenedEvent:
    actor: Optional[Actor] = None
    closable: Closable
    created_at: DateTime
    id: ID
    state_reason: Optional[IssueStateReason] = None


@dataclass(kw_only=True)
class ReviewDismissedEvent:
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
    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    pull_request: PullRequest
    requested_reviewer: Optional[RequestedReviewer] = None


@dataclass(kw_only=True)
class ReviewRequestedEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    pull_request: PullRequest
    requested_reviewer: Optional[RequestedReviewer] = None


@dataclass(kw_only=True)
class SubscribedEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    subscribable: Subscribable


@dataclass(kw_only=True)
class UnassignedEvent:
    actor: Optional[Actor] = None
    assignable: Assignable
    assignee: Optional[Assignee] = None
    created_at: DateTime
    id: ID


@dataclass(kw_only=True)
class UnlabeledEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    label: Label
    labelable: Labelable


@dataclass(kw_only=True)
class UnlockedEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    lockable: Lockable


@dataclass(kw_only=True)
class UnsubscribedEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    subscribable: Subscribable


@dataclass(kw_only=True)
class UserBlockedEvent:
    actor: Optional[Actor] = None
    block_duration: UserBlockDuration
    created_at: DateTime
    id: ID
    subject: Optional[User] = None


@dataclass(kw_only=True)
class PullRequestTimelineItemEdge:
    cursor: str
    node: Optional[PullRequestTimelineItem] = None


@dataclass(kw_only=True)
class PullRequestTimelineConnection:
    edges: Optional[list[PullRequestTimelineItemEdge]] = None
    nodes: Optional[list[PullRequestTimelineItem]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class AddedToMergeQueueEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    enqueuer: Optional[User] = None
    id: ID
    merge_queue: Optional[MergeQueue] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class AddedToProjectEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    database_id: Optional[int] = None
    id: ID
    project: Optional[Project] = None
    project_card: Optional[ProjectCard] = None
    project_column_name: str


@dataclass(kw_only=True)
class AutoMergeDisabledEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    disabler: Optional[User] = None
    id: ID
    pull_request: Optional[PullRequest] = None
    reason: Optional[str] = None
    reason_code: Optional[str] = None


@dataclass(kw_only=True)
class AutoMergeEnabledEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    enabler: Optional[User] = None
    id: ID
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class AutoRebaseEnabledEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    enabler: Optional[User] = None
    id: ID
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class AutoSquashEnabledEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    enabler: Optional[User] = None
    id: ID
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class AutomaticBaseChangeFailedEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    new_base: str
    old_base: str
    pull_request: PullRequest


@dataclass(kw_only=True)
class AutomaticBaseChangeSucceededEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    new_base: str
    old_base: str
    pull_request: PullRequest


@dataclass(kw_only=True)
class BaseRefChangedEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    current_ref_name: str
    database_id: Optional[int] = None
    id: ID
    previous_ref_name: str
    pull_request: PullRequest


@dataclass(kw_only=True)
class CommentDeletedEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    database_id: Optional[int] = None
    deleted_comment_author: Optional[Actor] = None
    id: ID


@dataclass(kw_only=True)
class ConnectedEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    is_cross_repository: bool
    source: ReferencedSubject
    subject: ReferencedSubject


@dataclass(kw_only=True)
class ConvertToDraftEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    pull_request: PullRequest
    resource_path: URI
    url: URI


@dataclass(kw_only=True)
class ConvertedNoteToIssueEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    database_id: Optional[int] = None
    id: ID
    project: Optional[Project] = None
    project_card: Optional[ProjectCard] = None
    project_column_name: str


@dataclass(kw_only=True)
class ConvertedToDiscussionEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    discussion: Optional[Discussion] = None
    id: ID


@dataclass(kw_only=True)
class DisconnectedEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    is_cross_repository: bool
    source: ReferencedSubject
    subject: ReferencedSubject


@dataclass(kw_only=True)
class MarkedAsDuplicateEvent:
    actor: Optional[Actor] = None
    canonical: Optional[IssueOrPullRequest] = None
    created_at: DateTime
    duplicate: Optional[IssueOrPullRequest] = None
    id: ID
    is_cross_repository: bool


@dataclass(kw_only=True)
class MentionedEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    database_id: Optional[int] = None
    id: ID


@dataclass(kw_only=True)
class MovedColumnsInProjectEvent:
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
    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    issue: Issue


@dataclass(kw_only=True)
class PullRequestCommitCommentThread:
    comments: CommitCommentConnection
    commit: Commit
    id: ID
    path: Optional[str] = None
    position: Optional[int] = None
    pull_request: PullRequest
    repository: Repository


@dataclass(kw_only=True)
class PullRequestRevisionMarker:
    created_at: DateTime
    last_seen_commit: Commit
    pull_request: PullRequest


@dataclass(kw_only=True)
class ReadyForReviewEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    pull_request: PullRequest
    resource_path: URI
    url: URI


@dataclass(kw_only=True)
class RemovedFromMergeQueueEvent:
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
    actor: Optional[Actor] = None
    created_at: DateTime
    database_id: Optional[int] = None
    id: ID
    project: Optional[Project] = None
    project_column_name: str


@dataclass(kw_only=True)
class TransferredEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    from_repository: Optional[Repository] = None
    id: ID
    issue: Issue


@dataclass(kw_only=True)
class UnmarkedAsDuplicateEvent:
    actor: Optional[Actor] = None
    canonical: Optional[IssueOrPullRequest] = None
    created_at: DateTime
    duplicate: Optional[IssueOrPullRequest] = None
    id: ID
    is_cross_repository: bool


@dataclass(kw_only=True)
class UnpinnedEvent:
    actor: Optional[Actor] = None
    created_at: DateTime
    id: ID
    issue: Issue


@dataclass(kw_only=True)
class PullRequestTimelineItemsEdge:
    cursor: str
    node: Optional[PullRequestTimelineItems] = None


@dataclass(kw_only=True)
class PullRequestTimelineItemsConnection:
    edges: Optional[list[PullRequestTimelineItemsEdge]] = None
    filtered_count: int
    nodes: Optional[list[PullRequestTimelineItems]] = None
    page_count: int
    page_info: PageInfo
    total_count: int
    updated_at: DateTime


@dataclass(kw_only=True)
class PullRequestEdge:
    cursor: str
    node: Optional[PullRequest] = None


@dataclass(kw_only=True)
class GitActor:
    avatar_url: URI
    date: Optional[GitTimestamp] = None
    email: Optional[str] = None
    name: Optional[str] = None
    user: Optional[User] = None


@dataclass(kw_only=True)
class GitActorEdge:
    cursor: str
    node: Optional[GitActor] = None


@dataclass(kw_only=True)
class GitActorConnection:
    edges: Optional[list[GitActorEdge]] = None
    nodes: Optional[list[GitActor]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class BlameRange:
    age: int
    commit: Commit
    ending_line: int
    starting_line: int


@dataclass(kw_only=True)
class Blame:
    ranges: list[BlameRange]


@dataclass(kw_only=True)
class CheckAnnotationSpan:
    end: CheckAnnotationPosition
    start: CheckAnnotationPosition


@dataclass(kw_only=True)
class CheckAnnotation:
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
    cursor: str
    node: Optional[CheckAnnotation] = None


@dataclass(kw_only=True)
class CheckAnnotationConnection:
    edges: Optional[list[CheckAnnotationEdge]] = None
    nodes: Optional[list[CheckAnnotation]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class DeploymentRequest:
    current_user_can_approve: bool
    environment: Environment
    reviewers: DeploymentReviewerConnection
    wait_timer: int
    wait_timer_started_at: Optional[DateTime] = None


@dataclass(kw_only=True)
class CheckStepEdge:
    cursor: str
    node: Optional[CheckStep] = None


@dataclass(kw_only=True)
class CheckStepConnection:
    edges: Optional[list[CheckStepEdge]] = None
    nodes: Optional[list[CheckStep]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class CheckRun:
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
    cursor: str
    node: Optional[CheckRun] = None


@dataclass(kw_only=True)
class CheckRunConnection:
    edges: Optional[list[CheckRunEdge]] = None
    nodes: Optional[list[CheckRun]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class Push:
    id: ID
    next_sha: Optional[GitObjectID] = None
    permalink: URI
    previous_sha: Optional[GitObjectID] = None
    pusher: Actor
    repository: Repository


@dataclass(kw_only=True)
class DeploymentReview:
    comment: str
    database_id: Optional[int] = None
    environments: EnvironmentConnection
    id: ID
    state: DeploymentReviewState
    user: User


@dataclass(kw_only=True)
class DeploymentReviewEdge:
    cursor: str
    node: Optional[DeploymentReview] = None


@dataclass(kw_only=True)
class DeploymentReviewConnection:
    edges: Optional[list[DeploymentReviewEdge]] = None
    nodes: Optional[list[DeploymentReview]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class WorkflowRunFile:
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
    cursor: str
    node: Optional[DeploymentRequest] = None


@dataclass(kw_only=True)
class DeploymentRequestConnection:
    edges: Optional[list[DeploymentRequestEdge]] = None
    nodes: Optional[list[DeploymentRequest]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class WorkflowRunEdge:
    cursor: str
    node: Optional[WorkflowRun] = None


@dataclass(kw_only=True)
class WorkflowRunConnection:
    edges: Optional[list[WorkflowRunEdge]] = None
    nodes: Optional[list[WorkflowRun]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class Workflow:
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
    cursor: str
    node: Optional[CheckSuite] = None


@dataclass(kw_only=True)
class CheckSuiteConnection:
    edges: Optional[list[CheckSuiteEdge]] = None
    nodes: Optional[list[CheckSuite]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class TreeEntry:
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
    edges: Optional[list[CommitEdge]] = None
    nodes: Optional[list[Commit]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class CommitConnection:
    edges: Optional[list[CommitEdge]] = None
    nodes: Optional[list[Commit]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class GitSignature:
    email: str
    is_valid: bool
    payload: str
    signature: str
    signer: Optional[User] = None
    state: GitSignatureState
    was_signed_by_git_hub: bool


@dataclass(kw_only=True)
class StatusContext:
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
    cursor: str
    node: Optional[StatusCheckRollupContext] = None


@dataclass(kw_only=True)
class StatusCheckRollupContextConnection:
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
    combined_contexts: StatusCheckRollupContextConnection
    commit: Optional[Commit] = None
    context: Optional[StatusContext] = None
    contexts: list[StatusContext]
    id: ID
    state: StatusState


@dataclass(kw_only=True)
class StatusCheckRollup:
    commit: Optional[Commit] = None
    contexts: StatusCheckRollupContextConnection
    id: ID
    state: StatusState


@dataclass(kw_only=True)
class Tree:
    abbreviated_oid: str
    commit_resource_path: URI
    commit_url: URI
    entries: Optional[list[TreeEntry]] = None
    id: ID
    oid: GitObjectID
    repository: Repository


@dataclass(kw_only=True)
class CommitComment:
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
    cursor: str
    node: Optional[CommitComment] = None


@dataclass(kw_only=True)
class CreatedCommitContribution:
    commit_count: int
    is_restricted: bool
    occurred_at: DateTime
    repository: Repository
    resource_path: URI
    url: URI
    user: User


@dataclass(kw_only=True)
class CreatedCommitContributionEdge:
    cursor: str
    node: Optional[CreatedCommitContribution] = None


@dataclass(kw_only=True)
class CreatedCommitContributionConnection:
    edges: Optional[list[CreatedCommitContributionEdge]] = None
    nodes: Optional[list[CreatedCommitContribution]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class CommitContributionsByRepository:
    contributions: CreatedCommitContributionConnection
    repository: Repository
    resource_path: URI
    url: URI


@dataclass(kw_only=True)
class ContributionCalendarWeek:
    contribution_days: list[ContributionCalendarDay]
    first_day: Date


@dataclass(kw_only=True)
class ContributionCalendar:
    colors: list[str]
    is_halloween: bool
    months: list[ContributionCalendarMonth]
    total_contributions: int
    weeks: list[ContributionCalendarWeek]


@dataclass(kw_only=True)
class CreatedIssueContribution:
    is_restricted: bool
    issue: Issue
    occurred_at: DateTime
    resource_path: URI
    url: URI
    user: User


@dataclass(kw_only=True)
class RestrictedContribution:
    is_restricted: bool
    occurred_at: DateTime
    resource_path: URI
    url: URI
    user: User


@dataclass(kw_only=True)
class CreatedPullRequestContribution:
    is_restricted: bool
    occurred_at: DateTime
    pull_request: PullRequest
    resource_path: URI
    url: URI
    user: User


@dataclass(kw_only=True)
class CreatedRepositoryContribution:
    is_restricted: bool
    occurred_at: DateTime
    repository: Repository
    resource_path: URI
    url: URI
    user: User


@dataclass(kw_only=True)
class CreatedIssueContributionEdge:
    cursor: str
    node: Optional[CreatedIssueContribution] = None


@dataclass(kw_only=True)
class CreatedIssueContributionConnection:
    edges: Optional[list[CreatedIssueContributionEdge]] = None
    nodes: Optional[list[CreatedIssueContribution]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class IssueContributionsByRepository:
    contributions: CreatedIssueContributionConnection
    repository: Repository


@dataclass(kw_only=True)
class JoinedGitHubContribution:
    is_restricted: bool
    occurred_at: DateTime
    resource_path: URI
    url: URI
    user: User


@dataclass(kw_only=True)
class CreatedPullRequestContributionEdge:
    cursor: str
    node: Optional[CreatedPullRequestContribution] = None


@dataclass(kw_only=True)
class CreatedPullRequestContributionConnection:
    edges: Optional[list[CreatedPullRequestContributionEdge]] = None
    nodes: Optional[list[CreatedPullRequestContribution]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PullRequestContributionsByRepository:
    contributions: CreatedPullRequestContributionConnection
    repository: Repository


@dataclass(kw_only=True)
class CreatedPullRequestReviewContribution:
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
    cursor: str
    node: Optional[CreatedPullRequestReviewContribution] = None


@dataclass(kw_only=True)
class CreatedPullRequestReviewContributionConnection:
    edges: Optional[list[CreatedPullRequestReviewContributionEdge]] = None
    nodes: Optional[list[CreatedPullRequestReviewContribution]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PullRequestReviewContributionsByRepository:
    contributions: CreatedPullRequestReviewContributionConnection
    repository: Repository


@dataclass(kw_only=True)
class CreatedRepositoryContributionEdge:
    cursor: str
    node: Optional[CreatedRepositoryContribution] = None


@dataclass(kw_only=True)
class CreatedRepositoryContributionConnection:
    edges: Optional[list[CreatedRepositoryContributionEdge]] = None
    nodes: Optional[list[CreatedRepositoryContribution]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class EnterpriseEdge:
    cursor: str
    node: Optional[Enterprise] = None


@dataclass(kw_only=True)
class EnterpriseConnection:
    edges: Optional[list[EnterpriseEdge]] = None
    nodes: Optional[list[Enterprise]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class FollowerConnection:
    edges: Optional[list[UserEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class FollowingConnection:
    edges: Optional[list[UserEdge]] = None
    nodes: Optional[list[User]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class UserListItemsEdge:
    cursor: str
    node: Optional[UserListItems] = None


@dataclass(kw_only=True)
class UserListItemsConnection:
    edges: Optional[list[UserListItemsEdge]] = None
    nodes: Optional[list[UserListItems]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class UserList:
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
    cursor: str
    node: Optional[UserList] = None


@dataclass(kw_only=True)
class UserListConnection:
    edges: Optional[list[UserListEdge]] = None
    nodes: Optional[list[UserList]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class PublicKeyEdge:
    cursor: str
    node: Optional[PublicKey] = None


@dataclass(kw_only=True)
class PublicKeyConnection:
    edges: Optional[list[PublicKeyEdge]] = None
    nodes: Optional[list[PublicKey]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class SavedReply:
    body: str
    body_h_t_m_l: HTML
    database_id: Optional[int] = None
    id: ID
    title: str
    user: Optional[Actor] = None


@dataclass(kw_only=True)
class SavedReplyEdge:
    cursor: str
    node: Optional[SavedReply] = None


@dataclass(kw_only=True)
class SavedReplyConnection:
    edges: Optional[list[SavedReplyEdge]] = None
    nodes: Optional[list[SavedReply]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class SocialAccountEdge:
    cursor: str
    node: Optional[SocialAccount] = None


@dataclass(kw_only=True)
class SocialAccountConnection:
    edges: Optional[list[SocialAccountEdge]] = None
    nodes: Optional[list[SocialAccount]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class StarredRepositoryEdge:
    cursor: str
    node: Repository
    starred_at: DateTime


@dataclass(kw_only=True)
class StarredRepositoryConnection:
    edges: Optional[list[StarredRepositoryEdge]] = None
    is_over_limit: bool
    nodes: Optional[list[Repository]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class LinkedBranch:
    id: ID
    ref: Optional[Ref] = None


@dataclass(kw_only=True)
class LinkedBranchEdge:
    cursor: str
    node: Optional[LinkedBranch] = None


@dataclass(kw_only=True)
class LinkedBranchConnection:
    edges: Optional[list[LinkedBranchEdge]] = None
    nodes: Optional[list[LinkedBranch]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class IssueTimelineItemEdge:
    cursor: str
    node: Optional[IssueTimelineItem] = None


@dataclass(kw_only=True)
class IssueTimelineConnection:
    edges: Optional[list[IssueTimelineItemEdge]] = None
    nodes: Optional[list[IssueTimelineItem]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class IssueTimelineItemsEdge:
    cursor: str
    node: Optional[IssueTimelineItems] = None


@dataclass(kw_only=True)
class IssueTimelineItemsConnection:
    edges: Optional[list[IssueTimelineItemsEdge]] = None
    filtered_count: int
    nodes: Optional[list[IssueTimelineItems]] = None
    page_count: int
    page_info: PageInfo
    total_count: int
    updated_at: DateTime


@dataclass(kw_only=True)
class AddCommentPayload:
    client_mutation_id: Optional[str] = None
    comment_edge: Optional[IssueCommentEdge] = None
    subject: Optional[Node] = None
    timeline_edge: Optional[IssueTimelineItemEdge] = None


@dataclass(kw_only=True)
class AddProjectCardPayload:
    card_edge: Optional[ProjectCardEdge] = None
    client_mutation_id: Optional[str] = None
    project_column: Optional[ProjectColumn] = None


@dataclass(kw_only=True)
class AddProjectColumnPayload:
    client_mutation_id: Optional[str] = None
    column_edge: Optional[ProjectColumnEdge] = None
    project: Optional[Project] = None


@dataclass(kw_only=True)
class AddPullRequestReviewCommentPayload:
    client_mutation_id: Optional[str] = None
    comment: Optional[PullRequestReviewComment] = None
    comment_edge: Optional[PullRequestReviewCommentEdge] = None


@dataclass(kw_only=True)
class AddPullRequestReviewInput:
    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    comments: Optional[list[DraftPullRequestReviewComment]] = None
    commit_o_i_d: Optional[GitObjectID] = None
    event: Optional[PullRequestReviewEvent] = None
    pull_request_id: ID
    threads: Optional[list[DraftPullRequestReviewThread]] = None


@dataclass(kw_only=True)
class AddPullRequestReviewPayload:
    client_mutation_id: Optional[str] = None
    pull_request_review: Optional[PullRequestReview] = None
    review_edge: Optional[PullRequestReviewEdge] = None


@dataclass(kw_only=True)
class AddReactionPayload:
    client_mutation_id: Optional[str] = None
    reaction: Optional[Reaction] = None
    reaction_groups: Optional[list[ReactionGroup]] = None
    subject: Optional[Reactable] = None


@dataclass(kw_only=True)
class AuditEntry:
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
    annotation_level: CheckAnnotationLevel
    location: CheckAnnotationRange
    message: str
    path: str
    raw_details: Optional[str] = None
    title: Optional[str] = None


@dataclass(kw_only=True)
class CheckRunOutput:
    annotations: Optional[list[CheckAnnotationData]] = None
    images: Optional[list[CheckRunOutputImage]] = None
    summary: str
    text: Optional[str] = None
    title: str


@dataclass(kw_only=True)
class Comment:
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
    client_mutation_id: Optional[str] = None
    owner: Optional[Organization] = None
    source: Optional[Claimable] = None
    target: Optional[Claimable] = None


@dataclass(kw_only=True)
class CreateCheckRunInput:
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
    additions: Optional[list[FileAddition]] = None
    deletions: Optional[list[FileDeletion]] = None


@dataclass(kw_only=True)
class CreateCommitOnBranchInput:
    branch: CommittableBranch
    client_mutation_id: Optional[str] = None
    expected_head_oid: GitObjectID
    file_changes: Optional[FileChanges] = None
    message: CommitMessage


@dataclass(kw_only=True)
class CreateCommitOnBranchPayload:
    client_mutation_id: Optional[str] = None
    commit: Optional[Commit] = None
    ref: Optional[Ref] = None


@dataclass(kw_only=True)
class CreateEnterpriseOrganizationPayload:
    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    organization: Optional[Organization] = None


@dataclass(kw_only=True)
class CreateLinkedBranchPayload:
    client_mutation_id: Optional[str] = None
    issue: Optional[Issue] = None
    linked_branch: Optional[LinkedBranch] = None


@dataclass(kw_only=True)
class RepositoryPropertyConditionTargetInput:
    exclude: list[PropertyTargetDefinitionInput]
    include: list[PropertyTargetDefinitionInput]


@dataclass(kw_only=True)
class RepositoryRuleConditionsInput:
    ref_name: Optional[RefNameConditionTargetInput] = None
    repository_id: Optional[RepositoryIdConditionTargetInput] = None
    repository_name: Optional[RepositoryNameConditionTargetInput] = None
    repository_property: Optional[RepositoryPropertyConditionTargetInput] = None


@dataclass(kw_only=True)
class RequiredStatusChecksParametersInput:
    required_status_checks: list[StatusCheckConfigurationInput]
    strict_required_status_checks_policy: bool


@dataclass(kw_only=True)
class WorkflowsParametersInput:
    workflows: list[WorkflowFileReferenceInput]


@dataclass(kw_only=True)
class RuleParametersInput:
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
    id: Optional[ID] = None
    parameters: Optional[RuleParametersInput] = None
    type: RepositoryRuleType


@dataclass(kw_only=True)
class CreateRepositoryRulesetInput:
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
    client_mutation_id: Optional[str] = None
    list: Optional[UserList] = None
    viewer: Optional[User] = None


@dataclass(kw_only=True)
class DeletePullRequestReviewCommentPayload:
    client_mutation_id: Optional[str] = None
    pull_request_review: Optional[PullRequestReview] = None
    pull_request_review_comment: Optional[PullRequestReviewComment] = None


@dataclass(kw_only=True)
class DisablePullRequestAutoMergePayload:
    actor: Optional[Actor] = None
    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class EnablePullRequestAutoMergePayload:
    actor: Optional[Actor] = None
    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class LinkRepositoryToProjectPayload:
    client_mutation_id: Optional[str] = None
    project: Optional[Project] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class LockLockablePayload:
    actor: Optional[Actor] = None
    client_mutation_id: Optional[str] = None
    locked_record: Optional[Lockable] = None


@dataclass(kw_only=True)
class MarketplaceListing:
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
    cursor: str
    node: Optional[MarketplaceListing] = None


@dataclass(kw_only=True)
class MarketplaceListingConnection:
    edges: Optional[list[MarketplaceListingEdge]] = None
    nodes: Optional[list[MarketplaceListing]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class MergePullRequestPayload:
    actor: Optional[Actor] = None
    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class ProfileOwner:
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
    cursor: str
    node: Optional[ProjectV2Actor] = None


@dataclass(kw_only=True)
class ProjectV2ActorConnection:
    edges: Optional[list[ProjectV2ActorEdge]] = None
    nodes: Optional[list[ProjectV2Actor]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class ProjectV2ItemFieldValueCommon:
    created_at: DateTime
    creator: Optional[Actor] = None
    database_id: Optional[int] = None
    field: ProjectV2FieldConfiguration
    id: ID
    item: ProjectV2Item
    updated_at: DateTime


@dataclass(kw_only=True)
class PullRequestThread:
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
    admin: Optional[User] = None
    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None
    viewer: Optional[User] = None


@dataclass(kw_only=True)
class RemoveEnterpriseMemberPayload:
    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    user: Optional[User] = None
    viewer: Optional[User] = None


@dataclass(kw_only=True)
class RemoveEnterpriseOrganizationPayload:
    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    organization: Optional[Organization] = None
    viewer: Optional[User] = None


@dataclass(kw_only=True)
class RemoveReactionPayload:
    client_mutation_id: Optional[str] = None
    reaction: Optional[Reaction] = None
    reaction_groups: Optional[list[ReactionGroup]] = None
    subject: Optional[Reactable] = None


@dataclass(kw_only=True)
class RequestReviewsPayload:
    actor: Optional[Actor] = None
    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None
    requested_reviewers_edge: Optional[UserEdge] = None


@dataclass(kw_only=True)
class RevertPullRequestPayload:
    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None
    revert_pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class TextMatch:
    fragment: str
    highlights: list[TextMatchHighlight]
    property: str


@dataclass(kw_only=True)
class SearchResultItemEdge:
    cursor: str
    node: Optional[SearchResultItem] = None
    text_matches: Optional[list[TextMatch]] = None


@dataclass(kw_only=True)
class SearchResultItemConnection:
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
    cursor: str
    node: Optional[SecurityAdvisory] = None


@dataclass(kw_only=True)
class SecurityAdvisoryConnection:
    edges: Optional[list[SecurityAdvisoryEdge]] = None
    nodes: Optional[list[SecurityAdvisory]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class SponsorableItemEdge:
    cursor: str
    node: Optional[SponsorableItem] = None


@dataclass(kw_only=True)
class SponsorableItemConnection:
    edges: Optional[list[SponsorableItemEdge]] = None
    nodes: Optional[list[SponsorableItem]] = None
    page_info: PageInfo
    total_count: int


@dataclass(kw_only=True)
class Tag:
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
    client_mutation_id: Optional[str] = None
    project: Optional[Project] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class UnlockLockablePayload:
    actor: Optional[Actor] = None
    client_mutation_id: Optional[str] = None
    unlocked_record: Optional[Lockable] = None


@dataclass(kw_only=True)
class UpdateCheckRunInput:
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
    actor: Optional[Actor] = None
    client_mutation_id: Optional[str] = None
    issue: Optional[Issue] = None


@dataclass(kw_only=True)
class UpdatePullRequestPayload:
    actor: Optional[Actor] = None
    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class UpdateRepositoryRulesetInput:
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
    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None
    teams: Optional[list[Team]] = None


@dataclass(kw_only=True)
class UpdateUserListsForItemPayload:
    client_mutation_id: Optional[str] = None
    item: Optional[UserListItems] = None
    lists: Optional[list[UserList]] = None
    user: Optional[User] = None


@dataclass(kw_only=True)
class ViewerHovercardContext:
    message: str
    octicon: str
    viewer: User


@dataclass(kw_only=True)
class VerifyVerifiableDomainPayload:
    client_mutation_id: Optional[str] = None
    domain: Optional[VerifiableDomain] = None


@dataclass(kw_only=True)
class UpdateUserListPayload:
    client_mutation_id: Optional[str] = None
    list: Optional[UserList] = None


@dataclass(kw_only=True)
class UpdateTopicsPayload:
    client_mutation_id: Optional[str] = None
    invalid_topic_names: Optional[list[str]] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class UpdateTeamReviewAssignmentPayload:
    client_mutation_id: Optional[str] = None
    team: Optional[Team] = None


@dataclass(kw_only=True)
class UpdateTeamDiscussionPayload:
    client_mutation_id: Optional[str] = None
    team_discussion: Optional[TeamDiscussion] = None


@dataclass(kw_only=True)
class UpdateTeamDiscussionCommentPayload:
    client_mutation_id: Optional[str] = None
    team_discussion_comment: Optional[TeamDiscussionComment] = None


@dataclass(kw_only=True)
class UpdateSubscriptionPayload:
    client_mutation_id: Optional[str] = None
    subscribable: Optional[Subscribable] = None


@dataclass(kw_only=True)
class UpdateSponsorshipPreferencesPayload:
    client_mutation_id: Optional[str] = None
    sponsorship: Optional[Sponsorship] = None


@dataclass(kw_only=True)
class UpdateRepositoryWebCommitSignoffSettingPayload:
    client_mutation_id: Optional[str] = None
    message: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class UpdateRepositoryRulesetPayload:
    client_mutation_id: Optional[str] = None
    ruleset: Optional[RepositoryRuleset] = None


@dataclass(kw_only=True)
class UpdateRepositoryPayload:
    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class UpdateRefsInput:
    client_mutation_id: Optional[str] = None
    ref_updates: list[RefUpdate]
    repository_id: ID


@dataclass(kw_only=True)
class UpdateRefPayload:
    client_mutation_id: Optional[str] = None
    ref: Optional[Ref] = None


@dataclass(kw_only=True)
class UpdatePullRequestReviewPayload:
    client_mutation_id: Optional[str] = None
    pull_request_review: Optional[PullRequestReview] = None


@dataclass(kw_only=True)
class UpdatePullRequestReviewCommentPayload:
    client_mutation_id: Optional[str] = None
    pull_request_review_comment: Optional[PullRequestReviewComment] = None


@dataclass(kw_only=True)
class UpdatePullRequestBranchPayload:
    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class UpdateProjectV2Payload:
    client_mutation_id: Optional[str] = None
    project_v2: Optional[ProjectV2] = None


@dataclass(kw_only=True)
class UpdateProjectV2ItemPositionPayload:
    client_mutation_id: Optional[str] = None
    items: Optional[ProjectV2ItemConnection] = None


@dataclass(kw_only=True)
class UpdateProjectV2ItemFieldValuePayload:
    client_mutation_id: Optional[str] = None
    project_v2_item: Optional[ProjectV2Item] = None


@dataclass(kw_only=True)
class UpdateProjectV2ItemFieldValueInput:
    client_mutation_id: Optional[str] = None
    field_id: ID
    item_id: ID
    project_id: ID
    value: ProjectV2FieldValue


@dataclass(kw_only=True)
class UpdateProjectV2DraftIssuePayload:
    client_mutation_id: Optional[str] = None
    draft_issue: Optional[DraftIssue] = None


@dataclass(kw_only=True)
class UpdateProjectV2CollaboratorsPayload:
    client_mutation_id: Optional[str] = None
    collaborators: Optional[ProjectV2ActorConnection] = None


@dataclass(kw_only=True)
class UpdateProjectV2CollaboratorsInput:
    client_mutation_id: Optional[str] = None
    collaborators: list[ProjectV2Collaborator]
    project_id: ID


@dataclass(kw_only=True)
class UpdateProjectPayload:
    client_mutation_id: Optional[str] = None
    project: Optional[Project] = None


@dataclass(kw_only=True)
class UpdateProjectColumnPayload:
    client_mutation_id: Optional[str] = None
    project_column: Optional[ProjectColumn] = None


@dataclass(kw_only=True)
class UpdateProjectCardPayload:
    client_mutation_id: Optional[str] = None
    project_card: Optional[ProjectCard] = None


@dataclass(kw_only=True)
class UpdatePatreonSponsorabilityPayload:
    client_mutation_id: Optional[str] = None
    sponsors_listing: Optional[SponsorsListing] = None


@dataclass(kw_only=True)
class UpdateOrganizationWebCommitSignoffSettingPayload:
    client_mutation_id: Optional[str] = None
    message: Optional[str] = None
    organization: Optional[Organization] = None


@dataclass(kw_only=True)
class UpdateOrganizationAllowPrivateRepositoryForkingSettingPayload:
    client_mutation_id: Optional[str] = None
    message: Optional[str] = None
    organization: Optional[Organization] = None


@dataclass(kw_only=True)
class UpdateNotificationRestrictionSettingPayload:
    client_mutation_id: Optional[str] = None
    owner: Optional[VerifiableDomainOwner] = None


@dataclass(kw_only=True)
class UpdateLabelPayload:
    client_mutation_id: Optional[str] = None
    label: Optional[Label] = None


@dataclass(kw_only=True)
class UpdateIssueCommentPayload:
    client_mutation_id: Optional[str] = None
    issue_comment: Optional[IssueComment] = None


@dataclass(kw_only=True)
class UpdateIpAllowListForInstalledAppsEnabledSettingPayload:
    client_mutation_id: Optional[str] = None
    owner: Optional[IpAllowListOwner] = None


@dataclass(kw_only=True)
class UpdateIpAllowListEntryPayload:
    client_mutation_id: Optional[str] = None
    ip_allow_list_entry: Optional[IpAllowListEntry] = None


@dataclass(kw_only=True)
class UpdateIpAllowListEnabledSettingPayload:
    client_mutation_id: Optional[str] = None
    owner: Optional[IpAllowListOwner] = None


@dataclass(kw_only=True)
class UpdateEnvironmentPayload:
    client_mutation_id: Optional[str] = None
    environment: Optional[Environment] = None


@dataclass(kw_only=True)
class UpdateEnterpriseTwoFactorAuthenticationRequiredSettingPayload:
    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseTeamDiscussionsSettingPayload:
    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseRepositoryProjectsSettingPayload:
    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseProfilePayload:
    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None


@dataclass(kw_only=True)
class UpdateEnterpriseOrganizationProjectsSettingPayload:
    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanViewDependencyInsightsSettingPayload:
    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingPayload:
    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanMakePurchasesSettingPayload:
    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanInviteCollaboratorsSettingPayload:
    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanDeleteRepositoriesSettingPayload:
    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanDeleteIssuesSettingPayload:
    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanCreateRepositoriesSettingPayload:
    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingPayload:
    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseDefaultRepositoryPermissionSettingPayload:
    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseAllowPrivateRepositoryForkingSettingPayload:
    client_mutation_id: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateDiscussionPayload:
    client_mutation_id: Optional[str] = None
    discussion: Optional[Discussion] = None


@dataclass(kw_only=True)
class UpdateDiscussionCommentPayload:
    client_mutation_id: Optional[str] = None
    comment: Optional[DiscussionComment] = None


@dataclass(kw_only=True)
class UpdateCheckSuitePreferencesPayload:
    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class UpdateCheckSuitePreferencesInput:
    auto_trigger_preferences: list[CheckSuiteAutoTriggerPreference]
    client_mutation_id: Optional[str] = None
    repository_id: ID


@dataclass(kw_only=True)
class UpdateCheckRunPayload:
    check_run: Optional[CheckRun] = None
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class UpdateBranchProtectionRulePayload:
    branch_protection_rule: Optional[BranchProtectionRule] = None
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class UpdateBranchProtectionRuleInput:
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
    client_mutation_id: Optional[str] = None
    thread: Optional[PullRequestReviewThread] = None


@dataclass(kw_only=True)
class UnpinIssuePayload:
    client_mutation_id: Optional[str] = None
    id: Optional[ID] = None
    issue: Optional[Issue] = None


@dataclass(kw_only=True)
class UnminimizeCommentPayload:
    client_mutation_id: Optional[str] = None
    unminimized_comment: Optional[Minimizable] = None


@dataclass(kw_only=True)
class UnmarkProjectV2AsTemplatePayload:
    client_mutation_id: Optional[str] = None
    project_v2: Optional[ProjectV2] = None


@dataclass(kw_only=True)
class UnmarkIssueAsDuplicatePayload:
    client_mutation_id: Optional[str] = None
    duplicate: Optional[IssueOrPullRequest] = None


@dataclass(kw_only=True)
class UnmarkFileAsViewedPayload:
    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class UnmarkDiscussionCommentAsAnswerPayload:
    client_mutation_id: Optional[str] = None
    discussion: Optional[Discussion] = None


@dataclass(kw_only=True)
class UnlinkProjectV2FromTeamPayload:
    client_mutation_id: Optional[str] = None
    team: Optional[Team] = None


@dataclass(kw_only=True)
class UnlinkProjectV2FromRepositoryPayload:
    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class UnknownSignature:
    email: str
    is_valid: bool
    payload: str
    signature: str
    signer: Optional[User] = None
    state: GitSignatureState
    was_signed_by_git_hub: bool


@dataclass(kw_only=True)
class UnfollowUserPayload:
    client_mutation_id: Optional[str] = None
    user: Optional[User] = None


@dataclass(kw_only=True)
class UnfollowOrganizationPayload:
    client_mutation_id: Optional[str] = None
    organization: Optional[Organization] = None


@dataclass(kw_only=True)
class UnarchiveRepositoryPayload:
    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class UnarchiveProjectV2ItemPayload:
    client_mutation_id: Optional[str] = None
    item: Optional[ProjectV2Item] = None


@dataclass(kw_only=True)
class TransferIssuePayload:
    client_mutation_id: Optional[str] = None
    issue: Optional[Issue] = None


@dataclass(kw_only=True)
class TransferEnterpriseOrganizationPayload:
    client_mutation_id: Optional[str] = None
    organization: Optional[Organization] = None


@dataclass(kw_only=True)
class TopicAuditEntryData:
    topic: Optional[Topic] = None
    topic_name: Optional[str] = None


@dataclass(kw_only=True)
class TeamAuditEntryData:
    team: Optional[Team] = None
    team_name: Optional[str] = None
    team_resource_path: Optional[URI] = None
    team_url: Optional[URI] = None


@dataclass(kw_only=True)
class SubmitPullRequestReviewPayload:
    client_mutation_id: Optional[str] = None
    pull_request_review: Optional[PullRequestReview] = None


@dataclass(kw_only=True)
class StartRepositoryMigrationPayload:
    client_mutation_id: Optional[str] = None
    repository_migration: Optional[RepositoryMigration] = None


@dataclass(kw_only=True)
class StartOrganizationMigrationPayload:
    client_mutation_id: Optional[str] = None
    org_migration: Optional[OrganizationMigration] = None


@dataclass(kw_only=True)
class Starrable:
    id: ID
    stargazer_count: int
    stargazers: StargazerConnection
    viewer_has_starred: bool


@dataclass(kw_only=True)
class SshSignature:
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
    email: str
    is_valid: bool
    payload: str
    signature: str
    signer: Optional[User] = None
    state: GitSignatureState
    was_signed_by_git_hub: bool


@dataclass(kw_only=True)
class SetUserInteractionLimitPayload:
    client_mutation_id: Optional[str] = None
    user: Optional[User] = None


@dataclass(kw_only=True)
class SetRepositoryInteractionLimitPayload:
    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class SetOrganizationInteractionLimitPayload:
    client_mutation_id: Optional[str] = None
    organization: Optional[Organization] = None


@dataclass(kw_only=True)
class SetEnterpriseIdentityProviderPayload:
    client_mutation_id: Optional[str] = None
    identity_provider: Optional[EnterpriseIdentityProvider] = None


@dataclass(kw_only=True)
class RevokeEnterpriseOrganizationsMigratorRolePayload:
    client_mutation_id: Optional[str] = None
    organizations: Optional[OrganizationConnection] = None


@dataclass(kw_only=True)
class RetireSponsorsTierPayload:
    client_mutation_id: Optional[str] = None
    sponsors_tier: Optional[SponsorsTier] = None


@dataclass(kw_only=True)
class ResolveReviewThreadPayload:
    client_mutation_id: Optional[str] = None
    thread: Optional[PullRequestReviewThread] = None


@dataclass(kw_only=True)
class RerequestCheckSuitePayload:
    check_suite: Optional[CheckSuite] = None
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class RepositoryNode:
    repository: Repository


@dataclass(kw_only=True)
class RepositoryDiscussionCommentAuthor:
    repository_discussion_comments: DiscussionCommentConnection


@dataclass(kw_only=True)
class RepositoryDiscussionAuthor:
    repository_discussions: DiscussionConnection


@dataclass(kw_only=True)
class RepositoryAuditEntryData:
    repository: Optional[Repository] = None
    repository_name: Optional[str] = None
    repository_resource_path: Optional[URI] = None
    repository_url: Optional[URI] = None


@dataclass(kw_only=True)
class ReopenPullRequestPayload:
    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class ReopenIssuePayload:
    client_mutation_id: Optional[str] = None
    issue: Optional[Issue] = None


@dataclass(kw_only=True)
class ReopenDiscussionPayload:
    client_mutation_id: Optional[str] = None
    discussion: Optional[Discussion] = None


@dataclass(kw_only=True)
class RemoveUpvotePayload:
    client_mutation_id: Optional[str] = None
    subject: Optional[Votable] = None


@dataclass(kw_only=True)
class RemoveStarPayload:
    client_mutation_id: Optional[str] = None
    starrable: Optional[Starrable] = None


@dataclass(kw_only=True)
class RemoveOutsideCollaboratorPayload:
    client_mutation_id: Optional[str] = None
    removed_user: Optional[User] = None


@dataclass(kw_only=True)
class RemoveLabelsFromLabelablePayload:
    client_mutation_id: Optional[str] = None
    labelable: Optional[Labelable] = None


@dataclass(kw_only=True)
class RemoveEnterpriseIdentityProviderPayload:
    client_mutation_id: Optional[str] = None
    identity_provider: Optional[EnterpriseIdentityProvider] = None


@dataclass(kw_only=True)
class RemoveAssigneesFromAssignablePayload:
    assignable: Optional[Assignable] = None
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class RejectDeploymentsPayload:
    client_mutation_id: Optional[str] = None
    deployments: Optional[list[Deployment]] = None


@dataclass(kw_only=True)
class RegenerateEnterpriseIdentityProviderRecoveryCodesPayload:
    client_mutation_id: Optional[str] = None
    identity_provider: Optional[EnterpriseIdentityProvider] = None


@dataclass(kw_only=True)
class PublishSponsorsTierPayload:
    client_mutation_id: Optional[str] = None
    sponsors_tier: Optional[SponsorsTier] = None


@dataclass(kw_only=True)
class ProjectV2Recent:
    recent_projects: ProjectV2Connection


@dataclass(kw_only=True)
class ProjectV2FieldCommon:
    created_at: DateTime
    data_type: ProjectV2FieldType
    database_id: Optional[int] = None
    id: ID
    name: str
    project: ProjectV2
    updated_at: DateTime


@dataclass(kw_only=True)
class ProjectColumnImport:
    column_name: str
    issues: Optional[list[ProjectCardImport]] = None
    position: int


@dataclass(kw_only=True)
class PinIssuePayload:
    client_mutation_id: Optional[str] = None
    issue: Optional[Issue] = None


@dataclass(kw_only=True)
class PackageTag:
    id: ID
    name: str
    version: Optional[PackageVersion] = None


@dataclass(kw_only=True)
class PackageOwner:
    id: ID
    packages: PackageConnection


@dataclass(kw_only=True)
class OrganizationsHovercardContext:
    message: str
    octicon: str
    relevant_organizations: OrganizationConnection
    total_organization_count: int


@dataclass(kw_only=True)
class OrganizationTeamsHovercardContext:
    message: str
    octicon: str
    relevant_teams: TeamConnection
    teams_resource_path: URI
    teams_url: URI
    total_team_count: int


@dataclass(kw_only=True)
class OrganizationAuditEntryData:
    organization: Optional[Organization] = None
    organization_name: Optional[str] = None
    organization_resource_path: Optional[URI] = None
    organization_url: Optional[URI] = None


@dataclass(kw_only=True)
class MoveProjectColumnPayload:
    client_mutation_id: Optional[str] = None
    column_edge: Optional[ProjectColumnEdge] = None


@dataclass(kw_only=True)
class MoveProjectCardPayload:
    card_edge: Optional[ProjectCardEdge] = None
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class MinimizeCommentPayload:
    client_mutation_id: Optional[str] = None
    minimized_comment: Optional[Minimizable] = None


@dataclass(kw_only=True)
class Migration:
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
    client_mutation_id: Optional[str] = None
    merge_commit: Optional[Commit] = None


@dataclass(kw_only=True)
class MemberStatusable:
    member_statuses: UserStatusConnection


@dataclass(kw_only=True)
class MarkPullRequestReadyForReviewPayload:
    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class MarkProjectV2AsTemplatePayload:
    client_mutation_id: Optional[str] = None
    project_v2: Optional[ProjectV2] = None


@dataclass(kw_only=True)
class MarkNotificationAsDonePayload:
    client_mutation_id: Optional[str] = None
    success: Optional[bool] = None
    viewer: Optional[User] = None


@dataclass(kw_only=True)
class MarkFileAsViewedPayload:
    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class MarkDiscussionCommentAsAnswerPayload:
    client_mutation_id: Optional[str] = None
    discussion: Optional[Discussion] = None


@dataclass(kw_only=True)
class LinkProjectV2ToTeamPayload:
    client_mutation_id: Optional[str] = None
    team: Optional[Team] = None


@dataclass(kw_only=True)
class LinkProjectV2ToRepositoryPayload:
    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class InviteEnterpriseAdminPayload:
    client_mutation_id: Optional[str] = None
    invitation: Optional[EnterpriseAdministratorInvitation] = None


@dataclass(kw_only=True)
class ImportProjectPayload:
    client_mutation_id: Optional[str] = None
    project: Optional[Project] = None


@dataclass(kw_only=True)
class ImportProjectInput:
    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    column_imports: list[ProjectColumnImport]
    name: str
    owner_name: str
    public: Optional[bool] = None


@dataclass(kw_only=True)
class GrantEnterpriseOrganizationsMigratorRolePayload:
    client_mutation_id: Optional[str] = None
    organizations: Optional[OrganizationConnection] = None


@dataclass(kw_only=True)
class GpgSignature:
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
    client_mutation_id: Optional[str] = None
    user: Optional[User] = None


@dataclass(kw_only=True)
class FollowOrganizationPayload:
    client_mutation_id: Optional[str] = None
    organization: Optional[Organization] = None


@dataclass(kw_only=True)
class EnqueuePullRequestPayload:
    client_mutation_id: Optional[str] = None
    merge_queue_entry: Optional[MergeQueueEntry] = None


@dataclass(kw_only=True)
class DismissRepositoryVulnerabilityAlertPayload:
    client_mutation_id: Optional[str] = None
    repository_vulnerability_alert: Optional[RepositoryVulnerabilityAlert] = None


@dataclass(kw_only=True)
class DismissPullRequestReviewPayload:
    client_mutation_id: Optional[str] = None
    pull_request_review: Optional[PullRequestReview] = None


@dataclass(kw_only=True)
class DequeuePullRequestPayload:
    client_mutation_id: Optional[str] = None
    merge_queue_entry: Optional[MergeQueueEntry] = None


@dataclass(kw_only=True)
class DeleteVerifiableDomainPayload:
    client_mutation_id: Optional[str] = None
    owner: Optional[VerifiableDomainOwner] = None


@dataclass(kw_only=True)
class DeleteUserListPayload:
    client_mutation_id: Optional[str] = None
    user: Optional[User] = None


@dataclass(kw_only=True)
class DeletePullRequestReviewPayload:
    client_mutation_id: Optional[str] = None
    pull_request_review: Optional[PullRequestReview] = None


@dataclass(kw_only=True)
class DeleteProjectV2WorkflowPayload:
    client_mutation_id: Optional[str] = None
    deleted_workflow_id: Optional[ID] = None
    project_v2: Optional[ProjectV2] = None


@dataclass(kw_only=True)
class DeleteProjectV2Payload:
    client_mutation_id: Optional[str] = None
    project_v2: Optional[ProjectV2] = None


@dataclass(kw_only=True)
class DeleteProjectV2FieldPayload:
    client_mutation_id: Optional[str] = None
    project_v2_field: Optional[ProjectV2FieldConfiguration] = None


@dataclass(kw_only=True)
class DeleteProjectPayload:
    client_mutation_id: Optional[str] = None
    owner: Optional[ProjectOwner] = None


@dataclass(kw_only=True)
class DeleteProjectColumnPayload:
    client_mutation_id: Optional[str] = None
    deleted_column_id: Optional[ID] = None
    project: Optional[Project] = None


@dataclass(kw_only=True)
class DeleteProjectCardPayload:
    client_mutation_id: Optional[str] = None
    column: Optional[ProjectColumn] = None
    deleted_card_id: Optional[ID] = None


@dataclass(kw_only=True)
class DeleteLinkedBranchPayload:
    client_mutation_id: Optional[str] = None
    issue: Optional[Issue] = None


@dataclass(kw_only=True)
class DeleteIssuePayload:
    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class DeleteIpAllowListEntryPayload:
    client_mutation_id: Optional[str] = None
    ip_allow_list_entry: Optional[IpAllowListEntry] = None


@dataclass(kw_only=True)
class DeleteDiscussionPayload:
    client_mutation_id: Optional[str] = None
    discussion: Optional[Discussion] = None


@dataclass(kw_only=True)
class DeleteDiscussionCommentPayload:
    client_mutation_id: Optional[str] = None
    comment: Optional[DiscussionComment] = None


@dataclass(kw_only=True)
class DeclineTopicSuggestionPayload:
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class CreateTeamDiscussionPayload:
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class CreateTeamDiscussionCommentPayload:
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class CreateSponsorshipsPayload:
    client_mutation_id: Optional[str] = None
    sponsorables: Optional[list[Sponsorable]] = None


@dataclass(kw_only=True)
class CreateSponsorshipsInput:
    client_mutation_id: Optional[str] = None
    privacy_level: Optional[SponsorshipPrivacy] = None
    receive_emails: Optional[bool] = None
    recurring: Optional[bool] = None
    sponsor_login: str
    sponsorships: list[BulkSponsorship]


@dataclass(kw_only=True)
class CreateSponsorshipPayload:
    client_mutation_id: Optional[str] = None
    sponsorship: Optional[Sponsorship] = None


@dataclass(kw_only=True)
class CreateSponsorsTierPayload:
    client_mutation_id: Optional[str] = None
    sponsors_tier: Optional[SponsorsTier] = None


@dataclass(kw_only=True)
class CreateSponsorsListingPayload:
    client_mutation_id: Optional[str] = None
    sponsors_listing: Optional[SponsorsListing] = None


@dataclass(kw_only=True)
class CreateRepositoryRulesetPayload:
    client_mutation_id: Optional[str] = None
    ruleset: Optional[RepositoryRuleset] = None


@dataclass(kw_only=True)
class CreateRepositoryPayload:
    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class CreateRefPayload:
    client_mutation_id: Optional[str] = None
    ref: Optional[Ref] = None


@dataclass(kw_only=True)
class CreatePullRequestPayload:
    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class CreateProjectV2Payload:
    client_mutation_id: Optional[str] = None
    project_v2: Optional[ProjectV2] = None


@dataclass(kw_only=True)
class CreateProjectV2FieldPayload:
    client_mutation_id: Optional[str] = None
    project_v2_field: Optional[ProjectV2FieldConfiguration] = None


@dataclass(kw_only=True)
class CreateProjectV2FieldInput:
    client_mutation_id: Optional[str] = None
    data_type: ProjectV2CustomFieldType
    name: str
    project_id: ID
    single_select_options: Optional[list[ProjectV2SingleSelectFieldOptionInput]] = None


@dataclass(kw_only=True)
class CreateProjectPayload:
    client_mutation_id: Optional[str] = None
    project: Optional[Project] = None


@dataclass(kw_only=True)
class CreateMigrationSourcePayload:
    client_mutation_id: Optional[str] = None
    migration_source: Optional[MigrationSource] = None


@dataclass(kw_only=True)
class CreateLabelPayload:
    client_mutation_id: Optional[str] = None
    label: Optional[Label] = None


@dataclass(kw_only=True)
class CreateIssuePayload:
    client_mutation_id: Optional[str] = None
    issue: Optional[Issue] = None


@dataclass(kw_only=True)
class CreateIpAllowListEntryPayload:
    client_mutation_id: Optional[str] = None
    ip_allow_list_entry: Optional[IpAllowListEntry] = None


@dataclass(kw_only=True)
class CreateEnvironmentPayload:
    client_mutation_id: Optional[str] = None
    environment: Optional[Environment] = None


@dataclass(kw_only=True)
class CreateDiscussionPayload:
    client_mutation_id: Optional[str] = None
    discussion: Optional[Discussion] = None


@dataclass(kw_only=True)
class CreateDeploymentStatusPayload:
    client_mutation_id: Optional[str] = None
    deployment_status: Optional[DeploymentStatus] = None


@dataclass(kw_only=True)
class CreateDeploymentPayload:
    auto_merged: Optional[bool] = None
    client_mutation_id: Optional[str] = None
    deployment: Optional[Deployment] = None


@dataclass(kw_only=True)
class CreateCheckSuitePayload:
    check_suite: Optional[CheckSuite] = None
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class CreateCheckRunPayload:
    check_run: Optional[CheckRun] = None
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class CreateBranchProtectionRulePayload:
    branch_protection_rule: Optional[BranchProtectionRule] = None
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class CreateBranchProtectionRuleInput:
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
    client_mutation_id: Optional[str] = None
    project_v2: Optional[ProjectV2] = None


@dataclass(kw_only=True)
class ConvertPullRequestToDraftPayload:
    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class ConvertProjectCardNoteToIssuePayload:
    client_mutation_id: Optional[str] = None
    project_card: Optional[ProjectCard] = None


@dataclass(kw_only=True)
class Contribution:
    is_restricted: bool
    occurred_at: DateTime
    resource_path: URI
    url: URI
    user: User


@dataclass(kw_only=True)
class ClosePullRequestPayload:
    client_mutation_id: Optional[str] = None
    pull_request: Optional[PullRequest] = None


@dataclass(kw_only=True)
class CloseIssuePayload:
    client_mutation_id: Optional[str] = None
    issue: Optional[Issue] = None


@dataclass(kw_only=True)
class CloseDiscussionPayload:
    client_mutation_id: Optional[str] = None
    discussion: Optional[Discussion] = None


@dataclass(kw_only=True)
class CloneTemplateRepositoryPayload:
    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class CloneProjectPayload:
    client_mutation_id: Optional[str] = None
    job_status_id: Optional[str] = None
    project: Optional[Project] = None


@dataclass(kw_only=True)
class ClearProjectV2ItemFieldValuePayload:
    client_mutation_id: Optional[str] = None
    project_v2_item: Optional[ProjectV2Item] = None


@dataclass(kw_only=True)
class ClearLabelsFromLabelablePayload:
    client_mutation_id: Optional[str] = None
    labelable: Optional[Labelable] = None


@dataclass(kw_only=True)
class ChangeUserStatusPayload:
    client_mutation_id: Optional[str] = None
    status: Optional[UserStatus] = None


@dataclass(kw_only=True)
class CancelSponsorshipPayload:
    client_mutation_id: Optional[str] = None
    sponsors_tier: Optional[SponsorsTier] = None


@dataclass(kw_only=True)
class CancelEnterpriseAdminInvitationPayload:
    client_mutation_id: Optional[str] = None
    invitation: Optional[EnterpriseAdministratorInvitation] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class Blob:
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
    client_mutation_id: Optional[str] = None
    repository: Optional[Repository] = None


@dataclass(kw_only=True)
class ArchiveProjectV2ItemPayload:
    client_mutation_id: Optional[str] = None
    item: Optional[ProjectV2Item] = None


@dataclass(kw_only=True)
class ApproveVerifiableDomainPayload:
    client_mutation_id: Optional[str] = None
    domain: Optional[VerifiableDomain] = None


@dataclass(kw_only=True)
class ApproveDeploymentsPayload:
    client_mutation_id: Optional[str] = None
    deployments: Optional[list[Deployment]] = None


@dataclass(kw_only=True)
class AddVerifiableDomainPayload:
    client_mutation_id: Optional[str] = None
    domain: Optional[VerifiableDomain] = None


@dataclass(kw_only=True)
class AddUpvotePayload:
    client_mutation_id: Optional[str] = None
    subject: Optional[Votable] = None


@dataclass(kw_only=True)
class AddStarPayload:
    client_mutation_id: Optional[str] = None
    starrable: Optional[Starrable] = None


@dataclass(kw_only=True)
class AddPullRequestReviewThreadReplyPayload:
    client_mutation_id: Optional[str] = None
    comment: Optional[PullRequestReviewComment] = None


@dataclass(kw_only=True)
class AddPullRequestReviewThreadPayload:
    client_mutation_id: Optional[str] = None
    thread: Optional[PullRequestReviewThread] = None


@dataclass(kw_only=True)
class AddProjectV2ItemByIdPayload:
    client_mutation_id: Optional[str] = None
    item: Optional[ProjectV2Item] = None


@dataclass(kw_only=True)
class AddProjectV2DraftIssuePayload:
    client_mutation_id: Optional[str] = None
    project_item: Optional[ProjectV2Item] = None


@dataclass(kw_only=True)
class AddLabelsToLabelablePayload:
    client_mutation_id: Optional[str] = None
    labelable: Optional[Labelable] = None


@dataclass(kw_only=True)
class AddEnterpriseOrganizationMemberPayload:
    client_mutation_id: Optional[str] = None
    users: Optional[list[User]] = None


@dataclass(kw_only=True)
class AddDiscussionPollVotePayload:
    client_mutation_id: Optional[str] = None
    poll_option: Optional[DiscussionPollOption] = None


@dataclass(kw_only=True)
class AddDiscussionCommentPayload:
    client_mutation_id: Optional[str] = None
    comment: Optional[DiscussionComment] = None


@dataclass(kw_only=True)
class AddAssigneesToAssignablePayload:
    assignable: Optional[Assignable] = None
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class AcceptTopicSuggestionPayload:
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class AcceptEnterpriseAdministratorInvitationPayload:
    client_mutation_id: Optional[str] = None
    invitation: Optional[EnterpriseAdministratorInvitation] = None
    message: Optional[str] = None
