from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .enums import SecurityAdvisoryClassification, SecurityAdvisorySeverity
from .gql_simple_types import SecurityAdvisoryReference
from .scalars import ID, URI, DateTime

if TYPE_CHECKING:
    from .gql_types import CVSS
    from .gql_types import SecurityAdvisoryIdentifier
    from .gql_types import CWEConnection
    from .gql_types import SecurityVulnerabilityConnection


@dataclass(kw_only=True)
class SecurityAdvisory:
    classification: SecurityAdvisoryClassification
    cvss: CVSS
    cwes: CWEConnection
    database_id: Optional[int] = None
    description: str
    ghsa_id: str
    id: ID
    identifiers: list[SecurityAdvisoryIdentifier]
    notifications_permalink: Optional[URI] = None
    origin: str
    permalink: Optional[URI] = None
    published_at: DateTime
    references: list[SecurityAdvisoryReference]
    severity: SecurityAdvisorySeverity
    summary: str
    updated_at: DateTime
    vulnerabilities: SecurityVulnerabilityConnection
    withdrawn_at: Optional[DateTime] = None
