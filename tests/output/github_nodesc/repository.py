from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import (
    MergeCommitMessage,
    MergeCommitTitle,
    PullRequestMergeMethod,
    RepositoryLockReason,
    RepositoryPermission,
    RepositoryVisibility,
    SquashMergeCommitMessage,
    SquashMergeCommitTitle,
    SubscriptionState,
)
from .gql_simple_types import (
    ContributingGuidelines,
    FundingLink,
    Language,
    RepositoryContactLink,
)
from .scalars import HTML, ID, URI, DateTime, GitSSHRemote

if TYPE_CHECKING:
    from .user_connection import UserConnection
    from .pull_request import PullRequest
    from .pull_request_connection import PullRequestConnection
    from .ref import Ref
    from .project_v2 import ProjectV2
    from .issue import Issue
    from .commit_comment_connection import CommitCommentConnection
    from .discussion import Discussion
    from .release import Release
    from .merge_queue import MergeQueue
    from .project import Project
    from .repository_ruleset import RepositoryRuleset
    from .gql_types import CodeOfConduct
    from .gql_types import RepositoryInteractionAbility
    from .gql_types import BranchProtectionRuleConnection
    from .gql_types import RepositoryCodeowners
    from .gql_types import ProjectV2Connection
    from .gql_types import IssueConnection
    from .gql_types import Label
    from .gql_types import LabelConnection
    from .gql_types import Milestone
    from .gql_types import RepositoryConnection
    from .gql_types import RepositoryCollaboratorConnection
    from .gql_types import DependencyGraphManifestConnection
    from .gql_types import DeployKeyConnection
    from .gql_types import DeploymentConnection
    from .gql_types import DiscussionCategory
    from .gql_types import DiscussionCategoryConnection
    from .gql_types import DiscussionConnection
    from .gql_types import Environment
    from .gql_types import EnvironmentConnection
    from .gql_unions import IssueOrPullRequest
    from .gql_types import IssueTemplate
    from .gql_types import LanguageConnection
    from .gql_types import License
    from .gql_types import MilestoneConnection
    from .gql_types import GitObject
    from .gql_types import RepositoryOwner
    from .gql_types import PackageConnection
    from .gql_types import PinnedDiscussionConnection
    from .gql_types import PinnedIssueConnection
    from .gql_types import ProjectConnection
    from .gql_types import PullRequestTemplate
    from .gql_types import RefConnection
    from .gql_types import ReleaseConnection
    from .gql_types import StargazerConnection
    from .gql_types import RepositoryTopicConnection
    from .gql_types import RepositoryRulesetConnection
    from .gql_types import SubmoduleConnection
    from .gql_types import RepositoryVulnerabilityAlert
    from .gql_types import RepositoryVulnerabilityAlertConnection


@dataclass(kw_only=True)
class Repository:
    allow_update_branch: bool
    archived_at: Optional[DateTime] = None
    assignable_users: UserConnection
    auto_merge_allowed: bool
    branch_protection_rules: BranchProtectionRuleConnection
    code_of_conduct: Optional[CodeOfConduct] = None
    codeowners: Optional[RepositoryCodeowners] = None
    collaborators: Optional[RepositoryCollaboratorConnection] = None
    commit_comments: CommitCommentConnection
    contact_links: Optional[list[RepositoryContactLink]] = None
    contributing_guidelines: Optional[ContributingGuidelines] = None
    created_at: DateTime
    database_id: Optional[int] = None
    default_branch_ref: Optional[Ref] = None
    delete_branch_on_merge: bool
    dependency_graph_manifests: Optional[DependencyGraphManifestConnection] = None
    deploy_keys: DeployKeyConnection
    deployments: DeploymentConnection
    description: Optional[str] = None
    description_h_t_m_l: HTML
    discussion: Optional[Discussion] = None
    discussion_categories: DiscussionCategoryConnection
    discussion_category: Optional[DiscussionCategory] = None
    discussions: DiscussionConnection
    disk_usage: Optional[int] = None
    environment: Optional[Environment] = None
    environments: EnvironmentConnection
    fork_count: int
    forking_allowed: bool
    forks: RepositoryConnection
    funding_links: list[FundingLink]
    has_discussions_enabled: bool
    has_issues_enabled: bool
    has_projects_enabled: bool
    has_sponsorships_enabled: bool
    has_vulnerability_alerts_enabled: bool
    has_wiki_enabled: bool
    homepage_url: Optional[URI] = None
    id: ID
    interaction_ability: Optional[RepositoryInteractionAbility] = None
    is_archived: bool
    is_blank_issues_enabled: bool
    is_disabled: bool
    is_empty: bool
    is_fork: bool
    is_in_organization: bool
    is_locked: bool
    is_mirror: bool
    is_private: bool
    is_security_policy_enabled: Optional[bool] = None
    is_template: bool
    is_user_configuration_repository: bool
    issue: Optional[Issue] = None
    issue_or_pull_request: Optional[IssueOrPullRequest] = None
    issue_templates: Optional[list[IssueTemplate]] = None
    issues: IssueConnection
    label: Optional[Label] = None
    labels: Optional[LabelConnection] = None
    languages: Optional[LanguageConnection] = None
    latest_release: Optional[Release] = None
    license_info: Optional[License] = None
    lock_reason: Optional[RepositoryLockReason] = None
    mentionable_users: UserConnection
    merge_commit_allowed: bool
    merge_commit_message: MergeCommitMessage
    merge_commit_title: MergeCommitTitle
    merge_queue: Optional[MergeQueue] = None
    milestone: Optional[Milestone] = None
    milestones: Optional[MilestoneConnection] = None
    mirror_url: Optional[URI] = None
    name: str
    name_with_owner: str
    object: Optional[GitObject] = None
    open_graph_image_url: URI
    owner: RepositoryOwner
    packages: PackageConnection
    parent: Optional["Repository"] = None
    pinned_discussions: PinnedDiscussionConnection
    pinned_issues: Optional[PinnedIssueConnection] = None
    primary_language: Optional[Language] = None
    project: Optional[Project] = None
    project_v2: Optional[ProjectV2] = None
    projects: ProjectConnection
    projects_resource_path: URI
    projects_url: URI
    projects_v2: ProjectV2Connection
    pull_request: Optional[PullRequest] = None
    pull_request_templates: Optional[list[PullRequestTemplate]] = None
    pull_requests: PullRequestConnection
    pushed_at: Optional[DateTime] = None
    rebase_merge_allowed: bool
    recent_projects: ProjectV2Connection
    ref: Optional[Ref] = None
    refs: Optional[RefConnection] = None
    release: Optional[Release] = None
    releases: ReleaseConnection
    repository_topics: RepositoryTopicConnection
    resource_path: URI
    ruleset: Optional[RepositoryRuleset] = None
    rulesets: Optional[RepositoryRulesetConnection] = None
    security_policy_url: Optional[URI] = None
    short_description_h_t_m_l: HTML
    squash_merge_allowed: bool
    squash_merge_commit_message: SquashMergeCommitMessage
    squash_merge_commit_title: SquashMergeCommitTitle
    ssh_url: GitSSHRemote
    stargazer_count: int
    stargazers: StargazerConnection
    submodules: SubmoduleConnection
    temp_clone_token: Optional[str] = None
    template_repository: Optional["Repository"] = None
    updated_at: DateTime
    url: URI
    uses_custom_open_graph_image: bool
    viewer_can_administer: bool
    viewer_can_create_projects: bool
    viewer_can_subscribe: bool
    viewer_can_update_topics: bool
    viewer_default_commit_email: Optional[str] = None
    viewer_default_merge_method: PullRequestMergeMethod
    viewer_has_starred: bool
    viewer_permission: Optional[RepositoryPermission] = None
    viewer_possible_commit_emails: Optional[list[str]] = None
    viewer_subscription: Optional[SubscriptionState] = None
    visibility: RepositoryVisibility
    vulnerability_alert: Optional[RepositoryVulnerabilityAlert] = None
    vulnerability_alerts: Optional[RepositoryVulnerabilityAlertConnection] = None
    watchers: UserConnection
    web_commit_signoff_required: bool
