from dataclasses import dataclass, field
from typing import Any, List, Optional


@dataclass
class CustodyMovementResponse:
    statusCode: Optional[int] = None
    message: Optional[str] = None
    movimento: Optional[dict] = None
    errorMessages: Optional[List[str]] = None
    messages: Optional[List[str]] = None
    errorCodeMessages: Optional[List[str]] = None
    isSuccess: Optional[bool] = None

    def from_dict(data: dict):
        return CustodyMovementResponse(
            statusCode=data.get("statusCode"),
            message=data.get("message"),
            movimento=data.get("movimento"),
            errorMessages=data.get("errorMessages"),
            messages=data.get("messages"),
            errorCodeMessages=data.get("errorCodeMessages"),
            isSuccess=data.get("isSuccess"),
        )
