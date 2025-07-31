from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class WalletsActiveParams:
    conciliationReferenceDate: Optional[datetime] = None  # yyyy-MM-dd

    def to_dict(self):
        d = {}
        for k, v in self.__dict__.items():
            if v is not None:
                if isinstance(v, datetime):
                    d[k] = v.strftime("%Y-%m-%d")
                else:
                    d[k] = v
        return d
