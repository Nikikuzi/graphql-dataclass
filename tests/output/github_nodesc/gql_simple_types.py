from dataclasses import dataclass
from typing import Optional

from .enums import (
    ActorType,
    AuditLogOrderField,
    CheckConclusionState,
    CheckStatusState,
    CommentCannotUpdateReason,
    DeploymentStatusState,
    DiscussionCloseReason,
    DiscussionOrderField,
    EnterpriseAdministratorInvitationOrderField,
    EnterpriseAdministratorRole,
    EnterpriseDefaultRepositoryPermissionSettingValue,
    EnterpriseEnabledDisabledSettingValue,
    EnterpriseMembersCanCreateRepositoriesSettingValue,
    EnterpriseMembersCanMakePurchasesSettingValue,
    EnterpriseOrderField,
    EnterpriseServerInstallationOrderField,
    EnterpriseServerUserAccountOrderField,
    EnvironmentOrderField,
    FileViewedState,
    FundingPlatform,
    GistOrderField,
    IssueCommentOrderField,
    IssueOrderField,
    LockReason,
    MannequinOrderField,
    MergeQueueMergingStrategy,
    MigrationSourceType,
    MilestoneOrderField,
    OrderDirection,
    OrganizationMemberRole,
    OrganizationMigrationState,
    PackageFileOrderField,
    PatchStatus,
    ProjectOrderField,
    ProjectV2ItemFieldValueOrderField,
    ProjectV2Roles,
    ProjectV2SingleSelectFieldOptionColor,
    ProjectV2ViewOrderField,
    PullRequestMergeMethod,
    PullRequestReviewDecision,
    PullRequestUpdateState,
    RefOrderField,
    ReportedContentClassifiers,
    RepositoryInteractionLimit,
    RepositoryInteractionLimitExpiry,
    RepositoryInvitationOrderField,
    RepositoryOrderField,
    RepositoryPermission,
    RepositoryRulesetBypassActorBypassMode,
    RepositoryVisibility,
    RoleInOrganization,
    SamlDigestAlgorithm,
    SamlSignatureAlgorithm,
    SavedReplyOrderField,
    SecurityAdvisoryEcosystem,
    SecurityAdvisoryIdentifierType,
    SocialAccountProvider,
    SponsorOrderField,
    SponsorsActivityOrderField,
    SponsorsCountryOrRegionCode,
    SponsorshipOrderField,
    SponsorshipPrivacy,
    SponsorsTierOrderField,
    StatusState,
    SubscriptionState,
    TeamDiscussionOrderField,
    TeamOrderField,
    ThreadSubscriptionFormAction,
    ThreadSubscriptionState,
    UserStatusOrderField,
    WorkflowRunOrderField,
)
from .scalars import ID, URI, Base64String, Date, DateTime, GitObjectID


@dataclass(kw_only=True)
class AbortQueuedMigrationsInput:
    client_mutation_id: Optional[str] = None
    owner_id: ID


@dataclass(kw_only=True)
class AbortRepositoryMigrationInput:
    client_mutation_id: Optional[str] = None
    migration_id: ID


@dataclass(kw_only=True)
class AcceptEnterpriseAdministratorInvitationInput:
    client_mutation_id: Optional[str] = None
    invitation_id: ID


@dataclass(kw_only=True)
class Actor:
    avatar_url: URI
    login: str
    resource_path: URI
    url: URI


@dataclass(kw_only=True)
class AddAssigneesToAssignableInput:
    assignable_id: ID
    assignee_ids: list[ID]
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class AddDiscussionCommentInput:
    body: str
    client_mutation_id: Optional[str] = None
    discussion_id: ID
    reply_to_id: Optional[ID] = None


@dataclass(kw_only=True)
class AddEnterpriseOrganizationMemberInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    organization_id: ID
    role: Optional[OrganizationMemberRole] = None
    user_ids: list[ID]


@dataclass(kw_only=True)
class AddEnterpriseSupportEntitlementPayload:
    client_mutation_id: Optional[str] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class AddProjectCardInput:
    client_mutation_id: Optional[str] = None
    content_id: Optional[ID] = None
    note: Optional[str] = None
    project_column_id: ID


@dataclass(kw_only=True)
class AddProjectV2DraftIssueInput:
    assignee_ids: Optional[list[ID]] = None
    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    project_id: ID
    title: str


@dataclass(kw_only=True)
class AddPullRequestReviewCommentInput:
    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    commit_o_i_d: Optional[GitObjectID] = None
    in_reply_to: Optional[ID] = None
    path: Optional[str] = None
    position: Optional[int] = None
    pull_request_id: Optional[ID] = None
    pull_request_review_id: Optional[ID] = None


@dataclass(kw_only=True)
class AddPullRequestReviewThreadReplyInput:
    body: str
    client_mutation_id: Optional[str] = None
    pull_request_review_id: Optional[ID] = None
    pull_request_review_thread_id: ID


@dataclass(kw_only=True)
class AddStarInput:
    client_mutation_id: Optional[str] = None
    starrable_id: ID


@dataclass(kw_only=True)
class AddVerifiableDomainInput:
    client_mutation_id: Optional[str] = None
    domain: URI
    owner_id: ID


@dataclass(kw_only=True)
class ApproveDeploymentsInput:
    client_mutation_id: Optional[str] = None
    comment: Optional[str] = None
    environment_ids: list[ID]
    workflow_run_id: ID


@dataclass(kw_only=True)
class ArchiveProjectV2ItemInput:
    client_mutation_id: Optional[str] = None
    item_id: ID
    project_id: ID


@dataclass(kw_only=True)
class AuditLogOrder:
    direction: Optional[OrderDirection] = None
    field: Optional[AuditLogOrderField] = None


@dataclass(kw_only=True)
class BranchNamePatternParameters:
    name: Optional[str] = None
    negate: bool
    operator: str
    pattern: str


@dataclass(kw_only=True)
class BulkSponsorship:
    amount: int
    sponsorable_id: Optional[ID] = None
    sponsorable_login: Optional[str] = None


@dataclass(kw_only=True)
class CWE:
    cwe_id: str
    description: str
    id: ID
    name: str


@dataclass(kw_only=True)
class CancelSponsorshipInput:
    client_mutation_id: Optional[str] = None
    sponsor_id: Optional[ID] = None
    sponsor_login: Optional[str] = None
    sponsorable_id: Optional[ID] = None
    sponsorable_login: Optional[str] = None


@dataclass(kw_only=True)
class CheckAnnotationPosition:
    column: Optional[int] = None
    line: int


@dataclass(kw_only=True)
class CheckRunAction:
    description: str
    identifier: str
    label: str


@dataclass(kw_only=True)
class CheckRunOutputImage:
    alt: str
    caption: Optional[str] = None
    image_url: URI


@dataclass(kw_only=True)
class CheckStep:
    completed_at: Optional[DateTime] = None
    conclusion: Optional[CheckConclusionState] = None
    external_id: Optional[str] = None
    name: str
    number: int
    seconds_to_completion: Optional[int] = None
    started_at: Optional[DateTime] = None
    status: CheckStatusState


@dataclass(kw_only=True)
class CheckSuiteFilter:
    app_id: Optional[int] = None
    check_name: Optional[str] = None


@dataclass(kw_only=True)
class ClearProjectV2ItemFieldValueInput:
    client_mutation_id: Optional[str] = None
    field_id: ID
    item_id: ID
    project_id: ID


@dataclass(kw_only=True)
class CloneTemplateRepositoryInput:
    client_mutation_id: Optional[str] = None
    description: Optional[str] = None
    include_all_branches: Optional[bool] = None
    name: str
    owner_id: ID
    repository_id: ID
    visibility: RepositoryVisibility


@dataclass(kw_only=True)
class CloseDiscussionInput:
    client_mutation_id: Optional[str] = None
    discussion_id: ID
    reason: Optional[DiscussionCloseReason] = None


@dataclass(kw_only=True)
class ClosePullRequestInput:
    client_mutation_id: Optional[str] = None
    pull_request_id: ID


@dataclass(kw_only=True)
class CommitAuthor:
    emails: Optional[list[str]] = None
    id: Optional[ID] = None


@dataclass(kw_only=True)
class CommitAuthorEmailPatternParametersInput:
    name: Optional[str] = None
    negate: Optional[bool] = None
    operator: str
    pattern: str


@dataclass(kw_only=True)
class CommitMessage:
    body: Optional[str] = None
    headline: str


@dataclass(kw_only=True)
class CommitMessagePatternParametersInput:
    name: Optional[str] = None
    negate: Optional[bool] = None
    operator: str
    pattern: str


@dataclass(kw_only=True)
class CommitterEmailPatternParameters:
    name: Optional[str] = None
    negate: bool
    operator: str
    pattern: str


@dataclass(kw_only=True)
class ContributingGuidelines:
    body: Optional[str] = None
    resource_path: Optional[URI] = None
    url: Optional[URI] = None


@dataclass(kw_only=True)
class ContributionCalendarMonth:
    first_day: Date
    name: str
    total_weeks: int
    year: int


@dataclass(kw_only=True)
class ConvertProjectCardNoteToIssueInput:
    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    project_card_id: ID
    repository_id: ID
    title: Optional[str] = None


@dataclass(kw_only=True)
class CopyProjectV2Input:
    client_mutation_id: Optional[str] = None
    include_draft_issues: Optional[bool] = None
    owner_id: ID
    project_id: ID
    title: str


@dataclass(kw_only=True)
class CreateCheckSuiteInput:
    client_mutation_id: Optional[str] = None
    head_sha: GitObjectID
    repository_id: ID


@dataclass(kw_only=True)
class CreateDeploymentStatusInput:
    auto_inactive: Optional[bool] = None
    client_mutation_id: Optional[str] = None
    deployment_id: ID
    description: Optional[str] = None
    environment: Optional[str] = None
    environment_url: Optional[str] = None
    log_url: Optional[str] = None
    state: DeploymentStatusState


@dataclass(kw_only=True)
class CreateEnterpriseOrganizationInput:
    admin_logins: list[str]
    billing_email: str
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    login: str
    profile_name: str


@dataclass(kw_only=True)
class CreateIpAllowListEntryInput:
    allow_list_value: str
    client_mutation_id: Optional[str] = None
    is_active: bool
    name: Optional[str] = None
    owner_id: ID


@dataclass(kw_only=True)
class CreateLabelInput:
    client_mutation_id: Optional[str] = None
    color: str
    description: Optional[str] = None
    name: str
    repository_id: ID


@dataclass(kw_only=True)
class CreateMigrationSourceInput:
    access_token: Optional[str] = None
    client_mutation_id: Optional[str] = None
    github_pat: Optional[str] = None
    name: str
    owner_id: ID
    type: MigrationSourceType
    url: Optional[str] = None


@dataclass(kw_only=True)
class CreateProjectV2Input:
    client_mutation_id: Optional[str] = None
    owner_id: ID
    repository_id: Optional[ID] = None
    team_id: Optional[ID] = None
    title: str


@dataclass(kw_only=True)
class CreateRefInput:
    client_mutation_id: Optional[str] = None
    name: str
    oid: GitObjectID
    repository_id: ID


@dataclass(kw_only=True)
class CreateSponsorsListingInput:
    billing_country_or_region_code: Optional[SponsorsCountryOrRegionCode] = None
    client_mutation_id: Optional[str] = None
    contact_email: Optional[str] = None
    fiscal_host_login: Optional[str] = None
    fiscally_hosted_project_profile_url: Optional[str] = None
    full_description: Optional[str] = None
    residence_country_or_region_code: Optional[SponsorsCountryOrRegionCode] = None
    sponsorable_login: Optional[str] = None


@dataclass(kw_only=True)
class CreateSponsorshipInput:
    amount: Optional[int] = None
    client_mutation_id: Optional[str] = None
    is_recurring: Optional[bool] = None
    privacy_level: Optional[SponsorshipPrivacy] = None
    receive_emails: Optional[bool] = None
    sponsor_id: Optional[ID] = None
    sponsor_login: Optional[str] = None
    sponsorable_id: Optional[ID] = None
    sponsorable_login: Optional[str] = None
    tier_id: Optional[ID] = None


@dataclass(kw_only=True)
class CreateTeamDiscussionInput:
    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    private: Optional[bool] = None
    team_id: Optional[ID] = None
    title: Optional[str] = None


@dataclass(kw_only=True)
class DeclineTopicSuggestionInput:
    client_mutation_id: Optional[str] = None
    name: Optional[str] = None
    reason: Optional[TopicSuggestionDeclineReason] = None
    repository_id: Optional[ID] = None


@dataclass(kw_only=True)
class DeleteBranchProtectionRuleInput:
    branch_protection_rule_id: ID
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class DeleteDeploymentInput:
    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class DeleteDiscussionCommentInput:
    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class DeleteEnvironmentInput:
    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class DeleteIpAllowListEntryInput:
    client_mutation_id: Optional[str] = None
    ip_allow_list_entry_id: ID


@dataclass(kw_only=True)
class DeleteIssueCommentPayload:
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class DeleteLabelInput:
    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class DeleteLinkedBranchInput:
    client_mutation_id: Optional[str] = None
    linked_branch_id: ID


@dataclass(kw_only=True)
class DeletePackageVersionPayload:
    client_mutation_id: Optional[str] = None
    success: Optional[bool] = None


@dataclass(kw_only=True)
class DeleteProjectColumnInput:
    client_mutation_id: Optional[str] = None
    column_id: ID


@dataclass(kw_only=True)
class DeleteProjectV2FieldInput:
    client_mutation_id: Optional[str] = None
    field_id: ID


@dataclass(kw_only=True)
class DeleteProjectV2ItemInput:
    client_mutation_id: Optional[str] = None
    item_id: ID
    project_id: ID


@dataclass(kw_only=True)
class DeleteProjectV2WorkflowInput:
    client_mutation_id: Optional[str] = None
    workflow_id: ID


@dataclass(kw_only=True)
class DeletePullRequestReviewInput:
    client_mutation_id: Optional[str] = None
    pull_request_review_id: ID


@dataclass(kw_only=True)
class DeleteRefPayload:
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class DeleteRepositoryRulesetPayload:
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class DeleteTeamDiscussionCommentPayload:
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class DeleteTeamDiscussionPayload:
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class DeleteVerifiableDomainInput:
    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class DeployKey:
    created_at: DateTime
    id: ID
    key: str
    read_only: bool
    title: str
    verified: bool


@dataclass(kw_only=True)
class DequeuePullRequestInput:
    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class DiscussionOrder:
    direction: OrderDirection
    field: DiscussionOrderField


@dataclass(kw_only=True)
class DismissPullRequestReviewInput:
    client_mutation_id: Optional[str] = None
    message: str
    pull_request_review_id: ID


@dataclass(kw_only=True)
class DraftPullRequestReviewComment:
    body: str
    path: str
    position: int


@dataclass(kw_only=True)
class EnablePullRequestAutoMergeInput:
    author_email: Optional[str] = None
    client_mutation_id: Optional[str] = None
    commit_body: Optional[str] = None
    commit_headline: Optional[str] = None
    expected_head_oid: Optional[GitObjectID] = None
    merge_method: Optional[PullRequestMergeMethod] = None
    pull_request_id: ID


@dataclass(kw_only=True)
class EnterpriseAdministratorInvitationOrder:
    direction: OrderDirection
    field: EnterpriseAdministratorInvitationOrderField


@dataclass(kw_only=True)
class EnterpriseBillingInfo:
    all_licensable_users_count: int
    asset_packs: int
    bandwidth_quota: float
    bandwidth_usage: float
    bandwidth_usage_percentage: int
    storage_quota: float
    storage_usage: float
    storage_usage_percentage: int
    total_available_licenses: int
    total_licenses: int


@dataclass(kw_only=True)
class EnterpriseOrder:
    direction: OrderDirection
    field: EnterpriseOrderField


@dataclass(kw_only=True)
class EnterpriseServerInstallationOrder:
    direction: OrderDirection
    field: EnterpriseServerInstallationOrderField


@dataclass(kw_only=True)
class EnterpriseServerUserAccountOrder:
    direction: OrderDirection
    field: EnterpriseServerUserAccountOrderField


@dataclass(kw_only=True)
class Environments:
    direction: OrderDirection
    field: EnvironmentOrderField


@dataclass(kw_only=True)
class FileAddition:
    contents: Base64String
    path: str


@dataclass(kw_only=True)
class FollowOrganizationInput:
    client_mutation_id: Optional[str] = None
    organization_id: ID


@dataclass(kw_only=True)
class FundingLink:
    platform: FundingPlatform
    url: URI


@dataclass(kw_only=True)
class GistOrder:
    direction: OrderDirection
    field: GistOrderField


@dataclass(kw_only=True)
class GrantEnterpriseOrganizationsMigratorRoleInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    login: str


@dataclass(kw_only=True)
class GrantMigratorRolePayload:
    client_mutation_id: Optional[str] = None
    success: Optional[bool] = None


@dataclass(kw_only=True)
class InviteEnterpriseAdminInput:
    client_mutation_id: Optional[str] = None
    email: Optional[str] = None
    enterprise_id: ID
    invitee: Optional[str] = None
    role: Optional[EnterpriseAdministratorRole] = None


@dataclass(kw_only=True)
class IssueCommentOrder:
    direction: OrderDirection
    field: IssueCommentOrderField


@dataclass(kw_only=True)
class IssueOrder:
    direction: OrderDirection
    field: IssueOrderField


@dataclass(kw_only=True)
class Language:
    color: Optional[str] = None
    id: ID
    name: str


@dataclass(kw_only=True)
class LicenseRule:
    description: str
    key: str
    label: str


@dataclass(kw_only=True)
class LinkProjectV2ToTeamInput:
    client_mutation_id: Optional[str] = None
    project_id: ID
    team_id: ID


@dataclass(kw_only=True)
class LockLockableInput:
    client_mutation_id: Optional[str] = None
    lock_reason: Optional[LockReason] = None
    lockable_id: ID


@dataclass(kw_only=True)
class MannequinOrder:
    direction: OrderDirection
    field: MannequinOrderField


@dataclass(kw_only=True)
class MarkFileAsViewedInput:
    client_mutation_id: Optional[str] = None
    path: str
    pull_request_id: ID


@dataclass(kw_only=True)
class MarkProjectV2AsTemplateInput:
    client_mutation_id: Optional[str] = None
    project_id: ID


@dataclass(kw_only=True)
class MarketplaceCategory:
    description: Optional[str] = None
    how_it_works: Optional[str] = None
    id: ID
    name: str
    primary_listing_count: int
    resource_path: URI
    secondary_listing_count: int
    slug: str
    url: URI


@dataclass(kw_only=True)
class MergeBranchInput:
    author_email: Optional[str] = None
    base: str
    client_mutation_id: Optional[str] = None
    commit_message: Optional[str] = None
    head: str
    repository_id: ID


@dataclass(kw_only=True)
class MergeQueueConfiguration:
    check_response_timeout: Optional[int] = None
    maximum_entries_to_build: Optional[int] = None
    maximum_entries_to_merge: Optional[int] = None
    merge_method: Optional[PullRequestMergeMethod] = None
    merging_strategy: Optional[MergeQueueMergingStrategy] = None
    minimum_entries_to_merge: Optional[int] = None
    minimum_entries_to_merge_wait_time: Optional[int] = None


@dataclass(kw_only=True)
class MilestoneOrder:
    direction: OrderDirection
    field: MilestoneOrderField


@dataclass(kw_only=True)
class MinimizeCommentInput:
    classifier: ReportedContentClassifiers
    client_mutation_id: Optional[str] = None
    subject_id: ID


@dataclass(kw_only=True)
class MoveProjectColumnInput:
    after_column_id: Optional[ID] = None
    client_mutation_id: Optional[str] = None
    column_id: ID


@dataclass(kw_only=True)
class OauthApplicationAuditEntryData:
    oauth_application_name: Optional[str] = None
    oauth_application_resource_path: Optional[URI] = None
    oauth_application_url: Optional[URI] = None


@dataclass(kw_only=True)
class OrganizationMigration:
    created_at: DateTime
    database_id: Optional[str] = None
    failure_reason: Optional[str] = None
    id: ID
    remaining_repositories_count: Optional[int] = None
    source_org_name: str
    source_org_url: URI
    state: OrganizationMigrationState
    target_org_name: str
    total_repositories_count: Optional[int] = None


@dataclass(kw_only=True)
class PackageFileOrder:
    direction: Optional[OrderDirection] = None
    field: Optional[PackageFileOrderField] = None


@dataclass(kw_only=True)
class PackageStatistics:
    downloads_total_count: int


@dataclass(kw_only=True)
class PackageVersionStatistics:
    downloads_total_count: int


@dataclass(kw_only=True)
class PinIssueInput:
    client_mutation_id: Optional[str] = None
    issue_id: ID


@dataclass(kw_only=True)
class ProjectOrder:
    direction: OrderDirection
    field: ProjectOrderField


@dataclass(kw_only=True)
class ProjectV2Collaborator:
    role: ProjectV2Roles
    team_id: Optional[ID] = None
    user_id: Optional[ID] = None


@dataclass(kw_only=True)
class ProjectV2FieldValue:
    date: Optional[Date] = None
    iteration_id: Optional[str] = None
    number: Optional[float] = None
    single_select_option_id: Optional[str] = None
    text: Optional[str] = None


@dataclass(kw_only=True)
class ProjectV2ItemFieldValueOrder:
    direction: OrderDirection
    field: ProjectV2ItemFieldValueOrderField


@dataclass(kw_only=True)
class ProjectV2IterationFieldIteration:
    duration: int
    id: str
    start_date: Date
    title: str
    title_h_t_m_l: str


@dataclass(kw_only=True)
class ProjectV2SingleSelectFieldOption:
    color: ProjectV2SingleSelectFieldOptionColor
    description: str
    description_h_t_m_l: str
    id: str
    name: str
    name_h_t_m_l: str


@dataclass(kw_only=True)
class ProjectV2ViewOrder:
    direction: OrderDirection
    field: ProjectV2ViewOrderField


@dataclass(kw_only=True)
class PropertyTargetDefinition:
    name: str
    property_values: list[str]


@dataclass(kw_only=True)
class PublicKey:
    accessed_at: Optional[DateTime] = None
    created_at: Optional[DateTime] = None
    fingerprint: str
    id: ID
    is_read_only: Optional[bool] = None
    key: str
    updated_at: Optional[DateTime] = None


@dataclass(kw_only=True)
class PullRequestChangedFile:
    additions: int
    change_type: PatchStatus
    deletions: int
    path: str
    viewer_viewed_state: FileViewedState


@dataclass(kw_only=True)
class PullRequestParameters:
    dismiss_stale_reviews_on_push: bool
    require_code_owner_review: bool
    require_last_push_approval: bool
    required_approving_review_count: int
    required_review_thread_resolution: bool


@dataclass(kw_only=True)
class RateLimit:
    cost: int
    limit: int
    node_count: int
    remaining: int
    reset_at: DateTime
    used: int


@dataclass(kw_only=True)
class RefNameConditionTarget:
    exclude: list[str]
    include: list[str]


@dataclass(kw_only=True)
class RefOrder:
    direction: OrderDirection
    field: RefOrderField


@dataclass(kw_only=True)
class RefUpdateRule:
    allows_deletions: bool
    allows_force_pushes: bool
    blocks_creations: bool
    pattern: str
    required_approving_review_count: Optional[int] = None
    required_status_check_contexts: Optional[list[str]] = None
    requires_code_owner_reviews: bool
    requires_conversation_resolution: bool
    requires_linear_history: bool
    requires_signatures: bool
    viewer_allowed_to_dismiss_reviews: bool
    viewer_can_push: bool


@dataclass(kw_only=True)
class RegenerateVerifiableDomainTokenInput:
    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class RejectDeploymentsInput:
    client_mutation_id: Optional[str] = None
    comment: Optional[str] = None
    environment_ids: list[ID]
    workflow_run_id: ID


@dataclass(kw_only=True)
class RemoveAssigneesFromAssignableInput:
    assignable_id: ID
    assignee_ids: list[ID]
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class RemoveEnterpriseIdentityProviderInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID


@dataclass(kw_only=True)
class RemoveEnterpriseOrganizationInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    organization_id: ID


@dataclass(kw_only=True)
class RemoveEnterpriseSupportEntitlementPayload:
    client_mutation_id: Optional[str] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class RemoveOutsideCollaboratorInput:
    client_mutation_id: Optional[str] = None
    organization_id: ID
    user_id: ID


@dataclass(kw_only=True)
class RemoveStarInput:
    client_mutation_id: Optional[str] = None
    starrable_id: ID


@dataclass(kw_only=True)
class ReopenDiscussionInput:
    client_mutation_id: Optional[str] = None
    discussion_id: ID


@dataclass(kw_only=True)
class ReopenPullRequestInput:
    client_mutation_id: Optional[str] = None
    pull_request_id: ID


@dataclass(kw_only=True)
class RepositoryContactLink:
    about: str
    name: str
    url: URI


@dataclass(kw_only=True)
class RepositoryIdConditionTargetInput:
    repository_ids: list[ID]


@dataclass(kw_only=True)
class RepositoryInvitationOrder:
    direction: OrderDirection
    field: RepositoryInvitationOrderField


@dataclass(kw_only=True)
class RepositoryNameConditionTarget:
    exclude: list[str]
    include: list[str]
    protected: bool


@dataclass(kw_only=True)
class RepositoryOrder:
    direction: OrderDirection
    field: RepositoryOrderField


@dataclass(kw_only=True)
class RepositoryRulesetBypassActorInput:
    actor_id: Optional[ID] = None
    bypass_mode: RepositoryRulesetBypassActorBypassMode
    organization_admin: Optional[bool] = None
    repository_role_database_id: Optional[int] = None


@dataclass(kw_only=True)
class RequirableByPullRequest:
    is_required: bool


@dataclass(kw_only=True)
class RequiredDeploymentsParametersInput:
    required_deployment_environments: list[str]


@dataclass(kw_only=True)
class RerequestCheckSuiteInput:
    check_suite_id: ID
    client_mutation_id: Optional[str] = None
    repository_id: ID


@dataclass(kw_only=True)
class RetireSponsorsTierInput:
    client_mutation_id: Optional[str] = None
    tier_id: ID


@dataclass(kw_only=True)
class ReviewStatusHovercardContext:
    message: str
    octicon: str
    review_decision: Optional[PullRequestReviewDecision] = None


@dataclass(kw_only=True)
class RevokeMigratorRoleInput:
    actor: str
    actor_type: ActorType
    client_mutation_id: Optional[str] = None
    organization_id: ID


@dataclass(kw_only=True)
class SavedReplyOrder:
    direction: OrderDirection
    field: SavedReplyOrderField


@dataclass(kw_only=True)
class SecurityAdvisoryIdentifierFilter:
    type: SecurityAdvisoryIdentifierType
    value: str


@dataclass(kw_only=True)
class SecurityAdvisoryPackage:
    ecosystem: SecurityAdvisoryEcosystem
    name: str


@dataclass(kw_only=True)
class SecurityAdvisoryReference:
    url: URI


@dataclass(kw_only=True)
class SetEnterpriseIdentityProviderInput:
    client_mutation_id: Optional[str] = None
    digest_method: SamlDigestAlgorithm
    enterprise_id: ID
    idp_certificate: str
    issuer: Optional[str] = None
    signature_method: SamlSignatureAlgorithm
    sso_url: URI


@dataclass(kw_only=True)
class SetRepositoryInteractionLimitInput:
    client_mutation_id: Optional[str] = None
    expiry: Optional[RepositoryInteractionLimitExpiry] = None
    limit: RepositoryInteractionLimit
    repository_id: ID


@dataclass(kw_only=True)
class SocialAccount:
    display_name: str
    provider: SocialAccountProvider
    url: URI


@dataclass(kw_only=True)
class SponsorOrder:
    direction: OrderDirection
    field: SponsorOrderField


@dataclass(kw_only=True)
class SponsorsActivityOrder:
    direction: OrderDirection
    field: SponsorsActivityOrderField


@dataclass(kw_only=True)
class SponsorsTierOrder:
    direction: OrderDirection
    field: SponsorsTierOrderField


@dataclass(kw_only=True)
class SponsorshipOrder:
    direction: OrderDirection
    field: SponsorshipOrderField


@dataclass(kw_only=True)
class StartOrganizationMigrationInput:
    client_mutation_id: Optional[str] = None
    source_access_token: str
    source_org_url: URI
    target_enterprise_id: ID
    target_org_name: str


@dataclass(kw_only=True)
class StatusCheckConfiguration:
    context: str
    integration_id: Optional[int] = None


@dataclass(kw_only=True)
class StatusContextStateCount:
    count: int
    state: StatusState


@dataclass(kw_only=True)
class Submodule:
    branch: Optional[str] = None
    git_url: URI
    name: str
    name_raw: Base64String
    path: str
    path_raw: Base64String
    subproject_commit_oid: Optional[GitObjectID] = None


@dataclass(kw_only=True)
class SubscribableThread:
    id: ID
    viewer_thread_subscription_form_action: Optional[
        ThreadSubscriptionFormAction
    ] = None
    viewer_thread_subscription_status: Optional[ThreadSubscriptionState] = None


@dataclass(kw_only=True)
class TagNamePatternParametersInput:
    name: Optional[str] = None
    negate: Optional[bool] = None
    operator: str
    pattern: str


@dataclass(kw_only=True)
class TeamDiscussionOrder:
    direction: OrderDirection
    field: TeamDiscussionOrderField


@dataclass(kw_only=True)
class TeamOrder:
    direction: OrderDirection
    field: TeamOrderField


@dataclass(kw_only=True)
class TextMatchHighlight:
    begin_indice: int
    end_indice: int
    text: str


@dataclass(kw_only=True)
class TransferIssueInput:
    client_mutation_id: Optional[str] = None
    create_labels_if_missing: Optional[bool] = None
    issue_id: ID
    repository_id: ID


@dataclass(kw_only=True)
class UnarchiveRepositoryInput:
    client_mutation_id: Optional[str] = None
    repository_id: ID


@dataclass(kw_only=True)
class UnfollowUserInput:
    client_mutation_id: Optional[str] = None
    user_id: ID


@dataclass(kw_only=True)
class UnlinkProjectV2FromRepositoryInput:
    client_mutation_id: Optional[str] = None
    project_id: ID
    repository_id: ID


@dataclass(kw_only=True)
class UnlinkRepositoryFromProjectInput:
    client_mutation_id: Optional[str] = None
    project_id: ID
    repository_id: ID


@dataclass(kw_only=True)
class UnmarkDiscussionCommentAsAnswerInput:
    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class UnmarkIssueAsDuplicateInput:
    canonical_id: ID
    client_mutation_id: Optional[str] = None
    duplicate_id: ID


@dataclass(kw_only=True)
class UnminimizeCommentInput:
    client_mutation_id: Optional[str] = None
    subject_id: ID


@dataclass(kw_only=True)
class UnresolveReviewThreadInput:
    client_mutation_id: Optional[str] = None
    thread_id: ID


@dataclass(kw_only=True)
class UnsubscribeFromNotificationsPayload:
    client_mutation_id: Optional[str] = None
    success: Optional[bool] = None


@dataclass(kw_only=True)
class UpdatableComment:
    viewer_cannot_update_reasons: list[CommentCannotUpdateReason]


@dataclass(kw_only=True)
class UpdateDiscussionInput:
    body: Optional[str] = None
    category_id: Optional[ID] = None
    client_mutation_id: Optional[str] = None
    discussion_id: ID
    title: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseAdministratorRolePayload:
    client_mutation_id: Optional[str] = None
    message: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseDefaultRepositoryPermissionSettingInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    setting_value: EnterpriseDefaultRepositoryPermissionSettingValue


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanCreateRepositoriesSettingInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    members_can_create_internal_repositories: Optional[bool] = None
    members_can_create_private_repositories: Optional[bool] = None
    members_can_create_public_repositories: Optional[bool] = None
    members_can_create_repositories_policy_enabled: Optional[bool] = None
    setting_value: Optional[EnterpriseMembersCanCreateRepositoriesSettingValue] = None


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    setting_value: EnterpriseEnabledDisabledSettingValue


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanMakePurchasesSettingInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    setting_value: EnterpriseMembersCanMakePurchasesSettingValue


@dataclass(kw_only=True)
class UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    setting_value: EnterpriseEnabledDisabledSettingValue


@dataclass(kw_only=True)
class UpdateEnterpriseOwnerOrganizationRoleInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    organization_id: ID
    organization_role: RoleInOrganization


@dataclass(kw_only=True)
class UpdateEnterpriseProfileInput:
    client_mutation_id: Optional[str] = None
    description: Optional[str] = None
    enterprise_id: ID
    location: Optional[str] = None
    name: Optional[str] = None
    website_url: Optional[str] = None


@dataclass(kw_only=True)
class UpdateEnterpriseTeamDiscussionsSettingInput:
    client_mutation_id: Optional[str] = None
    enterprise_id: ID
    setting_value: EnterpriseEnabledDisabledSettingValue


@dataclass(kw_only=True)
class UpdateEnvironmentInput:
    client_mutation_id: Optional[str] = None
    environment_id: ID
    prevent_self_review: Optional[bool] = None
    reviewers: Optional[list[ID]] = None
    wait_timer: Optional[int] = None


@dataclass(kw_only=True)
class UpdateIpAllowListEntryInput:
    allow_list_value: str
    client_mutation_id: Optional[str] = None
    ip_allow_list_entry_id: ID
    is_active: bool
    name: Optional[str] = None


@dataclass(kw_only=True)
class UpdateIssueCommentInput:
    body: str
    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class UpdateLabelInput:
    client_mutation_id: Optional[str] = None
    color: Optional[str] = None
    description: Optional[str] = None
    id: ID
    name: Optional[str] = None


@dataclass(kw_only=True)
class UpdateOrganizationAllowPrivateRepositoryForkingSettingInput:
    client_mutation_id: Optional[str] = None
    forking_enabled: bool
    organization_id: ID


@dataclass(kw_only=True)
class UpdateParameters:
    update_allows_fetch_and_merge: bool


@dataclass(kw_only=True)
class UpdatePatreonSponsorabilityInput:
    client_mutation_id: Optional[str] = None
    enable_patreon_sponsorships: bool
    sponsorable_login: Optional[str] = None


@dataclass(kw_only=True)
class UpdateProjectColumnInput:
    client_mutation_id: Optional[str] = None
    name: str
    project_column_id: ID


@dataclass(kw_only=True)
class UpdateProjectV2DraftIssueInput:
    assignee_ids: Optional[list[ID]] = None
    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    draft_issue_id: ID
    title: Optional[str] = None


@dataclass(kw_only=True)
class UpdateProjectV2ItemPositionInput:
    after_id: Optional[ID] = None
    client_mutation_id: Optional[str] = None
    item_id: ID
    project_id: ID


@dataclass(kw_only=True)
class UpdatePullRequestInput:
    assignee_ids: Optional[list[ID]] = None
    base_ref_name: Optional[str] = None
    body: Optional[str] = None
    client_mutation_id: Optional[str] = None
    label_ids: Optional[list[ID]] = None
    maintainer_can_modify: Optional[bool] = None
    milestone_id: Optional[ID] = None
    project_ids: Optional[list[ID]] = None
    pull_request_id: ID
    state: Optional[PullRequestUpdateState] = None
    title: Optional[str] = None


@dataclass(kw_only=True)
class UpdatePullRequestReviewInput:
    body: str
    client_mutation_id: Optional[str] = None
    pull_request_review_id: ID


@dataclass(kw_only=True)
class UpdateRefsPayload:
    client_mutation_id: Optional[str] = None


@dataclass(kw_only=True)
class UpdateRepositoryWebCommitSignoffSettingInput:
    client_mutation_id: Optional[str] = None
    repository_id: ID
    web_commit_signoff_required: bool


@dataclass(kw_only=True)
class UpdateSubscriptionInput:
    client_mutation_id: Optional[str] = None
    state: SubscriptionState
    subscribable_id: ID


@dataclass(kw_only=True)
class UpdateTeamDiscussionInput:
    body: Optional[str] = None
    body_version: Optional[str] = None
    client_mutation_id: Optional[str] = None
    id: ID
    pinned: Optional[bool] = None
    title: Optional[str] = None


@dataclass(kw_only=True)
class UpdateTeamsRepositoryInput:
    client_mutation_id: Optional[str] = None
    permission: RepositoryPermission
    repository_id: ID
    team_ids: list[ID]


@dataclass(kw_only=True)
class UpdateUserListInput:
    client_mutation_id: Optional[str] = None
    description: Optional[str] = None
    is_private: Optional[bool] = None
    list_id: ID
    name: Optional[str] = None


@dataclass(kw_only=True)
class UserEmailMetadata:
    primary: Optional[bool] = None
    type: Optional[str] = None
    value: str


@dataclass(kw_only=True)
class UserStatusOrder:
    direction: OrderDirection
    field: UserStatusOrderField


@dataclass(kw_only=True)
class VerifyVerifiableDomainInput:
    client_mutation_id: Optional[str] = None
    id: ID


@dataclass(kw_only=True)
class WorkflowFileReference:
    path: str
    ref: Optional[str] = None
    repository_id: int
    sha: Optional[str] = None


@dataclass(kw_only=True)
class WorkflowRunOrder:
    direction: OrderDirection
    field: WorkflowRunOrderField
