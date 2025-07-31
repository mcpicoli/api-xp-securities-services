from enum import Enum


class FileTypeEnum(Enum):
    CARTEIRA_DIARIA = 1
    DEMONSTRATIVO_CAIXA = 2
    XML_ANBIMA_401 = 5
    # Adicione outros tipos conforme documentação


class FileFormatEnum(Enum):
    CSV = 1
    PDF = 2
    XLSX = 4
    XML = 5
    # Adicione outros formatos conforme documentação


class FilePortfolioEnum(Enum):
    FUNDO = 1
    CARTEIRA = 2
    # Adicione outros portfolios conforme documentação


# Exemplos de uso:
# tipo = FileTypeEnum.CARTEIRA_DIARIA
# print(tipo.name, tipo.value)
