"""
Modelos genéricos para tratamento de erros nas respostas das APIs XP Securities Services.
Utilize ApiErrorResponse em endpoints que retornam erros padronizados.
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ApiErrorResponse:
    """
    Modelo genérico para resposta de erro das APIs XP Securities Services.
    Campos presentes na maioria dos endpoints em caso de erro.
    """

    errorMessages: Optional[List[str]] = None
    messages: Optional[List[str]] = None
    errorCodeMessages: Optional[List[str]] = None
    isSuccess: Optional[bool] = None
    statusCode: Optional[int] = None
    message: Optional[str] = None

    @staticmethod
    def from_dict(data: dict):
        return ApiErrorResponse(
            errorMessages=data.get("errorMessages"),
            messages=data.get("messages"),
            errorCodeMessages=data.get("errorCodeMessages"),
            isSuccess=data.get("isSuccess"),
            statusCode=data.get("statusCode"),
            message=data.get("message"),
        )


# Exemplo de uso:
# resp = ApiErrorResponse.from_dict(response_json)
# if not resp.isSuccess:
#     print(resp.errorMessages or resp.message)
