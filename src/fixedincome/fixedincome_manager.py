from typing import Union

import requests

from src.api.api_endpoints import ApiEndpoints
from src.auth.base_auth import BaseAuthProvider


class FixedIncomeManager:
    """
    Gerencia o acesso aos endpoints de boletas de renda fixa.
    """

    def __init__(
        self, auth_provider: Union[BaseAuthProvider, str], subscription_key: str
    ):
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

    def create_order(self, data: dict):
        response = requests.post(
            ApiEndpoints.FIXEDINCOME_CREATE, headers=self._get_headers(), json=data
        )
        response.raise_for_status()
        return response.json()

    def list_orders(self, params: dict):
        """
        Listagem de Ordens de Renda Fixa

        Args:
            params: Dicionário com os parâmetros de consulta

        Returns:
            dict: Resposta JSON da API com as ordens de renda fixa
        """
        # Filtramos apenas parâmetros não nulos para evitar problemas com a API
        filtered_params = {k: v for k, v in params.items() if v is not None}

        response = requests.get(
            ApiEndpoints.FIXEDINCOME_LIST,
            headers=self._get_headers(),
            params=filtered_params,
        )

        response.raise_for_status()

        return response.json()
