from passlib.context import CryptContext


class BaseUserService:
    algorithm = 'HS256'
    pwd_context = CryptContext(schemes=['bcrypt'])

    def encode_password(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, password: str, encoded_password: str) -> bool:
        return self.pwd_context.verify(password, encoded_password)
