from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import ProjectColumnPurpose
from .scalars import ID, URI, DateTime

if TYPE_CHECKING:
    from .project import Project
    from .gql_types import ProjectCardConnection


@dataclass(kw_only=True)
class ProjectColumn:
    cards: ProjectCardConnection
    created_at: DateTime
    database_id: Optional[int] = None
    id: ID
    name: str
    project: Project
    purpose: Optional[ProjectColumnPurpose] = None
    resource_path: URI
    updated_at: DateTime
    url: URI
