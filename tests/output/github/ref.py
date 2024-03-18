from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .gql_simple_types import RefUpdateRule
from .scalars import ID

if TYPE_CHECKING:
    from .pull_request_connection import PullRequestConnection
    from .branch_protection_rule import BranchProtectionRule
    from .repository import Repository
    from .gql_types import GitObject
    from .gql_types import RepositoryRuleConnection
    from .gql_types import Comparison


@dataclass(kw_only=True)
class Ref:
    """
    Ref - Represents a Git reference.

    associatedPullRequests - A list of pull requests with this ref as the head ref.

    branchProtectionRule - Branch protection rules for this ref

    compare - Compares the current ref as a base ref to another head ref, if the comparison can be made.

    id - The Node ID of the Ref object

    name - The ref name.

    prefix - The ref's prefix, such as `refs/heads/` or `refs/tags/`.

    refUpdateRule - Branch protection rules that are viewable by non-admins

    repository - The repository the ref belongs to.

    rules - A list of rules from active Repository and Organization rulesets that apply to this ref.

    target - The object the ref points to. Returns null when object does not exist.

    """

    associated_pull_requests: PullRequestConnection
    branch_protection_rule: Optional[BranchProtectionRule] = None
    compare: Optional[Comparison] = None
    id: ID
    name: str
    prefix: str
    ref_update_rule: Optional[RefUpdateRule] = None
    repository: Repository
    rules: Optional[RepositoryRuleConnection] = None
    target: Optional[GitObject] = None
