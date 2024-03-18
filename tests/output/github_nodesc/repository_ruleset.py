from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import RepositoryRulesetTarget, RuleEnforcement
from .scalars import ID, DateTime

if TYPE_CHECKING:
    from .gql_types import RepositoryRulesetBypassActorConnection
    from .gql_types import RepositoryRuleConditions
    from .gql_types import RepositoryRuleConnection
    from .gql_unions import RuleSource


@dataclass(kw_only=True)
class RepositoryRuleset:
    bypass_actors: Optional[RepositoryRulesetBypassActorConnection] = None
    conditions: RepositoryRuleConditions
    created_at: DateTime
    database_id: Optional[int] = None
    enforcement: RuleEnforcement
    id: ID
    name: str
    rules: Optional[RepositoryRuleConnection] = None
    source: RuleSource
    target: Optional[RepositoryRulesetTarget] = None
    updated_at: DateTime
