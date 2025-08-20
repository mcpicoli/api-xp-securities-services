import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.api.api_endpoints import ApiEndpoints
from src.auth.ad_auth_manager import ADAuthManager

# Endpoint XP para autenticação
from src.auth.auth_manager import AuthManager
from src.export.params import PassiveOrdersExportParams
from src.files.params import FileListParams
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


app = FastAPI()


# Health check/root
@app.get("/")
def root():
    return {"message": "XP Securities Services Demo API"}


# -------------------
# ARQUIVOS XP
# -------------------
# GET /files/types
@app.get("/files/types")
def get_file_types():
    # result = FilesManager.get_file_types()
    return {"mock": "file types"}


# GET /files/formats
@app.get("/files/formats")
def get_file_formats():
    # result = FilesManager.get_file_formats()
    return {"mock": "file formats"}


# GET /files/portfolios
@app.get("/files/portfolios")
def get_file_portfolios():
    # result = FilesManager.get_file_portfolios()
    return {"mock": "file portfolios"}


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


# -------------------
# RENDA FIXA XP
# -------------------
# GET /fixedincome/list (params via query)
@app.get("/fixedincome/list")
def fixedincome_list(
    managerLegalId: str = None,
    fundLegalId: str = None,
    requesterName: str = None,
    origin: str = None,
    orderDate: str = None,
    settlementDate: str = None,
    fundISINCode: str = None,
    operationType: str = None,
    assetType: str = None,
    marketType: str = None,
    assetCode: str = None,
    quantity: float = None,
    assetUnitPrice: float = None,
    tax: float = None,
    totalValue: float = None,
    paymentType: str = None,
    bankTransfer: bool = None,
    bank: str = None,
    agency: str = None,
    account: str = None,
    counterPartName: str = None,
    counterPartLegalId: str = None,
    cetipAccountCounterparty: str = None,
    fundCetipAccount: str = None,
    externalId: str = None,
    dueDate: str = None,
):
    # result = FixedIncomeManager.list_orders({...})
    return {"mock": "fixedincome list"}


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

        return auth_manager.get_access_token()

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

        return auth_manager.get_access_token(scope=ApiEndpoints.AD_TOKEN_SCOPE)

    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


# Arquivos XP
# GET /files/list (params via query)
@app.get("/files/list")
def list_files(
    file_type: str = None,
    date_from: str = None,
    date_to: str = None,
    status: str = None,
):
    try:
        params = {
            "file_type": file_type,
            "date_from": date_from,
            "date_to": date_to,
            "status": status,
        }
        file_params = FileListParams(
            **{k: v for k, v in params.items() if v is not None}
        )
        # result = FilesManager.list_files(file_params)
        return {"received": file_params.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# POST /files/download (body: file_id)
class FileDownloadParams(BaseModel):
    file_id: str


@app.post("/files/download")
def download_file(params: FileDownloadParams):
    try:
        # result = FilesManager.download_file(params.file_id)
        return {"downloaded": params.file_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Carteiras XP
# GET /wallets/active (params via query)
@app.get("/wallets/active")
def wallets_active(user_id: str = None, status: str = None):
    try:
        params = {"user_id": user_id, "status": status}
        wallets_params = WalletsActiveParams(
            **{k: v for k, v in params.items() if v is not None}
        )
        # result = WalletsManager.active(wallets_params)
        return {"received": wallets_params.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Renda Fixa XP
# GET /fixedincome/list (params via query)
@app.get("/fixedincome/list")
def fixedincome_list(
    asset_type: str = None,
    date_from: str = None,
    date_to: str = None,
    status: str = None,
):
    try:
        params = {
            "asset_type": asset_type,
            "date_from": date_from,
            "date_to": date_to,
            "status": status,
        }
        fi_params = FixedIncomeOrderParams(
            **{k: v for k, v in params.items() if v is not None}
        )
        # result = FixedIncomeManager.list(fi_params)
        return {"received": fi_params.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# POST /fixedincome/create (body)
@app.post("/fixedincome/create")
def fixedincome_create(params: dict):
    try:
        fi_params = FixedIncomeOrderParams(**params)
        # result = FixedIncomeManager.create(fi_params)
        return {"created": fi_params.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Fund Quota XP
# GET /fundquota/list (params via query)
@app.get("/fundquota/list")
def fundquota_list(
    quota_type: str = None,
    date_from: str = None,
    date_to: str = None,
    status: str = None,
):
    try:
        params = {
            "quota_type": quota_type,
            "date_from": date_from,
            "date_to": date_to,
            "status": status,
        }
        fq_params = FundQuotaOrderParams(
            **{k: v for k, v in params.items() if v is not None}
        )
        # result = FundQuotaManager.list(fq_params)
        return {"received": fq_params.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# POST /fundquota/create (body)
@app.post("/fundquota/create")
def fundquota_create(params: dict):
    try:
        fq_params = FundQuotaOrderParams(**params)
        # result = FundQuotaManager.create(fq_params)
        return {"created": fq_params.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Exportação de ordens passivas XP
# GET /passive_orders/export (params via query)
@app.get("/passive_orders/export")
def passive_orders_export(
    managerLegalId: str = None, date_from: str = None, date_to: str = None
):
    try:
        params = {
            "managerLegalId": managerLegalId,
            "date_from": date_from,
            "date_to": date_to,
        }
        export_params = PassiveOrdersExportParams(
            **{k: v for k, v in params.items() if v is not None}
        )
        # result = PassiveOrdersManager.export(export_params)
        return {"received": export_params.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# POST /passive_orders/validation (body)
@app.post("/passive_orders/validation")
def passive_orders_validation(params: dict):
    try:
        validation_params = PassiveOrdersValidationParams(**params)
        # result = PassiveOrdersManager.validate(validation_params)
        return {"received": validation_params.managerLegalId}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# POST /passive_orders/file (body)
@app.post("/passive_orders/file")
def passive_orders_file(params: dict):
    try:
        file_params = PassiveOrdersFileParams(**params)
        # result = PassiveOrdersManager.upload_file(file_params)
        return {"received": file_params.managerLegalId}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Outros endpoints podem ser adicionados seguindo o mesmo padrão
