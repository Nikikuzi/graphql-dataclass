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
    """
    RepositoryRuleset - A repository ruleset.

    bypassActors - The actors that can bypass this ruleset

    conditions - The set of conditions that must evaluate to true for this ruleset to apply

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    enforcement - The enforcement level of this ruleset

    id - The Node ID of the RepositoryRuleset object

    name - Name of the ruleset.

    rules - List of rules.

    source - Source of ruleset.

    target - Target of the ruleset.

    updatedAt - Identifies the date and time when the object was last updated.

    """

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
