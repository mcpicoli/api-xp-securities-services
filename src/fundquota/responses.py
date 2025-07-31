from dataclasses import dataclass, field
from typing import Any, List, Optional

from .enums import (
    FundQuotaMarketTypeEnum,
    FundQuotaOperationTypeEnum,
    FundQuotaSettlementTypeEnum,
    FundQuotaStatusEnum,
)


@dataclass
class FundQuotaOrderResponse:
    success: Optional[bool] = None
    message: Optional[str] = None
    correlationId: Optional[str] = None
    orderId: Optional[int] = None
    errorMessages: Optional[List[str]] = None

    def from_dict(data: dict):
        return FundQuotaOrderResponse(
            success=data.get("success"),
            message=data.get("message"),
            correlationId=data.get("correlationId"),
            orderId=data.get("orderId"),
            errorMessages=data.get("errorMessages"),
        )


@dataclass
class FundQuotaOrderListItem:
    fundISIN: Optional[str] = None
    settlementDate: Optional[str] = None
    quotationDate: Optional[str] = None
    operationType: Optional[FundQuotaOperationTypeEnum] = None
    assetLegalId: Optional[str] = None
    assetISINCode: Optional[str] = None
    totalValue: Optional[float] = None
    quantity: Optional[float] = None
    settlementType: Optional[FundQuotaSettlementTypeEnum] = None
    strategy: Optional[str] = None
    marketType: Optional[FundQuotaMarketTypeEnum] = None
    cetipAccountCounterparty: Optional[str] = None
    fundCetipAccount: Optional[str] = None
    assetUnitPrice: Optional[float] = None
    counterPartyName: Optional[str] = None
    counterPartyLegalId: Optional[str] = None
    earlyRedemptionCondition: Optional[bool] = None
    cetipResponsible: Optional[str] = None
    phoneNumber: Optional[str] = None
    chamadaCapital: Optional[bool] = None
    assetSerie: Optional[str] = None
    requesterName: Optional[str] = None
    externalId: Optional[str] = None
    fundLegalId: Optional[str] = None
    custodianLegalId: Optional[int] = None
    assetCode: Optional[str] = None
    bank: Optional[str] = None
    agency: Optional[str] = None
    account: Optional[str] = None
    status: Optional[FundQuotaStatusEnum] = None
    statusMessage: Optional[str] = None
    bankTransfer: Optional[str] = None
    orderDate: Optional[str] = None


@dataclass
class FundQuotaOrderListResponse:
    orders: List[FundQuotaOrderListItem] = field(default_factory=list)
    totalItems: Optional[int] = None
    page: Optional[int] = None
    pageSize: Optional[int] = None
    errorMessages: Optional[List[str]] = None
    messages: Optional[List[str]] = None
    errorCodeMessages: Optional[Any] = None
    isSuccess: Optional[bool] = None

    @staticmethod
    def from_dict(data: dict):
        orders = [
            FundQuotaOrderListItem(
                fundISIN=item.get("fundISIN"),
                settlementDate=item.get("settlementDate"),
                quotationDate=item.get("quotationDate"),
                operationType=(
                    FundQuotaOperationTypeEnum(item["operationType"])
                    if item.get("operationType") is not None
                    else None
                ),
                assetLegalId=item.get("assetLegalId"),
                assetISINCode=item.get("assetISINCode"),
                totalValue=item.get("totalValue"),
                quantity=item.get("quantity"),
                settlementType=(
                    FundQuotaSettlementTypeEnum(item["settlementType"])
                    if item.get("settlementType") is not None
                    else None
                ),
                strategy=item.get("strategy"),
                marketType=(
                    FundQuotaMarketTypeEnum(item["marketType"])
                    if item.get("marketType") is not None
                    else None
                ),
                cetipAccountCounterparty=item.get("cetipAccountCounterparty"),
                fundCetipAccount=item.get("fundCetipAccount"),
                assetUnitPrice=item.get("assetUnitPrice"),
                counterPartyName=item.get("counterPartyName"),
                counterPartyLegalId=item.get("counterPartyLegalId"),
                earlyRedemptionCondition=item.get("earlyRedemptionCondition"),
                cetipResponsible=item.get("cetipResponsible"),
                phoneNumber=item.get("phoneNumber"),
                chamadaCapital=item.get("chamadaCapital"),
                assetSerie=item.get("assetSerie"),
                requesterName=item.get("requesterName"),
                externalId=item.get("externalId"),
                fundLegalId=item.get("fundLegalId"),
                custodianLegalId=item.get("custodianLegalId"),
                assetCode=item.get("assetCode"),
                bank=item.get("bank"),
                agency=item.get("agency"),
                account=item.get("account"),
                status=(
                    FundQuotaStatusEnum(item["status"])
                    if item.get("status") is not None
                    else None
                ),
                statusMessage=item.get("statusMessage"),
                bankTransfer=item.get("bankTransfer"),
                orderDate=item.get("orderDate"),
            )
            for item in data.get("orders", [])
        ]
        return FundQuotaOrderListResponse(
            orders=orders,
            totalItems=data.get("totalItems"),
            page=data.get("page"),
            pageSize=data.get("pageSize"),
            errorMessages=data.get("errorMessages"),
            messages=data.get("messages"),
            errorCodeMessages=data.get("errorCodeMessages"),
            isSuccess=data.get("isSuccess"),
        )
