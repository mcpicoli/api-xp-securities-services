import requests

from src.api.api_endpoints import ApiEndpoints
from src.auth.auth_manager import AuthManager


class ExportManager:
    """
    Gerencia o acesso aos endpoints de exportação de ordens passivas de fundos.
    """

    def __init__(self, auth_manager: AuthManager, subscription_key: str):
        self.auth_manager = auth_manager
        self.subscription_key = subscription_key

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.auth_manager.get_access_token()}",
            "Ocp-Apim-Subscription-Key": self.subscription_key,
            "User-Agent": "/",
        }

    def request_export(self, data: dict):
        response = requests.post(
            ApiEndpoints.PASSIVE_ORDERS_EXPORT, headers=self._get_headers(), json=data
        )
        response.raise_for_status()
        return response.json()

    def list_exports(self, params: dict):
        response = requests.get(
            ApiEndpoints.PASSIVE_ORDERS_EXPORT,
            headers=self._get_headers(),
            params=params,
        )
        response.raise_for_status()
        return response.json()

    def get_export_by_id(self, export_id):
        url = ApiEndpoints.PASSIVE_ORDERS_EXPORT_ID.format(id=export_id)
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def download_export(self, export_id):
        url = ApiEndpoints.PASSIVE_ORDERS_EXPORT_DOWNLOAD.format(id=export_id)
        response = requests.get(url, headers=self._get_headers(), stream=True)
        response.raise_for_status()
        return response.content

    def get_funds(self, params: dict):
        response = requests.get(
            ApiEndpoints.PASSIVE_ORDERS_EXPORT_FUNDS,
            headers=self._get_headers(),
            params=params,
        )
        response.raise_for_status()
        return response.json()

    def get_shareholders(self, params: dict):
        response = requests.get(
            ApiEndpoints.PASSIVE_ORDERS_EXPORT_SHAREHOLDERS,
            headers=self._get_headers(),
            params=params,
        )
        response.raise_for_status()
        return response.json()
