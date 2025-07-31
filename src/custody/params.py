from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CustodyMovementSearchParams:
    correlationIds: list

    def to_dict(self):
        return {"correlationIds": self.correlationIds}


@dataclass
class CustodyMovementCreateParams:
    codigoCorrelacao: str
    cnpjFundo: Optional[str] = None
    codigoDistribuidor: str = ""
    dataMovimento: str = ""
    codigoCotista: str = ""
    tipoMovimento: str = ""
    formaLiquidacao: Optional[str] = None
    valorMovimento: Optional[float] = None
    quantidadeCotas: Optional[float] = None
    produtoOrigem: str = ""

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}
