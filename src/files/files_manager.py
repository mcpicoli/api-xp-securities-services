from typing import Union

import requests

from src.api.api_endpoints import ApiEndpoints
from src.auth.base_auth import BaseAuthProvider


class FilesManager:
    """
    Gerencia o acesso aos endpoints de arquivos da XP Securities Services.
    """

    def __init__(
        self, auth_provider: Union[BaseAuthProvider, str], subscription_key: str
    ):
        """
        Inicializa o gerenciador com um provedor de autenticação ou token direto.

        Args:
            auth_provider: Provedor de autenticação ou token string.
            subscription_key: Chave de assinatura para a API.
        """
        self.auth_provider = auth_provider
        self.subscription_key = subscription_key

    def _get_token(self) -> str:
        """
        Obtém o token de autenticação.

        Returns:
            str: Token de autenticação.
        """
        if isinstance(self.auth_provider, str):
            return self.auth_provider
        else:
            return self.auth_provider.get_token()

    def _get_headers(self):
        """
        Constrói os cabeçalhos para requisições à API.

        Returns:
            dict: Cabeçalhos HTTP.
        """
        return {
            "Authorization": f"Bearer {self._get_token()}",
            "Ocp-Apim-Subscription-Key": self.subscription_key,
            "User-Agent": "/",
        }

    def get_file_types(self):

        headers = self._get_headers()

        req = requests.Request(
            "GET",
            ApiEndpoints.FILE_TYPES,
            headers=headers,
        )
        prepared = req.prepare()

        print("=== RAW REQUEST ===")
        print(f"{prepared.method} {prepared.url}")
        print("Headers:")
        for k, v in prepared.headers.items():
            print(f"{k}: {v}")
        print("\nBody:")
        print(prepared.body)
        print("==================")

        response = requests.Session().send(prepared)

        print("=== RAW RESPONSE ===")
        print(f"{response.status_code} {response.url}")
        print("Headers:")
        for k, v in response.headers.items():
            print(f"{k}: {v}")
        print("\nBody:")
        print(response.text)
        print("==================")

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
