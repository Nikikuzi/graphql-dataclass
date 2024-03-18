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
    """
    ProjectColumn - A column inside a project.

    cards - List of cards in the column

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    id - The Node ID of the ProjectColumn object

    name - The project column's name.

    project - The project that contains this column.

    purpose - The semantic purpose of the column

    resourcePath - The HTTP path for this project column

    updatedAt - Identifies the date and time when the object was last updated.

    url - The HTTP URL for this project column

    """

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
