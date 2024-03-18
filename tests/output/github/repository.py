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
    """
        Repository - A repository contains the content for a project.

        allowUpdateBranch - Whether or not a pull request head branch that is behind its base branch can
    always be updated even if it is not required to be up to date before merging.

        archivedAt - Identifies the date and time when the repository was archived.

        assignableUsers - A list of users that can be assigned to issues in this repository.

        autoMergeAllowed - Whether or not Auto-merge can be enabled on pull requests in this repository.

        branchProtectionRules - A list of branch protection rules for this repository.

        codeOfConduct - Returns the code of conduct for this repository

        codeowners - Information extracted from the repository's `CODEOWNERS` file.

        collaborators - A list of collaborators associated with the repository.

        commitComments - A list of commit comments associated with the repository.

        contactLinks - Returns a list of contact links associated to the repository

        contributingGuidelines - Returns the contributing guidelines for this repository.

        createdAt - Identifies the date and time when the object was created.

        databaseId - Identifies the primary key from the database.

        defaultBranchRef - The Ref associated with the repository's default branch.

        deleteBranchOnMerge - Whether or not branches are automatically deleted when merged in this repository.

        dependencyGraphManifests - A list of dependency manifests contained in the repository

        deployKeys - A list of deploy keys that are on this repository.

        deployments - Deployments associated with the repository

        description - The description of the repository.

        descriptionHTML - The description of the repository rendered to HTML.

        discussion - Returns a single discussion from the current repository by number.

        discussionCategories - A list of discussion categories that are available in the repository.

        discussionCategory - A discussion category by slug.

        discussions - A list of discussions that have been opened in the repository.

        diskUsage - The number of kilobytes this repository occupies on disk.

        environment - Returns a single active environment from the current repository by name.

        environments - A list of environments that are in this repository.

        forkCount - Returns how many forks there are of this repository in the whole network.

        forkingAllowed - Whether this repository allows forks.

        forks - A list of direct forked repositories.

        fundingLinks - The funding links for this repository

        hasDiscussionsEnabled - Indicates if the repository has the Discussions feature enabled.

        hasIssuesEnabled - Indicates if the repository has issues feature enabled.

        hasProjectsEnabled - Indicates if the repository has the Projects feature enabled.

        hasSponsorshipsEnabled - Indicates if the repository displays a Sponsor button for financial contributions.

        hasVulnerabilityAlertsEnabled - Whether vulnerability alerts are enabled for the repository.

        hasWikiEnabled - Indicates if the repository has wiki feature enabled.

        homepageUrl - The repository's URL.

        id - The Node ID of the Repository object

        interactionAbility - The interaction ability settings for this repository.

        isArchived - Indicates if the repository is unmaintained.

        isBlankIssuesEnabled - Returns true if blank issue creation is allowed

        isDisabled - Returns whether or not this repository disabled.

        isEmpty - Returns whether or not this repository is empty.

        isFork - Identifies if the repository is a fork.

        isInOrganization - Indicates if a repository is either owned by an organization, or is a private fork of an organization repository.

        isLocked - Indicates if the repository has been locked or not.

        isMirror - Identifies if the repository is a mirror.

        isPrivate - Identifies if the repository is private or internal.

        isSecurityPolicyEnabled - Returns true if this repository has a security policy

        isTemplate - Identifies if the repository is a template that can be used to generate new repositories.

        isUserConfigurationRepository - Is this repository a user configuration repository?

        issue - Returns a single issue from the current repository by number.

        issueOrPullRequest - Returns a single issue-like object from the current repository by number.

        issueTemplates - Returns a list of issue templates associated to the repository

        issues - A list of issues that have been opened in the repository.

        label - Returns a single label by name

        labels - A list of labels associated with the repository.

        languages - A list containing a breakdown of the language composition of the repository.

        latestRelease - Get the latest release for the repository if one exists.

        licenseInfo - The license associated with the repository

        lockReason - The reason the repository has been locked.

        mentionableUsers - A list of Users that can be mentioned in the context of the repository.

        mergeCommitAllowed - Whether or not PRs are merged with a merge commit on this repository.

        mergeCommitMessage - How the default commit message will be generated when merging a pull request.

        mergeCommitTitle - How the default commit title will be generated when merging a pull request.

        mergeQueue - The merge queue for a specified branch, otherwise the default branch if not provided.

        milestone - Returns a single milestone from the current repository by number.

        milestones - A list of milestones associated with the repository.

        mirrorUrl - The repository's original mirror URL.

        name - The name of the repository.

        nameWithOwner - The repository's name with owner.

        object - A Git object in the repository

        openGraphImageUrl - The image used to represent this repository in Open Graph data.

        owner - The User owner of the repository.

        packages - A list of packages under the owner.

        parent - The repository parent, if this is a fork.

        pinnedDiscussions - A list of discussions that have been pinned in this repository.

        pinnedIssues - A list of pinned issues for this repository.

        primaryLanguage - The primary language of the repository's code.

        project - Find project by number.

        projectV2 - Finds and returns the Project according to the provided Project number.

        projects - A list of projects under the owner.

        projectsResourcePath - The HTTP path listing the repository's projects

        projectsUrl - The HTTP URL listing the repository's projects

        projectsV2 - List of projects linked to this repository.

        pullRequest - Returns a single pull request from the current repository by number.

        pullRequestTemplates - Returns a list of pull request templates associated to the repository

        pullRequests - A list of pull requests that have been opened in the repository.

        pushedAt - Identifies the date and time when the repository was last pushed to.

        rebaseMergeAllowed - Whether or not rebase-merging is enabled on this repository.

        recentProjects - Recent projects that this user has modified in the context of the owner.

        ref - Fetch a given ref from the repository

        refs - Fetch a list of refs from the repository

        release - Lookup a single release given various criteria.

        releases - List of releases which are dependent on this repository.

        repositoryTopics - A list of applied repository-topic associations for this repository.

        resourcePath - The HTTP path for this repository

        ruleset - Returns a single ruleset from the current repository by ID.

        rulesets - A list of rulesets for this repository.

        securityPolicyUrl - The security policy URL.

        shortDescriptionHTML - A description of the repository, rendered to HTML without any links in it.

        squashMergeAllowed - Whether or not squash-merging is enabled on this repository.

        squashMergeCommitMessage - How the default commit message will be generated when squash merging a pull request.

        squashMergeCommitTitle - How the default commit title will be generated when squash merging a pull request.

        sshUrl - The SSH URL to clone this repository

        stargazerCount - Returns a count of how many stargazers there are on this object

        stargazers - A list of users who have starred this starrable.

        submodules - Returns a list of all submodules in this repository parsed from the
    .gitmodules file as of the default branch's HEAD commit.

        tempCloneToken - Temporary authentication token for cloning this repository.

        templateRepository - The repository from which this repository was generated, if any.

        updatedAt - Identifies the date and time when the object was last updated.

        url - The HTTP URL for this repository

        usesCustomOpenGraphImage - Whether this repository has a custom image to use with Open Graph as opposed to being represented by the owner's avatar.

        viewerCanAdminister - Indicates whether the viewer has admin permissions on this repository.

        viewerCanCreateProjects - Can the current viewer create new projects on this owner.

        viewerCanSubscribe - Check if the viewer is able to change their subscription status for the repository.

        viewerCanUpdateTopics - Indicates whether the viewer can update the topics of this repository.

        viewerDefaultCommitEmail - The last commit email for the viewer.

        viewerDefaultMergeMethod - The last used merge method by the viewer or the default for the repository.

        viewerHasStarred - Returns a boolean indicating whether the viewing user has starred this starrable.

        viewerPermission - The users permission level on the repository. Will return null if authenticated as an GitHub App.

        viewerPossibleCommitEmails - A list of emails this viewer can commit with.

        viewerSubscription - Identifies if the viewer is watching, not watching, or ignoring the subscribable entity.

        visibility - Indicates the repository's visibility level.

        vulnerabilityAlert - Returns a single vulnerability alert from the current repository by number.

        vulnerabilityAlerts - A list of vulnerability alerts that are on this repository.

        watchers - A list of users watching the repository.

        webCommitSignoffRequired - Whether contributors are required to sign off on web-based commits in this repository.

    """

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
