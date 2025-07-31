from dataclasses import dataclass, field
from typing import Optional

from src.fundquota.enums import (
    FundQuotaOperationType,
    MarketType,
    SettlementType,
    StrategyType,
)


@dataclass
class FundQuotaOrderParams:
    origin: str
    orderDate: str
    managerLegalId: str
    fundLegalId: str
    fundISINCode: Optional[str] = None
    operationType: Optional[FundQuotaOperationType] = None
    assetLegalId: str = ""
    assetISINCode: Optional[str] = None
    settlementDate: str = ""
    quotationDate: str = ""
    quantity: float = 0.0
    value: float = 0.0
    settlementType: Optional[SettlementType] = None
    strategy: Optional[StrategyType] = None
    marketType: Optional[MarketType] = None
    cetipAccountCounterparty: Optional[str] = None
    fundCetipAccount: Optional[str] = None
    assetCode: Optional[str] = None
    assetUnitPrice: Optional[float] = None
    counterpartyLegalId: Optional[str] = None
    counterpartyName: Optional[str] = None
    earlyRedemptionCondition: Optional[bool] = None
    cetipResponsible: Optional[str] = None
    phoneNumber: Optional[str] = None
    externalId: Optional[str] = None
    chamadaCapital: Optional[bool] = None
    assetSerie: Optional[str] = None
    requesterName: Optional[str] = None
    bank: Optional[str] = None
    agency: Optional[str] = None
    account: Optional[str] = None

    def to_dict(self):
        d = {}
        for k, v in self.__dict__.items():
            if v is not None:
                if hasattr(v, "value"):
                    d[k] = v.value
                else:
                    d[k] = v
        return d
