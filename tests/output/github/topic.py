from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from .scalars import ID

if TYPE_CHECKING:
    from .gql_types import RepositoryConnection
    from .gql_types import StargazerConnection


@dataclass(kw_only=True)
class Topic:
    """
        Topic - A topic aggregates entities that are related to a subject.

        id - The Node ID of the Topic object

        name - The topic's name.

        relatedTopics - A list of related topics, including aliases of this topic, sorted with the most relevant
    first. Returns up to 10 Topics.

        repositories - A list of repositories.

        stargazerCount - Returns a count of how many stargazers there are on this object

        stargazers - A list of users who have starred this starrable.

        viewerHasStarred - Returns a boolean indicating whether the viewing user has starred this starrable.

    """

    id: ID
    name: str
    related_topics: list[Topic]
    repositories: RepositoryConnection
    stargazer_count: int
    stargazers: StargazerConnection
    viewer_has_starred: bool
