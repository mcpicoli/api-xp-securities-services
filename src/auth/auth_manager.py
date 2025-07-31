from datetime import datetime, timedelta

import requests

from src.api.api_endpoints import ApiEndpoints


class AuthManager:
    """
    Gerencia a autenticação OAuth 2.0 para acessar as APIs da XP Securities Services.
    """

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = ApiEndpoints.AUTH_TOKEN
        self.access_token = None
        self.token_expiry = None

    def get_access_token(self):
        """
        Obtém um token de acesso válido. Renova o token se necessário.
        """
        if self.access_token and self.token_expiry > datetime.now():
            return self.access_token

        response = requests.post(
            self.token_url,
            data={
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                # Valores fixos
                "grant_type": "client_credentials",
                "scope": "products",
            },
        )

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


# Exemplo de uso
# auth_manager = AuthManager(
#     client_id="seu_client_id",
#     client_secret="seu_client_secret"
# )
# token = auth_manager.get_access_token()
# print(token)
