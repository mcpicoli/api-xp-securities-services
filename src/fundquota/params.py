from dataclasses import dataclass, field
from datetime import datetime
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
    orderDate: datetime
    managerLegalId: str
    fundLegalId: str
    fundISINCode: Optional[str] = None
    operationType: Optional[FundQuotaOperationType] = None
    assetLegalId: str = ""
    assetISINCode: Optional[str] = None
    settlementDate: Optional[datetime] = None
    quotationDate: Optional[datetime] = None
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
                elif isinstance(v, datetime):
                    if k in ["orderDate"]:
                        d[k] = v.strftime("%Y-%m-%d")
                    elif k in ["settlementDate", "quotationDate"]:
                        d[k] = v.strftime("%Y-%m-%dT%H:%M:%S")
                    else:
                        d[k] = v.isoformat()
                else:
                    d[k] = v
        return d
