from typing import Optional

import requests
from fastapi import Depends, FastAPI, Header, HTTPException, Query, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel

from src.api.api_endpoints import ApiEndpoints
from src.auth.auth_providers import ADAuthManager, AuthManager

# Endpoint XP para autenticação
from src.export.params import PassiveOrdersExportParams
from src.files.files_manager import FilesManager
from src.files.params import FileListParams
from src.fixedincome.fixedincome_manager import FixedIncomeManager
from src.fixedincome.params import FixedIncomeOrderParams
from src.fundquota.params import FundQuotaOrderParams
from src.passive_orders.params import (
    PassiveOrdersFileParams,
    PassiveOrdersValidationParams,
)
from src.wallets.params import WalletsActiveParams


class AuthParams(BaseModel):
    client_id: str
    client_secret: str


app = FastAPI(title="XP Securities Services API")

# Configuração de autenticação Bearer para Swagger UI
security_scheme = HTTPBearer()


# Helper para extrair token
def get_token(
    credentials: HTTPAuthorizationCredentials = Security(security_scheme),
) -> str:
    """
    Extrai o token Bearer de autenticação.
    Este método é chamado automaticamente pelo FastAPI quando decorado com Depends.
    O Swagger UI fornecerá automaticamente a interface para o token.
    """
    return credentials.credentials


def get_tokenaaa(
    credentials: HTTPAuthorizationCredentials = Security(security_scheme),
) -> str:
    """
    Extrai o token Bearer de autenticação.
    Este método é chamado automaticamente pelo FastAPI quando decorado com Depends.
    O Swagger UI fornecerá automaticamente a interface para o token.
    """
    return credentials.credentials


# Health check/root
@app.get("/")
def root():
    return {"message": "XP Securities Services Demo API"}


# -------------------
# ARQUIVOS XP
# -------------------
# GET /files/types
@app.get("/files/types")
def get_file_types(token: str = Depends(get_tokenaaa)):
    """
    Retorna os tipos de arquivos disponíveis.
    Requer autenticação Bearer token.
    """
    try:
        # Usa o token diretamente no FilesManager
        files_manager = FilesManager(token, ApiEndpoints.SUBSCRIPTION_KEY)
        return files_manager.get_file_types()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# GET /files/formats
@app.get("/files/formats")
def get_file_formats(token: str = Depends(get_token)):
    """
    Retorna os formatos de arquivos disponíveis.
    Requer autenticação Bearer token.
    """
    try:
        # Usa o token diretamente no FilesManager
        files_manager = FilesManager(token, ApiEndpoints.SUBSCRIPTION_KEY)
        return files_manager.get_file_formats()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# GET /files/portfolios
@app.get("/files/portfolios")
def get_file_portfolios(token: str = Depends(get_token)):
    """
    Retorna os portfólios de arquivos disponíveis.
    Requer autenticação Bearer token.
    """
    try:
        # Usa o token diretamente no FilesManager
        files_manager = FilesManager(token, ApiEndpoints.SUBSCRIPTION_KEY)
        return files_manager.get_file_portfolios()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# GET /files/list (params via query)
@app.get("/files")
def files_list(
    positionDate: str,
    page: int,
    pageSize: int,
    identification: str = None,
    fileType: int = None,
    fileFormat: int = None,
    filePortfolio: int = None,
    AvailabilityStartDate: str = None,
    AvailabilityEndDate: str = None,
):
    # result = FilesManager.list_files({...})
    return {"mock": "files list"}


# GET /files/download (params via query)
@app.get("/files/download")
def files_download(file_id: str):
    # result = FilesManager.download_file({"file_id": file_id})
    return {"mock": f"downloaded file {file_id}"}


# -------------------
# CARTEIRAS XP
# -------------------
# GET /wallets/active (params via query)
@app.get("/wallets/active")
def wallets_active(conciliationReferenceDate: str = None):
    # result = WalletsManager.get_active_wallets({...})
    return {"mock": "wallets active"}


# POST /fixedincome/create (body)
@app.post("/fixedincome/create")
def fixedincome_create(params: dict):
    # result = FixedIncomeManager.create_order(params)
    return {"mock": "fixedincome created"}


# -------------------
# FUND QUOTA XP
# -------------------
# GET /fundquota/list (params via query)
@app.get("/fundquota/list")
def fundquota_list(
    origin: str = None,
    orderDate: str = None,
    managerLegalId: str = None,
    fundLegalId: str = None,
    fundISINCode: str = None,
    operationType: str = None,
    assetLegalId: str = None,
    assetISINCode: str = None,
    settlementDate: str = None,
    quotationDate: str = None,
    quantity: float = None,
    value: float = None,
    settlementType: str = None,
    strategy: str = None,
    marketType: str = None,
    cetipAccountCounterparty: str = None,
    fundCetipAccount: str = None,
    assetCode: str = None,
    assetUnitPrice: float = None,
    counterpartyLegalId: str = None,
    counterpartyName: str = None,
    earlyRedemptionCondition: bool = None,
    cetipResponsible: str = None,
    phoneNumber: str = None,
    externalId: str = None,
    chamadaCapital: bool = None,
    assetSerie: str = None,
    requesterName: str = None,
    bank: str = None,
    agency: str = None,
    account: str = None,
):
    # result = FundQuotaManager.list_orders({...})
    return {"mock": "fundquota list"}


# POST /fundquota/create (body)
@app.post("/fundquota/create")
def fundquota_create(params: dict):
    # result = FundQuotaManager.create_order(params)
    return {"mock": "fundquota created"}


# -------------------
# ORDENS PASSIVAS XP
# -------------------
# POST /passive_orders/validation (body)
@app.post("/passive_orders/validation")
def passive_orders_validation(params: dict):
    # result = PassiveOrdersManager.validate_file(...)
    return {"mock": "passive orders validation"}


# POST /passive_orders/file (body)
@app.post("/passive_orders/file")
def passive_orders_file(params: dict):
    # result = PassiveOrdersManager.upload_file(...)
    return {"mock": "passive orders file uploaded"}


# GET /passive_orders/file (params via query)
@app.get("/passive_orders/file")
def passive_orders_file_list(managerLegalId: str = None, status: str = None):
    # result = PassiveOrdersManager.list_uploaded_files({...})
    return {"mock": "passive orders file list"}


# GET /passive_orders/file/download (params via query)
@app.get("/passive_orders/file/download")
def passive_orders_file_download(upload_id: str):
    # result = PassiveOrdersManager.download_result(upload_id)
    return {"mock": f"downloaded passive orders file {upload_id}"}


# -------------------
# EXPORTAÇÃO DE ORDENS PASSIVAS XP
# -------------------
# POST /passive_orders/export (body)
@app.post("/passive_orders/export")
def passive_orders_export(params: dict):
    # result = ExportManager.request_export(params)
    return {"mock": "passive orders export requested"}


# GET /passive_orders/export (params via query)
@app.get("/passive_orders/export")
def passive_orders_export_list(
    managerLegalId: str = None,
    date_from: str = None,
    date_to: str = None,
):
    # result = ExportManager.list_exports({...})
    return {"mock": "passive orders export list"}


# GET /passive_orders/export/{id}
@app.get("/passive_orders/export/{export_id}")
def passive_orders_export_by_id(export_id: str):
    # result = ExportManager.get_export_by_id(export_id)
    return {"mock": f"passive orders export {export_id}"}


# GET /passive_orders/export/{id}/download
@app.get("/passive_orders/export/{export_id}/download")
def passive_orders_export_download(export_id: str):
    # result = ExportManager.download_export(export_id)
    return {"mock": f"downloaded export {export_id}"}


# GET /passive_orders/export/funds
@app.get("/passive_orders/export/funds")
def passive_orders_export_funds():
    # result = ExportManager.get_funds({})
    return {"mock": "passive orders export funds"}


# GET /passive_orders/export/shareholders
@app.get("/passive_orders/export/shareholders")
def passive_orders_export_shareholders():
    # result = ExportManager.get_shareholders({})
    return {"mock": "passive orders export shareholders"}


# -------------------
# CUSTÓDIA DTVM (PCO)
# -------------------
# POST /custody/search-by-correlationid (body)
@app.post("/custody/search-by-correlationid")
def custody_search_by_correlationid(params: dict):
    # result = CustodyManager.search_movement_by_correlation_id(params.get("correlationIds"))
    return {"mock": "custody search by correlationid"}


# POST /custody/movementpco (body)
@app.post("/custody/movementpco")
def custody_create_movement(params: dict):
    # result = CustodyManager.create_movement(params)
    return {"mock": "custody movement created"}


# -------------------
# ENDPOINTS AUXILIARES DE EXPORTAÇÃO
# -------------------
# GET /export/funds
@app.get("/export/funds")
def export_funds():
    # result = ExportAuxManager.get_available_funds({})
    return {"mock": "export available funds"}


# GET /export/shareholders
@app.get("/export/shareholders")
def export_shareholders():
    # result = ExportAuxManager.get_available_shareholders({})
    return {"mock": "export available shareholders"}


# -------------------
# Outros endpoints podem ser adicionados seguindo o mesmo padrão


# Autenticação XP (POST)
@app.post("/auth/token")
def get_token(auth: AuthParams):
    data = {
        "client_id": auth.client_id,
        "client_secret": auth.client_secret,
    }

    try:
        auth_manager = AuthManager(
            client_id=auth.client_id,
            client_secret=auth.client_secret,
        )

        return auth_manager.get_token()

    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


# Autenticação XP via AD (POST)
@app.post("/auth/token/ad")
def get_token_via_ad(auth: AuthParams):
    data = {
        "client_id": auth.client_id,
        "client_secret": auth.client_secret,
    }

    try:
        auth_manager = ADAuthManager(
            client_id=auth.client_id,
            client_secret=auth.client_secret,
        )

        return auth_manager.get_token(scope=ApiEndpoints.AD_TOKEN_SCOPE)

    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


# Arquivos XP
# Modelo específico para query parameters na listagem de arquivos
class FilesListQueryParams(BaseModel):
    file_type: Optional[str] = None
    date_from: Optional[str] = None
    date_to: Optional[str] = None
    status: Optional[str] = None

    class Config:
        extra = "forbid"  # Impede parâmetros extras


# GET /files/list (params via query)
@app.get("/files/list", response_model=dict)
def list_files(
    token: str = Depends(get_token),
    file_type: Optional[str] = None,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
    status: Optional[str] = None,
):
    """
    Lista arquivos com base nos parâmetros fornecidos.
    Requer autenticação Bearer token.
    """
    try:
        # Criamos um dicionário com os parâmetros não-nulos
        params = {}
        if file_type:
            params["file_type"] = file_type
        if date_from:
            params["date_from"] = date_from
        if date_to:
            params["date_to"] = date_to
        if status:
            params["status"] = status

        # Cria FilesManager usando o token do cliente
        files_manager = FilesManager(token, ApiEndpoints.SUBSCRIPTION_KEY)
        # result = files_manager.list_files(params)

        return {"received": params}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# POST /files/download (body: file_id)
class FileDownloadParams(BaseModel):
    file_id: str


@app.post("/files/download")
def download_file(params: FileDownloadParams, token: str = Depends(get_token)):
    """
    Faz o download de um arquivo específico.
    Requer autenticação Bearer token.
    """
    try:
        # Cria FilesManager usando o token do cliente
        files_manager = FilesManager(token, ApiEndpoints.SUBSCRIPTION_KEY)
        # result = files_manager.download_file({"file_id": params.file_id})

        return {"downloaded": params.file_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Carteiras XP
# GET /wallets/active (params via query)
@app.get("/wallets/active")
def wallets_active(
    token: str = Depends(get_token), user_id: str = None, status: str = None
):
    """
    Lista carteiras ativas com base nos parâmetros fornecidos.
    Requer autenticação Bearer token.
    """
    try:
        params = {"user_id": user_id, "status": status}
        wallets_params = WalletsActiveParams(
            **{k: v for k, v in params.items() if v is not None}
        )
        # Cria WalletsManager usando o token do cliente
        # wallets_manager = WalletsManager(token, ApiEndpoints.SUBSCRIPTION_KEY)
        # result = wallets_manager.active(wallets_params)

        return {"received": wallets_params.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Renda Fixa XP
# GET /fixedincome/list (params via query)
@app.get("/fixedincome/list")
def fixedincome_list(
    token: str = Depends(get_tokenaaa),
    asset_type: Optional[str] = Query(None),
    date_from: Optional[str] = Query(None),
    date_to: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
):
    """
    Lista ordens de renda fixa com base nos parâmetros fornecidos.
    Requer autenticação Bearer token.

    Parâmetros de consulta:
    - asset_type: Tipo de ativo
    - date_from: Data inicial
    - date_to: Data final
    - status: Status da ordem
    """
    try:
        # Criamos um dicionário com os parâmetros não-nulos
        params = {}
        if asset_type:
            params["asset_type"] = asset_type
        if date_from:
            params["date_from"] = date_from
        if date_to:
            params["date_to"] = date_to
        if status:
            params["status"] = status

        # Cria FixedIncomeManager usando o token do cliente
        fixed_income_manager = FixedIncomeManager(token, ApiEndpoints.SUBSCRIPTION_KEY)
        result = fixed_income_manager.list_orders(params)

        return {"params": params, "data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# POST /fixedincome/create (body)
@app.post("/fixedincome/create")
def fixedincome_create(params: dict, token: str = Depends(get_token)):
    """
    Cria uma nova ordem de renda fixa.
    Requer autenticação Bearer token.
    """
    try:
        fi_params = FixedIncomeOrderParams(**params)
        # Cria FixedIncomeManager usando o token do cliente
        # fixed_income_manager = FixedIncomeManager(token, ApiEndpoints.SUBSCRIPTION_KEY)
        # result = fixed_income_manager.create(fi_params)

        return {"created": fi_params.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Fund Quota XP
# Modelo específico para query parameters na listagem de cotas de fundos
class FundQuotaListQueryParams(BaseModel):
    quota_type: Optional[str] = None
    date_from: Optional[str] = None
    date_to: Optional[str] = None
    status: Optional[str] = None

    class Config:
        extra = "forbid"  # Impede parâmetros extras


# GET /fundquota/list (params via query)
@app.get("/fundquota/list", response_model=dict)
def fundquota_list(
    token: str = Depends(get_token),
    quota_type: Optional[str] = None,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
    status: Optional[str] = None,
):
    """
    Lista ordens de cotas de fundos com base nos parâmetros fornecidos.
    Requer autenticação Bearer token.
    """
    try:
        # Criamos um dicionário com os parâmetros não-nulos
        params = {}
        if quota_type:
            params["quota_type"] = quota_type
        if date_from:
            params["date_from"] = date_from
        if date_to:
            params["date_to"] = date_to
        if status:
            params["status"] = status

        # Cria FundQuotaManager usando o token do cliente
        # fund_quota_manager = FundQuotaManager(token, ApiEndpoints.SUBSCRIPTION_KEY)
        # result = fund_quota_manager.list(params)

        return {"received": params}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# POST /fundquota/create (body)
@app.post("/fundquota/create")
def fundquota_create(params: dict, token: str = Depends(get_token)):
    """
    Cria uma nova ordem de cota de fundo.
    Requer autenticação Bearer token.
    """
    try:
        fq_params = FundQuotaOrderParams(**params)
        # Cria FundQuotaManager usando o token do cliente
        # fund_quota_manager = FundQuotaManager(token, ApiEndpoints.SUBSCRIPTION_KEY)
        # result = fund_quota_manager.create(fq_params)

        return {"created": fq_params.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Exportação de ordens passivas XP
# Modelo específico para query parameters na listagem de exportações de ordens passivas
class PassiveOrdersExportQueryParams(BaseModel):
    managerLegalId: Optional[str] = None
    date_from: Optional[str] = None
    date_to: Optional[str] = None

    class Config:
        extra = "forbid"  # Impede parâmetros extras


# GET /passive_orders/export (params via query)
@app.get("/passive_orders/export", response_model=dict)
def passive_orders_export(
    token: str = Depends(get_token),
    managerLegalId: Optional[str] = None,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
):
    """
    Lista exportações de ordens passivas.
    Requer autenticação Bearer token.
    """
    try:
        # Criamos um dicionário com os parâmetros não-nulos
        params = {}
        if managerLegalId:
            params["managerLegalId"] = managerLegalId
        if date_from:
            params["date_from"] = date_from
        if date_to:
            params["date_to"] = date_to

        # Cria PassiveOrdersManager usando o token do cliente
        # passive_orders_manager = PassiveOrdersManager(token, ApiEndpoints.SUBSCRIPTION_KEY)
        # result = passive_orders_manager.export(params)

        return {"received": params}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# POST /passive_orders/validation (body)
@app.post("/passive_orders/validation")
def passive_orders_validation(params: dict, token: str = Depends(get_token)):
    """
    Valida um arquivo de ordens passivas.
    Requer autenticação Bearer token.
    """
    try:
        validation_params = PassiveOrdersValidationParams(**params)
        # Cria PassiveOrdersManager usando o token do cliente
        # passive_orders_manager = PassiveOrdersManager(token, ApiEndpoints.SUBSCRIPTION_KEY)
        # result = passive_orders_manager.validate(validation_params)

        return {"received": validation_params.managerLegalId}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# POST /passive_orders/file (body)
@app.post("/passive_orders/file")
def passive_orders_file(params: dict, token: str = Depends(get_token)):
    """
    Envia um arquivo de ordens passivas.
    Requer autenticação Bearer token.
    """
    try:
        file_params = PassiveOrdersFileParams(**params)
        # Cria PassiveOrdersManager usando o token do cliente
        # passive_orders_manager = PassiveOrdersManager(token, ApiEndpoints.SUBSCRIPTION_KEY)
        # result = passive_orders_manager.upload_file(file_params)

        return {"received": file_params.managerLegalId}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Outros endpoints podem ser adicionados seguindo o mesmo padrão
