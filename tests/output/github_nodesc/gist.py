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
