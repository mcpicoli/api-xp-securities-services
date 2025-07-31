from enum import Enum


class FundQuotaOperationType(Enum):
    APLICACAO = "aplicacao"
    RESGATE_PARCIAL_VALOR = "resgate parcial valor"
    RESGATE_PARCIAL_COTA = "resgate parcial cota"
    RESGATE_TOTAL = "resgate total"
    # Adicione outros tipos conforme documentação


class SettlementType(Enum):
    CETIP = "cetip"
    TED = "ted"
    CONTA_ESPELHO = "conta espelho"
    # Adicione outros tipos conforme documentação


class StrategyType(Enum):
    PADRAO = "padrao"
    # Adicione outros tipos conforme documentação


class MarketType(Enum):
    PRIMARIO = "Primário"
    SECUNDARIO = "Secundário"
    # Adicione outros tipos conforme documentação


# Exemplos de uso:
# op = FundQuotaOperationType.APLICACAO
# print(op.value)
