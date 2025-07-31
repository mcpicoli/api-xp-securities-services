from dataclasses import dataclass, field
from typing import Any, List, Optional

from src.common.responses import ApiErrorResponse

from .enums import FileFormatEnum, FilePortfolioEnum, FileTypeEnum


@dataclass
class FileType:
    id: int
    typeName: str


@dataclass
class FileFormat:
    id: int
    format: str


@dataclass
class FilePortfolio:
    id: int
    portfolioName: str


@dataclass
class FileListItem:
    id: int
    legalId: str
    fileName: str
    ownerName: str
    type: FileTypeEnum
    format: FileFormatEnum
    portfolio: FilePortfolioEnum
    positionDate: str
    availabilityDate: str
    hasRoutine: bool


@dataclass
class FileListResponse(ApiErrorResponse):
    """
    Resposta da listagem de arquivos, incluindo tratamento de erro padronizado.
    """

    pagination: Optional[dict] = None
    count: Optional[int] = None
    files: List[FileListItem] = field(default_factory=list)

    @staticmethod
    def from_dict(data: dict):
        files = [
            FileListItem(
                id=item["id"],
                legalId=item["legalId"],
                fileName=item["fileName"],
                ownerName=item["ownerName"],
                type=FileTypeEnum(item["type"]),
                format=FileFormatEnum(item["format"]),
                portfolio=FilePortfolioEnum(item["portfolio"]),
                positionDate=item["positionDate"],
                availabilityDate=item["availabilityDate"],
                hasRoutine=item["hasRoutine"],
            )
            for item in data.get("files", [])
        ]
        return FileListResponse(
            pagination=data.get("pagination"),
            count=data.get("count"),
            files=files,
            errorMessages=data.get("errorMessages"),
            messages=data.get("messages"),
            errorCodeMessages=data.get("errorCodeMessages"),
            isSuccess=data.get("isSuccess"),
            statusCode=data.get("statusCode"),
            message=data.get("message"),
        )
