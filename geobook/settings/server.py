import typing

from pydantic import AnyHttpUrl, BaseModel


class ServerSettings(BaseModel):
    HOST: typing.Optional[AnyHttpUrl] = 'http://127.0.0.1:8000'
    IS_RELOAD: typing.Optional[bool] = False
    LOG_LEVEL: typing.Optional[str] = 'info'
    IS_DEBUG: typing.Optional[bool] = True
    WORKER: typing.Optional[int] = 1
    LIMIT_CONCURRENCY: typing.Optional[int] = 5
