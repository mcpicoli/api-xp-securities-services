import requests

from src.api.api_endpoints import ApiEndpoints
from src.auth.auth_manager import AuthManager


class FilesManager:
    """
    Gerencia o acesso aos endpoints de arquivos da XP Securities Services.
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

    def get_file_types(self):
        response = requests.get(ApiEndpoints.FILE_TYPES, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def get_file_formats(self):
        response = requests.get(ApiEndpoints.FILE_FORMATS, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def get_file_portfolios(self):
        response = requests.get(
            ApiEndpoints.FILE_PORTFOLIOS, headers=self._get_headers()
        )
        response.raise_for_status()
        return response.json()

    def list_files(self, params: dict):
        response = requests.get(
            ApiEndpoints.FILE_LIST, headers=self._get_headers(), params=params
        )
        response.raise_for_status()
        return response.json()

    def download_file(self, params: dict):
        response = requests.get(
            ApiEndpoints.FILE_DOWNLOAD,
            headers=self._get_headers(),
            params=params,
            stream=True,
        )
        response.raise_for_status()
        return response.content
