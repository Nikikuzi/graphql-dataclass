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
    """
    Deployment - Represents triggered deployment instance.

    commit - Identifies the commit sha of the deployment.

    commitOid - Identifies the oid of the deployment commit, even if the commit has been deleted.

    createdAt - Identifies the date and time when the object was created.

    creator - Identifies the actor who triggered the deployment.

    databaseId - Identifies the primary key from the database.

    description - The deployment description.

    environment - The latest environment to which this deployment was made.

    id - The Node ID of the Deployment object

    latestEnvironment - The latest environment to which this deployment was made.

    latestStatus - The latest status of this deployment.

    originalEnvironment - The original environment to which this deployment was made.

    payload - Extra information that a deployment system might need.

    ref - Identifies the Ref of the deployment, if the deployment was created by ref.

    repository - Identifies the repository associated with the deployment.

    state - The current state of the deployment.

    statuses - A list of statuses associated with the deployment.

    task - The deployment task.

    updatedAt - Identifies the date and time when the object was last updated.

    """

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
