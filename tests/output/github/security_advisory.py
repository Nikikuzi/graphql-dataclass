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
    """
    SecurityAdvisory - A GitHub Security Advisory

    classification - The classification of the advisory

    cvss - The CVSS associated with this advisory

    cwes - CWEs associated with this Advisory

    databaseId - Identifies the primary key from the database.

    description - This is a long plaintext description of the advisory

    ghsaId - The GitHub Security Advisory ID

    id - The Node ID of the SecurityAdvisory object

    identifiers - A list of identifiers for this advisory

    notificationsPermalink - The permalink for the advisory's dependabot alerts page

    origin - The organization that originated the advisory

    permalink - The permalink for the advisory

    publishedAt - When the advisory was published

    references - A list of references for this advisory

    severity - The severity of the advisory

    summary - A short plaintext summary of the advisory

    updatedAt - When the advisory was last updated

    vulnerabilities - Vulnerabilities associated with this Advisory

    withdrawnAt - When the advisory was withdrawn, if it has been withdrawn

    """

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
