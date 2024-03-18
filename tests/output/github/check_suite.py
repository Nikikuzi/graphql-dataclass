from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import CheckConclusionState, CheckStatusState
from .scalars import ID, URI, DateTime

if TYPE_CHECKING:
    from .pull_request_connection import PullRequestConnection
    from .ref import Ref
    from .app import App
    from .user import User
    from .repository import Repository
    from .commit import Commit
    from .workflow_run import WorkflowRun
    from .gql_types import CheckRunConnection
    from .gql_types import Push


@dataclass(kw_only=True)
class CheckSuite:
    """
    CheckSuite - A check suite.

    app - The GitHub App which created this check suite.

    branch - The name of the branch for this check suite.

    checkRuns - The check runs associated with a check suite.

    commit - The commit for this check suite

    conclusion - The conclusion of this check suite.

    createdAt - Identifies the date and time when the object was created.

    creator - The user who triggered the check suite.

    databaseId - Identifies the primary key from the database.

    id - The Node ID of the CheckSuite object

    matchingPullRequests - A list of open pull requests matching the check suite.

    push - The push that triggered this check suite.

    repository - The repository associated with this check suite.

    resourcePath - The HTTP path for this check suite

    status - The status of this check suite.

    updatedAt - Identifies the date and time when the object was last updated.

    url - The HTTP URL for this check suite

    workflowRun - The workflow run associated with this check suite.

    """

    app: Optional[App] = None
    branch: Optional[Ref] = None
    check_runs: Optional[CheckRunConnection] = None
    commit: Commit
    conclusion: Optional[CheckConclusionState] = None
    created_at: DateTime
    creator: Optional[User] = None
    database_id: Optional[int] = None
    id: ID
    matching_pull_requests: Optional[PullRequestConnection] = None
    push: Optional[Push] = None
    repository: Repository
    resource_path: URI
    status: CheckStatusState
    updated_at: DateTime
    url: URI
    workflow_run: Optional[WorkflowRun] = None
