from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from .scalars import ID, DateTime

if TYPE_CHECKING:
    from .gql_types import EnterpriseServerUserAccountConnection
    from .gql_types import EnterpriseServerUserAccountsUploadConnection


@dataclass(kw_only=True)
class EnterpriseServerInstallation:
    created_at: DateTime
    customer_name: str
    host_name: str
    id: ID
    is_connected: bool
    updated_at: DateTime
    user_accounts: EnterpriseServerUserAccountConnection
    user_accounts_uploads: EnterpriseServerUserAccountsUploadConnection
