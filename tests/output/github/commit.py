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
    """
        Commit - Represents a Git commit.

        abbreviatedOid - An abbreviated version of the Git object ID

        additions - The number of additions in this commit.

        associatedPullRequests - The merged Pull Request that introduced the commit to the repository. If the
    commit is not present in the default branch, additionally returns open Pull
    Requests associated with the commit

        author - Authorship details of the commit.

        authoredByCommitter - Check if the committer and the author match.

        authoredDate - The datetime when this commit was authored.

        authors - The list of authors for this commit based on the git author and the Co-authored-by
    message trailer. The git author will always be first.

        blame - Fetches `git blame` information.

        changedFilesIfAvailable - The number of changed files in this commit. If GitHub is unable to calculate
    the number of changed files (for example due to a timeout), this will return
    `null`. We recommend using this field instead of `changedFiles`.

        checkSuites - The check suites associated with a commit.

        comments - Comments made on the commit.

        commitResourcePath - The HTTP path for this Git object

        commitUrl - The HTTP URL for this Git object

        committedDate - The datetime when this commit was committed.

        committedViaWeb - Check if committed via GitHub web UI.

        committer - Committer details of the commit.

        deletions - The number of deletions in this commit.

        deployments - The deployments associated with a commit.

        file - The tree entry representing the file located at the given path.

        history - The linear commit history starting from (and including) this commit, in the same order as `git log`.

        id - The Node ID of the Commit object

        message - The Git commit message

        messageBody - The Git commit message body

        messageBodyHTML - The commit message body rendered to HTML.

        messageHeadline - The Git commit message headline

        messageHeadlineHTML - The commit message headline rendered to HTML.

        oid - The Git object ID

        onBehalfOf - The organization this commit was made on behalf of.

        parents - The parents of a commit.

        repository - The Repository this commit belongs to

        resourcePath - The HTTP path for this commit

        signature - Commit signing information, if present.

        status - Status information for this commit

        statusCheckRollup - Check and Status rollup information for this commit.

        submodules - Returns a list of all submodules in this repository as of this Commit parsed from the .gitmodules file.

        tarballUrl - Returns a URL to download a tarball archive for a repository.
    Note: For private repositories, these links are temporary and expire after five minutes.

        tree - Commit's root Tree

        treeResourcePath - The HTTP path for the tree of this commit

        treeUrl - The HTTP URL for the tree of this commit

        url - The HTTP URL for this commit

        viewerCanSubscribe - Check if the viewer is able to change their subscription status for the repository.

        viewerSubscription - Identifies if the viewer is watching, not watching, or ignoring the subscribable entity.

        zipballUrl - Returns a URL to download a zipball archive for a repository.
    Note: For private repositories, these links are temporary and expire after five minutes.

    """

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
