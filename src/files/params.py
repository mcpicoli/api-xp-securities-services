from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from src.files.enums import FileFormatEnum, FilePortfolioEnum, FileTypeEnum


@dataclass
class FileListParams:
    positionDate: str  # yyyy-MM-dd (required)
    page: int  # required
    pageSize: int  # required
    identification: Optional[str] = None
    fileType: Optional[FileTypeEnum] = None
    fileFormat: Optional[FileFormatEnum] = None
    filePortfolio: Optional[FilePortfolioEnum] = None
    AvailabilityStartDate: Optional[datetime] = None
    AvailabilityEndDate: Optional[datetime] = None

    def to_dict(self):
        d = {}
        for k, v in self.__dict__.items():
            if v is not None:
                if hasattr(v, "value"):
                    d[k] = v.value
                elif isinstance(v, datetime):
                    if k == "positionDate":
                        d[k] = v.strftime("%Y-%m-%d")
                    else:
                        d[k] = v.strftime("%Y-%m-%dT%H:%M:%S")
                else:
                    d[k] = v
        return d
