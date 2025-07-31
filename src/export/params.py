from dataclasses import dataclass, field
from typing import Optional

from src.export.enums import (
    ExportOrderCotizado,
    ExportOrderStatus,
    ExportOrderType,
    ExportOrderViewType,
)


@dataclass
class PassiveOrdersExportParams:
    startAt: str
    endAt: str
    dateTypeId: ExportOrderType
    orderTypeId: Optional[ExportOrderCotizado] = None
    viewTypeId: Optional[ExportOrderViewType] = None
    managerLegalId: Optional[str] = None
    distributorLegalId: Optional[str] = None
    fundLegalId: Optional[str] = None
    shareHolderLegalId: Optional[str] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None
    statusId: Optional[ExportOrderStatus] = None

    def to_dict(self):
        d = {}
        for k, v in self.__dict__.items():
            if v is not None:
                if hasattr(v, "value"):
                    d[k] = v.value
                else:
                    d[k] = v
        return d
