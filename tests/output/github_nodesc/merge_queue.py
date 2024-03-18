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
    configuration: Optional[MergeQueueConfiguration] = None
    entries: Optional[MergeQueueEntryConnection] = None
    id: ID
    next_entry_estimated_time_to_merge: Optional[int] = None
    repository: Optional[Repository] = None
    resource_path: URI
    url: URI
