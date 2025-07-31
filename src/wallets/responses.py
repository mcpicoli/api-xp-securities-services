from dataclasses import dataclass, field
from typing import Any, List, Optional

from src.common.responses import ApiErrorResponse


@dataclass
class WalletActiveItem:
    customerId: int
    walletProcessingDate: str
    conciliationReferenceDate: str
    walletConciliationDate: str
    status: str


@dataclass
class WalletsActiveResponse(ApiErrorResponse):
    """
    Resposta da listagem de carteiras, incluindo tratamento de erro padronizado.
    """

    totalWallets: Optional[int] = None
    wallets: List[WalletActiveItem] = field(default_factory=list)

    def from_dict(data: dict):
        wallets = [WalletActiveItem(**item) for item in data.get("wallets", [])]
        return WalletsActiveResponse(
            totalWallets=data.get("totalWallets"),
            wallets=wallets,
            errorMessages=data.get("errorMessages"),
            messages=data.get("messages"),
            errorCodeMessages=data.get("errorCodeMessages"),
            isSuccess=data.get("isSuccess"),
            statusCode=data.get("statusCode"),
            message=data.get("message"),
        )
