import typing
from datetime import datetime, timedelta

from geobook.settings import get_config
from pydantic import BaseModel, Field

config = get_config()


class JWTPayload(BaseModel):
    iss: str = config.JWT.ISS
    sub: typing.Optional[str]

    iat: datetime = Field(
        default_factory=datetime.utcnow)

    exp: datetime = Field(
        default_factory=datetime.utcnow() + timedelta(
            minutes=config.JWT.ACCESS_TOKEN_EXPIRES_MINUTES))


class AccessToken(BaseModel):
    token: str = Field(
        min_length=1)

    expires: datetime
