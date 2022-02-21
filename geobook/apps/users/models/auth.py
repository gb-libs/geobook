import typing
from datetime import timedelta

from pydantic import Field

from geobook.db.backends.mongodb import models
from geobook.settings import get_config

config = get_config()

JWK = typing.Dict[str, str]

models.
class JWT(CoreModel):
    iss: str = "phresh.io"
    aud: str = JWT_AUDIENCE
    iat: float = datetime.timestamp(datetime.utcnow())
    exp: float = datetime.timestamp(datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))


class AccessToken(models.MongoModel):
    token: str = Field(
        min_length=1)

    expires: timedelta = timedelta(
        minutes=config.JWT.ACCESS_TOKEN_EXPIRES_MINUTES)


class RefreshToken(AccessToken):
    token: str = Field(
        min_length=1)

    expires: timedelta = timedelta(
        minutes=config.JWT.REFRESH_TOKEN_EXPIRES_MINUTES)
