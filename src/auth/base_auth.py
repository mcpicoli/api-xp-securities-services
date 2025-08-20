"""
Base de autenticação para XP Securities Services.
Fornece uma interface comum para diferentes métodos de obtenção de tokens.
"""

from abc import ABC, abstractmethod


class BaseAuthProvider(ABC):
    """
    Classe base abstrata para provedores de autenticação.
    Define uma interface comum para obtenção de tokens.
    """

    @abstractmethod
    def get_token(self) -> str:
        """
        Obtém um token de acesso válido.

        Returns:
            str: Token de acesso válido.
        """
        pass


class TokenAuthProvider(BaseAuthProvider):
    """
    Provedor de autenticação que utiliza um token pré-existente.
    Útil para situações onde o cliente já possui um token válido.
    """

    def __init__(self, token: str):
        """
        Inicializa o provedor com um token existente.

        Args:
            token (str): Token de acesso pré-existente.
        """
        self.token = token

    def get_token(self) -> str:
        """
        Retorna o token pré-existente.

        Returns:
            str: Token de acesso.
        """
        return self.token
