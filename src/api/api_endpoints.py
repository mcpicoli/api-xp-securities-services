class ApiEndpoints:
    """
    Centraliza os endpoints das APIs XP Securities Services.
    """

    # Bases
    OAUTH_API_BASE = "https://identity.xpi.com.br"
    AD_API_BASE = "https://login.microsoftonline.com"
    RESOURCE_API_BASE = "https://api-parceiros.xpi.com.br/securitiesservices"
    FIXEDINCOME_API_BASE = "https://api-parceiros.xpi.com.br/partners/fixedincome"
    FUNDQUOTA_API_BASE = "https://api-parceiros.xpi.com.br/partners/fundquota"

    # Endpoints
    AUTH_TOKEN = f"{OAUTH_API_BASE}/connect/token"
    AD_TOKEN = f"{AD_API_BASE}/cf56e405-d2b0-4266-b210-aa04636b6161/oauth2/v2.0/token"
    FILE_TYPES = f"{RESOURCE_API_BASE}/v1/files/types"
    FILE_FORMATS = f"{RESOURCE_API_BASE}/v1/files/formats"
    FILE_PORTFOLIOS = f"{RESOURCE_API_BASE}/v1/files/portfolios"
    FILE_LIST = f"{RESOURCE_API_BASE}/v1/files"
    FILE_DOWNLOAD = f"{RESOURCE_API_BASE}/v1/files/download"
    WALLETS_ACTIVE = f"{RESOURCE_API_BASE}/v1/wallets/active"
    PCO_SEARCH = f"{RESOURCE_API_BASE}/v1/liabilities-management/movementpco/search-by-correlationid"
    PCO_CREATE = f"{RESOURCE_API_BASE}/v1/liabilities-management/movementpco"
    PASSIVE_ORDERS_VALIDATION = f"{RESOURCE_API_BASE}/v1/passive/orders/validation"
    PASSIVE_ORDERS_FILE = f"{RESOURCE_API_BASE}/v1/passive/orders/file"
    PASSIVE_ORDERS_FILE_DOWNLOAD = (
        f"{RESOURCE_API_BASE}/v1/passive/orders/{{id}}/download"
    )
    PASSIVE_ORDERS_EXPORT = f"{RESOURCE_API_BASE}/v1/passive/orders/export"
    PASSIVE_ORDERS_EXPORT_ID = f"{RESOURCE_API_BASE}/v1/passive/orders/export/{{id}}"
    PASSIVE_ORDERS_EXPORT_DOWNLOAD = (
        f"{RESOURCE_API_BASE}/v1/passive/orders/{{id}}/download"
    )
    PASSIVE_ORDERS_EXPORT_FUNDS = f"{RESOURCE_API_BASE}/v1/passive/orders/export/funds"
    PASSIVE_ORDERS_EXPORT_SHAREHOLDERS = (
        f"{RESOURCE_API_BASE}/v1/passive/orders/export/shareholders"
    )
    FIXEDINCOME_CREATE = f"{FIXEDINCOME_API_BASE}"
    FIXEDINCOME_LIST = f"{FIXEDINCOME_API_BASE}"
    FUNDQUOTA_CREATE = f"{FUNDQUOTA_API_BASE}"
    FUNDQUOTA_LIST = f"{FUNDQUOTA_API_BASE}"

    # Endpoints menos comuns
    # Fundos disponíveis para exportação
    EXPORT_FUNDS = f"{RESOURCE_API_BASE}/v1/passive/orders/export/funds"
    # Cotistas disponíveis para exportação
    EXPORT_SHAREHOLDERS = f"{RESOURCE_API_BASE}/v1/passive/orders/export/shareholders"
    # Consulta de boletas de renda fixa por filtros
    FIXEDINCOME_LIST_FILTER = f"{FIXEDINCOME_API_BASE}"
    # Consulta de boletas de cota de fundo por filtros
    FUNDQUOTA_LIST_FILTER = f"{FUNDQUOTA_API_BASE}"
    # Endpoint de autenticação AD (já presente)
    # Outros endpoints podem ser adicionados conforme surgirem na documentação
