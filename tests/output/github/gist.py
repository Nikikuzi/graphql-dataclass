from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .scalars import ID, URI, DateTime

if TYPE_CHECKING:
    from .gql_types import RepositoryOwner
    from .gql_types import StargazerConnection
    from .gql_types import GistCommentConnection
    from .gql_types import GistFile
    from .gql_types import GistConnection


@dataclass(kw_only=True)
class Gist:
    """
    Gist - A Gist.

    comments - A list of comments associated with the gist

    createdAt - Identifies the date and time when the object was created.

    description - The gist description.

    files - The files in this gist.

    forks - A list of forks associated with the gist

    id - The Node ID of the Gist object

    isFork - Identifies if the gist is a fork.

    isPublic - Whether the gist is public or not.

    name - The gist name.

    owner - The gist owner.

    pushedAt - Identifies when the gist was last pushed to.

    resourcePath - The HTML path to this resource.

    stargazerCount - Returns a count of how many stargazers there are on this object

    stargazers - A list of users who have starred this starrable.

    updatedAt - Identifies the date and time when the object was last updated.

    url - The HTTP URL for this Gist.

    viewerHasStarred - Returns a boolean indicating whether the viewing user has starred this starrable.

    """

    comments: GistCommentConnection
    created_at: DateTime
    description: Optional[str] = None
    files: Optional[list[GistFile]] = None
    forks: GistConnection
    id: ID
    is_fork: bool
    is_public: bool
    name: str
    owner: Optional[RepositoryOwner] = None
    pushed_at: Optional[DateTime] = None
    resource_path: URI
    stargazer_count: int
    stargazers: StargazerConnection
    updated_at: DateTime
    url: URI
    viewer_has_starred: bool
