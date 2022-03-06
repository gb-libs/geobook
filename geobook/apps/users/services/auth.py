import jwt
from fastapi import HTTPException
from geobook.apps.users.managers.user import UserManager
from geobook.apps.users.models.auth import AccessToken, JWTPayload
from geobook.apps.users.models.user import UserReadModel
from geobook.apps.users.services.base import BaseUserService
from geobook.settings.common import Settings


class AuthService(BaseUserService):

    def __init__(
            self,
            settings: Settings,
    ):
        self.settings = settings
        self.user_manager = UserManager(settings=settings)

    async def encode_token(self, username: str) -> AccessToken:
        jwt_payload = JWTPayload(sub=username)

        token = jwt.encode(
            payload=jwt_payload.dict(),
            key=self.settings.SECRET,
            algorithm=self.algorithm)

        return AccessToken(
            token=token,
            expires=jwt_payload.exp)

    async def decode_token(self, token: str) -> UserReadModel:
        try:
            decoded_token = jwt.decode(
                jwt=token,
                key=self.settings.SECRET,
                algorithms=[self.algorithm])

            jwt_payload = JWTPayload(**decoded_token)

            if jwt_payload.sub:
                user = await self.user_manager.get_user_by_username(
                    username=jwt_payload.sub)
                if user:
                    return user

            raise HTTPException(status_code=401, detail='Username is invalid')
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Token expired')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Invalid token')
