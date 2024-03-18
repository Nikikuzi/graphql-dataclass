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
