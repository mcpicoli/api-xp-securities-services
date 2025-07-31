from enum import Enum


class OperationType(Enum):
    COMPRA = "Compra"
    VENDA = "Venda"
    # Adicione outros tipos conforme documentação


class AssetType(Enum):
    SELIC = "SELIC"
    CETIP = "CETIP"
    # Adicione outros tipos conforme documentação


class MarketType(Enum):
    PRIMARIO = "Primario"
    SECUNDARIO = "Secundario"
    # Adicione outros tipos conforme documentação


class PaymentType(Enum):
    A_VISTA = "A Vista"
    A_PRAZO = "A Prazo"
    # Adicione outros tipos conforme documentação


# Exemplos de uso:
# op = OperationType.COMPRA
# print(op.value)
