from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .gql_simple_types import MergeQueueConfiguration
from .scalars import ID, URI

if TYPE_CHECKING:
    from .repository import Repository
    from .gql_types import MergeQueueEntryConnection


@dataclass(kw_only=True)
class MergeQueue:
    """
    MergeQueue - The queue of pull request entries to be merged into a protected branch in a repository.

    configuration - The configuration for this merge queue

    entries - The entries in the queue

    id - The Node ID of the MergeQueue object

    nextEntryEstimatedTimeToMerge - The estimated time in seconds until a newly added entry would be merged

    repository - The repository this merge queue belongs to

    resourcePath - The HTTP path for this merge queue

    url - The HTTP URL for this merge queue

    """

    configuration: Optional[MergeQueueConfiguration] = None
    entries: Optional[MergeQueueEntryConnection] = None
    id: ID
    next_entry_estimated_time_to_merge: Optional[int] = None
    repository: Optional[Repository] = None
    resource_path: URI
    url: URI
