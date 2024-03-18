from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from .scalars import ID

if TYPE_CHECKING:
    from .gql_types import RepositoryConnection
    from .gql_types import StargazerConnection


@dataclass(kw_only=True)
class Topic:
    id: ID
    name: str
    related_topics: list[Topic]
    repositories: RepositoryConnection
    stargazer_count: int
    stargazers: StargazerConnection
    viewer_has_starred: bool
