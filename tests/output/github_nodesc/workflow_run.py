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
