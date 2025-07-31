from dataclasses import dataclass, field
from typing import Any, List, Optional

from src.common.responses import ApiErrorResponse


@dataclass
class ExportFundsResponseItem:
    value: Optional[str] = None
    label: Optional[str] = None


@dataclass
class ExportFundsResponse(ApiErrorResponse):
    items: List[ExportFundsResponseItem] = field(default_factory=list)
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    count: Optional[int] = None

    def from_dict(data: dict):
        items = [ExportFundsResponseItem(**item) for item in data.get("items", [])]
        return ExportFundsResponse(
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


@dataclass
class ExportShareholdersResponseItem:
    value: Optional[str] = None
    label: Optional[str] = None


@dataclass
class ExportShareholdersResponse(ApiErrorResponse):
    items: List[ExportShareholdersResponseItem] = field(default_factory=list)
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    count: Optional[int] = None

    def from_dict(data: dict):
        items = [
            ExportShareholdersResponseItem(**item) for item in data.get("items", [])
        ]
        return ExportShareholdersResponse(
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
