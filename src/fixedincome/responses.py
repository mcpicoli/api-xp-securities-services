from dataclasses import dataclass, field
from typing import Any, List, Optional

from .enums import (
    AssetTypeEnum,
    FixedIncomeStatusEnum,
    MarketTypeEnum,
    OperationTypeEnum,
    PaymentTypeEnum,
)


@dataclass
class FixedIncomeOrderResponse:
    success: Optional[bool] = None
    message: Optional[str] = None
    correlationId: Optional[str] = None
    orderId: Optional[int] = None
    errorMessages: Optional[List[str]] = None

    def from_dict(data: dict):
        return FixedIncomeOrderResponse(
            success=data.get("success"),
            message=data.get("message"),
            correlationId=data.get("correlationId"),
            orderId=data.get("orderId"),
            errorMessages=data.get("errorMessages"),
        )


@dataclass
class FixedIncomeOrderListItem:
    managerLegalId: Optional[str] = None
    fundLegalId: Optional[str] = None
    requesterName: Optional[str] = None
    orderDate: Optional[str] = None
    settlementDate: Optional[str] = None
    fundISINCode: Optional[str] = None
    operationType: Optional[OperationTypeEnum] = None
    assetType: Optional[AssetTypeEnum] = None
    marketType: Optional[MarketTypeEnum] = None
    assetCode: Optional[str] = None
    quantity: Optional[float] = None
    assetUnitPrice: Optional[float] = None
    tax: Optional[float] = None
    totalValue: Optional[float] = None
    paymentType: Optional[PaymentTypeEnum] = None
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
    status: Optional[FixedIncomeStatusEnum] = None
    statusMessage: Optional[str] = None

    @staticmethod
    def from_dict(data: dict):
        return FixedIncomeOrderListItem(
            managerLegalId=data.get("managerLegalId"),
            fundLegalId=data.get("fundLegalId"),
            requesterName=data.get("requesterName"),
            orderDate=data.get("orderDate"),
            settlementDate=data.get("settlementDate"),
            fundISINCode=data.get("fundISINCode"),
            operationType=(
                OperationTypeEnum(data["operationType"])
                if data.get("operationType") is not None
                else None
            ),
            assetType=(
                AssetTypeEnum(data["assetType"])
                if data.get("assetType") is not None
                else None
            ),
            marketType=(
                MarketTypeEnum(data["marketType"])
                if data.get("marketType") is not None
                else None
            ),
            assetCode=data.get("assetCode"),
            quantity=data.get("quantity"),
            assetUnitPrice=data.get("assetUnitPrice"),
            tax=data.get("tax"),
            totalValue=data.get("totalValue"),
            paymentType=(
                PaymentTypeEnum(data["paymentType"])
                if data.get("paymentType") is not None
                else None
            ),
            bankTransfer=data.get("bankTransfer"),
            bank=data.get("bank"),
            agency=data.get("agency"),
            account=data.get("account"),
            counterPartName=data.get("counterPartName"),
            counterPartLegalId=data.get("counterPartLegalId"),
            cetipAccountCounterparty=data.get("cetipAccountCounterparty"),
            fundCetipAccount=data.get("fundCetipAccount"),
            externalId=data.get("externalId"),
            dueDate=data.get("dueDate"),
            status=(
                FixedIncomeStatusEnum(data["status"])
                if data.get("status") is not None
                else None
            ),
            statusMessage=data.get("statusMessage"),
        )


@dataclass
class FixedIncomeOrderListResponse:
    orders: List[FixedIncomeOrderListItem] = field(default_factory=list)
    totalItems: Optional[int] = None
    page: Optional[int] = None
    pageSize: Optional[int] = None
    errorMessages: Optional[List[str]] = None
    messages: Optional[List[str]] = None
    errorCodeMessages: Optional[Any] = None
    isSuccess: Optional[bool] = None

    def from_dict(data: dict):
        orders = [
            FixedIncomeOrderListItem.from_dict(item) for item in data.get("orders", [])
        ]
        return FixedIncomeOrderListResponse(
            orders=orders,
            totalItems=data.get("totalItems"),
            page=data.get("page"),
            pageSize=data.get("pageSize"),
            errorMessages=data.get("errorMessages"),
            messages=data.get("messages"),
            errorCodeMessages=data.get("errorCodeMessages"),
            isSuccess=data.get("isSuccess"),
        )
