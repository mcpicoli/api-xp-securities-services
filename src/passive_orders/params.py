from dataclasses import dataclass, field
from typing import Optional

from src.passive_orders.enums import PassiveOrderUploadStatus


@dataclass
class PassiveOrdersValidationParams:
    managerLegalId: str
    formFile: bytes  # arquivo CSV

    def to_dict(self):
        return {"managerLegalId": self.managerLegalId}


@dataclass
class PassiveOrdersFileParams:
    managerLegalId: str
    formFile: bytes  # arquivo CSV
    status: Optional[PassiveOrderUploadStatus] = None

    def to_dict(self):
        d = {"managerLegalId": self.managerLegalId}
        if self.status is not None:
            d["status"] = self.status.value
        return d
