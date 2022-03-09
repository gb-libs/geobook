from geobook.db.backends.mongodb import models
from pydantic import BaseConfig, Field, SecretStr


class UserModel(models.MongoModel):
    username: str = Field(
        regex=r'^[\w.@+-]+\Z',
        min_length=1,
        max_length=150)

    password: SecretStr = Field(
        min_length=1)


class UserWriteModel(UserModel):
    pass


class UserReadModel(UserModel):
    class Config(BaseConfig):
        fields = {
            'password': {'exclude': True},
        }
