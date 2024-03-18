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
