from enum import Enum


class ExportOrderStatus(Enum):
    RECEIVED = 0  # Recebemos sua solicitação, em breve iremos processa-lo
    PROCESSING = 1  # A exportação está em processamento
    COMPLETED = 2  # A exportação concluída e disponível para ser baixada
    ERROR = 3  # Erro no processamento da exportação

    def description(self):
        return {
            ExportOrderStatus.RECEIVED: "Recebemos sua solicitação, em breve iremos processa-lo.",
            ExportOrderStatus.PROCESSING: "A exportação está em processamento.",
            ExportOrderStatus.COMPLETED: "A exportação concluída e disponível para ser baixada.",
            ExportOrderStatus.ERROR: "Erro no processamento da exportação.",
        }[self]


class ExportOrderType(Enum):
    MOVIMENTACAO = 0
    LIQUIDACAO = 1
    COTIZACAO = 2


class ExportOrderCotizado(Enum):
    TODOS = 0
    COTIZADO = 1
    NAO_COTIZADO = 2


class ExportOrderViewType(Enum):
    ANALITICA = 0
    SINTETICA = 1


# Exemplos de uso:
# status = ExportOrderStatus.COMPLETED
# print(status.description())
