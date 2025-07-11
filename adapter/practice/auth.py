from abc import ABC, abstractmethod
# we have a custom AuthService interface used across our app
class AuthService(ABC):
    @abstractmethod
    def authenticate(self, token:str)->dict:...
    

#External auth0 provider
class Auth0Provider:
    def verify_token(self, jwt_token: str) -> dict:
        return {
            "sub": "auth0|abc123",
            "email": "user@example.com",
            "name": "John",
            "roles": ["admin"]
        }
        
class Auth0Adapter(AuthService):
    def __init__(self, provider:Auth0Provider):
        self.provider = provider
        
    def authenticate(self, token):
        raw_user = self.provider.verify_token(token)
        
        return {
            "id":raw_user["sub"],
            "username":raw_user["email"],
            "full_name":raw_user["name"],
            "roles":raw_user.get("roles", [])
        }