from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .gql_simple_types import Actor
from .scalars import ID, URI, DateTime

if TYPE_CHECKING:
    from .project_v2_item_connection import ProjectV2ItemConnection
    from .gql_types import TeamConnection
    from .gql_unions import ProjectV2FieldConfiguration
    from .gql_types import ProjectV2FieldConfigurationConnection
    from .gql_types import ProjectV2Owner
    from .gql_types import RepositoryConnection
    from .gql_types import ProjectV2View
    from .gql_types import ProjectV2ViewConnection
    from .gql_types import ProjectV2Workflow
    from .gql_types import ProjectV2WorkflowConnection


@dataclass(kw_only=True)
class ProjectV2:
    """
    ProjectV2 - New projects that manage issues, pull requests and drafts using tables and boards.

    closed - Returns true if the project is closed.

    closedAt - Identifies the date and time when the object was closed.

    createdAt - Identifies the date and time when the object was created.

    creator - The actor who originally created the project.

    databaseId - Identifies the primary key from the database.

    field - A field of the project

    fields - List of fields and their constraints in the project

    id - The Node ID of the ProjectV2 object

    items - List of items in the project

    number - The project's number.

    owner - The project's owner. Currently limited to organizations and users.

    public - Returns true if the project is public.

    readme - The project's readme.

    repositories - The repositories the project is linked to.

    resourcePath - The HTTP path for this project

    shortDescription - The project's short description.

    teams - The teams the project is linked to.

    template - Returns true if this project is a template.

    title - The project's name.

    updatedAt - Identifies the date and time when the object was last updated.

    url - The HTTP URL for this project

    view - A view of the project

    viewerCanClose - Indicates if the object can be closed by the viewer.

    viewerCanReopen - Indicates if the object can be reopened by the viewer.

    viewerCanUpdate - Check if the current viewer can update this object.

    views - List of views in the project

    workflow - A workflow of the project

    workflows - List of the workflows in the project

    """

    closed: bool
    closed_at: Optional[DateTime] = None
    created_at: DateTime
    creator: Optional[Actor] = None
    database_id: Optional[int] = None
    field: Optional[ProjectV2FieldConfiguration] = None
    fields: ProjectV2FieldConfigurationConnection
    id: ID
    items: ProjectV2ItemConnection
    number: int
    owner: ProjectV2Owner
    public: bool
    readme: Optional[str] = None
    repositories: RepositoryConnection
    resource_path: URI
    short_description: Optional[str] = None
    teams: TeamConnection
    template: bool
    title: str
    updated_at: DateTime
    url: URI
    view: Optional[ProjectV2View] = None
    viewer_can_close: bool
    viewer_can_reopen: bool
    viewer_can_update: bool
    views: ProjectV2ViewConnection
    workflow: Optional[ProjectV2Workflow] = None
    workflows: ProjectV2WorkflowConnection
