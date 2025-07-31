import requests

from src.api.api_endpoints import ApiEndpoints
from src.auth.auth_manager import AuthManager


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
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": scope,
        }
        response = requests.post(self.token_url, data=data)
        response.raise_for_status()
        token_data = response.json()
        self.access_token = token_data["access_token"]
        expires_in = token_data.get("expires_in", 3600)
        self.token_expiry = expires_in
        return self.access_token
