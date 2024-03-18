from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .scalars import HTML, ID, URI, DateTime

if TYPE_CHECKING:
    from .user_connection import UserConnection
    from .ref import Ref
    from .user import User
    from .repository import Repository
    from .reaction_group import ReactionGroup
    from .commit import Commit
    from .gql_types import ReactionConnection
    from .gql_types import ReleaseAssetConnection


@dataclass(kw_only=True)
class Release:
    author: Optional[User] = None
    created_at: DateTime
    database_id: Optional[int] = None
    description: Optional[str] = None
    description_h_t_m_l: Optional[HTML] = None
    id: ID
    is_draft: bool
    is_latest: bool
    is_prerelease: bool
    mentions: Optional[UserConnection] = None
    name: Optional[str] = None
    published_at: Optional[DateTime] = None
    reaction_groups: Optional[list[ReactionGroup]] = None
    reactions: ReactionConnection
    release_assets: ReleaseAssetConnection
    repository: Repository
    resource_path: URI
    short_description_h_t_m_l: Optional[HTML] = None
    tag: Optional[Ref] = None
    tag_commit: Optional[Commit] = None
    tag_name: str
    updated_at: DateTime
    url: URI
    viewer_can_react: bool
