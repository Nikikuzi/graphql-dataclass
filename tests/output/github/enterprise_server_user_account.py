from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .scalars import ID, DateTime

if TYPE_CHECKING:
    from .enterprise_server_installation import EnterpriseServerInstallation
    from .gql_types import EnterpriseServerUserAccountEmailConnection


@dataclass(kw_only=True)
class EnterpriseServerUserAccount:
    """
    EnterpriseServerUserAccount - A user account on an Enterprise Server installation.

    createdAt - Identifies the date and time when the object was created.

    emails - User emails belonging to this user account.

    enterpriseServerInstallation - The Enterprise Server installation on which this user account exists.

    id - The Node ID of the EnterpriseServerUserAccount object

    isSiteAdmin - Whether the user account is a site administrator on the Enterprise Server installation.

    login - The login of the user account on the Enterprise Server installation.

    profileName - The profile name of the user account on the Enterprise Server installation.

    remoteCreatedAt - The date and time when the user account was created on the Enterprise Server installation.

    remoteUserId - The ID of the user account on the Enterprise Server installation.

    updatedAt - Identifies the date and time when the object was last updated.

    """

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
