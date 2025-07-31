import requests

from src.api.api_endpoints import ApiEndpoints
from src.auth.auth_manager import AuthManager


class CustodyManager:
    """
    Gerencia o acesso aos endpoints de Custódia DTVM (movimento PCO).
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

    def search_movement_by_correlation_id(self, correlation_ids):
        data = {"correlationIds": correlation_ids}
        response = requests.post(
            ApiEndpoints.PCO_SEARCH, headers=self._get_headers(), json=data
        )
        response.raise_for_status()
        return response.json()

    def create_movement(self, movement_data):
        response = requests.post(
            ApiEndpoints.PCO_CREATE, headers=self._get_headers(), json=movement_data
        )
        response.raise_for_status()
        return response.json()
