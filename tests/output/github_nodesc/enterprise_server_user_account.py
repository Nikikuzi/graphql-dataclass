from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .scalars import ID, DateTime

if TYPE_CHECKING:
    from .enterprise_server_installation import EnterpriseServerInstallation
    from .gql_types import EnterpriseServerUserAccountEmailConnection


@dataclass(kw_only=True)
class EnterpriseServerUserAccount:
    created_at: DateTime
    emails: EnterpriseServerUserAccountEmailConnection
    enterprise_server_installation: EnterpriseServerInstallation
    id: ID
    is_site_admin: bool
    login: str
    profile_name: Optional[str] = None
    remote_created_at: DateTime
    remote_user_id: int
    updated_at: DateTime
