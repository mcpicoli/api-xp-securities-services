import requests

from src.api.api_endpoints import ApiEndpoints
from src.auth.auth_manager import AuthManager


class WalletsManager:
    """
    Gerencia o acesso ao endpoint de carteiras ativas da XP Securities Services.
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

    def get_active_wallets(self, params: dict = None):
        response = requests.get(
            ApiEndpoints.WALLETS_ACTIVE,
            headers=self._get_headers(),
            params=params or {},
        )
        response.raise_for_status()
        return response.json()
