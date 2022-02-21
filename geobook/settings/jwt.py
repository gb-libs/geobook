import typing

from pydantic import BaseModel


class JWTSettings(BaseModel):
    ACCESS_TOKEN_EXPIRES_MINUTES: typing.Optional[int] = 24 * 60
    REFRESH_TOKEN_EXPIRES_MINUTES: typing.Optional[int] = 7 * 24 * 60
    TOKEN_PREFIX: typing.Optional[str] = 'Bearer'
