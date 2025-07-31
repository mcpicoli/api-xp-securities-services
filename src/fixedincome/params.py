from dataclasses import dataclass, field
from typing import Optional

from src.fixedincome.enums import AssetType, MarketType, OperationType, PaymentType


@dataclass
class FixedIncomeOrderParams:
    managerLegalId: str
    fundLegalId: str
    requesterName: str
    origin: str
    orderDate: str
    settlementDate: str
    fundISINCode: Optional[str] = None
    operationType: Optional[OperationType] = None
    assetType: Optional[AssetType] = None
    marketType: Optional[MarketType] = None
    assetCode: str = ""
    quantity: float = 0.0
    assetUnitPrice: float = 0.0
    tax: Optional[float] = None
    totalValue: float = 0.0
    paymentType: Optional[PaymentType] = None
    bankTransfer: Optional[bool] = None
    bank: Optional[str] = None
    agency: Optional[str] = None
    account: Optional[str] = None
    counterPartName: Optional[str] = None
    counterPartLegalId: Optional[str] = None
    cetipAccountCounterparty: Optional[str] = None
    fundCetipAccount: Optional[str] = None
    externalId: Optional[str] = None
    dueDate: Optional[str] = None

    def to_dict(self):
        d = {}
        for k, v in self.__dict__.items():
            if v is not None:
                if hasattr(v, "value"):
                    d[k] = v.value
                else:
                    d[k] = v
        return d
