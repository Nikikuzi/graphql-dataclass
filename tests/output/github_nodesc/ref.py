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
