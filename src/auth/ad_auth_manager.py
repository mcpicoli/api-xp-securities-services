from datetime import datetime, timedelta

import requests

from src.api.api_endpoints import ApiEndpoints


class ADAuthManager:
    """
    Gerencia autenticação via AD (OAuth2) para XP Securities Services.
    """

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = ApiEndpoints.AD_TOKEN
        self.access_token = None
        self.token_expiry = None

    def get_access_token(self, scope: str):
        """
        Obtém um token de acesso OAuth 2.0 usando o AD.
        """
        if self.access_token and self.token_expiry > datetime.now():
            return self.access_token

        print("Preparando requisição para obter novo token via AD")
        print(f"Client ID: {self.client_id}")
        print(f"AD Token URL: {self.token_url}")

        response = requests.post(
            self.token_url,
            data={
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "scope": scope,
                # Valores fixos
                "grant_type": "client_credentials",
            },
        )

        # Debug, despejando a resposta completa
        # print("Resposta da requisição:")
        # print(response.json())

        print("Requisição enviada")

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
