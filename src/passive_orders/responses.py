from dataclasses import dataclass, field
from typing import Any, List, Optional

from .enums import PassiveOrderStatusEnum


@dataclass
class PassiveOrdersValidationResponse:
    isSuccess: Optional[bool] = None
    errorMessages: Optional[List[str]] = None
    messages: Optional[List[str]] = None
    errorCodeMessages: Optional[List[str]] = None
    statusCode: Optional[PassiveOrderStatusEnum] = None
    message: Optional[str] = None

    @staticmethod
    def from_dict(data: dict):
        return PassiveOrdersValidationResponse(
            isSuccess=data.get("isSuccess"),
            errorMessages=data.get("errorMessages"),
            messages=data.get("messages"),
            errorCodeMessages=data.get("errorCodeMessages"),
            statusCode=(
                PassiveOrderStatusEnum(data.get("statusCode"))
                if data.get("statusCode") is not None
                else None
            ),
            message=data.get("message"),
        )


@dataclass
class PassiveOrdersFileUploadResponse:
    id: Optional[str] = None
    errorMessages: Optional[List[str]] = None
    messages: Optional[List[str]] = None
    errorCodeMessages: Optional[List[str]] = None
    isSuccess: Optional[bool] = None
    statusCode: Optional[int] = None
    message: Optional[str] = None

    def from_dict(data: dict):
        return PassiveOrdersFileUploadResponse(
            id=data.get("id"),
            errorMessages=data.get("errorMessages"),
            messages=data.get("messages"),
            errorCodeMessages=data.get("errorCodeMessages"),
            isSuccess=data.get("isSuccess"),
            statusCode=data.get("statusCode"),
            message=data.get("message"),
        )
