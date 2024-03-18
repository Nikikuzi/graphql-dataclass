from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import DeploymentState
from .gql_simple_types import Actor
from .scalars import ID, DateTime

if TYPE_CHECKING:
    from .ref import Ref
    from .repository import Repository
    from .commit import Commit
    from .gql_types import DeploymentStatus
    from .gql_types import DeploymentStatusConnection


@dataclass(kw_only=True)
class Deployment:
    commit: Optional[Commit] = None
    commit_oid: str
    created_at: DateTime
    creator: Actor
    database_id: Optional[int] = None
    description: Optional[str] = None
    environment: Optional[str] = None
    id: ID
    latest_environment: Optional[str] = None
    latest_status: Optional[DeploymentStatus] = None
    original_environment: Optional[str] = None
    payload: Optional[str] = None
    ref: Optional[Ref] = None
    repository: Repository
    state: Optional[DeploymentState] = None
    statuses: Optional[DeploymentStatusConnection] = None
    task: Optional[str] = None
    updated_at: DateTime
