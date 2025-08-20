"""
Gerenciadores de autenticação para XP Securities Services.
"""

import json
from datetime import datetime, timedelta

import requests

from src.api.api_endpoints import ApiEndpoints
from src.auth.base_auth import BaseAuthProvider


class AuthManager(BaseAuthProvider):
    """
    Gerencia a autenticação OAuth 2.0 para acessar as APIs da XP Securities Services.
    """

    def __init__(self, client_id: str, client_secret: str):
        """
        Inicializa o gerenciador com credenciais de cliente.

        Args:
            client_id (str): ID do cliente para OAuth.
            client_secret (str): Segredo do cliente para OAuth.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = ApiEndpoints.AUTH_TOKEN
        self.access_token = None
        self.token_expiry = None

    def get_token(self) -> str:
        """
        Obtém um token de acesso válido. Renova o token se necessário.

        Returns:
            str: Token de acesso válido.
        """
        if (
            self.access_token
            and self.token_expiry
            and self.token_expiry > datetime.now()
        ):
            return self.access_token

        headers = {
            # "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "/",
        }

        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
            "scope": "products",
        }

        req = requests.Request(
            "POST",
            self.token_url,
            headers=headers,
            data=data,
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

        if response.status_code == 200:
            token_data = response.json()
            self.access_token = token_data["access_token"]
            expires_in = token_data.get("expires_in", 3600)  # Default to 1 hour
            self.token_expiry = datetime.now() + timedelta(seconds=expires_in)
            return self.access_token
        else:
            raise Exception(
                f"Erro ao obter token: {response.status_code} - {response.text}"
            )


class ADAuthManager(BaseAuthProvider):
    """
    Gerencia autenticação via AD (OAuth2) para XP Securities Services.
    """

    def __init__(self, client_id: str, client_secret: str, scope: str = None):
        """
        Inicializa o gerenciador com credenciais de cliente e escopo opcional.

        Args:
            client_id (str): ID do cliente registrado no Azure AD.
            client_secret (str): Segredo do cliente registrado no Azure AD.
            scope (str, optional): Escopo da solicitação. Se None, será solicitado ao chamar get_token.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.default_scope = scope
        self.token_url = ApiEndpoints.AD_TOKEN
        self.access_token = None
        self.token_expiry = None

    def get_token(self, scope: str = None) -> str:
        """
        Obtém um token de acesso via Azure AD.

        Args:
            scope (str, optional): Escopo da solicitação. Se None, usa o escopo padrão.

        Returns:
            str: Token de acesso.

        Raises:
            Exception: Se a solicitação falhar.
        """
        use_scope = scope or self.default_scope
        if not use_scope:
            raise ValueError("Escopo deve ser fornecido.")

        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": use_scope,
        }
        response = requests.post(self.token_url, data=data)
        response.raise_for_status()
        token_data = response.json()
        self.access_token = token_data["access_token"]
        expires_in = token_data.get("expires_in", 3600)
        self.token_expiry = datetime.now() + timedelta(seconds=expires_in)
        return self.access_token
