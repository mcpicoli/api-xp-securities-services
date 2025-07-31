import requests

from src.api.api_endpoints import ApiEndpoints
from src.auth.auth_manager import AuthManager


class FundQuotaManager:
    """
    Gerencia o acesso aos endpoints de boletas de cota de fundo.
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

    def create_order(self, data: dict):
        response = requests.post(
            ApiEndpoints.FUNDQUOTA_CREATE, headers=self._get_headers(), json=data
        )
        response.raise_for_status()
        return response.json()

    def list_orders(self, params: dict):
        response = requests.get(
            ApiEndpoints.FUNDQUOTA_LIST, headers=self._get_headers(), params=params
        )
        response.raise_for_status()
        return response.json()
