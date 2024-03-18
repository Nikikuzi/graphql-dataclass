from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import PackageType
from .gql_simple_types import PackageStatistics
from .scalars import ID

if TYPE_CHECKING:
    from .repository import Repository
    from .package_version import PackageVersion
    from .gql_types import PackageVersionConnection


@dataclass(kw_only=True)
class Package:
    id: ID
    latest_version: Optional[PackageVersion] = None
    name: str
    package_type: PackageType
    repository: Optional[Repository] = None
    statistics: Optional[PackageStatistics] = None
    version: Optional[PackageVersion] = None
    versions: PackageVersionConnection
