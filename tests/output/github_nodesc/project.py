from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import ProjectState
from .gql_simple_types import Actor
from .scalars import HTML, ID, URI, DateTime

if TYPE_CHECKING:
    from .gql_types import ProjectProgress
    from .gql_types import ProjectCardConnection
    from .gql_types import ProjectColumnConnection
    from .gql_types import ProjectOwner


@dataclass(kw_only=True)
class Project:
    body: Optional[str] = None
    body_h_t_m_l: HTML
    closed: bool
    closed_at: Optional[DateTime] = None
    columns: ProjectColumnConnection
    created_at: DateTime
    creator: Optional[Actor] = None
    database_id: Optional[int] = None
    id: ID
    name: str
    number: int
    owner: ProjectOwner
    pending_cards: ProjectCardConnection
    progress: ProjectProgress
    resource_path: URI
    state: ProjectState
    updated_at: DateTime
    url: URI
    viewer_can_close: bool
    viewer_can_reopen: bool
    viewer_can_update: bool
