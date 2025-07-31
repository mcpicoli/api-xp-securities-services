import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Endpoint XP para autenticação
from src.api.api_endpoints import ApiEndpoints
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
    username: str
    password: str
    scope: str = "securitiesservices"


app = FastAPI()


@app.get("/")
def root():
    return {"message": "XP Securities Services Demo API"}


# Endpoint para autenticação XP
@app.post("/auth/token")
def get_token(auth: AuthParams):
    data = {
        "client_id": auth.client_id,
        "client_secret": auth.client_secret,
        "username": auth.username,
        "password": auth.password,
        "scope": auth.scope,
        "grant_type": "password",
    }
    try:
        response = requests.post(ApiEndpoints.AUTH_TOKEN, data=data)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


# Exemplo de endpoint usando módulo Python
@app.post("/files/list")
def list_files(params: dict):
    try:
        file_params = FileListParams(**params)
        # Aqui você chamaria o manager responsável por acessar a API XP
        # Exemplo: result = FilesManager.list_files(file_params)
        # Retorne o resultado (mock para demonstração)
        return {"received": file_params.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/files/download")
def download_file(file_id: str):
    # result = FilesManager.download_file(file_id)
    return {"downloaded": file_id}


# Carteiras
@app.post("/wallets/active")
def wallets_active(params: dict):
    try:
        wallets_params = WalletsActiveParams(**params)
        # result = WalletsManager.active(wallets_params)
        return {"received": wallets_params.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Renda Fixa
@app.post("/fixedincome/list")
def fixedincome_list(params: dict):
    try:
        fi_params = FixedIncomeOrderParams(**params)
        # result = FixedIncomeManager.list(fi_params)
        return {"received": fi_params.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/fixedincome/create")
def fixedincome_create(params: dict):
    try:
        fi_params = FixedIncomeOrderParams(**params)
        # result = FixedIncomeManager.create(fi_params)
        return {"created": fi_params.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Fund Quota
@app.post("/fundquota/list")
def fundquota_list(params: dict):
    try:
        fq_params = FundQuotaOrderParams(**params)
        # result = FundQuotaManager.list(fq_params)
        return {"received": fq_params.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/fundquota/create")
def fundquota_create(params: dict):
    try:
        fq_params = FundQuotaOrderParams(**params)
        # result = FundQuotaManager.create(fq_params)
        return {"created": fq_params.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Exportação de ordens passivas
@app.post("/passive_orders/export")
def passive_orders_export(params: dict):
    try:
        export_params = PassiveOrdersExportParams(**params)
        # result = PassiveOrdersManager.export(export_params)
        return {"received": export_params.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Validação de ordens passivas
@app.post("/passive_orders/validation")
def passive_orders_validation(params: dict):
    try:
        validation_params = PassiveOrdersValidationParams(**params)
        # result = PassiveOrdersManager.validate(validation_params)
        return {"received": validation_params.managerLegalId}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Upload de arquivo de ordens passivas
@app.post("/passive_orders/file")
def passive_orders_file(params: dict):
    try:
        file_params = PassiveOrdersFileParams(**params)
        # result = PassiveOrdersManager.upload_file(file_params)
        return {"received": file_params.managerLegalId}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Outros endpoints podem ser adicionados seguindo o mesmo padrão
