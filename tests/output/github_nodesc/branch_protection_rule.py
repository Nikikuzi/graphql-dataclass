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
