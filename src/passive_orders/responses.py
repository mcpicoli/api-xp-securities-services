from dataclasses import dataclass, field
from typing import Any, List, Optional

from src.common.responses import ApiErrorResponse

from .enums import PassiveOrderStatusEnum


@dataclass
class PassiveOrdersValidationResponse(ApiErrorResponse):
    """
    Resposta da validação de arquivo de ordens passivas, incluindo tratamento de erro padronizado.
    """

    statusCode: Optional[PassiveOrderStatusEnum] = None

    @staticmethod
    def from_dict(data: dict):
        return PassiveOrdersValidationResponse(
            statusCode=(
                PassiveOrderStatusEnum(data.get("statusCode"))
                if data.get("statusCode") is not None
                else None
            ),
            errorMessages=data.get("errorMessages"),
            messages=data.get("messages"),
            errorCodeMessages=data.get("errorCodeMessages"),
            isSuccess=data.get("isSuccess"),
            message=data.get("message"),
        )


@dataclass
class PassiveOrdersFileUploadResponse(ApiErrorResponse):
    """
    Resposta do upload de arquivo de ordens passivas, incluindo tratamento de erro padronizado.
    """

    id: Optional[str] = None

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
