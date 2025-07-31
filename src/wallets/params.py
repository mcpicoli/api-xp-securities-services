from dataclasses import dataclass, field
from typing import Optional


@dataclass
class WalletsActiveParams:
    conciliationReferenceDate: Optional[str] = None  # yyyy-MM-dd

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}
