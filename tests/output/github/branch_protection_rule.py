from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .gql_simple_types import Actor
from .scalars import ID

if TYPE_CHECKING:
    from .repository import Repository
    from .gql_types import BranchProtectionRuleConflictConnection
    from .gql_types import RefConnection
    from .gql_types import BypassForcePushAllowanceConnection
    from .gql_types import BypassPullRequestAllowanceConnection
    from .gql_types import PushAllowanceConnection
    from .gql_types import RequiredStatusCheckDescription
    from .gql_types import ReviewDismissalAllowanceConnection


@dataclass(kw_only=True)
class BranchProtectionRule:
    """
        BranchProtectionRule - A branch protection rule.

        allowsDeletions - Can this branch be deleted.

        allowsForcePushes - Are force pushes allowed on this branch.

        blocksCreations - Is branch creation a protected operation.

        branchProtectionRuleConflicts - A list of conflicts matching branches protection rule and other branch protection rules

        bypassForcePushAllowances - A list of actors able to force push for this branch protection rule.

        bypassPullRequestAllowances - A list of actors able to bypass PRs for this branch protection rule.

        creator - The actor who created this branch protection rule.

        databaseId - Identifies the primary key from the database.

        dismissesStaleReviews - Will new commits pushed to matching branches dismiss pull request review approvals.

        id - The Node ID of the BranchProtectionRule object

        isAdminEnforced - Can admins override branch protection.

        lockAllowsFetchAndMerge - Whether users can pull changes from upstream when the branch is locked. Set to
    `true` to allow fork syncing. Set to `false` to prevent fork syncing.

        lockBranch - Whether to set the branch as read-only. If this is true, users will not be able to push to the branch.

        matchingRefs - Repository refs that are protected by this rule

        pattern - Identifies the protection rule pattern.

        pushAllowances - A list push allowances for this branch protection rule.

        repository - The repository associated with this branch protection rule.

        requireLastPushApproval - Whether the most recent push must be approved by someone other than the person who pushed it

        requiredApprovingReviewCount - Number of approving reviews required to update matching branches.

        requiredDeploymentEnvironments - List of required deployment environments that must be deployed successfully to update matching branches

        requiredStatusCheckContexts - List of required status check contexts that must pass for commits to be accepted to matching branches.

        requiredStatusChecks - List of required status checks that must pass for commits to be accepted to matching branches.

        requiresApprovingReviews - Are approving reviews required to update matching branches.

        requiresCodeOwnerReviews - Are reviews from code owners required to update matching branches.

        requiresCommitSignatures - Are commits required to be signed.

        requiresConversationResolution - Are conversations required to be resolved before merging.

        requiresDeployments - Does this branch require deployment to specific environments before merging

        requiresLinearHistory - Are merge commits prohibited from being pushed to this branch.

        requiresStatusChecks - Are status checks required to update matching branches.

        requiresStrictStatusChecks - Are branches required to be up to date before merging.

        restrictsPushes - Is pushing to matching branches restricted.

        restrictsReviewDismissals - Is dismissal of pull request reviews restricted.

        reviewDismissalAllowances - A list review dismissal allowances for this branch protection rule.

    """

    allows_deletions: bool
    allows_force_pushes: bool
    blocks_creations: bool
    branch_protection_rule_conflicts: BranchProtectionRuleConflictConnection
    bypass_force_push_allowances: BypassForcePushAllowanceConnection
    bypass_pull_request_allowances: BypassPullRequestAllowanceConnection
    creator: Optional[Actor] = None
    database_id: Optional[int] = None
    dismisses_stale_reviews: bool
    id: ID
    is_admin_enforced: bool
    lock_allows_fetch_and_merge: bool
    lock_branch: bool
    matching_refs: RefConnection
    pattern: str
    push_allowances: PushAllowanceConnection
    repository: Optional[Repository] = None
    require_last_push_approval: bool
    required_approving_review_count: Optional[int] = None
    required_deployment_environments: Optional[list[str]] = None
    required_status_check_contexts: Optional[list[str]] = None
    required_status_checks: Optional[list[RequiredStatusCheckDescription]] = None
    requires_approving_reviews: bool
    requires_code_owner_reviews: bool
    requires_commit_signatures: bool
    requires_conversation_resolution: bool
    requires_deployments: bool
    requires_linear_history: bool
    requires_status_checks: bool
    requires_strict_status_checks: bool
    restricts_pushes: bool
    restricts_review_dismissals: bool
    review_dismissal_allowances: ReviewDismissalAllowanceConnection
