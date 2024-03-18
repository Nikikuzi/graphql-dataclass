from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .scalars import ID, URI, DateTime

if TYPE_CHECKING:
    from .check_suite import CheckSuite
    from .gql_types import DeploymentReviewConnection
    from .gql_types import WorkflowRunFile
    from .gql_types import DeploymentRequestConnection
    from .gql_types import Workflow


@dataclass(kw_only=True)
class WorkflowRun:
    """
    WorkflowRun - A workflow run.

    checkSuite - The check suite this workflow run belongs to.

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    deploymentReviews - The log of deployment reviews

    event - The event that triggered the workflow run

    file - The workflow file

    id - The Node ID of the WorkflowRun object

    pendingDeploymentRequests - The pending deployment requests of all check runs in this workflow run

    resourcePath - The HTTP path for this workflow run

    runNumber - A number that uniquely identifies this workflow run in its parent workflow.

    updatedAt - Identifies the date and time when the object was last updated.

    url - The HTTP URL for this workflow run

    workflow - The workflow executed in this workflow run.

    """

    check_suite: CheckSuite
    created_at: DateTime
    database_id: Optional[int] = None
    deployment_reviews: DeploymentReviewConnection
    event: str
    file: Optional[WorkflowRunFile] = None
    id: ID
    pending_deployment_requests: DeploymentRequestConnection
    resource_path: URI
    run_number: int
    updated_at: DateTime
    url: URI
    workflow: Workflow
