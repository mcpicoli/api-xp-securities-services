from dataclasses import dataclass, field
from typing import Optional


@dataclass
class WalletsActiveParams:
    conciliationReferenceDate: Optional[str] = None  # yyyy-MM-dd

    # Se nenhum parâmetro for informado, a data atual será usada
    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}


@dataclass
class PassiveOrdersValidationParams:
    managerLegalId: str
    formFile: bytes  # arquivo CSV

    def to_dict(self):
        return {"managerLegalId": self.managerLegalId}


@dataclass
class PassiveOrdersFileParams:
    managerLegalId: str
    formFile: bytes  # arquivo CSV

    def to_dict(self):
        return {"managerLegalId": self.managerLegalId}


@dataclass
class PassiveOrdersExportParams:
    startAt: str  # yyyy-MM-dd
    endAt: str  # yyyy-MM-dd
    dateTypeId: int
    orderTypeId: Optional[int] = None
    viewTypeId: Optional[int] = None
    managerLegalId: Optional[str] = None
    distributorLegalId: Optional[str] = None
    fundLegalId: Optional[str] = None
    shareHolderLegalId: Optional[str] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None
    statusId: Optional[int] = None

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}


@dataclass
class CustodyMovementSearchParams:
    correlationIds: list

    def to_dict(self):
        return {"correlationIds": self.correlationIds}


@dataclass
class CustodyMovementCreateParams:
    codigoCorrelacao: str
    cnpjFundo: Optional[str] = None
    codigoDistribuidor: str = ""
    dataMovimento: str = ""
    codigoCotista: str = ""
    tipoMovimento: str = ""
    formaLiquidacao: Optional[str] = None
    valorMovimento: Optional[float] = None
    quantidadeCotas: Optional[float] = None
    produtoOrigem: str = ""

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}


@dataclass
class FixedIncomeOrderParams:
    managerLegalId: str
    fundLegalId: str
    requesterName: str
    origin: str
    orderDate: str
    settlementDate: str
    fundISINCode: Optional[str] = None
    operationType: str = ""
    assetType: str = ""
    marketType: Optional[str] = None
    assetCode: str = ""
    quantity: float = 0.0
    assetUnitPrice: float = 0.0
    tax: Optional[float] = None
    totalValue: float = 0.0
    paymentType: str = ""
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
        return {k: v for k, v in self.__dict__.items() if v is not None}


@dataclass
class FundQuotaOrderParams:
    origin: str
    orderDate: str
    managerLegalId: str
    fundLegalId: str
    fundISINCode: Optional[str] = None
    operationType: str = ""
    assetLegalId: str = ""
    assetISINCode: Optional[str] = None
    settlementDate: str = ""
    quotationDate: str = ""
    quantity: float = 0.0
    value: float = 0.0
    settlementType: str = ""
    strategy: str = ""
    marketType: Optional[str] = None
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
        return {k: v for k, v in self.__dict__.items() if v is not None}
