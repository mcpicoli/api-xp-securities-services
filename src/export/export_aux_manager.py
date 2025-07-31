import requests

from src.api.api_endpoints import ApiEndpoints
from src.auth.auth_manager import AuthManager


class ExportAuxManager:
    """
    Gerencia o acesso aos endpoints auxiliares de exportação (fundos e cotistas disponíveis).
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

    def get_available_funds(self, params: dict):
        response = requests.get(
            ApiEndpoints.EXPORT_FUNDS, headers=self._get_headers(), params=params
        )
        response.raise_for_status()
        return response.json()

    def get_available_shareholders(self, params: dict):
        response = requests.get(
            ApiEndpoints.EXPORT_SHAREHOLDERS, headers=self._get_headers(), params=params
        )
        response.raise_for_status()
        return response.json()
