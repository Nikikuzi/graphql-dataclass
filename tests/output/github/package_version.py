from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .gql_simple_types import PackageVersionStatistics
from .scalars import ID

if TYPE_CHECKING:
    from .release import Release
    from .package import Package
    from .gql_types import PackageFileConnection


@dataclass(kw_only=True)
class PackageVersion:
    """
    PackageVersion - Information about a specific package version.

    files - List of files associated with this package version

    id - The Node ID of the PackageVersion object

    package - The package associated with this version.

    platform - The platform this version was built for.

    preRelease - Whether or not this version is a pre-release.

    readme - The README of this package version.

    release - The release associated with this package version.

    statistics - Statistics about package activity.

    summary - The package version summary.

    version - The version string.

    """

    files: PackageFileConnection
    id: ID
    package: Optional[Package] = None
    platform: Optional[str] = None
    pre_release: bool
    readme: Optional[str] = None
    release: Optional[Release] = None
    statistics: Optional[PackageVersionStatistics] = None
    summary: Optional[str] = None
    version: str
