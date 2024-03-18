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
    """
    Release - A release contains the content for a release.

    author - The author of the release

    createdAt - Identifies the date and time when the object was created.

    databaseId - Identifies the primary key from the database.

    description - The description of the release.

    descriptionHTML - The description of this release rendered to HTML.

    id - The Node ID of the Release object

    isDraft - Whether or not the release is a draft

    isLatest - Whether or not the release is the latest releast

    isPrerelease - Whether or not the release is a prerelease

    mentions - A list of users mentioned in the release description

    name - The title of the release.

    publishedAt - Identifies the date and time when the release was created.

    reactionGroups - A list of reactions grouped by content left on the subject.

    reactions - A list of Reactions left on the Issue.

    releaseAssets - List of releases assets which are dependent on this release.

    repository - The repository that the release belongs to.

    resourcePath - The HTTP path for this issue

    shortDescriptionHTML - A description of the release, rendered to HTML without any links in it.

    tag - The Git tag the release points to

    tagCommit - The tag commit for this release.

    tagName - The name of the release's Git tag

    updatedAt - Identifies the date and time when the object was last updated.

    url - The HTTP URL for this issue

    viewerCanReact - Can user react to this subject

    """

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
