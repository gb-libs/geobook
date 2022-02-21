from datetime import datetime

from geobook.db.backends.mongodb import models
from pydantic import BaseConfig, Field, SecretStr


class UserModel(models.MongoModel):
    username: str = Field(
        regex=r'^[\w.@+-]+\Z',
        min_length=1,
        max_length=150)

    password: SecretStr = Field(
        min_length=1)

    created_at: datetime = Field(
        default_factory=datetime.utcnow)

    updated_at: datetime = Field(
        default_factory=datetime.utcnow)


class UserWriteModel(UserModel):
    pass


class UserReadModel(UserModel):
    class Config(BaseConfig):
        fields = {
            'password': {'exclude': True},
        }


class UserLoginModel(UserModel):
    class Config(BaseConfig):
        fields = {
            'created_at': {'exclude': True},
            'updated_at': {'exclude': True},
        }
