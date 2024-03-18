from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import SubscriptionState
from .scalars import HTML, ID, URI, DateTime, GitObjectID

if TYPE_CHECKING:
    from .pull_request_connection import PullRequestConnection
    from .organization import Organization
    from .repository import Repository
    from .commit_comment_connection import CommitCommentConnection
    from .gql_types import DeploymentConnection
    from .gql_types import SubmoduleConnection
    from .gql_types import GitActor
    from .gql_types import GitActorConnection
    from .gql_types import Blame
    from .gql_types import CheckSuiteConnection
    from .gql_types import TreeEntry
    from .gql_types import CommitHistoryConnection
    from .gql_types import CommitConnection
    from .gql_types import GitSignature
    from .gql_types import Status
    from .gql_types import StatusCheckRollup
    from .gql_types import Tree


@dataclass(kw_only=True)
class Commit:
    abbreviated_oid: str
    additions: int
    associated_pull_requests: Optional[PullRequestConnection] = None
    author: Optional[GitActor] = None
    authored_by_committer: bool
    authored_date: DateTime
    authors: GitActorConnection
    blame: Blame
    changed_files_if_available: Optional[int] = None
    check_suites: Optional[CheckSuiteConnection] = None
    comments: CommitCommentConnection
    commit_resource_path: URI
    commit_url: URI
    committed_date: DateTime
    committed_via_web: bool
    committer: Optional[GitActor] = None
    deletions: int
    deployments: Optional[DeploymentConnection] = None
    file: Optional[TreeEntry] = None
    history: CommitHistoryConnection
    id: ID
    message: str
    message_body: str
    message_body_h_t_m_l: HTML
    message_headline: str
    message_headline_h_t_m_l: HTML
    oid: GitObjectID
    on_behalf_of: Optional[Organization] = None
    parents: CommitConnection
    repository: Repository
    resource_path: URI
    signature: Optional[GitSignature] = None
    status: Optional[Status] = None
    status_check_rollup: Optional[StatusCheckRollup] = None
    submodules: SubmoduleConnection
    tarball_url: URI
    tree: Tree
    tree_resource_path: URI
    tree_url: URI
    url: URI
    viewer_can_subscribe: bool
    viewer_subscription: Optional[SubscriptionState] = None
    zipball_url: URI
