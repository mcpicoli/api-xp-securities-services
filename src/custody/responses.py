from dataclasses import dataclass, field
from typing import Any, List, Optional

from src.common.responses import ApiErrorResponse


@dataclass
class CustodyMovementResponse(ApiErrorResponse):
    movimento: Optional[dict] = None

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
