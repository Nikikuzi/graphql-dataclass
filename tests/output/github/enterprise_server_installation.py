from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from .scalars import ID, DateTime

if TYPE_CHECKING:
    from .gql_types import EnterpriseServerUserAccountConnection
    from .gql_types import EnterpriseServerUserAccountsUploadConnection


@dataclass(kw_only=True)
class EnterpriseServerInstallation:
    """
    EnterpriseServerInstallation - An Enterprise Server installation.

    createdAt - Identifies the date and time when the object was created.

    customerName - The customer name to which the Enterprise Server installation belongs.

    hostName - The host name of the Enterprise Server installation.

    id - The Node ID of the EnterpriseServerInstallation object

    isConnected - Whether or not the installation is connected to an Enterprise Server installation via GitHub Connect.

    updatedAt - Identifies the date and time when the object was last updated.

    userAccounts - User accounts on this Enterprise Server installation.

    userAccountsUploads - User accounts uploads for the Enterprise Server installation.

    """

    created_at: DateTime
    customer_name: str
    host_name: str
    id: ID
    is_connected: bool
    updated_at: DateTime
    user_accounts: EnterpriseServerUserAccountConnection
    user_accounts_uploads: EnterpriseServerUserAccountsUploadConnection
