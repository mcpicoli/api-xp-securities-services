from enum import Enum


class PassiveOrderUploadStatus(Enum):
    RECEIVED = 1  # Recebemos seu upload, em breve iremos processa-lo
    PROCESSING = 2  # O lote de ordens está em processamento
    ERROR = 3  # Houve algum erro, o lote não foi processado
    RECEIVED_VALID = 4  # As ordens válidas foram recebidas e gravadas na nossa base, esperando a serem integradas com o custodiante
    INTEGRATED = 5  # As ordens válidas foram integradas com o custodiante

    def description(self):
        return {
            PassiveOrderUploadStatus.RECEIVED: "Recebemos seu upload, em breve iremos processa-lo.",
            PassiveOrderUploadStatus.PROCESSING: "O lote de ordens está em processamento.",
            PassiveOrderUploadStatus.ERROR: "Houve algum erro, o lote não foi processado.",
            PassiveOrderUploadStatus.RECEIVED_VALID: "As ordens válidas foram recebidas e gravadas na nossa base, esperando a serem integradas com o custodiante.",
            PassiveOrderUploadStatus.INTEGRATED: "As ordens válidas foram integradas com o custodiante.",
        }[self]


# Exemplos de uso:
# status = PassiveOrderUploadStatus.RECEIVED
# print(status.description())
