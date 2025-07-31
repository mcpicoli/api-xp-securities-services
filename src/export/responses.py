from dataclasses import dataclass, field
from typing import Any, List, Optional

from .enums import (
    ExportDateTypeEnum,
    ExportOrderTypeEnum,
    ExportStatusEnum,
    ExportViewTypeEnum,
)


@dataclass
class ExportOrderResponse:
    id: Optional[int] = None
    errorMessages: Optional[List[str]] = None
    messages: Optional[List[str]] = None
    errorCodeMessages: Optional[List[str]] = None
    isSuccess: Optional[bool] = None
    statusCode: Optional[int] = None
    message: Optional[str] = None

    def from_dict(data: dict):
        return ExportOrderResponse(
            id=data.get("id"),
            errorMessages=data.get("errorMessages"),
            messages=data.get("messages"),
            errorCodeMessages=data.get("errorCodeMessages"),
            isSuccess=data.get("isSuccess"),
            statusCode=data.get("statusCode"),
            message=data.get("message"),
        )


@dataclass
class ExportOrderListItem:
    orderExportId: Optional[int] = None
    startAt: Optional[str] = None
    endAt: Optional[str] = None
    dateTypeId: Optional[ExportDateTypeEnum] = None
    dateTypeDesc: Optional[str] = None
    orderTypeId: Optional[ExportOrderTypeEnum] = None
    orderTypeDesc: Optional[str] = None
    viewTypeId: Optional[ExportViewTypeEnum] = None
    viewTypeDesc: Optional[str] = None
    distributorLegalId: Optional[str] = None
    managerLegalId: Optional[str] = None
    fundLegalId: Optional[str] = None
    shareHolderLegalId: Optional[str] = None
    fundId: Optional[int] = None
    fundDesc: Optional[str] = None
    statusId: Optional[ExportStatusEnum] = None
    statusDesc: Optional[str] = None
    ordersCount: Optional[int] = None
    downloadUrl: Optional[str] = None
    officeCode: Optional[int] = None
    user: Optional[str] = None
    createAt: Optional[str] = None
    updateAt: Optional[str] = None


@dataclass
class ExportOrderListResponse:
    items: List[ExportOrderListItem] = field(default_factory=list)
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    count: Optional[int] = None
    errorMessages: Optional[List[str]] = None
    messages: Optional[List[str]] = None
    errorCodeMessages: Optional[List[str]] = None
    isSuccess: Optional[bool] = None
    statusCode: Optional[int] = None
    message: Optional[str] = None

    @staticmethod
    def from_dict(data: dict):
        items = [
            ExportOrderListItem(
                orderExportId=item.get("orderExportId"),
                startAt=item.get("startAt"),
                endAt=item.get("endAt"),
                dateTypeId=(
                    ExportDateTypeEnum(item["dateTypeId"])
                    if item.get("dateTypeId") is not None
                    else None
                ),
                dateTypeDesc=item.get("dateTypeDesc"),
                orderTypeId=(
                    ExportOrderTypeEnum(item["orderTypeId"])
                    if item.get("orderTypeId") is not None
                    else None
                ),
                orderTypeDesc=item.get("orderTypeDesc"),
                viewTypeId=(
                    ExportViewTypeEnum(item["viewTypeId"])
                    if item.get("viewTypeId") is not None
                    else None
                ),
                viewTypeDesc=item.get("viewTypeDesc"),
                distributorLegalId=item.get("distributorLegalId"),
                managerLegalId=item.get("managerLegalId"),
                fundLegalId=item.get("fundLegalId"),
                shareHolderLegalId=item.get("shareHolderLegalId"),
                fundId=item.get("fundId"),
                fundDesc=item.get("fundDesc"),
                statusId=(
                    ExportStatusEnum(item["statusId"])
                    if item.get("statusId") is not None
                    else None
                ),
                statusDesc=item.get("statusDesc"),
                ordersCount=item.get("ordersCount"),
                downloadUrl=item.get("downloadUrl"),
                officeCode=item.get("officeCode"),
                user=item.get("user"),
                createAt=item.get("createAt"),
                updateAt=item.get("updateAt"),
            )
            for item in data.get("items", [])
        ]
        return ExportOrderListResponse(
            items=items,
            pageSize=data.get("pageSize"),
            pageNumber=data.get("pageNumber"),
            count=data.get("count"),
            errorMessages=data.get("errorMessages"),
            messages=data.get("messages"),
            errorCodeMessages=data.get("errorCodeMessages"),
            isSuccess=data.get("isSuccess"),
            statusCode=data.get("statusCode"),
            message=data.get("message"),
        )
