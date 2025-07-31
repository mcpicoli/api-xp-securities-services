import requests

from src.api.api_endpoints import ApiEndpoints
from src.auth.auth_manager import AuthManager


class PassiveOrdersManager:
    """
    Gerencia o acesso aos endpoints de ordens passivas da XP Securities Services.
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

    def validate_file(self, files, data=None):
        response = requests.post(
            ApiEndpoints.PASSIVE_ORDERS_VALIDATION,
            headers=self._get_headers(),
            files=files,
            data=data or {},
        )
        response.raise_for_status()
        return response.json()

    def upload_file(self, files, data=None):
        response = requests.post(
            ApiEndpoints.PASSIVE_ORDERS_FILE,
            headers=self._get_headers(),
            files=files,
            data=data or {},
        )
        response.raise_for_status()
        return response.json()

    def list_uploaded_files(self, params=None):
        response = requests.get(
            ApiEndpoints.PASSIVE_ORDERS_FILE,
            headers=self._get_headers(),
            params=params or {},
        )
        response.raise_for_status()
        return response.json()

    def download_result(self, upload_id):
        url = ApiEndpoints.PASSIVE_ORDERS_FILE_DOWNLOAD.format(id=upload_id)
        response = requests.get(url, headers=self._get_headers(), stream=True)
        response.raise_for_status()
        return response.content
