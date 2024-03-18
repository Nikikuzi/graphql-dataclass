from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import ProjectV2ItemType
from .gql_simple_types import Actor
from .scalars import ID, BigInt, DateTime

if TYPE_CHECKING:
    from .project_v2 import ProjectV2
    from .gql_unions import ProjectV2ItemContent
    from .gql_unions import ProjectV2ItemFieldValue
    from .gql_types import ProjectV2ItemFieldValueConnection


@dataclass(kw_only=True)
class ProjectV2Item:
    """
    ProjectV2Item - An item within a Project.

    content - The content of the referenced draft issue, issue, or pull request

    createdAt - Identifies the date and time when the object was created.

    creator - The actor who created the item.

    databaseId - Identifies the primary key from the database.

    fieldValueByName - The field value of the first project field which matches the 'name' argument that is set on the item.

    fieldValues - The field values that are set on the item.

    fullDatabaseId - Identifies the primary key from the database as a BigInt.

    id - The Node ID of the ProjectV2Item object

    isArchived - Whether the item is archived.

    project - The project that contains this item.

    type - The type of the item.

    updatedAt - Identifies the date and time when the object was last updated.

    """

    content: Optional[ProjectV2ItemContent] = None
    created_at: DateTime
    creator: Optional[Actor] = None
    database_id: Optional[int] = None
    field_value_by_name: Optional[ProjectV2ItemFieldValue] = None
    field_values: ProjectV2ItemFieldValueConnection
    full_database_id: Optional[BigInt] = None
    id: ID
    is_archived: bool
    project: ProjectV2
    type: ProjectV2ItemType
    updated_at: DateTime
