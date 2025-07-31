from dataclasses import dataclass, field
from typing import Any, List, Optional


@dataclass
class WalletActiveItem:
    customerId: int
    walletProcessingDate: str
    conciliationReferenceDate: str
    walletConciliationDate: str
    status: str


@dataclass
class WalletsActiveResponse:
    totalWallets: Optional[int] = None
    wallets: List[WalletActiveItem] = field(default_factory=list)
    errorMessages: Optional[List[str]] = None
    messages: Optional[List[str]] = None
    errorCodeMessages: Optional[List[str]] = None
    isSuccess: Optional[bool] = None
    statusCode: Optional[int] = None
    message: Optional[str] = None

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
