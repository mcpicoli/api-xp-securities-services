from dataclasses import dataclass, field
from typing import Any, List, Optional


@dataclass
class ExportFundsResponseItem:
    value: Optional[str] = None
    label: Optional[str] = None


@dataclass
class ExportFundsResponse:
    items: List[ExportFundsResponseItem] = field(default_factory=list)
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    count: Optional[int] = None
    errorMessages: Optional[List[str]] = None
    messages: Optional[List[str]] = None
    errorCodeMessages: Optional[List[str]] = None
    isSuccess: Optional[bool] = None
    statusCode: Optional[int] = None
    message: Optional[str] = None

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
class ExportShareholdersResponse:
    items: List[ExportShareholdersResponseItem] = field(default_factory=list)
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    count: Optional[int] = None
    errorMessages: Optional[List[str]] = None
    messages: Optional[List[str]] = None
    errorCodeMessages: Optional[List[str]] = None
    isSuccess: Optional[bool] = None
    statusCode: Optional[int] = None
    message: Optional[str] = None

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
