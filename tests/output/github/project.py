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
    """
    Project - Projects manage issues, pull requests and notes within a project owner.

    body - The project's description body.

    bodyHTML - The projects description body rendered to HTML.

    closed - Indicates if the object is closed (definition of closed may depend on type)

    closedAt - Identifies the date and time when the object was closed.

    columns - List of columns in the project

    createdAt - Identifies the date and time when the object was created.

    creator - The actor who originally created the project.

    databaseId - Identifies the primary key from the database.

    id - The Node ID of the Project object

    name - The project's name.

    number - The project's number.

    owner - The project's owner. Currently limited to repositories, organizations, and users.

    pendingCards - List of pending cards in this project

    progress - Project progress details.

    resourcePath - The HTTP path for this project

    state - Whether the project is open or closed.

    updatedAt - Identifies the date and time when the object was last updated.

    url - The HTTP URL for this project

    viewerCanClose - Indicates if the object can be closed by the viewer.

    viewerCanReopen - Indicates if the object can be reopened by the viewer.

    viewerCanUpdate - Check if the current viewer can update this object.

    """

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
