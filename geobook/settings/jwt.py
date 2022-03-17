import typing

from pydantic import BaseModel


class JWTSettings(BaseModel):
    ISS: str
    ALGORITHM: str
    TOKEN_PREFIX: typing.Optional[str] = 'Bearer'
    ACCESS_TOKEN_EXPIRES_MINUTES: typing.Optional[int] = 60
