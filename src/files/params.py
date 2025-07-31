from dataclasses import dataclass, field
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
    AvailabilityStartDate: Optional[str] = None
    AvailabilityEndDate: Optional[str] = None

    def to_dict(self):
        d = {}
        for k, v in self.__dict__.items():
            if v is not None:
                if hasattr(v, "value"):
                    d[k] = v.value
                else:
                    d[k] = v
        return d
