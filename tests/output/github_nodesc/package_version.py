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
